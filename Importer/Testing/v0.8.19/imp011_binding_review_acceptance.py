#!/usr/bin/env python3
"""IMP-011A real-source acceptance for truthful BindingConnector review disposition."""
from __future__ import annotations
import argparse,csv,sqlite3
from collections import Counter
from pathlib import Path

EXPECTED_CATEGORIES={
  "resolved Connection.exposes":23,
  "temporary local equals - no internal Connection":191,
  "same-owner nested internal binding":17,
  "same-owner sibling/non-hierarchical binding":1,
  "cross-owner binding":17,
}
EXPECTED_RELATIONS={"Connection.exposes":23,"Interface.equals (temporary)":191,"":35}

def norm(v): return str(v or "").strip().lower().replace("{","").replace("}","")

def main():
  ap=argparse.ArgumentParser();ap.add_argument("qeax",type=Path);ap.add_argument("vault",type=Path)
  a=ap.parse_args()
  con=sqlite3.connect(a.qeax)
  src={norm(r[0]) for r in con.execute(
    "select ea_guid from t_connector where Connector_Type='Connector' and Stereotype='BindingConnector'"
  )}
  p=a.vault/"99_System/11_Import/Review - Equals Direction.csv"
  with p.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
  failures=[]
  def req(ok,msg):
    if not ok: failures.append(msg)
  guids=[norm(r.get("ea_guid")) for r in rows]
  req(len(src)==249,f"source BindingConnector count {len(src)} != 249")
  req(len(rows)==249,f"review row count {len(rows)} != 249")
  req(len(set(guids))==249,f"unique review GUID count {len(set(guids))} != 249")
  req(set(guids)==src,f"review/source GUID sets differ: missing={len(src-set(guids))}, extra={len(set(guids)-src)}")
  cats=Counter(r.get("category","") for r in rows)
  rels=Counter(r.get("actual_relation","") for r in rows)
  req(dict(cats)==EXPECTED_CATEGORIES,f"category counts {dict(cats)} != {EXPECTED_CATEGORIES}")
  req(dict(rels)==EXPECTED_RELATIONS,f"relation counts {dict(rels)} != {EXPECTED_RELATIONS}")
  for r in rows:
    cat=r.get("category",""); rel=r.get("actual_relation","")
    req(bool(r.get("root_cause","").strip()),f"{r.get('ea_guid')} missing root_cause")
    if cat=="resolved Connection.exposes":
      req(rel=="Connection.exposes",f"{r.get('ea_guid')} exposure relation mismatch")
      req(bool(r.get("connection_local","").strip()),f"{r.get('ea_guid')} exposure missing connection_local")
      req(bool(r.get("exposes_local","").strip()),f"{r.get('ea_guid')} exposure missing exposes_local")
    elif cat=="temporary local equals - no internal Connection":
      req(rel=="Interface.equals (temporary)",f"{r.get('ea_guid')} equals relation mismatch")
      req(r.get("candidate_connection_count","")=="0",f"{r.get('ea_guid')} expected zero candidate Connections")
      req(bool(r.get("owner_note","").strip()),f"{r.get('ea_guid')} equals missing owner_note")
      req(bool(r.get("start_local","").strip()) and bool(r.get("end_local","").strip()),f"{r.get('ea_guid')} equals missing endpoint IDs")
    else:
      req(rel=="",f"{r.get('ea_guid')} unresolved category unexpectedly writes {rel!r}")
  print("IMP-011A BindingConnector review acceptance")
  print(f"source BindingConnectors: {len(src)}")
  print(f"review rows / unique GUIDs: {len(rows)} / {len(set(guids))}")
  print(f"category counts: {dict(cats)}")
  print(f"actual relation counts: {dict(rels)}")
  if failures:
    for x in failures[:80]: print("FAIL",x)
    if len(failures)>80: print(f"FAIL ... {len(failures)-80} additional failures")
    print(f"RESULT: FAIL ({len(failures)} failures)")
    return 2
  print("RESULT: PASS")
  return 0

if __name__=="__main__": raise SystemExit(main())
