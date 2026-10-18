"""Local-only source-bound generalization candidate handoff, not an authority token."""
import argparse,csv,hashlib,json,pathlib,sqlite3
from replay_phase8_local_normalization import check
def hashfile(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for chunk in iter(lambda:f.read(1048576),b""):h.update(chunk)
 return h.hexdigest()
def handoff(qeax,ledger,registry,connector_pk):
 replay=check(qeax,ledger,registry)
 if not replay["valid"] or replay["source_count"]!=replay["ledger_count"]:
  return {"ok":False,"reason":"FULL_LEDGER_REPLAY_FAILED","nativeCertified":False}
 with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
  source=db.execute("SELECT ea_guid,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_ID=?",(connector_pk,)).fetchone()
 if not source or source[1]!="Generalization" or (source[2] or "").strip() or source[3]!="Source -> Destination":
  return {"ok":False,"reason":"SOURCE_DIRECTION_OR_FAMILY_UNVERIFIED","nativeCertified":False}
 with open(ledger,encoding="utf-8",newline="") as f:
  rows=[row for row in csv.DictReader(f) if row.get("source_pk")==str(connector_pk)]
 if len(rows)!=1 or rows[0]["source_guid"]!=str(source[0] or "") or rows[0]["normalized_from"]!=str(source[4]) or rows[0]["normalized_to"]!=str(source[5]) or rows[0]["status"]!="orientation_normalized":
  return {"ok":False,"reason":"CANDIDATE_LEDGER_MISMATCH","nativeCertified":False}
 return {"ok":True,"reviewOnly":True,"nativeCertified":False,
  "sourceId":str(source[4]),"targetId":str(source[5]),"sourceRef":source[0],
  "direction":"subtype-to-supertype",
  "sourceBundle":{"qeaxSha256":hashfile(qeax),"ledgerSha256":hashfile(ledger),"registrySha256":hashfile(registry)}}
if __name__=="__main__":
 p=argparse.ArgumentParser()
 for a in ("qeax","ledger","registry","connector-pk"):p.add_argument("--"+a,required=True)
 p.add_argument("--local-output",required=True)
 a=p.parse_args();output=pathlib.Path(a.local_output).expanduser().resolve()
 if output.exists():p.error("output already exists")
 if any(output.is_relative_to(pathlib.Path(x).resolve().parent) for x in (a.qeax,a.ledger,a.registry)):
  p.error("output must be in a separate private directory")
 result=handoff(a.qeax,a.ledger,a.registry,a.connector_pk)
 output.write_text(json.dumps(result,indent=2)+"\n")
 try:output.chmod(0o600)
 except OSError:pass
 print(json.dumps({"ok":result["ok"],"reason":result.get("reason"),"reviewOnly":result.get("reviewOnly",False),"nativeCertified":False}))
 raise SystemExit(0 if result["ok"] else 1)
