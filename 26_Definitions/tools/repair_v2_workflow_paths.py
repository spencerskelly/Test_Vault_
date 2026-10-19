#!/usr/bin/env python3
"""Repair stale pre-migration paths in CI workflows and kit scripts.

Uses the exact old->new file moves recorded in
26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json (path_moves).
Only exact file paths are rewritten. Directory-level or glob references are
reported, never guessed, because files from one old folder were split between
the active v2 tree and 100_Archive/V1.

Idempotent. `--check` writes nothing and exits 1 if any mappable stale
reference remains (usable in CI).
"""
from pathlib import Path
import argparse, json, re, sys

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json"
TARGETS = [*sorted((ROOT / ".github/workflows").glob("*.yml")),
           ROOT / "25_Testing/check_v2_import_kit.py"]
LEGACY = ("00_Workspace", "10_Base Vault", "11_Importer", "13_Bootstrap",
          "14_Workbench", "15_Testing", "16_Definitions")
# A legacy folder name is only "stale" when it is not already inside another path.
STALE_DIR = re.compile(r"(?<![\w/])(?:%s)(?:/[^\s'\"`),;:\\]*)?" % "|".join(map(re.escape, LEGACY)))


def load_moves():
    moves = json.loads(MANIFEST.read_text(encoding="utf-8"))["path_moves"]
    return sorted(moves.items(), key=lambda kv: len(kv[0]), reverse=True)


def repair(text, moves):
    done = 0
    for old, new in moves:
        pat = re.compile(r"(?<![\w/])" + re.escape(old))
        text, n = pat.subn(lambda _m, new=new: new, text)
        done += n
    return text, done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="do not write; exit 1 if mappable refs remain")
    args = ap.parse_args()
    moves = load_moves()
    mappable = 0
    unmapped = {}
    for path in TARGETS:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        revised, n = repair(text, moves)
        mappable += n
        if n and not args.check:
            path.write_text(revised, encoding="utf-8")
        # Whatever stale folder reference is left after the exact-file repair needs a human decision.
        left = sorted({m.group(0) for m in STALE_DIR.finditer(revised)})
        if left:
            unmapped[path.relative_to(ROOT).as_posix()] = left
        if n:
            print(f"{'would repair' if args.check else 'repaired'} {n:3d} refs  {path.relative_to(ROOT)}")
    print(f"\nmappable references {'found' if args.check else 'rewritten'}: {mappable}")
    if unmapped:
        print("\nNEEDS DECISION (directory/glob/unmapped references, not rewritten):")
        for f, refs in unmapped.items():
            for r in refs:
                print(f"  {f}: {r}")
    return 1 if (args.check and mappable) else 0


if __name__ == "__main__":
    sys.exit(main())
