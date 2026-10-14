#!/usr/bin/env python3
"""Read-only inventory of candidate real-QEAX inputs and generated-vault evidence.

This tool finds candidates; it never assumes that the source QEAX and vault match.
"""
import argparse
import json
import os
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
        # os.walk prunes subtrees before traversal, unlike rglob plus a depth filter.
        for directory, dirs, files in os.walk(base, topdown=True, followlinks=False):
            current = Path(directory)
            depth = len(current.relative_to(base).parts)
            dirs[:] = sorted(
                name for name in dirs
                if depth < args.max_depth
                and not (current / name).is_symlink()
                and name not in {".git", "node_modules", ".trash"}
            )
            if (current / REVIEW).is_file() and (current / MAP).is_file():
                key = str(current)
                if key not in seen:
                    vaults.append({"path": key, "review": str(current / REVIEW),
                                   "source_map": str(current / MAP)})
                    seen.add(key)
            if depth >= args.max_depth:
                continue
            for name in sorted(files):
                path = current / name
                if path.is_symlink() or path.suffix.lower() not in (".qeax", ".qea"):
                    continue
                key = str(path)
                if key not in seen:
                    try:
                        source.append({"path": key, "bytes": path.stat().st_size})
                        seen.add(key)
                    except OSError as exc:
                        failures.append(f"Cannot inspect {path}: {exc}")
    report = {"sources": source, "candidate_vaults": vaults, "errors": failures,
              "pairing_verified": False,
              "note": "Candidate discovery only. Match provenance and run step120 acceptance on a verified pair."}
    print(json.dumps(report, indent=2))
    return 2 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
