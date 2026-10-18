#!/usr/bin/env python3
"""Read-only structural acceptance of Step20 synthetic MDSE fixture.

This cannot establish interactive Obsidian acceptance. It validates governed
schema shapes, exact synthetic topology and human acceptance status only.
"""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
import yaml
from step20_synthetic_vault import FOLDER,ELEMENTS,RELATIONS,ROOT,SCHEMAS,uid,name,wikilink

KINDS={"part":3,"ep":3,"conn":1,"flow":1}
TOKEN=r"[0-9]{17}[a-z-]{13}"
NOTE_RE=re.compile(r"(?m)^uid: ("+TOKEN+r")$")
BLOCK_RE=re.compile(r"(?m)^\^(part|ep|conn|flow)-("+TOKEN+r")$")
LOCAL_REF_RE=re.compile(r"\[\[#\^(part|ep|conn|flow)-("+TOKEN+r")\|[^\]]+\]\]")
DEF_RE=re.compile(r"(?m)^- definition: \[\[([^\]]+)\]\]$")
FRONT=re.compile(r"\A---\n(.*?)\n---\n",re.S)

def load(folder):
    folder=Path(folder)
    expected={name(e[0])+".md" for e in ELEMENTS}
    actual={p.name for p in folder.glob("*.md") if p.name!="README_TEST_ONLY.md" and p.name!="STEP20_GUI_ACCEPTANCE.md"}
    if actual!=expected:
        raise ValueError("Unexpected missing/extra synthetic model notes")
    notes={}
    note_uids=[]
    names={name(e[0]) for e in ELEMENTS}
    type_by_name={name(e[0]):e[1] for e in ELEMENTS}
    for i,(key,kind,subtype,prefix) in enumerate(ELEMENTS,1):
        f=folder/(name(key)+".md")
        raw=f.read_text(encoding="utf-8")
        m=FRONT.match(raw)
        if not m: raise ValueError("Missing YAML frontmatter: "+key)
        data=yaml.safe_load(m.group(1))
        if data.get("type")!=kind or data.get("subtype")!=subtype and subtype is not None:
            raise ValueError("Wrong governed element type/subtype: "+key)
        if kind=="Actor" and "subtype" in data:
            raise ValueError("Unapproved Actor subtype")
        if data.get("id") != prefix+"-"+str(99000+i) or data.get("uid")!=uid(i):
            raise ValueError("Wrong synthetic identity: "+key)
        if data.get("status")!="Draft" or data.get("tags")!=[]:
            raise ValueError("Fixture must remain Draft and untagged")
        if "# "+name(key) not in raw:
            raise ValueError("Missing Markdown element heading")
        for field,targets in RELATIONS.get(key,{}).items():
            if data.get(field)!=[wikilink(x) for x in targets]:
                raise ValueError("Authored relationships differ from contract: "+key+" "+field)
        for field,value in data.items():
            if field in ("type","subtype","id","uid","status","tags"):continue
            if field not in RELATIONS.get(key,{}):
                raise ValueError("Unexpected semantic relationship field: "+field)
            for target in value:
                if target[2:-2] not in names:
                    raise ValueError("Unresolved relationship: "+target)
        notes[key]=(raw,data)
        note_uids.append(data["uid"])
    if len(set(note_uids))!=len(note_uids):
        raise ValueError("Duplicate note UIDs")
    assembly=notes["Assembly"][0]
    if assembly.count("<!-- MDSE:LOCAL-MODEL START schema=0.5 -->")!=1 or assembly.count("<!-- MDSE:LOCAL-MODEL END -->")!=1:
        raise ValueError("Expected one exact Local Model 0.5 region")
    if any("<!-- MDSE:LOCAL-MODEL START" in v[0] for k,v in notes.items() if k!="Assembly"):
        raise ValueError("Local Model must be owned by assembly only")
    tokens=BLOCK_RE.findall(assembly)
    counts={k:sum(kind==k for kind,token in tokens) for k in KINDS}
    if counts!=KINDS:
        raise ValueError("Unexpected owned contextual topology "+repr(counts))
    token_set={token for kind,token in tokens}
    if len(token_set)!=len(tokens) or set(note_uids)&token_set:
        raise ValueError("Duplicate local/first-class UID namespace")
    ref_ids=LOCAL_REF_RE.findall(assembly)
    if len(ref_ids)!=5:  # 2 part ownership links, 2 connection ends, 1 exposed boundary
        raise ValueError("Unexpected local reference count: "+str(len(ref_ids)))
    for kind,token in ref_ids:
        if (kind,token) not in tokens:
            raise ValueError("Unresolved local occurrence reference")
    if assembly.count("- endpointA: [[#^ep-")!=1 or assembly.count("- endpointB: [[#^ep-")!=1:
        raise ValueError("Connection must have two contextual endpoint references")
    if assembly.count("- exposes: [[#^ep-")!=1:
        raise ValueError("Exactly one explicit boundary Interface expose required")
    if assembly.count("- multiplicity: 2")!=1:
        raise ValueError("Contextual HMI multiplicity missing")
    if re.search(r"(?m)^- (quantity|unitOfMeasure|usage):",assembly):
        raise ValueError("Unapproved Local Model quantity/usage changes")
    if re.search(r"(?m)^variantOf:", "\n".join(x[0] for x in notes.values())):
        raise ValueError("Experimental variantOf not permitted")
    defs=DEF_RE.findall(assembly)
    expected_defs={name(x) for x in ["Controller","CAN Transceiver","HMI","CAN Interface","CAN Status Flow"]}
    if set(defs)!=expected_defs:
        raise ValueError("Reusable Local Model definitions unresolved")
    if any(type_by_name[ref] != "Object" for ref in defs if ref != name("CAN Status Flow")):
        raise ValueError("Part/Interface definitions must be Objects")
    if type_by_name[name("CAN Status Flow")]!="Item Flow":
        raise ValueError("Nested Flow must target Item Flow")
    if assembly.count("##### Status information")!=1 or assembly.count("- endpointA: transmit")!=1 or assembly.count("- endpointB: receive")!=1:
        raise ValueError("Nested Flow role/membership incorrect")
    if (folder/"README_TEST_ONLY.md").is_file() is False or not (folder/"STEP20_GUI_ACCEPTANCE.md").is_file():
        raise ValueError("Human GUI runbook/fixture disclaimer missing")
    meta=json.loads((folder/"FIXTURE_PROVENANCE.json").read_text(encoding="utf-8"))
    if meta["status"]!="GUI_NOT_EXECUTED" or meta["guiResults"]!={}: raise ValueError("GUI results were claimed without evidence")
    if meta["localRecordCounts"]!={"part":3,"endpoint":3,"connection":1,"flow":1}:
        raise ValueError("Fixture provenance counts changed")
    base=folder.parent
    if ".obsidian/plugin-lock.yaml" not in [str(p.relative_to(base)) for p in [base/".obsidian/plugin-lock.yaml"] if p.exists()]:
        raise ValueError("Plugin lock missing from synthetic vault")
    if any((base/p).read_bytes()!=(ROOT/p).read_bytes() for p,_ in SCHEMAS.values()):
        raise ValueError("Governed schema modified in synthetic vault")
    if (base/".obsidian/plugin-lock.yaml").read_bytes()!=(ROOT/".obsidian/plugin-lock.yaml").read_bytes():
        raise ValueError("Generated fixture altered controlled lock")
    return {"noteCount":len(notes),"contextual":counts,"localReferences":len(ref_ids),
            "guiAccepted":False,"schemaLocalModel":"0.5","containsQEAX":False}

def validate(vault):
    base=Path(vault)
    if not (base/FOLDER).is_dir():
        raise ValueError("Synthetic fixture folder absent")
    out=load(base/FOLDER)
    if (base/"EA_2026_09_06_endgame.qeax.zip").exists() or (base/"00_Workspace").exists():
        raise ValueError("Forbidden development source archive leaked")
    return out

if __name__=="__main__":
    import argparse
    a=argparse.ArgumentParser();a.add_argument("--vault",required=True)
    x=a.parse_args()
    print("STEP20_STRUCTURAL_VALIDATION="+json.dumps(validate(x.vault),sort_keys=True))
    print("STEP20_GUI_ACCEPTANCE=NOT_EXECUTED")
