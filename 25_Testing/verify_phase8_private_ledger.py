"""Compare private Phase 8 ledger against original QEAX, emitting aggregate results only."""
import csv,sqlite3,pathlib,collections
CONNECTOR_FIELDS={"raw_from":"Start_Object_ID","raw_to":"End_Object_ID",
 "source_guid":"ea_guid","source_direction":"Direction","source_role":"SourceRole",
 "target_role":"DestRole","source_cardinality":"SourceCard",
 "target_cardinality":"DestCard","source_aggregation_flag":"SourceIsAggregate",
 "target_aggregation_flag":"DestIsAggregate"}
def value(x):return "" if x is None else str(x)
def audit(qeax,ledger):
 c=sqlite3.connect("file:"+str(pathlib.Path(qeax).resolve())+"?mode=ro",uri=True)
 c.row_factory=sqlite3.Row
 try:
  sources={str(r["Connector_ID"]):r for r in c.execute("SELECT * FROM t_connector")}
  objects={r["Object_ID"]:r for r in c.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
  counts=collections.Counter();statuses=collections.Counter();seen=set()
  with pathlib.Path(ledger).open(newline="",encoding="utf-8") as f:
   rows=csv.DictReader(f)
   required={"source_pk","raw_source_type","raw_source_stereotype",
     "raw_target_type","raw_target_stereotype","status",*CONNECTOR_FIELDS}
   if not required.issubset(rows.fieldnames or []):raise ValueError("MISSING_LEDGER_COLUMNS")
   for row in rows:
    counts["ledgerRows"]+=1
    statuses[row["status"]]+=1
    pk=row["source_pk"]
    if pk in seen:counts["duplicateIds"]+=1
    seen.add(pk)
    src=sources.get(pk)
    if src is None:
     counts["unknownIds"]+=1
     continue
    for col,field in CONNECTOR_FIELDS.items():
     if value(row[col])!=value(src[field]):counts["rawMismatches"]+=1
    for prefix,oid in (("raw_source",src["Start_Object_ID"]),("raw_target",src["End_Object_ID"])):
     obj=objects.get(oid)
     if obj is None:
      counts["missingObject"]+=1
      continue
     for suffix,field in (("type","Object_Type"),("stereotype","Stereotype")):
      if value(row[prefix+"_"+suffix])!=value(obj[field]):counts["rawMismatches"]+=1
  counts["missingIds"]=len(set(sources)-seen)
  problems=("duplicateIds","unknownIds","missingIds","rawMismatches","missingObject")
  return {"schema":"mdse-phase8-independent-fidelity/1","sourceRows":len(sources),
   "ledgerRows":counts["ledgerRows"],**{k:counts[k] for k in problems},
   "byStatus":dict(sorted(statuses.items())),"nativeCertified":0,
   "status":"BLOCKED" if any(counts[k] for k in problems) else "PASS"}
 finally:c.close()
