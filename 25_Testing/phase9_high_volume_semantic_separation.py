"""Independent aggregate separation of EA definition and usage generalizations."""
import argparse,collections,json,pathlib,sqlite3
HIGH={"Hardware Component","Physical Component","Module","Logical Signal"}
def classify(a,b):
    ta,sa=a;tb,sb=b
    if ta in ("Object","Part","Action") or tb in ("Object","Part","Action"):
        return "USAGE_OR_OCCURRENCE_REVIEW"
    if (ta,sa)==(tb,sb) and sa in HIGH and ta in ("Class","Signal"):
        return "SAME_STEREOTYPE_DEFINITION_CANDIDATE"
    if sa in HIGH or sb in HIGH:
        return "CROSS_STEREOTYPE_OR_KIND_REVIEW"
    return "OUTSIDE_SCOPE"
def audit(qeax):
    counts=collections.Counter()
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        nodes={str(i):(t,s or "") for i,t,s in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        for x,y in db.execute("SELECT Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'"):
            a=nodes.get(str(x));b=nodes.get(str(y))
            if a is None or b is None:counts["MISSING_ENDPOINT"]+=1;continue
            c=classify(a,b)
            if c!="OUTSIDE_SCOPE":counts[c]+=1
    return {"schema":"mdse-phase9-high-volume-separation/1","counts":dict(sorted(counts.items())),"native_certified":0}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);a=p.parse_args()
    if not pathlib.Path(a.qeax).is_file():p.error("QEAX not found")
    print(json.dumps(audit(a.qeax),indent=2))
