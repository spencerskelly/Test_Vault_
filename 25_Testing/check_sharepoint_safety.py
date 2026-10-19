#!/usr/bin/env python3
"""Preflight a generated vault folder for SharePoint / OneDrive sync safety. Read-only.

The final vault lives in SharePoint. Ruleset W-382 removed any total path-length limit
from the importer, so this is the replacement gate: it REPORTS, it never shortens a name.

Limits, from Microsoft "Restrictions and limitations in OneDrive and SharePoint"
(https://support.microsoft.com/en-us/help/3125202), read 2026-10-18:
  - decoded file path including file name: 400 characters (SharePoint in Microsoft 365)
  - OneDrive sync root path + relative path: 520 characters
  - Windows Explorer: 256 usable characters
  - each file or folder name: 255 characters when synced
  - invalid characters  " * : < > ? / \\ |  and leading/trailing spaces
  - invalid names: .lock CON PRN AUX NUL COM0-9 LPT0-9 _vti_ desktop.ini, names starting ~$
  - `forms` is not a supported folder name at a library root
  - sync no more than 300,000 files in total (recommended)
The 5,000 item threshold is a per-view display threshold; the source we could read is a
Microsoft Q&A answer, not primary documentation, so treat that figure as advisory.

Usage:
  python3 25_Testing/check_sharepoint_safety.py VAULT_DIR [--sync-root-length N] [--path-limit N]
Exit status 1 when any blocking finding exists.
"""
from pathlib import Path
import argparse, collections, re, sys

PATH_LIMIT = 400
SYNC_LIMIT = 520
EXPLORER_LIMIT = 256
SEGMENT_LIMIT = 255
FOLDER_ITEM_ADVISORY = 5000
SYNC_FILE_ADVISORY = 300_000
INVALID = set('"*:<>?/\\|')
RESERVED = {".lock", "con", "prn", "aux", "nul", "desktop.ini",
            *{f"com{i}" for i in range(10)}, *{f"lpt{i}" for i in range(10)}}
SKIP_DIRS = {".git"}


def segment_problems(name: str):
    p = []
    bad = sorted(set(name) & INVALID)
    if bad:
        p.append(f"invalid character(s) {''.join(bad)}")
    if name != name.strip():
        p.append("leading or trailing space")
    if name.endswith("."):
        p.append("trailing period (not documented by Microsoft; Windows strips it)")
    low = name.lower()
    stem = low.split(".")[0]
    if low in RESERVED or stem in RESERVED:
        p.append("reserved name")
    if "_vti_" in low:
        p.append("contains _vti_")
    if name.startswith("~$"):
        p.append("starts with ~$")
    if len(name) > SEGMENT_LIMIT:
        p.append(f"{len(name)} characters (limit {SEGMENT_LIMIT})")
    return p


def scan(root: Path, sync_root_length: int = 0, path_limit: int = PATH_LIMIT):
    blocking, advisory = [], []
    files, per_folder, lowered = 0, collections.Counter(), collections.defaultdict(list)
    longest = (0, "")
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        rels = rel.as_posix()
        for seg in rel.parts[-1:]:
            for why in segment_problems(seg):
                blocking.append((rels, why))
        if len(rel.parts) == 1 and p.is_dir() and p.name.lower() == "forms":
            blocking.append((rels, "`forms` is not supported as a library-root folder"))
        lowered[rels.lower()].append(rels)
        per_folder[rel.parent.as_posix()] += 1
        if p.is_file():
            files += 1
            n = len(rels) + 1  # leading slash of the library-relative path
            if n > longest[0]:
                longest = (n, rels)
            if n > path_limit:
                blocking.append((rels, f"path is {n} characters (SharePoint limit {path_limit})"))
            if sync_root_length and sync_root_length + n > SYNC_LIMIT:
                blocking.append((rels, f"sync root {sync_root_length} + path {n} = {sync_root_length + n} (limit {SYNC_LIMIT})"))
            elif n > EXPLORER_LIMIT:
                advisory.append((rels, f"{n} characters exceeds Windows Explorer's {EXPLORER_LIMIT}"))
    for key, names in lowered.items():
        if len(names) > 1:
            blocking.append((names[0], "case-insensitive collision with " + ", ".join(names[1:])))
    for folder, n in per_folder.items():
        if n > FOLDER_ITEM_ADVISORY:
            advisory.append((folder or ".", f"{n} items in one folder (advisory per-view threshold {FOLDER_ITEM_ADVISORY})"))
    if files > SYNC_FILE_ADVISORY:
        advisory.append((".", f"{files} files exceeds the {SYNC_FILE_ADVISORY} sync recommendation"))
    return {"files": files, "longest": longest, "blocking": blocking, "advisory": advisory}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vault")
    ap.add_argument("--sync-root-length", type=int, default=0,
                    help="length of the local OneDrive sync folder path your users have (e.g. 'C:\\Users\\x\\Co\\Site - Lib\\')")
    ap.add_argument("--path-limit", type=int, default=PATH_LIMIT)
    a = ap.parse_args()
    r = scan(Path(a.vault), a.sync_root_length, a.path_limit)
    for rel, why in r["blocking"]:
        print(f"BLOCKING  {rel}: {why}")
    for rel, why in r["advisory"]:
        print(f"advisory  {rel}: {why}")
    print(f"{r['files']} files; longest path {r['longest'][0]} characters; "
          f"{len(r['blocking'])} blocking, {len(r['advisory'])} advisory")
    return 1 if r["blocking"] else 0


if __name__ == "__main__":
    sys.exit(main())
