#!/usr/bin/env python3
"""Generate V2_NOTE_MAPPING_MATRIX.md: one view of the whole EA -> note -> SysML mapping.

Joins four existing sources; invents nothing:
  99_System/03_Schemas/ea-element-mapping.yaml   EA type -> MDSE note type/subtype (W-numbers)
  24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json   60 element + 26 relationship families -> native SysML
  99_System/03_Schemas/ea-field-dispositions.yaml, ea-tag-dispositions.yaml   where each EA value goes
  99_System/03_Schemas/element-types.yaml   governed classes, subtypes and id prefixes

The output is generated. Edit the sources, then re-run. `--check` exits 1 if the
committed file is out of date (used in CI).
"""
from pathlib import Path
import argparse, collections, json, sys
import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "26_Definitions/V2_NOTE_MAPPING_MATRIX.md"
EM = ROOT / "99_System/03_Schemas/ea-element-mapping.yaml"
RES = ROOT / "24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json"
FIELDS = ROOT / "99_System/03_Schemas/ea-field-dispositions.yaml"
TAGS = ROOT / "99_System/03_Schemas/ea-tag-dispositions.yaml"
TYPES = ROOT / "99_System/03_Schemas/element-types.yaml"


def cell(s, n=150):
    s = " ".join(str(s).split()).replace("|", "\\|")
    return s if len(s) <= n else s[: n - 1] + "…"


def note_outcome(e):
    if e.get("disposition") == "local":
        return f"**no note** — Local Model record ({e.get('localLabel')}); see {e.get('decision')}"
    if e.get("mapping"):
        rows = []
        for m in e["mapping"]:
            when = m.get("rule") or (f"eaType {m['eaType']}" if "eaType" in m else "")
            if "mdseType" in m:
                sub = m.get("subtype")
                rows.append(f"{cell(when, 70)} → **{m['mdseType']}**" + (f"/{sub}" if sub else ""))
            else:
                rows.append(f"{cell(when, 50)} → {cell(m.get('result', ''), 90)}")
        return "<br>".join(rows)
    if e.get("subtypeRule"):
        r = e["subtypeRule"]
        if "basis" in r:
            return f"**{e['mdseType']}**; subtype by rule: {cell(r['basis'], 95)}"
        keys = [k for k in r if k != "default"]
        return f"**{e['mdseType']}**; subtype `{keys[0]}` for recognized classes, else none" if keys else f"**{e['mdseType']}**"
    t = e.get("mdseType")
    sub = e.get("subtype")
    return f"**{t}**" + (f"/{sub}" if sub else "") if t else "—"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    em = {e["eaObjectType"]: e for e in yaml.safe_load(EM.read_text(encoding="utf-8"))["elementTypes"]}
    res = json.loads(RES.read_text(encoding="utf-8"))
    classes = yaml.safe_load(TYPES.read_text(encoding="utf-8"))["classes"]
    fields = yaml.safe_load(FIELDS.read_text(encoding="utf-8"))
    tags = yaml.safe_load(TAGS.read_text(encoding="utf-8"))["tags"]

    fam_by_type = collections.defaultdict(list)
    for f in res["elements"]:
        fam_by_type[f["family"].split(":")[0]].append(f)

    L = []
    w = L.append
    w("# V2 note mapping matrix — EA → MDSE note → native SysML v2")
    w("")
    w("> **Generated file — do not edit.** Source: `26_Definitions/tools/build_v2_mapping_matrix.py`. "
      "Edit the governed sources it joins, then regenerate. Status columns show what is approved and what is "
      "still only a candidate; nothing here enables emission.")
    w("")
    w("## How to read a note")
    w("")
    w("Every v2 note has the same shape. See [ADR-V2-06](ADR_V2_06_NOTE_FORMAT_2026-10-18.md).")
    w("")
    w("| Zone | Owner | Contents |")
    w("|---|---|---|")
    w("| Frontmatter | importer sets, humans may add | `type`, `subtype`, `id`, `uid`, `status`, `eaType`, `tags`, then `sourceRole`, `primarySymbol`, then relationship fields |")
    w("| **User zone** (top) | **humans** | title, note text, `## Notes`, aliases, former ids |")
    w("| `## Source: EA` | importer | EA GUID and kept EA values (translated notes only) |")
    w("| **`## SysML v2`** (bottom) | **importer / Workbench** | exactly one fenced `sysml` block: the authoritative model text |")
    w("")

    w("## Governed note types")
    w("")
    w("| type | id prefix | subtypes |")
    w("|---|---|---|")
    for c in classes:
        subs = ", ".join(c.get("subtype") or []) or "—"
        w(f"| {c['name']} | `{c['prefix']}-NNNNN` | {subs} |")
    w("")

    w(f"## Element families ({len(em)} EA object types, {len(res['elements'])} resolver families)")
    w("")
    w("`Native` is the approved candidate from the family resolver. `parser` and `emit` stay `no` until the "
      "official parser accepts the output (STEP-00 gate).")
    w("")
    w("| EA type | EA count | Note outcome (decision) | Native SysML v2 (resolver family → kind, disposition) | parser | emit |")
    w("|---|---:|---|---|---|---|")
    for name, e in sorted(em.items(), key=lambda kv: -kv[1].get("elements", 0)):
        fams = fam_by_type.get(name, [])
        native = "<br>".join(
            f"{cell(f['family'], 38)} → {f.get('native_kind') or '—'}, {f['disposition']}" for f in fams) or "—"
        parser = "yes" if fams and all(f["parser_accepted"] for f in fams) else "no"
        emit = "yes" if fams and all(f["emission_enabled"] for f in fams) else "no"
        w(f"| {name} | {e.get('elements', 0):,} | {note_outcome(e)} ({e.get('decision')}) | {native} | {parser} | {emit} |")
    w("")

    w(f"## Relationship families ({len(res['relationships'])})")
    w("")
    w("| EA family | EA count | Approved direction | Native SysML v2 operation | Disposition | Evidence required | parser | emit |")
    w("|---|---:|---|---|---|---|---|---|")
    for r in sorted(res["relationships"], key=lambda r: -r["source_count"]):
        w(f"| {r['family']} | {r['source_count']:,} | {cell(r['approved_direction'], 40)} | {r['native_operation'] or '—'} | "
          f"{r['disposition']} | {', '.join(r['required_evidence']) or '—'} | "
          f"{'yes' if r['parser_accepted'] else 'no'} | {'yes' if r['emission_enabled'] else 'no'} |")
    w("")

    w("## Where EA values go (properties)")
    w("")
    w("Dispositions are per EA field and tag. `property` becomes frontmatter; `body` becomes a `- <tag>: <value>` "
      "line in `## Source: EA`; `structure` is consumed by the translator; `archive`/`drop` are not in the note.")
    w("")
    w("| Source | property | body | structure | archive | drop | pending |")
    w("|---|---:|---:|---:|---:|---:|---:|")
    for table in ("tObject", "tConnector", "tPackage"):
        c = collections.Counter(f["disposition"] for f in fields.get(table, []))
        w(f"| EA field: {table} | " + " | ".join(str(c.get(k, 0)) for k in
                                               ("property", "body", "structure", "archive", "drop", "pending")) + " |")
    c = collections.Counter(t["disposition"] for t in tags)
    w("| EA tagged values | " + " | ".join(str(c.get(k, 0)) for k in
                                           ("property", "body", "structure", "archive", "drop", "pending")) + " |")
    w("")
    prop_fields = [f"{t}.{f['field']}" for t in ("tObject", "tConnector", "tPackage") for f in fields.get(t, [])
                   if f["disposition"] == "property"]
    w("Fields decided as frontmatter properties: " + (", ".join(f"`{p}`" for p in prop_fields) or "none") + ". "
      "Tagged values decided as frontmatter properties: "
      + (", ".join(f"`{t['tag']}`" for t in tags if t["disposition"] == "property") or "**none**") + ".")
    w("")
    body_tags = sorted((t for t in tags if t["disposition"] == "body"), key=lambda t: -(t.get("populated") or 0))
    w(f"### Tagged values kept as `## Source: EA` lines ({len(body_tags)}), most populated first")
    w("")
    w("| EA tag | rows with a value | real values | group |")
    w("|---|---:|---:|---|")
    for t in body_tags:
        w(f"| {cell(t['tag'], 50)} | {t.get('populated', 0):,} | {t.get('realValues', 0):,} | {t.get('orderGroup') or '—'} |")
    w("")

    w("## Open mapping items detected in the sources")
    w("")
    open_items = []
    for name, e in sorted(em.items()):
        pd = e.get("partialDecision")
        if pd and "not decided" in pd.lower():
            open_items.append(f"- **{name}** ({e.get('elements', 0):,}): {cell(pd, 260)}")
    for f in res["elements"]:
        if f.get("review_notes"):
            open_items.append(f"- **{f['family']}** resolver review note: {cell('; '.join(f['review_notes']), 200)}")
    w("\n".join(open_items) if open_items else "None.")
    w("")

    text = "\n".join(L).rstrip("\n") + "\n"
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print(f"{OUT.relative_to(ROOT)} is out of date; run {Path(__file__).name}")
            return 1
        print("mapping matrix is current")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(L)} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
