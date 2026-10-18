"""Local-only source-bound generalization edge check; no caller trust token.

Replays complete Phase8 ledger, then checks requested connector against read-only QEAX.
Does not certify SysML native semantics or expose source identities in output.
"""
import argparse,csv,json,pathlib,sqlite3
from replay_phase8_local_normalization import check as replay
def evaluate(qeax,ledger,registry,connector_pk,subtype_id,supertype_id):
    summary=replay(qeax,ledger,registry)
    errors=[]
    if not summary["valid"] or summary["source_count"]!=summary["ledger_count"]:
        errors.append("COMPLETE_LEDGER_REPLAY_FAILED")
        return {"eligibleForCanonicalReview":False,"diagnostics":errors,"nativeCertified":False}
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        db.row_factory=sqlite3.Row
        c=db.execute("SELECT Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_ID=?",(connector_pk,)).fetchone()
        if c is None:errors.append("SOURCE_CONNECTOR_MISSING")
        else:
            if c["Connector_Type"]!="Generalization" or (c["Stereotype"] or ""):
                errors.append("NOT_UNSTEREOTYPED_GENERALIZATION")
            if c["Direction"]!="Source -> Destination":errors.append("SOURCE_DIRECTION_UNVERIFIED")
            if (str(c["Start_Object_ID"]),str(c["End_Object_ID"]))!=(str(subtype_id),str(supertype_id)):
                errors.append("SOURCE_ENDPOINT_ORIENTATION_MISMATCH")
        matching=[]
        with open(ledger,newline="",encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row["source_pk"]==str(connector_pk):matching.append(row)
        if len(matching)!=1:errors.append("LEDGER_IDENTITY_NOT_UNIQUE")
        elif c is not None:
            row=matching[0]
            if row["family"]!="Generalization" or row["role"]!="source-subtype-to-destination-supertype" or row["status"]!="orientation_normalized":
                errors.append("LEDGER_ROLE_NOT_QUALIFIED")
            if (row["normalized_from"],row["normalized_to"])!=(str(subtype_id),str(supertype_id)):
                errors.append("LEDGER_ENDPOINT_ORIENTATION_MISMATCH")
    return {"eligibleForCanonicalReview":not errors,"diagnostics":sorted(set(errors)),"nativeCertified":False}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    for n in ("qeax","ledger","registry","connector-pk","subtype-id","supertype-id"):p.add_argument("--"+n,required=True)
    a=p.parse_args()
    out=evaluate(a.qeax,a.ledger,a.registry,a.connector_pk,a.subtype_id,a.supertype_id)
    print(json.dumps(out,indent=2))
    raise SystemExit(0 if out["eligibleForCanonicalReview"] else 1)
