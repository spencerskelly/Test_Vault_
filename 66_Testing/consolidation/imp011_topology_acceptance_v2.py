#!/usr/bin/env python3
"""Add vault-derived topology invariants to IMP-011 without altering its baseline."""
from __future__ import annotations
import argparse, csv, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from localmodel_topology_index_v3 import parse_index
from imp011_importer_owner_path_v1 import resolve_importer_owner

def check(vault: Path) -> list[str]:
    idx = parse_index(vault)
    errors = list(idx["errors"])
    review = vault / "99_System/11_Import/Review - Equals Direction.csv"
    with review.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    owners, boundary, connections, equality = (idx[k] for k in
        ("owners", "boundaries", "connections", "equality"))
    known_paths = set(owners.values()) | {c["owner"] for c in connections.values()}
    for row in rows:
        guid = row.get("ea_guid", "?")
        rel = row.get("actual_relation", "")
        owner = row.get("owner_note", "").strip()
        if rel in ("Interface.equals", "Connection.exposes"):
            try:
                owner = resolve_importer_owner(owner, known_paths)
            except ValueError as exc:
                errors.append(f"{guid}: {exc}")
                continue
        a, b = (row.get(key, "").strip() for key in ("start_local", "end_local"))
        if rel == "Interface.equals":
            if not a or not b or a == b:
                errors.append(f"{guid}: invalid equals endpoints")
                continue
            if owners.get(a) != owner or owners.get(b) != owner:
                errors.append(f"{guid}: equals endpoint owner mismatch")
            if (a, b) not in equality or (b, a) not in equality:
                errors.append(f"{guid}: missing symmetric local equality")
        elif rel == "Connection.exposes":
            conn_id = row.get("connection_local", "").strip()
            ep_id = row.get("exposes_local", "").strip()
            conn = connections.get(conn_id)
            if row.get("candidate_connection_count", "") != "1":
                errors.append(f"{guid}: ambiguous exposure")
            if not conn or conn["owner"] != owner:
                errors.append(f"{guid}: connection absent or wrong owner")
            if owners.get(ep_id) != owner or ep_id not in boundary:
                errors.append(f"{guid}: exposed endpoint not same-owner boundary")
            if conn and ep_id not in conn["exposes"]:
                errors.append(f"{guid}: exposure not present in Markdown")
            if conn and not ({a, b} & set(conn["endpoints"])):
                errors.append(f"{guid}: no binding end on connection")
            if a and b and ((a, b) in equality or (b, a) in equality):
                errors.append(f"{guid}: exposure also persisted as equals")
        elif rel == "":
            if a and b and ((a, b) in equality or (b, a) in equality):
                errors.append(f"{guid}: unresolved binding persisted as equals")
        else:
            errors.append(f"{guid}: unknown relation {rel!r}")
    return errors

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("qeax", type=Path)
    ap.add_argument("vault", type=Path)
    args = ap.parse_args()
    baseline = HERE.parents[1] / "Importer/Testing/v0.8.19/imp011_binding_review_acceptance.py"
    if not baseline.is_file():
        print(f"FAIL: baseline validator missing: {baseline}", file=sys.stderr)
        return 2
    result = subprocess.run([sys.executable, str(baseline), str(args.qeax), str(args.vault)])
    if result.returncode:
        return result.returncode
    failures = check(args.vault)
    for failure in failures[:100]:
        print("FAIL", failure)
    print(f"IMP-011 topology supplement: {'FAIL' if failures else 'PASS'} ({len(failures)} errors)")
    return 2 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
