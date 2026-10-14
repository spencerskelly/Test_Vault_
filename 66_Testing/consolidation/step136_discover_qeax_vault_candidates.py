#!/usr/bin/env python3
"""Read-only inventory of candidate real-QEAX inputs and generated-vault evidence.

This tool finds candidates; it never assumes that the source QEAX and vault match.
"""
import argparse
import json
from pathlib import Path

REVIEW = Path("99_System/11_Import/Review - Equals Direction.csv")
MAP = Path("99_System/11_Import/Local Model Source Map.csv")

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("roots", nargs="+", type=Path, help="Existing search directories")
    ap.add_argument("--max-depth", type=int, default=6)
    args = ap.parse_args()
    if args.max_depth < 0:
        ap.error("--max-depth must be >= 0")
    source = []
    vaults = []
    failures = []
    seen = set()
    for root in args.roots:
        if not root.is_dir():
            failures.append(f"Not a directory: {root}")
            continue
        base = root.resolve()
        for current in [base, *base.rglob("*")]:
            if current.is_symlink() or not current.exists():
                continue
            try:
                rel = current.relative_to(base)
            except ValueError:
                continue
            if len(rel.parts) > args.max_depth:
                continue
            if current.is_file() and current.suffix.lower() in (".qeax", ".qea"):
                key = str(current)
                if key not in seen:
                    source.append({"path": key, "bytes": current.stat().st_size})
                    seen.add(key)
            if current.is_dir() and (current / REVIEW).is_file() and (current / MAP).is_file():
                key = str(current)
                if key not in seen:
                    vaults.append({"path": key, "review": str(current / REVIEW), "source_map": str(current / MAP)})
                    seen.add(key)
    report = {"sources": source, "candidate_vaults": vaults, "errors": failures,
              "pairing_verified": False,
              "note": "Candidate discovery only. Match provenance and run step120 acceptance on a verified pair."}
    print(json.dumps(report, indent=2))
    return 2 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
