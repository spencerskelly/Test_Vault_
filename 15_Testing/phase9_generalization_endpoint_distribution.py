"""Aggregate-only review distribution for conservative Phase 9 generalization matrix."""
import argparse,collections,json,pathlib,sqlite3
from phase9_generalization_family_matrix import assess

def distribution(qeax):
    types=collections.Counter(); stereotypes=collections.Counter(); directions=collections.Counter()
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        obj={str(i):(t,(s or "").strip()) for i,t,s in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        for typ,sty,direction,a,b in db.execute("SELECT Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'"):
            x=obj.get(str(a));y=obj.get(str(b))
            category=assess(x,y,direction,sty) if x and y else "MISSING_ENDPOINT"
            if category=="SAME_DEFINITION_FAMILY_CANDIDATE:PartDefinition" or category.startswith("SAME_DEFINITION_FAMILY_CANDIDATE:"):
                continue
            if category!="ENDPOINT_KIND_REVIEW":
                continue
            types[((x or ("MISSING",""))[0],(y or ("MISSING",""))[0])]+=1
            stereotypes[(x or ("MISSING",""))[0],(x or ("",""))[1],(y or ("MISSING",""))[0],(y or ("",""))[1]]+=1
            directions[direction or "(none)"]+=1
    return {"schema":"mdse-phase9-generalization-endpoint-distribution/1",
            "review_count":sum(types.values()),
            "type_pairs":[{"source_type":a,"target_type":b,"count":n} for (a,b),n in sorted(types.items(),key=lambda v:(-v[1],v[0]))],
            "stereotype_pairs":[{"source_type":a,"source_stereotype":b,"target_type":c,"target_stereotype":d,"count":n} for (a,b,c,d),n in sorted(stereotypes.items(),key=lambda v:(-v[1],v[0]))],
            "directions":dict(sorted(directions.items())),"native_certified":0}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);a=p.parse_args()
    if not pathlib.Path(a.qeax).is_file():p.error("QEAX file not found")
    print(json.dumps(distribution(a.qeax),indent=2))
