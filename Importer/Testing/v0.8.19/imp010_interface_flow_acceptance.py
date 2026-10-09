#!/usr/bin/env python3
"""IMP-010C real-source acceptance for Interface FlowProperty carrier Parts."""
from __future__ import annotations
import argparse, csv, json, re, sqlite3
from collections import Counter
from pathlib import Path

GUID_CLEAN=re.compile(r"[^0-9a-f]")
EXPECTED_COPIES=16
EXPECTED_COPY_FLOW_NAMES={"3.3V":14,"can":2}
EXPECTED_COPY_SIGNAL_NAMES={"ps3V3Analog":14,"psCan":2}
EXPECTED_CLASS_OWNED_FLOWPROPERTIES=752

def ng(v): return GUID_CLEAN.sub("",str(v or "").lower())

def scalar(v):
    v=v.strip()
    try:return str(json.loads(v))
    except Exception:
        if len(v)>=2 and v[0]==v[-1] and v[0] in ('"',"'"):return v[1:-1]
        return v

def frontmatter(text):
    lines=text.splitlines()
    if not lines or lines[0].strip()!="---":return []
    for i in range(1,len(lines)):
        if lines[i].strip()=="---":return lines[1:i]
    return []

def parse_note(text):
    fm=frontmatter(text); uid=""; subtype=""; rels={}; current=""
    for line in fm:
        if line.startswith("uid:"): uid=scalar(line.split(":",1)[1]); current=""; continue
        if line.startswith("subtype:"): subtype=scalar(line.split(":",1)[1]); current=""; continue
        m=re.match(r"^([A-Za-z][A-Za-z0-9_]*):\s*$",line)
        if m: current=m.group(1); rels.setdefault(current,[]); continue
        if current and re.match(r"^\s+-\s+",line):
            rels[current].append(scalar(re.sub(r"^\s+-\s+","",line,count=1))); continue
        if line and not line.startswith(" "): current=""
    return uid,subtype,rels

def link_target(v):
    m=re.fullmatch(r"\[\[(.+?)\]\]",v.strip())
    if not m:return ""
    return m.group(1).split("|",1)[0].split("#",1)[0].replace("\\|","|").strip()

def link_matches(v,path,vault):
    t=link_target(v)
    if not t:return False
    rel=path.relative_to(vault).with_suffix("").as_posix()
    return t==path.stem or t==rel or rel.endswith("/"+t)

def read_csv(path):
    with path.open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("qeax",type=Path); ap.add_argument("vault",type=Path)
    args=ap.parse_args(); qeax=args.qeax.resolve(); vault=args.vault.resolve()
    con=sqlite3.connect(str(qeax)); con.row_factory=sqlite3.Row
    objects=list(con.execute("select * from t_object"))
    byid={int(r["Object_ID"]):r for r in objects}
    byg={ng(r["ea_guid"]):r for r in objects if ng(r["ea_guid"])}
    tags=Counter(int(r[0]) for r in con.execute("select Object_ID from t_objectproperties"))
    conn_touch=Counter()
    for r in con.execute("select Start_Object_ID,End_Object_ID from t_connector"):
        conn_touch[int(r[0] or 0)]+=1; conn_touch[int(r[1] or 0)]+=1
    diag=Counter(int(r[0]) for r in con.execute("select Object_ID from t_diagramobjects"))

    copies=[]
    for p in objects:
        if (p["Object_Type"] or "")!="Part" or (p["Stereotype"] or "")=="FlowProperty":continue
        parent=byid.get(int(p["ParentID"] or 0))
        classifier=byid.get(int(p["Classifier"] or 0)) or byg.get(ng(p["Classifier_guid"]))
        if not(parent and (parent["Object_Type"] or "")=="Port" and classifier and
               (classifier["Object_Type"] or "")=="Part" and (classifier["Stereotype"] or "")=="FlowProperty"):continue
        idef=byid.get(int(classifier["ParentID"] or 0)); typed=byg.get(ng(p["PDATA1"]))
        if not(idef and (idef["Object_Type"] or "")=="Class" and typed and
               ng(p["PDATA1"])==ng(classifier["PDATA1"]) and ng(parent["PDATA1"])==ng(idef["ea_guid"])):continue
        copies.append((p,parent,classifier,idef,typed))

    failures=[]
    def req(cond,msg):
        if not cond:failures.append(msg)

    req(len(copies)==EXPECTED_COPIES,f"exact contextual copies {len(copies)} != {EXPECTED_COPIES}")
    req(Counter(str(c[2]["Name"] or "") for c in copies)==Counter(EXPECTED_COPY_FLOW_NAMES),"copy FlowProperty grouping changed")
    req(Counter(str(c[4]["Name"] or "") for c in copies)==Counter(EXPECTED_COPY_SIGNAL_NAMES),"copy signal grouping changed")
    for p,_,_,_,_ in copies:
        req(not any(str(p[k] or "").strip() for k in ("Name","Note","Multiplicity","PDATA2")),f"copy {p['ea_guid']} has local name/note/multiplicity/PDATA2")
        req(tags[int(p["Object_ID"])]==0,f"copy {p['ea_guid']} has object properties")
        req(conn_touch[int(p["Object_ID"])]==0,f"copy {p['ea_guid']} touches connector(s)")
        req(diag[int(p["Object_ID"])]==0,f"copy {p['ea_guid']} appears on diagram(s)")

    flowprops=[r for r in objects if (r["Object_Type"] or "")=="Part" and (r["Stereotype"] or "")=="FlowProperty"]
    class_owned=[r for r in flowprops if byid.get(int(r["ParentID"] or 0)) is not None and (byid[int(r["ParentID"])]["Object_Type"] or "")=="Class"]
    req(len(flowprops)==760,f"FlowProperty definitions {len(flowprops)} != 760")
    req(len(class_owned)==EXPECTED_CLASS_OWNED_FLOWPROPERTIES,f"Class-owned FlowProperties {len(class_owned)} != {EXPECTED_CLASS_OWNED_FLOWPROPERTIES}")

    ledger=read_csv(vault/"99_System/11_Import/Ledger.csv")
    ledger_by_guid={ng(r.get("ea_guid")):r for r in ledger if ng(r.get("ea_guid"))}
    localmap=read_csv(vault/"99_System/11_Import/Local Model Source Map.csv")
    local_parts=[r for r in localmap if (r.get("local_kind") or "")=="part"]
    local_part_guids={ng(r.get("ea_guid")) for r in local_parts}
    req(len(local_parts)==2055,f"Local Model Part rows {len(local_parts)} != 2055 structural Object occurrences")
    semantic=read_csv(vault/"99_System/11_Import/Review - Semantic and Connectors.csv")

    wanted=set()
    for fp in class_owned:
        owner=byid[int(fp["ParentID"])]
        typed=byg.get(ng(fp["PDATA1"]))
        for raw in (fp,owner,typed):
            if raw is None: continue
            row=ledger_by_guid.get(ng(raw["ea_guid"]))
            if row and (row.get("uid") or "").strip():wanted.add((row.get("uid") or "").strip())
    for p,_,classifier,_,typed in copies:
        for raw in (classifier,typed):
            row=ledger_by_guid.get(ng(raw["ea_guid"]))
            if row and (row.get("uid") or "").strip():wanted.add((row.get("uid") or "").strip())

    notes={}
    for path in vault.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:continue
        try:text=path.read_text(encoding="utf-8")
        except UnicodeDecodeError:continue
        uid,subtype,rels=parse_note(text)
        if uid in wanted:
            req(uid not in notes,f"duplicate generated uid {uid}")
            notes[uid]=(path,subtype,rels,text)

    # Every class-owned FlowProperty has reusable interface ownership in current vocabulary.
    checked_owner=0
    for fp in class_owned:
        owner=byid[int(fp["ParentID"])]
        fr=ledger_by_guid.get(ng(fp["ea_guid"])); orow=ledger_by_guid.get(ng(owner["ea_guid"]))
        req(fr is not None and orow is not None,f"missing ledger owner/flow row for FlowProperty {fp['ea_guid']}")
        if not(fr and orow):continue
        fn=notes.get((fr.get("uid") or "").strip()); on=notes.get((orow.get("uid") or "").strip())
        req(fn is not None and on is not None,f"missing generated owner/flow note for FlowProperty {fp['ea_guid']}")
        if not(fn and on):continue
        fpath,_,frels,ftext=fn; opath,osub,orels,_=on
        req(osub=="interface",f"FlowProperty owner {opath.relative_to(vault)} is subtype {osub!r}, expected interface")
        req(any(link_matches(v,fpath,vault) for v in orels.get("hasChild",[])),f"missing interface hasChild FlowProperty: {opath.relative_to(vault)} -> {fpath.relative_to(vault)}")
        req(any(link_matches(v,opath,vault) for v in frels.get("childOf",[])),f"missing FlowProperty childOf interface: {fpath.relative_to(vault)} -> {opath.relative_to(vault)}")
        typed=byg.get(ng(fp["PDATA1"]))
        if typed:
            tr=ledger_by_guid.get(ng(typed["ea_guid"])); tn=notes.get((tr.get("uid") or "").strip()) if tr else None
            req(tn is not None,f"missing typed target note for FlowProperty {fp['ea_guid']}")
            if tn:
                tpath=tn[0]
                req(any(line.startswith("- FlowProperty type: ") and link_matches(line.split(": ",1)[1],tpath,vault) for line in ftext.splitlines()),
                    f"missing FlowProperty type evidence in {fpath.relative_to(vault)}")
        dirs=[str(r[0] or r[1] or "").strip() for r in con.execute("select Value,Notes from t_objectproperties where Object_ID=? and lower(Property)='direction'",(int(fp["Object_ID"]),)) if str(r[0] or r[1] or "").strip()]
        for d in set(dirs):req(f"- Direction: {d}" in ftext,f"missing Direction {d!r} in {fpath.relative_to(vault)}")
        checked_owner+=1

    copy_guids={ng(p["ea_guid"]) for p,_,_,_,_ in copies}
    for p,_,classifier,_,_ in copies:
        pr=ledger_by_guid.get(ng(p["ea_guid"])); cr=ledger_by_guid.get(ng(classifier["ea_guid"]))
        req(pr is not None and cr is not None,f"missing ledger copy/classifier row for {p['ea_guid']}")
        if pr and cr:
            req((pr.get("outcome") or "")=="folded",f"copy {p['ea_guid']} outcome {(pr.get('outcome') or '')!r} != folded")
            req((pr.get("folded_into_uid") or "")==(cr.get("uid") or ""),f"copy {p['ea_guid']} does not fold to FlowProperty UID")
        req(ng(p["ea_guid"]) not in local_part_guids,f"copy {p['ea_guid']} emitted as Local Model Part")

    folded_reviews=[r for r in semantic if "Folded EA Part" in (r.get("detail") or "")]
    copy_reviews=[r for r in folded_reviews if ng(r.get("source_guid")) in copy_guids]
    req(not copy_reviews,f"{len(copy_reviews)} exact Interface FlowProperty copies still emit Local Model warnings")
    review_counts=Counter(ng(r.get("source_guid")) for r in folded_reviews if ng(r.get("source_guid")))
    dup=[g for g,n in review_counts.items() if n>1]
    req(not dup,f"{len(dup)} folded Part source GUIDs still emit duplicate review rows")

    print("IMP-010C Interface FlowProperty acceptance")
    print(f"exact contextual copies checked: {len(copies)}")
    print(f"copy FlowProperty groups: {dict(Counter(str(c[2]['Name'] or '') for c in copies))}")
    print(f"copy signal groups: {dict(Counter(str(c[4]['Name'] or '') for c in copies))}")
    print(f"reusable FlowProperty definitions: {len(flowprops)}")
    print(f"interface-owned FlowProperty definitions checked: {checked_owner}")
    print(f"Local Model Part occurrences for exact copy GUIDs: {len(copy_guids & local_part_guids)}")
    print(f"exact-copy Local Model warning rows: {len(copy_reviews)}")
    print(f"duplicate folded-Part review GUIDs: {len(dup)}")
    if failures:
        for x in failures[:80]:print("FAIL",x)
        if len(failures)>80:print(f"FAIL ... {len(failures)-80} additional failures")
        print(f"RESULT: FAIL ({len(failures)} failures)")
        return 2
    print("RESULT: PASS")
    return 0

if __name__=="__main__":raise SystemExit(main())
