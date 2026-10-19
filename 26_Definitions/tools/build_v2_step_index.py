#!/usr/bin/env python3
"""Generate V2_STEP_INDEX.md: every STEP_* note in 26_Definitions, newest step first.

The master MOC links to this one page, and the note-coverage test treats it as a MOC,
so a new STEP note is indexed by regenerating this file, not by hand-editing the MOC.
`--check` exits 1 if the committed index is out of date (used in CI).
"""
from pathlib import Path
from urllib.parse import quote
import argparse, re, sys

ROOT = Path(__file__).resolve().parents[2]
DEFS = ROOT / "26_Definitions"
OUT = DEFS / "V2_STEP_INDEX.md"
CODE = re.compile(r"^STEP_(\d+)([A-Z]?)_")


def sort_key(p):
    m = CODE.match(p.name)
    return (int(m.group(1)), m.group(2)) if m else (-1, p.name)


def describe(p):
    title, status = p.stem.replace("_", " "), ""
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines()[:25]:
        if line.startswith("# ") and title == p.stem.replace("_", " "):
            title = line[2:].strip()
        m = re.match(r"\**\s*Status\s*:?\**\s*:?\s*(.+)", line)
        if m and not status:
            status = " ".join(m.group(1).replace("*", "").split())
    return title, status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    notes = sorted((p for p in DEFS.glob("STEP_*.md")), key=sort_key, reverse=True)
    rows = []
    for p in notes:
        m = CODE.match(p.name)
        code = f"{m.group(1)}{m.group(2)}" if m else "—"
        title, status = describe(p)
        status = (status[:110] + "…") if len(status) > 111 else status
        rows.append((code, title.replace("|", "\\|"), quote(p.name), status.replace("|", "\\|")))
    with_status = any(r[3] for r in rows)
    L = ["# V2 implementation step index", "",
         "> **Generated file — do not edit.** Source: `26_Definitions/tools/build_v2_step_index.py`. "
         "Lists every `STEP_*` note, newest first. Run the tool after adding a step note.", "",
         f"{len(notes)} step notes.", "",
         "| Step | Note |" + (" Status line |" if with_status else ""),
         "|---|---|" + ("---|" if with_status else "")]
    for code, title, href, status in rows:
        L.append(f"| {code} | [{title}]({href}) |" + (f" {status} |" if with_status else ""))
    text = "\n".join(L) + "\n"
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print(f"{OUT.relative_to(ROOT)} is out of date; run {Path(__file__).name}")
            return 1
        print("step index is current")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(notes)} steps)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
