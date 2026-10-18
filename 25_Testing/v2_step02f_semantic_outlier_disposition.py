#!/usr/bin/env python3
"""STEP-02F: conservative MDSE v2 semantic disposition over a *verified private* Phase 8 ledger.
No QEAX queries, diagrams, model export, native emission, or silent link deletion.
"""
import argparse
import collections
import csv
import hashlib
import json
import pathlib
import shutil
import tempfile

FIELDS = (
    "source_pk", "source_guid", "raw_from", "raw_to", "family", "rule",
    "role", "status", "normalized_from", "normalized_to", "source_kind",
    "target_kind", "diagnostics", "source_direction", "source_role",
    "target_role", "source_cardinality", "target_cardinality",
    "raw_source_type", "raw_source_stereotype", "raw_target_type",
    "raw_target_stereotype", "source_aggregation_flag", "target_aggregation_flag",
)
NON_NATIVE = {
    "InformationItem", "Note", "Issue", "Change", "Decision", "Text",
    "Text:NavigationCell", "Artifact:Image", "Artifact:Document",
    "Sequence", "ProxyConnector", "Boundary", "Package",
}
CONDITIONAL = {"Trigger", "Synchronization"}
REFERENCE_ONLY = {"NoteLink", "Sequence"}
MDSE_REFERENCE_FAMILIES = {
    "Dependency", "Dependency:trace", "Abstraction:trace",
    "Dependency:refine", "Abstraction:Refine",
}
OUTPUT_FIELDS = ("source_pk", "source_guid", "family", "disposition", "reason",
                 "raw_from", "raw_to", "source_direction")

def family(type_, stereo):
    return type_ + (":" + stereo if stereo else "")

def classify(row):
    """Evidence-specific routing; NEVER returns 'native accepted'."""
    rel = row["family"]
    source = family(row["raw_source_type"], row["raw_source_stereotype"])
    target = family(row["raw_target_type"], row["raw_target_stereotype"])
    non_native = source in NON_NATIVE or target in NON_NATIVE
    conditional = source in CONDITIONAL or target in CONDITIONAL
    reverse = row["source_direction"] == "Destination -> Source"

    if rel in REFERENCE_ONLY:
        return "reference_only", "Approved non-native source reference; preserve on owning note"
    if rel == "Abstraction:allocate" and reverse and {source,target} == {
            "Trigger", "Requirement:requirement"}:
        return "flaglink_candidate", "OUTLIER-DIR-01: reversed Trigger/Requirement allocation"
    if rel == "Dependency:trace" and reverse and "Boundary" in (source,target):
        return "boundary_reference", "OUTLIER-DIR-02: retain reversed trace in grouped Boundary note"
    if rel == "Aggregation" and source == "Change" and target == "Change":
        return "mdse_hierarchy", "Approved Change hierarchy is MDSE-only, not PartUsage"
    if rel == "Aggregation" and "InformationItem" in (source,target):
        return "flaglink_candidate", "OUTLIER-AGG-01: incompatible InformationItem aggregation"
    if rel == "Aggregation":
        return "aggregation_group_gate", "Apply existing approved 2267-row typed-usage/56-flagLink group ledger"
    if rel in {"Dependency:deriveReqt", "Dependency:RecoveryRequirement",
               "Abstraction:Derive", "Realisation:deriveReqt"} and non_native:
        return "flaglink_candidate", "Non-native endpoint cannot establish requirement derivation"
    if non_native and rel in MDSE_REFERENCE_FAMILIES:
        return "mdse_descriptive_link", "Retain source relation in MDSE note/attachment owner with provenance"
    if non_native and rel == "Abstraction:allocate":
        return "semantic_role_review", "Non-native allocation: MDSE link or flagLink after role evidence"
    if non_native and rel == "ControlFlow":
        return "workflow_context_review", "Decision/Issue behavior must be preserved in workflow context"
    if non_native:
        return "non_native_context_review", "Check approved note/link role before native fallback"
    if conditional:
        return "conditional_usage_review", "Resolve Trigger/Synchronization within owning behavioral context"
    if rel in ("Association", "Connector"):
        return "connection_evidence_review", "Native ConnectionUsage only when physical/port evidence is present"
    if row["source_direction"] != "Source -> Destination":
        return "direction_evidence_review", "Cannot silently assert directed native semantics"
    return "native_candidate_unverified", "Approved family candidate; native parser/use-site acceptance pending"

def sha256_file(path):
    d = hashlib.sha256()
    with pathlib.Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            d.update(chunk)
    return d.hexdigest()

def reconcile(gated_dir, out_dir, *, repo_root=None):
    gated_dir, out_dir = pathlib.Path(gated_dir).resolve(), pathlib.Path(out_dir).resolve()
    if out_dir.exists(): raise ValueError("OUTPUT_ALREADY_EXISTS")
    if not out_dir.parent.is_dir(): raise ValueError("OUTPUT_PARENT_MISSING")
    if repo_root is not None:
        root = pathlib.Path(repo_root).resolve()
        if out_dir == root or root in out_dir.parents:
            raise ValueError("PRIVATE_OUTPUT_MUST_BE_OUTSIDE_REPOSITORY")
    gate = json.loads((gated_dir/"gate.local.json").read_text())
    summary = json.loads((gated_dir/"aggregate_only.json").read_text())
    attestation = json.loads((gated_dir/"input_attestation.local.json").read_text())
    if not (gate.get("verified") is True and gate.get("native_certified") == 0
            and gate.get("ea_diagrams_processed") == 0
            and summary.get("policy_mode") == "approved_exact_groups"
            and summary.get("native_certified") == 0
            and summary.get("native_emission_authorized") is False
            and summary.get("ea_diagrams_processed") == 0
            and attestation.get("native_certified") == 0
            and len(attestation.get("source_sha256", "")) == 64):
        raise ValueError("VERIFIED_APPROVED_PHASE8_GATE_REQUIRED")
    expected = gate["verified_connector_rows"]
    if expected != summary.get("total") or expected != gate["selected_counts"]["connectors"]:
        raise ValueError("GATED_COUNTS_DISAGREE")
    stage = pathlib.Path(tempfile.mkdtemp(prefix=".step02f-private-", dir=out_dir.parent))
    counts, reasons, families = collections.Counter(), collections.Counter(), collections.Counter()
    seen_pk, seen_guid = set(), set()
    try:
        with (gated_dir/"local_only_phase8_ledger.csv").open(newline="", encoding="utf-8") as inp, (
                stage/"semantic_disposition.local.csv").open("w", newline="", encoding="utf-8") as dest:
            reader = csv.DictReader(inp)
            if reader.fieldnames != list(FIELDS): raise ValueError("PHASE8_SCHEMA_MISMATCH")
            writer = csv.DictWriter(dest, fieldnames=OUTPUT_FIELDS)
            writer.writeheader()
            n = 0
            for r in reader:
                pk, guid = r["source_pk"], r["source_guid"]
                if not pk or not guid or pk in seen_pk or guid in seen_guid:
                    raise ValueError("BAD_OR_DUPLICATE_SOURCE_IDENTITY")
                if r["status"] not in ("deferred_review", "evidence_only"):
                    raise ValueError("UNAPPROVED_PHASE8_DISPOSITION")
                if not r["raw_source_type"] or not r["raw_target_type"]:
                    raise ValueError("MISSING_ENDPOINT_TYPE")
                if r["raw_from"] != r["normalized_from"] or r["raw_to"] != r["normalized_to"]:
                    raise ValueError("UNATTESTED_ORIENTATION")
                seen_pk.add(pk); seen_guid.add(guid)
                disposition, reason = classify(r)
                if (r["status"] == "evidence_only") != (disposition == "reference_only"):
                    raise ValueError("REFERENCE_ONLY_STATUS_MISMATCH")
                writer.writerow({**{k:r[k] for k in ("source_pk","source_guid","family",
                               "raw_from","raw_to","source_direction")},
                                 "disposition":disposition,"reason":reason})
                counts[disposition]+=1; reasons[reason]+=1; families[r["family"]]+=1; n+=1
        if n != expected: raise ValueError("SOURCE_LEDGER_COUNT_MISMATCH")
        output = {
            "schema":"mdse-v2-step02f-semantic-disposition/1",
            "status":"EVIDENCE_CLASSIFIED_NOT_NATIVE_CERTIFIED",
            "source_connectors":n, "exclusive_dispositions":dict(sorted(counts.items())),
            "disposition_total":sum(counts.values()),
            "families_observed":len(families),
            "flaglink_candidates_not_final":counts["flaglink_candidate"],
            "native_certified":0,"native_emission_authorized":False,
            "ea_diagrams_processed":0,
            "phase8_ledger_sha256":sha256_file(gated_dir/"local_only_phase8_ledger.csv"),
            "source_sha256_private_attestation_only":attestation["source_sha256"],
            "caveat":"Candidate bucket is not an issued flagLink or parser-accepted SysML relationship.",
        }
        (stage/"aggregate.local.json").write_text(json.dumps(output, indent=2)+"\n")
        stage.rename(out_dir)
        return output
    finally:
        if stage.exists(): shutil.rmtree(stage)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--gated-dir", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    p.add_argument("--repo-root", type=pathlib.Path)
    args = p.parse_args()
    output = reconcile(args.gated_dir, args.out, repo_root=args.repo_root)
    print(json.dumps({k:v for k,v in output.items()
                      if k not in ("source_sha256_private_attestation_only",
                                   "phase8_ledger_sha256")}, indent=2))

if __name__ == "__main__": main()
