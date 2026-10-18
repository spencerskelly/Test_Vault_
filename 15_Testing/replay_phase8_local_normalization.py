"""Local-only independent replay of Phase 8 normalize_qeax_phase8.decide against ledger."""
import collections,csv,importlib.util,json,pathlib,sqlite3,sys
BASE=pathlib.Path(__file__).resolve().parents[1]
SOURCE=BASE/"14_Workbench/registry/runtime/normalize_qeax_phase8.py"
spec=importlib.util.spec_from_file_location("phase8_qeax_normalizer",SOURCE)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def check(qeax,ledger,registry):
 errors=collections.Counter();count=0;seen=set()
 with sqlite3.connect("file:"+str(pathlib.Path(qeax).resolve())+"?mode=ro",uri=True) as db:
  db.row_factory=sqlite3.Row
  elements={str(r["Object_ID"]):(r["Object_Type"],r["Stereotype"] or "") for r in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
  sources={str(r["Connector_ID"]):r for r in db.execute("SELECT Connector_ID,ea_guid,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID,SourceIsAggregate,DestIsAggregate,SourceRole,DestRole,SourceCard,DestCard FROM t_connector")}
  registered={x["family"] for x in json.loads(pathlib.Path(registry).read_text())["families"]}
  with open(ledger,newline="",encoding="utf-8") as f:
   reader=csv.DictReader(f)
   fields={"source_pk","source_guid","raw_from","raw_to","family","rule","role","status","normalized_from","normalized_to","source_kind","target_kind","diagnostics","source_direction","source_role","target_role","source_cardinality","target_cardinality","source_aggregation_flag","target_aggregation_flag"}
   if not fields.issubset(reader.fieldnames or []):
    errors["LEDGER_FIELDS_MISSING"]+=1
   else:
    for row in reader:
     count+=1;pk=row["source_pk"]
     if pk in seen:errors["DUPLICATE_SOURCE_PK"]+=1
     seen.add(pk);src=sources.get(pk)
     if src is None:errors["UNKNOWN_CONNECTOR"]+=1;continue
     raw={"source_guid":src["ea_guid"],"raw_from":src["Start_Object_ID"],"raw_to":src["End_Object_ID"],"source_direction":src["Direction"],"source_role":src["SourceRole"],"target_role":src["DestRole"],"source_cardinality":src["SourceCard"],"target_cardinality":src["DestCard"],"source_aggregation_flag":src["SourceIsAggregate"],"target_aggregation_flag":src["DestIsAggregate"]}
     for key,value in raw.items():
      if row[key]!=(str(value) if value is not None else ""):errors["RAW_"+key.upper()+"_MISMATCH"]+=1
     a=elements.get(str(src["Start_Object_ID"]));b=elements.get(str(src["End_Object_ID"]))
     prediction=mod.decide(src,a,b,registered)
     for key in ("family","rule","role","status","normalized_from","normalized_to","source_kind","target_kind"):
      if row[key]!=str(prediction[key]):errors["NORMALIZED_"+key.upper()+"_MISMATCH"]+=1
     if row["diagnostics"]!=";".join(prediction["diagnostics"]):errors["NORMALIZED_DIAGNOSTICS_MISMATCH"]+=1
  missing=len(set(sources)-seen)
  if missing:errors["MISSING_SOURCE_ROWS"]+=missing
 return {"schema":"mdse-phase8-local-normalization-replay/1","source_count":len(sources),"ledger_count":count,"valid":not errors,"error_counts":dict(sorted(errors.items())),"native_certified":0}
if __name__=="__main__":
 import argparse
 p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);p.add_argument("--ledger",required=True);p.add_argument("--registry",required=True);a=p.parse_args()
 result=check(a.qeax,a.ledger,a.registry);print(json.dumps(result,indent=2));sys.exit(0 if result["valid"] else 1)
