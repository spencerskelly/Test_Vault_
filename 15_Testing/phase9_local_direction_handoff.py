"""Local-only source direction gate. Derives direction from read-only QEAX, not a caller boolean."""
import collections,csv,json,pathlib,sqlite3

def examine(qeax,ledger):
 counts=collections.Counter()
 with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
  rows={str(i):(str(g or ""),t,s or "",d,str(a),str(b)) for i,g,t,s,d,a,b in db.execute(
   "SELECT Connector_ID,ea_guid,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector")}
  seen=set()
  with open(ledger,encoding="utf-8",newline="") as f:
   rd=csv.DictReader(f)
   required={"source_pk","source_guid","family","raw_from","raw_to","normalized_from","normalized_to","status"}
   if not required.issubset(rd.fieldnames or []):raise ValueError("LEDGER_SCHEMA_MISMATCH")
   for rec in rd:
    key=rec["source_pk"]
    if key in seen:counts["DUPLICATE_LEDGER_ID"]+=1
    seen.add(key)
    src=rows.get(key)
    if not src:counts["UNKNOWN_LEDGER_ID"]+=1;continue
    guid,typ,sty,d,a,b=src
    if (rec["source_guid"],rec["raw_from"],rec["raw_to"])!=(guid,a,b):
     counts["SOURCE_MISMATCH"]+=1;continue
    if typ!="Generalization":continue
    counts["source_generalizations"]+=1
    if (rec["normalized_from"],rec["normalized_to"])!=(a,b):
     counts["NORMALIZED_ORIENTATION_MISMATCH"]+=1;continue
    if rec["family"]!="Generalization" or rec["status"]!="orientation_normalized":
     counts["UNQUALIFIED_LEDGER_DISPOSITION"]+=1;continue
    if sty.strip() or d!="Source -> Destination":
     counts["DIRECTION_OR_STEREOTYPE_REVIEW"]+=1;continue
    # Identity and direction match source, but endpoint native semantics remain review.
    counts["SOURCE_DIRECTION_MATCH_CANDIDATE_ONLY"]+=1
  counts["missing_ledger_rows"]=len(set(rows)-seen)
 return {"schema":"mdse-phase9-local-direction-comparison/1",
         "counts":dict(sorted(counts.items())),"native_certified":0,
         "canonical_mutation_authorized":False}

if __name__=="__main__":
 import argparse
 p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);p.add_argument("--ledger",required=True);a=p.parse_args()
 for path in (a.qeax,a.ledger):
  if not pathlib.Path(path).is_file():p.error("Missing local input file")
 print(json.dumps(examine(a.qeax,a.ledger),indent=2))
