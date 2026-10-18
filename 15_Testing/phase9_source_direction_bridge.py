"""Local-only QEAX-backed evidence gate; emits aggregates, never a trust token.

Checks raw source generalization orientation against a complete Phase 8 ledger.
"""
import argparse,collections,csv,json,pathlib,sqlite3
from phase9_generalization_family_matrix import assess

def audit(qeax,ledger):
 errors=collections.Counter();out=collections.Counter();seen=set()
 with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
  db.row_factory=sqlite3.Row
  nodes={str(r["Object_ID"]):(r["Object_Type"],r["Stereotype"] or "") for r in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
  source={str(r["Connector_ID"]):r for r in db.execute("SELECT Connector_ID,ea_guid,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector")}
  with open(ledger,newline="",encoding="utf-8") as f:
   reader=csv.DictReader(f)
   required={"source_pk","source_guid","family","raw_from","raw_to","normalized_from","normalized_to","source_direction","role","status"}
   if not required.issubset(reader.fieldnames or []):
    return {"valid":False,"errors":{"LEDGER_SCHEMA":1},"native_certified":0}
   for row in reader:
    key=row["source_pk"]
    if key in seen:errors["DUPLICATE_ID"]+=1
    seen.add(key)
    original=source.get(key)
    if original is None:errors["UNKNOWN_ID"]+=1;continue
    raw=(str(original["ea_guid"] or ""),str(original["Start_Object_ID"]),str(original["End_Object_ID"]),str(original["Direction"] or ""))
    if tuple(row[k] for k in ("source_guid","raw_from","raw_to","source_direction"))!=raw:
     errors["RAW_SOURCE_MISMATCH"]+=1;continue
    if original["Connector_Type"]!="Generalization":continue
    out["generalizations_checked"]+=1
    if original["Direction"]!="Source -> Destination":
     out["direction_review"]+=1;continue
    if row["normalized_from"]!=raw[1] or row["normalized_to"]!=raw[2]:
     errors["NORMALIZED_ENDPOINT_MISMATCH"]+=1;continue
    if row["family"]!="Generalization" or row["role"]!="source-subtype-to-destination-supertype":
     errors["ROLE_OR_FAMILY_MISMATCH"]+=1;continue
    a=nodes.get(raw[1]);b=nodes.get(raw[2])
    if not a or not b:errors["MISSING_NODE"]+=1;continue
    category=assess(a,b,original["Direction"],original["Stereotype"])
    if category.startswith("SAME_DEFINITION_FAMILY_CANDIDATE:") or category.startswith("STEREOTYPE_MAPPING_REVIEW:"):
     out["direction_and_family_review_candidate"]+=1
    else:out["endpoint_semantics_review"]+=1
  missing=len(set(source)-seen)
  if missing:errors["MISSING_LEDGER_ROWS"]+=missing
 return {"schema":"mdse-phase9-source-direction-bridge/1","valid":not errors,
         "checked_source":len(source),"ledger_distinct":len(seen),
         "categories":dict(sorted(out.items())),"errors":dict(sorted(errors.items())),
         "native_certified":0,"may_emit_native":False}
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--qeax",required=True);p.add_argument("--ledger",required=True);a=p.parse_args()
 for name in ("qeax","ledger"):
  if not pathlib.Path(getattr(a,name)).is_file():p.error("Missing local "+name)
 print(json.dumps(audit(a.qeax,a.ledger),indent=2))
