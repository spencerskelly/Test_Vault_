"""Local-only Phase 8 to canonical specialization candidate handoff.

This is NOT a trusted issuer: no private connector IDs, GUIDs or edges are printed.
"""
import argparse,collections,csv,json,pathlib,sqlite3
def assess(record,source):
    if source is None:return "SOURCE_CONNECTOR_MISSING"
    if source["Connector_Type"]!="Generalization":return "WRONG_SOURCE_FAMILY"
    if record.get("source_guid")!=str(source["ea_guid"] or ""):return "SOURCE_IDENTITY_MISMATCH"
    if record.get("raw_from")!=str(source["Start_Object_ID"]) or record.get("raw_to")!=str(source["End_Object_ID"]):return "RAW_ENDPOINT_MISMATCH"
    if source["Direction"]!="Source -> Destination" or record.get("source_direction")!=source["Direction"]:return "SOURCE_DIRECTION_UNVERIFIED"
    if record.get("normalized_from")!=str(source["Start_Object_ID"]) or record.get("normalized_to")!=str(source["End_Object_ID"]):return "NORMALIZED_ENDPOINT_MISMATCH"
    if record.get("family")!="Generalization" or record.get("rule")!="GENERALIZE":return "NORMALIZATION_FAMILY_MISMATCH"
    if record.get("role")!="source-subtype-to-destination-supertype":return "NORMALIZED_ROLE_UNVERIFIED"
    if record.get("status")!="orientation_normalized":return "REVIEW_STATUS"
    return "STRUCTURAL_DIRECTION_CANDIDATE_ONLY"
def audit(qeax,ledger):
    counts=collections.Counter();observed=set()
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        db.row_factory=sqlite3.Row
        sources={str(r["Connector_ID"]):r for r in db.execute("SELECT Connector_ID,ea_guid,Connector_Type,Direction,Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'")}
        with open(ledger,newline="",encoding="utf-8") as f:
            reader=csv.DictReader(f)
            required={"source_pk","source_guid","raw_from","raw_to","source_direction","normalized_from","normalized_to","family","rule","role","status"}
            if not required.issubset(reader.fieldnames or []):raise ValueError("LEDGER_SCHEMA_MISMATCH")
            for row in reader:
                pk=row["source_pk"]
                if pk not in sources:continue
                if pk in observed:counts["DUPLICATE_CONNECTOR"]+=1;continue
                observed.add(pk)
                counts[assess(row,sources[pk])]+=1
    counts["MISSING_GENERALIZATION_ROWS"]=len(set(sources)-observed)
    counts["SOURCE_GENERALIZATIONS"]=len(sources)
    return {"schema":"mdse-phase9-local-direction-handoff/1","counts":dict(sorted(counts.items())),"native_certified":0,"trust_issuer":False}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);p.add_argument("--ledger",required=True);a=p.parse_args()
    for name,path in (("qeax",a.qeax),("ledger",a.ledger)):
        if not pathlib.Path(path).is_file():p.error(name+" file not found")
    print(json.dumps(audit(a.qeax,a.ledger),indent=2))
