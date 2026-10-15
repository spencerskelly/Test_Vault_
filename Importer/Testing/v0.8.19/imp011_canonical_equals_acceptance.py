#!/usr/bin/env python3
"""IMP-011B real-source acceptance for Local Model 0.5 canonical BindingConnector equals."""
from __future__ import annotations
import argparse,csv,re,sqlite3
from collections import Counter,defaultdict
from pathlib import Path

EXPECTED_CATEGORIES={
  "resolved Connection.exposes":23,
  "canonical local equals - boundary/internal no internal Connection":191,
  "canonical local equals - same-owner nested internal binding":17,
  "canonical local equals - same-owner sibling/non-hierarchical binding":1,
  "cross-owner binding":17,
}
EXPECTED_RELATIONS={"Connection.exposes":23,"Interface.equals":209,"":17}
EP_BLOCK=re.compile(r"^\^(ep-\d{17}[a-z-]{13})\s*$")
EP_REF=re.compile(r"#\^(ep-\d{17}[a-z-]{13})\b")

def norm(v): return str(v or "").strip().lower().replace("{","").replace("}","")

def main():
  ap=argparse.ArgumentParser();ap.add_argument("qeax",type=Path);ap.add_argument("vault",type=Path)
  a=ap.parse_args(); failures=[]
  def req(ok,msg):
    if not ok: failures.append(msg)

  con=sqlite3.connect(a.qeax)
  src={norm(r[0]) for r in con.execute(
    "select ea_guid from t_connector where Connector_Type='Connector' and Stereotype='BindingConnector'"
  )}
  review=a.vault/"99_System/11_Import/Review - Equals Direction.csv"
  with review.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
  guids=[norm(r.get("ea_guid")) for r in rows]
  cats=Counter(r.get("category","") for r in rows)
  rels=Counter(r.get("actual_relation","") for r in rows)
  req(len(src)==249,f"source BindingConnector count {len(src)} != 249")
  req(len(rows)==249 and len(set(guids))==249,"review must contain 249 unique BindingConnector rows")
  req(set(guids)==src,"review/source BindingConnector GUID sets differ")
  req(dict(cats)==EXPECTED_CATEGORIES,f"category counts {dict(cats)} != {EXPECTED_CATEGORIES}")
  req(dict(rels)==EXPECTED_RELATIONS,f"relation counts {dict(rels)} != {EXPECTED_RELATIONS}")

  schema=(a.vault/"99_System/03_Schemas/local-model.yaml").read_text(encoding="utf-8")
  req(re.search(r'^schemaVersion:\s*["\']?0\.5["\']?\s*$',schema,re.M) is not None,"runtime Local Model schema is not 0.5")
  req('writableVersion: "0.5"' in schema,"runtime schema writableVersion is not 0.5")
  req('temporary: true' not in next((line for line in schema.splitlines() if "equals:" in line),""),
      "0.5 equals field is still temporary")

  endpoint_owner={}
  directed=set()
  markers=0
  for p in a.vault.rglob("*.md"):
    if ".git" in p.parts or ".obsidian" in p.parts: continue
    try: lines=p.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError: continue
    in_local=False; section=""; current=""
    for line in lines:
      if line.strip()=="<!-- MDSE:LOCAL-MODEL START schema=0.5 -->":
        in_local=True;section="";markers+=1;continue
      if line.strip().startswith("<!-- MDSE:LOCAL-MODEL START schema=") and "schema=0.5" not in line:
        failures.append(f"non-0.5 Local Model marker in {p.relative_to(a.vault)}: {line.strip()}")
      if line.strip()=="<!-- MDSE:LOCAL-MODEL END -->":
        in_local=False;section="";current="";continue
      if not in_local: continue
      if line.startswith("### ") and not line.startswith("#### "):
        section=line[4:].strip();current="";continue
      m=EP_BLOCK.match(line.strip())
      if m and section=="Interfaces":
        current=m.group(1);endpoint_owner[current]=str(p.relative_to(a.vault));continue
      if section=="Interfaces" and line.startswith("#### "):
        current="";continue
      if section=="Interfaces" and line.startswith("- equals:"):
        # The block ID appears after the fields, so attach refs to the record by scanning forward is awkward.
        # Capture temporarily against a synthetic record index below.
        pass

  # Second scan: parse each Interface record from heading through block ID.
  directed.clear()
  for p in a.vault.rglob("*.md"):
    if ".git" in p.parts or ".obsidian" in p.parts: continue
    try: lines=p.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError: continue
    in_local=False;section="";record_lines=[]
    for line in lines+["<!-- MDSE:LOCAL-MODEL END -->"]:
      if line.strip()=="<!-- MDSE:LOCAL-MODEL START schema=0.5 -->":
        in_local=True;section="";record_lines=[];continue
      if not in_local: continue
      if line.strip()=="<!-- MDSE:LOCAL-MODEL END -->":
        record_lines=[];in_local=False;section="";continue
      if line.startswith("### ") and not line.startswith("#### "):
        section=line[4:].strip();record_lines=[];continue
      if section!="Interfaces": continue
      if line.startswith("#### "):
        record_lines=[line];continue
      if record_lines:
        record_lines.append(line)
        m=EP_BLOCK.match(line.strip())
        if m:
          src_id=m.group(1)
          for rl in record_lines:
            if rl.startswith("- equals:"):
              for dst in EP_REF.findall(rl):
                directed.add((src_id,dst))
          record_lines=[]

  undirected={tuple(sorted((x,y))) for x,y in directed}
  req(markers>0,"no Local Model 0.5 regions found")
  req(len(directed)==418,f"directed equals links {len(directed)} != 418 (209 symmetric edges)")
  req(len(undirected)==209,f"undirected equals pairs {len(undirected)} != 209")
  req(all(x!=y for x,y in directed),"self-equality link exists")
  req(all((y,x) in directed for x,y in directed),"equals links are not fully symmetric")

  for r in rows:
    a_id=(r.get("start_local") or "").strip();b_id=(r.get("end_local") or "").strip()
    rel=r.get("actual_relation","")
    pair=tuple(sorted((a_id,b_id))) if a_id and b_id else None
    if rel=="Interface.equals":
      req(pair in undirected,f"{r.get('ea_guid')} canonical equals pair missing from Markdown")
      req(bool(r.get("owner_note","").strip()),f"{r.get('ea_guid')} canonical equals missing owner note")
    elif pair:
      req(pair not in undirected,f"{r.get('ea_guid')} non-equals BindingConnector unexpectedly persisted as equals")

  print("IMP-011B Local Model 0.5 BindingConnector acceptance")
  print(f"source/review BindingConnectors: {len(src)} / {len(rows)}")
  print(f"category counts: {dict(cats)}")
  print(f"actual relation counts: {dict(rels)}")
  print(f"Local Model 0.5 regions: {markers}")
  print(f"directed / undirected equals edges: {len(directed)} / {len(undirected)}")
  if failures:
    for x in failures[:100]: print("FAIL",x)
    if len(failures)>100: print(f"FAIL ... {len(failures)-100} additional failures")
    print(f"RESULT: FAIL ({len(failures)} failures)");return 2
  print("RESULT: PASS");return 0

if __name__=="__main__": raise SystemExit(main())
