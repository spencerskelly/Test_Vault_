#!/usr/bin/env python3
"""Read-only, fail-closed operator gate for a paired QEAX and generated vault."""
import argparse
import hashlib
import json
import sqlite3
import subprocess
import sys
import zipfile
from pathlib import Path

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qeax", type=Path, required=True)
    ap.add_argument("--vault", type=Path, required=True)
    ap.add_argument("--source-zip", type=Path)
    ap.add_argument("--results", type=Path, required=True)
    args = ap.parse_args()
    repo = Path(__file__).resolve().parents[2]
    checks = [
        repo / "Importer/Testing/v0.8.19/imp011_binding_review_acceptance.py",
        repo / "Importer/Testing/v0.8.19/imp011_canonical_equals_acceptance.py",
        repo / "66_Testing/consolidation/imp011_topology_acceptance_v2.py",
    ]
    needed = [args.qeax, args.vault / "99_System/11_Import/Review - Equals Direction.csv",
              args.vault / "99_System/11_Import/Local Model Source Map.csv", *checks]
    failures = [str(p) + ": missing" for p in needed if not p.exists()]
    report = {"qeax": str(args.qeax), "vault": str(args.vault),
              "source_zip": str(args.source_zip) if args.source_zip else None,
              "files": {}, "checks": [], "failures": failures}
    for p in needed:
        if p.is_file():
            report["files"][str(p)] = {"sha256": sha256(p), "size": p.stat().st_size}
    if args.source_zip:
        if not args.source_zip.is_file():
            failures.append("source ZIP missing")
        else:
            report["files"][str(args.source_zip)] = {"sha256": sha256(args.source_zip),
                                                       "size": args.source_zip.stat().st_size}
            try:
                with zipfile.ZipFile(args.source_zip) as z:
                    invalid = z.testzip()
                    if invalid:
                        failures.append("corrupt ZIP member: " + invalid)
                    report["zip_members"] = z.namelist()
            except (OSError, zipfile.BadZipFile) as e:
                failures.append("ZIP validation error: " + str(e))
    if args.qeax.is_file():
        try:
            with sqlite3.connect("file:" + args.qeax.resolve().as_posix() + "?mode=ro", uri=True) as db:
                integrity = db.execute("PRAGMA integrity_check").fetchone()[0]
                count = db.execute("SELECT COUNT(*) FROM t_connector WHERE Connector_Type='Connector' AND Stereotype='BindingConnector'").fetchone()[0]
            report["sqlite_integrity"] = integrity
            report["binding_connector_count"] = count
            if integrity != "ok" or count != 249:
                failures.append("QEAX integrity or expected BindingConnector count mismatch")
        except sqlite3.Error as e:
            failures.append("QEAX database error: " + str(e))
    if not failures:
        for path in checks:
            result = subprocess.run([sys.executable, str(path), str(args.qeax), str(args.vault)],
                                    capture_output=True, text=True, check=False)
            report["checks"].append({"script": str(path), "exit_code": result.returncode,
                                     "stdout": result.stdout, "stderr": result.stderr})
            if result.returncode:
                failures.append("validator failed: " + path.name)
    report["result"] = "FAIL" if failures else "PASS"
    args.results.mkdir(parents=True, exist_ok=True)
    out = args.results / "qeax_imp011_acceptance.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(report["result"], out)
    return 2 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
