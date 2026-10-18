#!/usr/bin/env python3
"""Fail-closed, idempotent importer CI path migration. Run in Test_Vault_ checkout."""
from pathlib import Path
import argparse
import sys

REPLACEMENTS = {
    '"Importer/**"': '"11_Importer/**"',
    '"Base Vault/**"': '"10_Base Vault/**"',
    '"00_Workspace/**"': '"55_Workspace/**"',
    '"Importer/': '"11_Importer/',
    '"Base Vault/': '"10_Base Vault/',
    '"00_Workspace/': '"55_Workspace/',
}

def rewrite(src: str) -> str:
    out = src
    for a, b in REPLACEMENTS.items():
        out = out.replace(a, b)
    if '"Importer/**"' in out or '"Base Vault/**"' in out or '"00_Workspace/**"' in out:
        raise ValueError("Old CI trigger remains")
    for item in ["11_Importer/**", "10_Base Vault/**", "55_Workspace/**"]:
        if item not in out:
            raise ValueError("Required CI trigger missing: " + item)
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("checkout", type=Path)
    parser.add_argument("--apply", action="store_true", help="Write only after reviewing dry-run")
    args = parser.parse_args()
    p = args.checkout / ".github/workflows/importer-candidate.yml"
    if not p.is_file():
        sys.exit("BLOCKER CI_WORKFLOW_NOT_FOUND: " + str(p))
    original = p.read_text()
    updated = rewrite(original)
    if original == updated:
        print("PASS: importer CI path migration already applied")
    elif args.apply:
        p.write_text(updated)
        print("UPDATED: " + str(p))
    else:
        print("DRY RUN: " + str(p) + " needs path migration; rerun with --apply")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
