"""Fail-closed local-only Phase 8 to canonical specialization evidence audit.

Checks source/ledger parity without producing portable 'trusted' flags or source rows.
"""
import argparse,collections,csv,json,pathlib,sqlite3
from verify_phase8_rows_against_qeax import sha

def audit(qeax,ledger):
    errors=collections.Counter()
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        db.row_factory=sqlite3.Row
        originals={str(r["Connector_ID"]):r for r in db.execute(
            "SELECT Connector_ID,ea_guid,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector")}
        nodes={str(r[0]):(r[1],r[2] or "") for r in db.execute(
            "SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
    seen=set(); candidates=0; checked=0
    with open(ledger,encoding="utf-8",newline="") as handle:
        reader=csv.DictReader(handle)
        required={"source_pk","source_guid","raw_from","raw_to","family","normalized_from","normalized_to","status"}
        if not required.issubset(reader.fieldnames or []):
            errors["LEDGER_SCHEMA_MISMATCH"]+=1
        else:
            for row in reader:
                checked+=1;pk=row["source_pk"]
                if pk in seen:errors["DUPLICATE_KEY"]+=1
                seen.add(pk);src=originals.get(pk)
                if not src:errors["UNKNOWN_SOURCE_KEY"]+=1;continue
                if (row["source_guid"],row["raw_from"],row["raw_to"])!=(
                    str(src["ea_guid"] or ""),str(src["Start_Object_ID"]),str(src["End_Object_ID"])):
                    errors["RAW_SOURCE_MISMATCH"]+=1
                if src["Connector_Type"]!="Generalization":continue
                if row["family"]!="Generalization":errors["GENERALIZATION_FAMILY_MISMATCH"]+=1
                if src["Direction"]!="Source -> Destination":
                    errors["GENERALIZATION_DIRECTION_REVIEW"]+=1;continue
                if row["normalized_from"]!=str(src["Start_Object_ID"]) or row["normalized_to"]!=str(src["End_Object_ID"]):
                    errors["GENERALIZATION_ORIENTATION_MISMATCH"]+=1;continue
                if (src["Stereotype"] or "").strip():
                    errors["GENERALIZATION_CONNECTOR_STEREOTYPE_REVIEW"]+=1;continue
                a=nodes.get(str(src["Start_Object_ID"]));b=nodes.get(str(src["End_Object_ID"]))
                if not a or not b:errors["ENDPOINT_MISSING"]+=1;continue
                if a!=b:errors["DEFINITION_INTENT_REVIEW"]+=1;continue
                if a[0] not in ("Class","Activity","State","Requirement","Signal"):
                    errors["DEFINITION_KIND_REVIEW"]+=1;continue
                candidates+=1
    missing=len(set(originals)-seen)
    if missing:errors["MISSING_SOURCE_KEYS"]+=missing
    return {"schema":"mdse-phase9-local-specialization-evidence-screen/1",
            "source_count":len(originals),"ledger_count":checked,
            "consistent":not any(errors[k] for k in ("LEDGER_SCHEMA_MISMATCH","DUPLICATE_KEY","UNKNOWN_SOURCE_KEY","RAW_SOURCE_MISMATCH","GENERALIZATION_FAMILY_MISMATCH","GENERALIZATION_ORIENTATION_MISMATCH","MISSING_SOURCE_KEYS")),
            "candidate_screen_count":candidates,"diagnostic_counts":dict(sorted(errors.items())),
            "local_input_sha256":{"qeax":sha(qeax),"ledger":sha(ledger)},
            "native_certified":0,"may_emit_native":False}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--qeax",required=True);p.add_argument("--ledger",required=True)
    a=p.parse_args()
    for name in ("qeax","ledger"):
        if not pathlib.Path(getattr(a,name)).is_file():p.error(name+" not found")
    result=audit(a.qeax,a.ledger);print(json.dumps(result,indent=2))
    raise SystemExit(0 if result["consistent"] else 1)
