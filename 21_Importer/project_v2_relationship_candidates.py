#!/usr/bin/env python3
"""Read-only, bounded EA connector candidate projection for SysML v2 review.

Emits aggregate candidate/gate counts only. This is NOT a SysML v2 exporter.
"""
import argparse
import collections
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
RULES = ROOT / "24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json"


def family_of(kind, stereotype):
    return (kind or "").strip() + ":" + (stereotype or "").strip()


def project(source, limit=100, registry_path=RULES):
    if not 1 <= limit <= 1000:
        raise ValueError("INVALID_LIMIT")
    path = pathlib.Path(source).resolve()
    if not path.is_file():
        raise ValueError("SOURCE_NOT_FOUND")
    registry = json.loads(pathlib.Path(registry_path).read_text(encoding="utf-8"))
    if (registry.get("schema") != "mdse-v2-semantic-rules/0.2"
            or registry.get("automaticNativeEmission") is not False):
        raise ValueError("INVALID_OR_UNSAFE_REGISTRY")
    rules = registry.get("relationshipRules")
    if not isinstance(rules, list) or any(
        r.get("emission") != "deferred_pending_evidence_and_parser"
        or not isinstance(r.get("family"), str) for r in rules
    ):
        raise ValueError("UNSAFE_RELATIONSHIP_RULES")
    families = [r["family"] for r in rules]
    if len(families) != len(set(families)):
        raise ValueError("AMBIGUOUS_RELATIONSHIP_RULES")

    with sqlite3.connect(path.as_uri() + "?mode=ro", uri=True) as db:
        columns = {x[1] for x in db.execute("PRAGMA table_info(t_connector)")}
        required = {"Connector_ID", "Connector_Type", "Stereotype"}
        if not required.issubset(columns):
            raise ValueError("UNSUPPORTED_CONNECTOR_SCHEMA")
        rows = db.execute(
            "SELECT Connector_Type, Stereotype FROM t_connector "
            "ORDER BY Connector_ID LIMIT ?", (limit,)
        ).fetchall()

    index = {r["family"]: r for r in rules}
    candidates = collections.Counter()
    gates = collections.Counter()
    dispositions = collections.Counter()
    for kind, stereo in rows:
        key = family_of(kind, stereo)
        rule = index.get(key)
        # Only generic *empty-stereotype* family fallback is allowed;
        # a named stereotype with no exact rule must remain unmatched.
        if rule is None and not (stereo or "").strip():
            rule = index.get((kind or "").strip() + ":")
        if rule is None:
            candidates["UNMATCHED_REVIEW"] += 1
            gates["requires_semantic_review"] += 1
            dispositions["review"] += 1
            continue
        candidates[str(rule.get("nativeCandidate") or "NO_NATIVE_CANDIDATE")] += 1
        gates[str(rule.get("gate") or "UNSPECIFIED")] += 1
        dispositions[str(rule.get("sourceDisposition") or "review")] += 1
    return {
        "schema": "mdse-v2-relationship-candidate-review/1",
        "source_connectors": len(rows),
        "candidate_targets": dict(sorted(candidates.items())),
        "evidence_gates": dict(sorted(gates.items())),
        "source_dispositions": dict(sorted(dispositions.items())),
        "deferred_rows": len(rows),
        "native_relationships_emitted": 0,
        "source_data_modified": False,
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("qeax")
    ap.add_argument("--limit", type=int, default=100)
    args = ap.parse_args()
    try:
        print(json.dumps(project(args.qeax, args.limit), indent=2))
    except (ValueError, OSError, sqlite3.DatabaseError) as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}), file=sys.stderr)
        sys.exit(1)
