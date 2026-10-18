"""Local-only, fail-closed Phase 8 source-to-canonical specialization gate.

Never trusts a caller-provided attestation boolean. Replays the complete ledger
before evaluating requested connector IDs. No model records are written to stdout.
"""
import csv,pathlib,sqlite3
from replay_phase8_local_normalization import check as replay

def qualify(qeax,ledger,registry,connector_ids):
    baseline=replay(qeax,ledger,registry)
    errors=[]
    if not baseline["valid"] or baseline["source_count"]!=baseline["ledger_count"]:
        return {"qualified":0,"requested":len(connector_ids),"errors":["FULL_REPLAY_FAILED"],"native_certified":0}
    if len(connector_ids)!=len(set(connector_ids)):
        return {"qualified":0,"requested":len(connector_ids),"errors":["DUPLICATE_REQUEST"],"native_certified":0}
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        db.row_factory=sqlite3.Row
        originals={str(r["Connector_ID"]):r for r in db.execute("SELECT Connector_ID,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector")}
        nodes={str(r["Object_ID"]):(r["Object_Type"],r["Stereotype"] or "") for r in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
    with open(ledger,newline="",encoding="utf-8") as f:
        indexed={r["source_pk"]:r for r in csv.DictReader(f)}
    qualified=0
    for pk in connector_ids:
        source=originals.get(str(pk));row=indexed.get(str(pk))
        if source is None or row is None:
            errors.append("MISSING_SOURCE_CONNECTOR");continue
        if source["Connector_Type"]!="Generalization" or (source["Stereotype"] or "").strip():
            errors.append("NOT_PLAIN_GENERALIZATION");continue
        if source["Direction"]!="Source -> Destination":
            errors.append("DIRECTION_NOT_EXPLICIT");continue
        a=nodes.get(str(source["Start_Object_ID"]));b=nodes.get(str(source["End_Object_ID"]))
        if not a or not b or a[0]!=b[0] or a[1]!=b[1]:
            errors.append("ENDPOINT_KIND_REVIEW");continue
        if a[0] not in ("Class","Activity","State","Requirement","Signal","InformationItem"):
            errors.append("DEFINITION_INTENT_UNVERIFIED");continue
        if row["normalized_from"]!=str(source["Start_Object_ID"]) or row["normalized_to"]!=str(source["End_Object_ID"]):
            errors.append("LEDGER_DIRECTION_MISMATCH");continue
        qualified+=1
    return {"qualified":qualified,"requested":len(connector_ids),
            "review_required":len(connector_ids)-qualified,"errors":sorted(set(errors)),
            "schema":"mdse-phase9-local-specialization-evidence/1",
            "semantic_approved":False,"native_certified":0}
