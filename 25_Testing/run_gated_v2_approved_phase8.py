#!/usr/bin/env python3
"""STEP-02D: approved, diagram-free QEAX gate for the existing Phase 8/9 ledger.

No native SysML emission. Every source connector is compared with its private
staged ledger row before the directory is atomically published outside the repo.
"""
import argparse
import collections
import csv
import importlib.util
import json
import pathlib
import shutil
import sqlite3
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREFLIGHT = ROOT / "21_Importer/qeax_v2_preflight.py"
PHASE8 = ROOT / "24_Workbench/registry/runtime/normalize_qeax_phase8.py"
REGISTRY = ROOT / "24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json"
REQUIRED_FIELDS = (
    "source_pk", "source_guid", "raw_from", "raw_to", "family", "rule",
    "role", "status", "normalized_from", "normalized_to", "source_kind",
    "target_kind", "diagnostics", "source_direction", "source_role",
    "target_role", "source_cardinality", "target_cardinality",
    "raw_source_type", "raw_source_stereotype", "raw_target_type",
    "raw_target_stereotype", "source_aggregation_flag", "target_aggregation_flag",
)
SOURCE_COLUMNS = (
    "Connector_ID", "ea_guid", "Connector_Type", "Stereotype",
    "Start_Object_ID", "End_Object_ID", "Direction", "SourceRole",
    "DestRole", "SourceCard", "DestCard", "SourceIsAggregate",
    "DestIsAggregate",
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise ValueError("REQUIRED_V2_MODULE_MISSING")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ensure_private_destination(out):
    out = pathlib.Path(out).resolve()
    if out == ROOT or ROOT in out.parents:
        raise ValueError("PRIVATE_LEDGER_MUST_BE_OUTSIDE_REPOSITORY")
    if out.exists():
        raise ValueError("OUTPUT_ALREADY_EXISTS")
    if not out.parent.is_dir():
        raise ValueError("OUTPUT_PARENT_MISSING")
    return out


def value(x):
    return "" if x is None else str(x)


def verify_ledger(qeax, ledger, summary, expected):
    """Check every ledger ID, raw source field, status and summary; never print rows."""
    headers = {
        "ea_guid": "source_guid", "Start_Object_ID": "raw_from",
        "End_Object_ID": "raw_to", "Direction": "source_direction",
        "SourceRole": "source_role", "DestRole": "target_role",
        "SourceCard": "source_cardinality", "DestCard": "target_cardinality",
        "SourceIsAggregate": "source_aggregation_flag",
        "DestIsAggregate": "target_aggregation_flag",
    }
    statuses = collections.Counter()
    rules = collections.Counter()
    diagnostics = collections.Counter()
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri() + "?mode=ro", uri=True) as db:
        db.row_factory = sqlite3.Row
        q = "SELECT " + ",".join(SOURCE_COLUMNS) + " FROM t_connector ORDER BY Connector_ID"
        source = db.execute(q)
        with pathlib.Path(ledger).open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames != list(REQUIRED_FIELDS):
                raise ValueError("LEDGER_SCHEMA_MISMATCH")
            count = 0
            for original in source:
                row = next(reader, None)
                if row is None:
                    raise ValueError("MISSING_SOURCE_LEDGER_ROW")
                if None in row or not row["source_pk"] or not row["status"]:
                    raise ValueError("INCOMPLETE_LEDGER_ROW")
                if row["source_pk"] != value(original["Connector_ID"]):
                    raise ValueError("LEDGER_ID_OR_ORDER_MISMATCH")
                for source_col, ledger_col in headers.items():
                    if row[ledger_col] != value(original[source_col]):
                        raise ValueError("SOURCE_EVIDENCE_MISMATCH:" + ledger_col)
                family = value(original["Connector_Type"]) + (
                    ":" + value(original["Stereotype"]) if original["Stereotype"] else "")
                if row["family"] != family:
                    raise ValueError("SOURCE_FAMILY_MISMATCH")
                # Approved Phase 8 keeps raw endpoint order until role attestation.
                if row["role"] != "approved-group-review":
                    raise ValueError("UNAPPROVED_ROLE_REINTERPRETATION")
                if (row["normalized_from"], row["normalized_to"]) != (
                    row["raw_from"], row["raw_to"]):
                    raise ValueError("UNATTESTED_ENDPOINT_REORIENTATION")
                if row["status"] not in ("deferred_review", "evidence_only"):
                    raise ValueError("UNAUTHORIZED_ROW_DISPOSITION")
                statuses[row["status"]] += 1
                rules[row["rule"] or "(none)"] += 1
                diagnostics.update(filter(None, row["diagnostics"].split(";")))
                count += 1
            if next(reader, None) is not None:
                raise ValueError("EXTRA_LEDGER_ROW")
    if count != expected or count != summary.get("total"):
        raise ValueError("SOURCE_LEDGER_COUNT_MISMATCH")
    if dict(statuses) != summary.get("status") or dict(rules) != summary.get("rule_candidates"):
        raise ValueError("SUMMARY_DISPOSITION_MISMATCH")
    if dict(diagnostics) != summary.get("diagnostics"):
        raise ValueError("SUMMARY_DIAGNOSTICS_MISMATCH")
    if (summary.get("policy_mode") != "approved_exact_groups" or
            summary.get("native_certified") != 0 or
            summary.get("native_emission_authorized") is not False or
            summary.get("ea_diagrams_processed") != 0):
        raise ValueError("UNAPPROVED_PHASE8_OUTPUT")
    return count


def execute(qeax, out, *, expected_counts=None, registry=REGISTRY, expected_sha256=None):
    """Commit private ledger only after strict source, schema, row and hash checks.

    expected_counts is solely for synthetic test fixtures; normal CLI pins
    the selected reduced QEAX profile through the existing V2 preflight.
    """
    qeax = pathlib.Path(qeax).resolve()
    out = ensure_private_destination(out)
    preflight = load_module("v2_source_preflight", PREFLIGHT)
    normalizer = load_module("v2_phase8_normalizer", PHASE8)
    original_profile = preflight.PROFILE
    if expected_counts is not None:
        if set(expected_counts) != set(original_profile):
            raise ValueError("INVALID_TEST_PROFILE")
        preflight.PROFILE = dict(expected_counts)
    try:
        profile = preflight.inspect(qeax, strict=False)
    finally:
        preflight.PROFILE = original_profile
    if profile["status"] != "PASS":
        return {"status": "BLOCKED", "reason": "SOURCE_PROFILE_DRIFT",
                "counts": profile["counts"], "ledgerWritten": False}
    # Refuse any provisional or diagram-aware registry before staging a ledger.
    api = normalizer._approved_module()
    approved = api.load_registry(registry)
    if approved["metadata"]["ea_diagrams_enabled"]:
        raise ValueError("DIAGRAM_SCOPE_FORBIDDEN")
    before = normalizer.input_attestation(qeax, registry)
    if expected_sha256 is not None and before["source_sha256"] != expected_sha256:
        return {"status": "BLOCKED", "reason": "SOURCE_SNAPSHOT_HASH_MISMATCH",
                "ledgerWritten": False}
    stage = pathlib.Path(tempfile.mkdtemp(prefix=".v2-approved-stage-", dir=out.parent))
    try:
        summary = normalizer.reconcile(qeax, registry, stage)
        ledger = stage / "local_only_phase8_ledger.csv"
        aggregate = stage / "aggregate_only.json"
        if not ledger.is_file() or not aggregate.is_file():
            raise ValueError("MISSING_STAGED_LEDGER")
        if json.loads(aggregate.read_text(encoding="utf-8")) != summary:
            raise ValueError("AGGREGATE_ARTIFACT_MISMATCH")
        count = verify_ledger(qeax, ledger, summary, profile["counts"]["connectors"])
        after = normalizer.input_attestation(qeax, registry)
        if after != before:
            raise ValueError("SOURCE_OR_RULES_CHANGED_DURING_RUN")
        (stage / "input_attestation.local.json").write_text(
            json.dumps(before, indent=2) + "\n", encoding="utf-8")
        (stage / "gate.local.json").write_text(
            json.dumps({"schema": "mdse-v2-approved-phase8-gate/1",
                        "selected_counts": profile["counts"],
                        "verified_connector_rows": count,
                        "verified": True, "native_certified": 0,
                        "ea_diagrams_processed": 0}, indent=2) + "\n",
            encoding="utf-8")
        if out.exists():
            raise ValueError("OUTPUT_ALREADY_EXISTS")
        stage.rename(out)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return {"status": "RECONCILED_EVIDENCE_ONLY", "ledgerWritten": True,
            "verified_connector_rows": count, "aggregate": summary,
            "nativeCertified": 0, "eaDiagramsProcessed": 0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qeax", type=pathlib.Path, required=True)
    ap.add_argument("--out", type=pathlib.Path, required=True)
    ap.add_argument("--source-sha256", required=True,
                    help="Previously selected private QEAX SHA-256 fingerprint")
    args = ap.parse_args()
    result = execute(args.qeax, args.out, expected_sha256=args.source_sha256)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "RECONCILED_EVIDENCE_ONLY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
