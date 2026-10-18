"""Local-only, fail-closed EA Generalization direction evidence assessment.

Reads immutable SQLite source and matching private ledger. Never prints source rows.
This is a source consistency gate, not a SysML semantic or native approval gate.
"""
import argparse,collections,csv,json,pathlib,sqlite3
from verify_phase8_rows_against_qeax import sha

def assess(qeax,ledger):
    counts=collections.Counter()
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        source={str(pk):(str(guid or ""),str(a),str(b),direction or "") for pk,guid,a,b,direction in db.execute("SELECT Connector_ID,ea_guid,Start_Object_ID,End_Object_ID,Direction FROM t_connector WHERE Connector_Type='Generalization'")}
    seen=set()
    with open(ledger,encoding="utf-8",newline="") as file:
        rows=csv.DictReader(file)
        required={"source_pk","source_guid","raw_from","raw_to","normalized_from","normalized_to","source_direction","family"}
        if not required.issubset(rows.fieldnames or []):
            return {"schema":"mdse-phase9-source-direction-assessment/1","error_counts":{"LEDGER_SCHEMA_MISMATCH":1},"source_count":len(source),"native_certified":0,"direction_semantics_certified":False}
        for row in rows:
            pk=row["source_pk"]
            if pk not in source:continue
            if pk in seen:counts["DUPLICATE_GENERALIZATION"]+=1
            seen.add(pk)
            guid,a,b,direction=source[pk]
            if (row["source_guid"],row["raw_from"],row["raw_to"],row["source_direction"])!=(guid,a,b,direction):
                counts["SOURCE_EVIDENCE_MISMATCH"]+=1
            if row["normalized_from"]!=a or row["normalized_to"]!=b:counts["ORIENTATION_MISMATCH"]+=1
            if row["family"]!="Generalization":counts["FAMILY_MISMATCH"]+=1
            if direction!="Source -> Destination":counts["EXPLICIT_DIRECTION_NOT_PRESENT"]+=1
    counts["MISSING_GENERALIZATIONS"]=len(set(source)-seen)
    return {"schema":"mdse-phase9-source-direction-assessment/1","source_count":len(source),
            "ledger_count":len(seen),"error_counts":dict(sorted(counts.items())),
            "source_sha256":sha(qeax),"ledger_sha256":sha(ledger),
            "native_certified":0,"direction_semantics_certified":False}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);p.add_argument("--ledger",required=True);a=p.parse_args()
    for name,path in (("QEAX",a.qeax),("ledger",a.ledger)):
        if not pathlib.Path(path).is_file():p.error(name+" file not found")
    print(json.dumps(assess(a.qeax,a.ledger),indent=2))
