"""Local-only Phase 8 evidence bundle verifier. Never publishes model rows."""
import argparse,csv,hashlib,json,pathlib
def digest(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for chunk in iter(lambda:f.read(1048576),b""):h.update(chunk)
 return h.hexdigest()
def verify(qeax,ledger,registry,source_attestation):
 att=json.loads(pathlib.Path(source_attestation).read_text())
 errors=[]
 if att.get("schema")!="mdse-phase8-input-attestation/1":errors.append("BAD_INPUT_ATTESTATION_SCHEMA")
 if att.get("source_sha256")!=digest(qeax):errors.append("QEAX_HASH_MISMATCH")
 if att.get("registry_sha256")!=digest(registry):errors.append("REGISTRY_HASH_MISMATCH")
 if att.get("native_certified")!=0:errors.append("NATIVE_CERTIFICATION_FORBIDDEN")
 with open(ledger,newline="",encoding="utf-8") as f:
  reader=csv.DictReader(f)
  required={"source_pk","source_guid","raw_from","raw_to","normalized_from","normalized_to","status","diagnostics"}
  if not required.issubset(reader.fieldnames or []):errors.append("LEDGER_SCHEMA_MISMATCH")
  rows=list(reader) if not errors else []
 seen=set()
 for row in rows:
  key=row["source_pk"]
  if not key or key in seen:errors.append("DUPLICATE_OR_EMPTY_CONNECTOR_KEY")
  seen.add(key)
  if not row["source_guid"] or not row["raw_from"] or not row["raw_to"]:errors.append("INCOMPLETE_SOURCE_IDENTITY")
 result={"schema":"mdse-phase8-local-ledger-verification/1","verified":not errors,
         "native_certified":0,"connector_count":len(rows),
         "errors":sorted(set(errors)),"input_hashes":{"qeax":digest(qeax),"ledger":digest(ledger),"registry":digest(registry)}}
 return result
def main():
 p=argparse.ArgumentParser()
 for name in ("qeax","ledger","registry","source-attestation"):p.add_argument("--"+name,required=True)
 p.add_argument("--report",required=True)
 a=p.parse_args()
 report=pathlib.Path(a.report).resolve()
 if report.exists():p.error("REPORT_ALREADY_EXISTS")
 inputs=[pathlib.Path(getattr(a,k.replace("-","_"))).resolve() for k in ("qeax","ledger","registry","source-attestation")]
 if report.parent in [x.parent for x in inputs] or any(report==x for x in inputs):p.error("REPORT_MUST_BE_SEPARATE")
 result=verify(*inputs)
 report.write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps({"verified":result["verified"],"connector_count":result["connector_count"],"errors":result["errors"]}))
 raise SystemExit(0 if result["verified"] else 1)
if __name__=="__main__":main()
