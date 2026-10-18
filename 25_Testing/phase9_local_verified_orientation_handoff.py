"""Local-only verified Phase8 generalization orientation projection.

Reads authoritative QEAX rows, cross-checks Phase8 ledger, and writes candidates
only to an explicit private output file. No native approval or network action.
"""
import argparse,csv,json,pathlib,sqlite3,sys,collections
from verify_phase8_rows_against_qeax import sha

def reconcile(qeax,ledger,registry,out):
    qa,le,re,output=(pathlib.Path(p).resolve() for p in (qeax,ledger,registry,out))
    if output.exists():raise ValueError("OUTPUT_ALREADY_EXISTS")
    if output.parent in {qa.parent,le.parent,re.parent} or output.parent==pathlib.Path.cwd():raise ValueError("OUTPUT_LOCATION_NOT_ISOLATED")
    errors=collections.Counter(); candidates=[]
    with sqlite3.connect(qa.as_uri()+"?mode=ro",uri=True) as db:
        db.row_factory=sqlite3.Row
        src={str(r["Connector_ID"]):r for r in db.execute("SELECT Connector_ID,ea_guid,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector")}
        with le.open(newline="",encoding="utf-8") as file:
            reader=csv.DictReader(file)
            required={"source_pk","source_guid","raw_from","raw_to","family","normalized_from","normalized_to","status"}
            if not required.issubset(reader.fieldnames or []):raise ValueError("LEDGER_SCHEMA_MISMATCH")
            seen=set()
            for row in reader:
                key=row["source_pk"]
                if key in seen:errors["DUPLICATE_LEDGER_KEY"]+=1;continue
                seen.add(key);original=src.get(key)
                if original is None:errors["EXTRA_LEDGER_ROW"]+=1;continue
                if (row["source_guid"],row["raw_from"],row["raw_to"])!=(str(original["ea_guid"] or ""),str(original["Start_Object_ID"]),str(original["End_Object_ID"])):
                    errors["RAW_IDENTITY_MISMATCH"]+=1;continue
                if original["Connector_Type"]!="Generalization":continue
                if original["Direction"]!="Source -> Destination":errors["GENERALIZATION_DIRECTION_REVIEW"]+=1;continue
                if (original["Stereotype"] or "").strip():errors["GENERALIZATION_STEREOTYPE_REVIEW"]+=1;continue
                if row["family"]!="Generalization" or row["normalized_from"]!=row["raw_from"] or row["normalized_to"]!=row["raw_to"]:
                    errors["GENERALIZATION_LEDGER_ORIENTATION_MISMATCH"]+=1;continue
                candidates.append({"kind":"specialization","sourceConnector":key,"fromId":row["raw_from"],"toId":row["raw_to"],"direction":"subtype-to-supertype","evidenceStatus":"source-orientation-matched-review-only"})
            absent=len(set(src)-seen)
            if absent:errors["MISSING_LEDGER_ROWS"]+=absent
    summary={"schema":"mdse-phase9-local-orientation-handoff/1","source_count":len(src),"review_candidates":len(candidates),
             "errors":dict(sorted(errors.items())),"native_certified":0,
             "hashes":{"qeax":sha(qa),"ledger":sha(le),"registry":sha(re)}}
    # Never issue an apparently trusted handoff if there are integrity failures.
    if errors:return summary
    output.write_text(json.dumps({"summary":summary,"candidates":candidates},indent=2)+"\n",encoding="utf-8")
    return summary

def main():
    p=argparse.ArgumentParser()
    for k in ("qeax","ledger","registry","out"):p.add_argument("--"+k,required=True)
    a=p.parse_args()
    try:result=reconcile(a.qeax,a.ledger,a.registry,a.out)
    except (ValueError,OSError,sqlite3.Error) as exc:p.error(type(exc).__name__+": "+str(exc))
    print(json.dumps(result,indent=2))
    return 0 if not result["errors"] else 1
if __name__=="__main__":sys.exit(main())
