"""Independent conservative generalization checks; never certifies native emission.

Consumes source evidence fields without calling Phase 8 decide() or kind().
"""
import collections,csv,json,pathlib,sqlite3,sys,argparse

def classify(element_type,stereotype):
    if element_type=="Class" and stereotype=="block": return "block_definition_candidate"
    if element_type=="Class" and stereotype=="": return "unstereotyped_class_review"
    return "other_review"

def decision(connector,source,target):
    if connector["Connector_Type"]!="Generalization":return "NOT_GENERALIZATION"
    if (connector["Stereotype"] or "").strip():return "STEREOTYPED_GENERALIZATION_REVIEW"
    if connector["Direction"]!="Source -> Destination":return "DIRECTION_UNVERIFIED"
    if not source or not target:return "MISSING_ENDPOINT"
    src=classify(source[0],source[1])
    dst=classify(target[0],target[1])
    if src=="block_definition_candidate" and dst=="block_definition_candidate":
        return "ORIENTATION_AND_BLOCK_KINDS_CANDIDATE"
    return "ENDPOINT_SEMANTICS_REVIEW"

def audit(qeax,ledger):
    counts=collections.Counter()
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        db.row_factory=sqlite3.Row
        nodes={str(r["Object_ID"]):(r["Object_Type"],r["Stereotype"] or "") for r in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        source={str(r["Connector_ID"]):r for r in db.execute("SELECT Connector_ID,Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'")}
        observed=set()
        with open(ledger,newline="",encoding="utf-8") as file:
            reader=csv.DictReader(file)
            necessary={"source_pk","family","normalized_from","normalized_to","status"}
            if not necessary.issubset(reader.fieldnames or []):raise ValueError("LEDGER_SCHEMA_MISMATCH")
            for row in reader:
                pk=row["source_pk"]
                if pk not in source:continue
                if pk in observed:counts["DUPLICATE_GENERALIZATION_ROW"]+=1
                observed.add(pk)
                c=source[pk]
                result=decision(c,nodes.get(str(c["Start_Object_ID"])),nodes.get(str(c["End_Object_ID"])))
                counts[result]+=1
                if row["normalized_from"]!=str(c["Start_Object_ID"]) or row["normalized_to"]!=str(c["End_Object_ID"]):
                    counts["ORIENTATION_LEDGER_MISMATCH"]+=1
                if result!="ORIENTATION_AND_BLOCK_KINDS_CANDIDATE" and row["status"]=="orientation_normalized":
                    counts["PHASE8_BROADER_THAN_STRICT_BLOCK_POLICY"]+=1
        counts["MISSING_GENERALIZATION_ROWS"]=len(set(source)-observed)
        counts["GENERALIZATION_SOURCE_COUNT"]=len(source)
    return {"schema":"mdse-phase9-generalization-independent-audit/1","counts":dict(sorted(counts.items())),"native_certified":0}

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--qeax",required=True);parser.add_argument("--ledger",required=True)
    args=parser.parse_args()
    missing=[name for name,path in (("qeax",args.qeax),("ledger",args.ledger)) if not pathlib.Path(path).is_file()]
    if missing:parser.error("Missing local inputs: "+", ".join(missing))
    print(json.dumps(audit(args.qeax,args.ledger),indent=2))
