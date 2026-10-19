#!/usr/bin/env python3
"""STEP-04 local-only, read-only reconciliation of an already produced JSONL ledger.

Does not translate EA models and never writes source rows to the repository.
"""
import argparse
import collections
import json
from pathlib import Path

REQUIRED = ("source_system", "fixture_hash", "source_table", "source_pk",
            "rule_id", "rule_version", "disposition", "evidence")
DISPOSITIONS = {"native", "alias_merged", "evidence_only", "deferred_review",
                "excluded_by_policy", "error"}
TABLES = {"t_object", "t_connector"}
TARGETED = {"native", "alias_merged"}

def audit(records, expected=None):
    counts = collections.Counter()
    reasons = collections.Counter()
    seen = set()
    failures = []
    fixture = None
    for line_no, row in enumerate(records, 1):
        if not isinstance(row, dict):
            failures.append((line_no, "NOT_OBJECT")); continue
        missing = [k for k in REQUIRED if row.get(k) in (None, "")]
        if missing:
            failures.append((line_no, "MISSING:" + ",".join(missing)))
        table = row.get("source_table")
        if table not in TABLES:
            failures.append((line_no, "BAD_TABLE")); continue
        key = (table, str(row.get("source_pk")))
        if key in seen:
            failures.append((line_no, "DUPLICATE_SOURCE"))
        seen.add(key)
        counts[table] += 1
        disp = row.get("disposition")
        if disp not in DISPOSITIONS:
            failures.append((line_no, "BAD_DISPOSITION"))
        counts["disposition:" + str(disp)] += 1
        if disp in TARGETED and not row.get("target_stable_id"):
            failures.append((line_no, "MISSING_TARGET_ID"))
        if disp in ("deferred_review", "excluded_by_policy", "error", "evidence_only"):
            if not row.get("diagnostic_code") and not row.get("operator_action"):
                failures.append((line_no, "MISSING_REASON_OR_ACTION"))
        if row.get("fixture_hash"):
            if fixture is None: fixture = row["fixture_hash"]
            elif fixture != row["fixture_hash"]:
                failures.append((line_no, "MIXED_FIXTURE"))
        if row.get("diagnostic_code"):
            reasons[str(row["diagnostic_code"])] += 1
    if expected:
        for table, count in expected.items():
            if counts[table] != count:
                failures.append((0, "COUNT_MISMATCH:" + table))
    return {"passed": not failures, "rows": len(seen), "counts": dict(sorted(counts.items())),
            "diagnostics": dict(sorted(reasons.items())),
            "failures": [{"line": ln, "code": code} for ln, code in failures]}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", required=True, type=Path, help="Local private JSONL ledger")
    parser.add_argument("--objects", type=int)
    parser.add_argument("--connectors", type=int)
    args = parser.parse_args()
    expected = {k: v for k, v in (("t_object", args.objects),
                                  ("t_connector", args.connectors)) if v is not None}
    with args.ledger.open(encoding="utf-8") as f:
        records = (json.loads(line) for line in f if line.strip())
        result = audit(records, expected)
    print(json.dumps(result, sort_keys=True, indent=2))
    raise SystemExit(0 if result["passed"] else 1)

if __name__ == "__main__":
    main()
