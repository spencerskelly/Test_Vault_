"""Full local QEAX-to-Phase8 ledger row reconciliation; never exports source rows."""
import collections
import csv
import hashlib
import json
import pathlib
import sqlite3

def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1048576),b""): h.update(b)
    return h.hexdigest()

def verify_rows(qeax, ledger, registry, input_attestation, expected_count=None):
    errors=collections.Counter()
    att=json.loads(pathlib.Path(input_attestation).read_text(encoding="utf-8"))
    if att.get("schema")!="mdse-phase8-input-attestation/1": errors["BAD_ATTESTATION_SCHEMA"]+=1
    if att.get("source_sha256")!=sha(qeax): errors["QEAX_HASH_MISMATCH"]+=1
    if att.get("registry_sha256")!=sha(registry): errors["REGISTRY_HASH_MISMATCH"]+=1
    if att.get("native_certified")!=0: errors["NATIVE_CERTIFICATION_FORBIDDEN"]+=1
    source={}
    uri=pathlib.Path(qeax).resolve().as_uri()+"?mode=ro"
    with sqlite3.connect(uri,uri=True) as db:
        for pk,guid,a,b in db.execute("SELECT Connector_ID,ea_guid,Start_Object_ID,End_Object_ID FROM t_connector"):
            source[str(pk)]=(str(guid or ""),str(a),str(b))
    if expected_count is not None and len(source)!=expected_count: errors["SOURCE_COUNT_MISMATCH"]+=1
    seen=set()
    with open(ledger,encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f)
        required={"source_pk","source_guid","raw_from","raw_to","normalized_from","normalized_to"}
        if not required.issubset(reader.fieldnames or []):
            errors["LEDGER_SCHEMA_MISMATCH"]+=1
        else:
            for row in reader:
                pk=row["source_pk"]
                if not pk or pk in seen: errors["DUPLICATE_OR_EMPTY_KEY"]+=1
                seen.add(pk)
                original=source.get(pk)
                if original is None: errors["UNKNOWN_LEDGER_KEY"]+=1
                elif (row["source_guid"],row["raw_from"],row["raw_to"])!=original:
                    errors["SOURCE_ROW_MISMATCH"]+=1
                if not row["normalized_from"] or not row["normalized_to"]:
                    errors["MISSING_NORMALIZED_ENDPOINT"]+=1
    missing=len(set(source)-seen)
    if missing: errors["MISSING_LEDGER_ROWS"]+=missing
    hashes={"qeax":sha(qeax),"registry":sha(registry),"ledger":sha(ledger),"input_attestation":sha(input_attestation)}
    return {"schema":"mdse-phase8-reconciled-local-manifest/1","verified":not errors,
            "native_certified":0,"source_count":len(source),"ledger_count":len(seen),
            "error_counts":dict(sorted(errors.items())),"sha256":hashes}
