"""Read-only QEAX -> canonical specialization review handoff. Never emits native SysML."""
import argparse,csv,hashlib,json,pathlib,sqlite3
def sha256(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for part in iter(lambda:f.read(1024*1024),b""):h.update(part)
 return h.hexdigest()
def inspect(qeax,ledger,graph):
 errors={};count=0
 def fail(code):errors[code]=errors.get(code,0)+1
 with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
  source={str(pk):(str(guid or ""),str(a),str(b),direction,typ)
          for pk,guid,a,b,direction,typ in db.execute("SELECT Connector_ID,ea_guid,Start_Object_ID,End_Object_ID,Direction,Connector_Type FROM t_connector WHERE Connector_Type='Generalization'")}
 nodes={str(n.get("sourceId")):n for n in graph.get("nodes",[]) if n.get("sourceId") is not None}
 seen=set()
 with open(ledger,newline="",encoding="utf-8") as f:
  reader=csv.DictReader(f)
  required={"source_pk","source_guid","raw_from","raw_to","family","normalized_from","normalized_to","status"}
  if not required.issubset(reader.fieldnames or []):
   fail("LEDGER_SCHEMA_MISMATCH")
  else:
   for r in reader:
    pk=r["source_pk"]
    if pk not in source:continue
    count+=1
    if pk in seen:fail("DUPLICATE_GENERALIZATION")
    seen.add(pk)
    guid,a,b,direction,typ=source[pk]
    if (r["source_guid"],r["raw_from"],r["raw_to"])!=(guid,a,b):
     fail("RAW_SOURCE_MISMATCH");continue
    if r["family"]!="Generalization":fail("FAMILY_MISMATCH")
    if r["normalized_from"]!=a or r["normalized_to"]!=b:fail("NORMALIZATION_DIRECTION_MISMATCH")
    if direction!="Source -> Destination":fail("SOURCE_DIRECTION_NOT_EXPLICIT")
    if r["status"]!="orientation_normalized":continue
    left,right=nodes.get(a),nodes.get(b)
    if not left or not right:fail("CANONICAL_NODE_MAPPING_MISSING");continue
    if left.get("kind")!=right.get("kind") or not str(left.get("kind","")).endswith("Definition"):
     fail("DEFINITION_COMPATIBILITY_UNVERIFIED")
    if left.get("id")==right.get("id"):fail("SELF_SPECIALIZATION")
 if len(seen)!=len(source):fail("GENERALIZATION_COVERAGE_MISMATCH")
 return {"schema":"mdse-phase9-source-bound-specialization-review/1","source_count":len(source),
         "ledger_generalizations":count,"graph_mapped_source_ids":len(nodes),
         "errors":dict(sorted(errors.items())),"native_certified":0,"may_emit_native":False,
         "input_sha256":{"qeax":sha256(qeax),"ledger":sha256(ledger)}}
if __name__=="__main__":
 p=argparse.ArgumentParser()
 for name in ("qeax","ledger","graph"):p.add_argument("--"+name,required=True)
 a=p.parse_args()
 for name in ("qeax","ledger","graph"):
  if not pathlib.Path(getattr(a,name)).is_file():p.error(name+" file does not exist")
 result=inspect(a.qeax,a.ledger,json.loads(pathlib.Path(a.graph).read_text()))
 print(json.dumps(result,indent=2))
