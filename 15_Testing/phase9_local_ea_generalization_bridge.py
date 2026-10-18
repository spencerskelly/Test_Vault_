"""Local-only EA generalization evidence bridge. Emits no native SysML, no public rows.
Review-only projection; callers must not mistake a self-reported token for trusted attestation.
"""
import argparse,csv,hashlib,json,pathlib,sqlite3,sys

def digest(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for chunk in iter(lambda:f.read(1024*1024),b""):h.update(chunk)
 return h.hexdigest()

def bridge(qeax,ledger,registry):
 from replay_phase8_local_normalization import check
 replay=check(qeax,ledger,registry)
 if not replay["valid"] or replay["source_count"]!=replay["ledger_count"]:
  return {"valid":False,"errors":["SOURCE_REPLAY_FAILED"],"replay_errors":replay["error_counts"],"native_certified":0},[]
 with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
  source={str(pk):(str(a),str(b),d,typ,sty or "") for pk,a,b,d,typ,sty in db.execute("SELECT Connector_ID,Start_Object_ID,End_Object_ID,Direction,Connector_Type,Stereotype FROM t_connector WHERE Connector_Type='Generalization'")}
 results=[];rejected=0
 with open(ledger,newline="",encoding="utf-8") as f:
  for row in csv.DictReader(f):
   x=source.get(row["source_pk"])
   if x is None:continue
   start,end,direction,typ,stereo=x
   accepted=(direction=="Source -> Destination" and not stereo and
    row["raw_from"]==start and row["raw_to"]==end and
    row["normalized_from"]==start and row["normalized_to"]==end and
    row["status"]=="orientation_normalized")
   if not accepted:rejected+=1;continue
   results.append({"kind":"specialization","fromId":start,"toId":end,
                   "direction":"subtype-to-supertype","sourceRef":row["source_guid"],
                   "reviewStatus":"SOURCE_ORIENTATION_ONLY","nativeCertified":False})
 report={"schema":"mdse-phase9-local-ea-generalization-bridge/1","valid":True,
   "source_generalizations":len(source),"orientation_candidates":len(results),
   "review_or_deferred":rejected,"native_certified":0,
   "sha256":{"qeax":digest(qeax),"ledger":digest(ledger),"registry":digest(registry)}}
 return report,results

def main():
 p=argparse.ArgumentParser()
 for key in ("qeax","ledger","registry"):p.add_argument("--"+key,required=True)
 p.add_argument("--private-output",required=True,help="Outside repository; contains source identifiers")
 a=p.parse_args()
 target=pathlib.Path(a.private_output).expanduser().resolve()
 if target.exists():p.error("Refusing to overwrite private output")
 repo=pathlib.Path(__file__).resolve().parents[1]
 if target==repo or repo in target.parents:p.error("Private output must be outside repository")
 for key in ("qeax","ledger","registry"):
  if not pathlib.Path(getattr(a,key)).is_file():p.error(key+" not found")
 report,rows=bridge(a.qeax,a.ledger,a.registry)
 if not report["valid"]:print(json.dumps(report));return 1
 target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps({"report":report,"reviewOnlyRelationships":rows},indent=2)+"\n")
 try:target.chmod(0o600)
 except OSError:pass
 print(json.dumps(report,indent=2))
 return 0
if __name__=="__main__":sys.exit(main())
