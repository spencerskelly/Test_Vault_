#!/usr/bin/env python3
"""IMP-010A/B real-source acceptance for folded non-Object Part references.

Proves that EA Part carrier rows targeting Activity/State are represented by
canonical note-level hierarchy/state-design relationships, not Local Model
physical Part occurrences.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path

EXPECTED_PARTS = 203
EXPECTED_TARGETS = {"Activity": 142, "State": 61}
EXPECTED_OWNER_TYPES_FOR_STATE = {"State": 60, "Class": 1}
EXPECTED_FORWARD_BY_SOURCE = {"hasChild": 202, "hasDesign": 1}
EXPECTED_UNIQUE_FORWARD = {"hasChild": 201, "hasDesign": 1}
GUID_CLEAN = re.compile(r"[^0-9a-f]")

def norm_guid(v: object) -> str:
    return GUID_CLEAN.sub("", str(v or "").lower())

def scalar(v: str) -> str:
    v = v.strip()
    try:
        return str(json.loads(v))
    except Exception:
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "\'"):
            return v[1:-1]
        return v

def frontmatter(text: str) -> list[str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return []
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i]
    return []

def parse_frontmatter(lines: list[str]) -> tuple[str, dict[str, list[str]]]:
    uid = ""
    rels: dict[str, list[str]] = {}
    current = ""
    for line in lines:
        if line.startswith("uid:"):
            uid = scalar(line.split(":", 1)[1])
            current = ""
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9_]*):\s*$", line)
        if m:
            current = m.group(1)
            rels.setdefault(current, [])
            continue
        if current and re.match(r"^\s+-\s+", line):
            rels[current].append(scalar(re.sub(r"^\s+-\s+", "", line, count=1)))
            continue
        if line and not line.startswith(" "):
            current = ""
    return uid, rels

def link_target(value: str) -> str:
    m = re.fullmatch(r"\[\[(.+?)\]\]", value.strip())
    if not m:
        return ""
    inner = m.group(1).split("|", 1)[0].split("#", 1)[0]
    return inner.replace("\\|", "|").strip()

def link_matches(value: str, path: Path, vault: Path) -> bool:
    target = link_target(value)
    if not target:
        return False
    rel = path.relative_to(vault).with_suffix("").as_posix()
    return target == path.stem or target == rel or rel.endswith("/" + target)

def read_ledger(vault: Path) -> dict[str, dict[str, str]]:
    p = vault / "99_System/11_Import/Ledger.csv"
    if not p.is_file():
        raise RuntimeError(f"missing Ledger.csv: {p}")
    out = {}
    with p.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            g = norm_guid(row.get("ea_guid"))
            if g:
                out[g] = row
    return out

def read_source_map_part_guids(vault: Path) -> set[str]:
    p = vault / "99_System/11_Import/Local Model Source Map.csv"
    if not p.is_file():
        raise RuntimeError(f"missing Local Model Source Map.csv: {p}")
    out = set()
    with p.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("local_kind") or "").strip() == "part":
                g = norm_guid(row.get("ea_guid"))
                if g:
                    out.add(g)
    return out

def index_notes(vault: Path) -> dict[str, tuple[Path, dict[str, list[str]]]]:
    out = {}
    for p in vault.rglob("*.md"):
        if ".git" in p.parts or ".obsidian" in p.parts:
            continue
        try:
            fm = frontmatter(p.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            continue
        if not fm:
            continue
        uid, rels = parse_frontmatter(fm)
        if uid:
            if uid in out:
                raise RuntimeError(f"duplicate note uid {uid}: {out[uid][0]} and {p}")
            out[uid] = (p, rels)
    return out

def package_paths(con: sqlite3.Connection) -> dict[int, list[str]]:
    rows = {int(r[0]): (int(r[1] or 0), str(r[2] or "")) for r in con.execute("select Package_ID, Parent_ID, Name from t_package")}
    cache: dict[int, list[str]] = {}
    def get(pid: int) -> list[str]:
        if pid in cache:
            return cache[pid]
        out, seen = [], set()
        cur = pid
        while cur and cur in rows and cur not in seen:
            seen.add(cur)
            parent, name = rows[cur]
            out.append(name)
            cur = parent
        cache[pid] = list(reversed(out))
        return cache[pid]
    return {pid: get(pid) for pid in rows}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("qeax", type=Path)
    ap.add_argument("vault", type=Path)
    args = ap.parse_args()
    qeax = args.qeax.resolve()
    vault = args.vault.resolve()
    if not qeax.is_file():
        print(f"FAIL missing QEAX: {qeax}")
        return 2
    if not vault.is_dir():
        print(f"FAIL missing vault: {vault}")
        return 2

    con = sqlite3.connect(str(qeax))
    con.row_factory = sqlite3.Row
    objects = list(con.execute("select * from t_object"))
    by_id = {int(r["Object_ID"]): r for r in objects}
    by_guid = {norm_guid(r["ea_guid"]): r for r in objects if norm_guid(r["ea_guid"])}
    pkg_paths = package_paths(con)

    cases = []
    for p in objects:
        if (p["Object_Type"] or "") != "Part" or (p["Stereotype"] or "") == "FlowProperty":
            continue
        target = by_guid.get(norm_guid(p["PDATA1"]))
        if not target or (target["Object_Type"] or "") not in ("Activity", "State"):
            continue
        owner = by_id.get(int(p["ParentID"] or 0))
        if not owner:
            raise RuntimeError(f"Part {p['ea_guid']} has missing owner {p['ParentID']}")
        cases.append((p, owner, target))

    failures = []
    def require(cond: bool, msg: str) -> None:
        if not cond:
            failures.append(msg)

    require(len(cases) == EXPECTED_PARTS, f"source cases {len(cases)} != {EXPECTED_PARTS}")
    target_counts = Counter((t["Object_Type"] or "") for _, _, t in cases)
    require(dict(target_counts) == EXPECTED_TARGETS, f"target counts {dict(target_counts)} != {EXPECTED_TARGETS}")
    state_owner_counts = Counter((o["Object_Type"] or "") for _, o, t in cases if (t["Object_Type"] or "") == "State")
    require(dict(state_owner_counts) == EXPECTED_OWNER_TYPES_FOR_STATE, f"State owner counts {dict(state_owner_counts)} != {EXPECTED_OWNER_TYPES_FOR_STATE}")

    ledger = read_ledger(vault)
    local_part_guids = read_source_map_part_guids(vault)
    notes = index_notes(vault)

    expected_rows = Counter()
    expected_pairs = set()
    checked = 0
    examples = {}
    for p, owner, target in cases:
        pg, og, tg = map(norm_guid, (p["ea_guid"], owner["ea_guid"], target["ea_guid"]))
        prow, orow, trow = ledger.get(pg), ledger.get(og), ledger.get(tg)
        require(prow is not None, f"missing Ledger row for folded Part {p['ea_guid']}")
        require(orow is not None, f"missing Ledger row for owner {owner['ea_guid']}")
        require(trow is not None, f"missing Ledger row for target {target['ea_guid']}")
        if not (prow and orow and trow):
            continue
        require((prow.get("outcome") or "") == "folded", f"Part {p['ea_guid']} outcome is {prow.get('outcome')!r}, expected folded")
        require((prow.get("folded_into_uid") or "") == (trow.get("uid") or ""), f"Part {p['ea_guid']} folded_into_uid does not match target UID")
        require(pg not in local_part_guids, f"Part {p['ea_guid']} was emitted as a Local Model part")

        if (target["Object_Type"] or "") == "Activity":
            require((owner["Object_Type"] or "") == "Activity", f"Behavior carrier {p['ea_guid']} owner is {(owner['Object_Type'] or '')!r}")
            fwd, inv = "hasChild", "childOf"
        else:
            if (owner["Object_Type"] or "") == "State":
                fwd, inv = "hasChild", "childOf"
            elif (owner["Object_Type"] or "") == "Class":
                is_design = "05 Product Design" in pkg_paths.get(int(target["Package_ID"] or 0), [])
                fwd, inv = ("hasDesign", "designOf") if is_design else ("hasState", "stateOf")
            else:
                failures.append(f"Condition carrier {p['ea_guid']} unsupported owner type {(owner['Object_Type'] or '')!r}")
                continue

        expected_rows[fwd] += 1
        expected_pairs.add((orow.get("uid") or "", fwd, trow.get("uid") or ""))
        owner_note = notes.get(orow.get("uid") or "")
        target_note = notes.get(trow.get("uid") or "")
        require(owner_note is not None, f"owner note UID not found for {owner['ea_guid']}")
        require(target_note is not None, f"target note UID not found for {target['ea_guid']}")
        if not (owner_note and target_note):
            continue
        opath, orels = owner_note
        tpath, trels = target_note
        require(any(link_matches(v, tpath, vault) for v in orels.get(fwd, [])),
                f"missing {fwd} link: {opath.relative_to(vault)} -> {tpath.relative_to(vault)} for Part {p['ea_guid']}")
        require(any(link_matches(v, opath, vault) for v in trels.get(inv, [])),
                f"missing {inv} inverse: {tpath.relative_to(vault)} -> {opath.relative_to(vault)} for Part {p['ea_guid']}")
        examples.setdefault(fwd, (p, owner, target, opath, tpath, inv))
        checked += 1

    require(dict(expected_rows) == EXPECTED_FORWARD_BY_SOURCE, f"expected relationship rows {dict(expected_rows)} != {EXPECTED_FORWARD_BY_SOURCE}")
    unique_counts = Counter(field for _, field, _ in expected_pairs)
    require(dict(unique_counts) == EXPECTED_UNIQUE_FORWARD, f"unique relationship pairs {dict(unique_counts)} != {EXPECTED_UNIQUE_FORWARD}")

    print("IMP-010A/B hierarchy acceptance")
    print(f"source Parts checked: {len(cases)}")
    print(f"target counts: {dict(target_counts)}")
    print(f"state owner counts: {dict(state_owner_counts)}")
    print(f"expected relationship rows: {dict(expected_rows)}")
    print(f"unique relationship pairs: {dict(unique_counts)}")
    print(f"generated owner/target note pairs checked: {checked}")
    print(f"Local Model part occurrences for these source GUIDs: {len({norm_guid(p['ea_guid']) for p,_,_ in cases} & local_part_guids)}")
    for field, ex in sorted(examples.items()):
        p, owner, target, opath, tpath, inv = ex
        print(f"SAMPLE {field}/{inv}: {owner['Name']} -> {target['Name']} | Part {p['ea_guid']} | {opath.relative_to(vault)} -> {tpath.relative_to(vault)}")
    if failures:
        for msg in failures[:80]:
            print("FAIL", msg)
        if len(failures) > 80:
            print(f"FAIL ... {len(failures)-80} additional failures")
        print(f"RESULT: FAIL ({len(failures)} failures)")
        return 2
    print("RESULT: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
