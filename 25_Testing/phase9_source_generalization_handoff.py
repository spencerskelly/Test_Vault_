"""Local-only EA generalization evidence boundary, never native authorization.

Use after full Phase8 replay; return only aggregate counters. No source row export.
"""
import argparse,collections,json,pathlib,sqlite3
from replay_phase8_local_normalization import check as replay_check

def audit(qeax,ledger,registry):
    replay=replay_check(qeax,ledger,registry)
    counts=collections.Counter()
    if not replay["valid"] or replay["source_count"]!=replay["ledger_count"]:
        return {"schema":"mdse-phase9-source-generalization-handoff/1","eligible_for_review":False,
                "reason":"REPLAY_GATE_FAILED","error_categories":list(replay["error_counts"]),
                "native_certified":0}
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        nodes={str(i):(t,s or "") for i,t,s in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        for kind,stereotype,direction,a,b in db.execute(
                "SELECT Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'"):
            counts["generalizations"]+=1
            x,y=nodes.get(str(a)),nodes.get(str(b))
            if not x or not y:
                counts["endpoint_missing"]+=1
            elif direction!="Source -> Destination":
                counts["direction_not_explicit"]+=1
            elif (stereotype or "").strip():
                counts["connector_stereotype_review"]+=1
            elif x[0]!=y[0] or x[1]!=y[1]:
                counts["endpoint_semantic_review"]+=1
            else:
                counts["same_ea_kind_and_stereotype_review"]+=1
    return {"schema":"mdse-phase9-source-generalization-handoff/1","eligible_for_review":True,
            "counts":dict(sorted(counts.items())),"native_certified":0,
            "semantic_authorization":False,"exported_source_rows":0}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    for name in ("qeax","ledger","registry"):p.add_argument("--"+name,required=True)
    a=p.parse_args()
    for name in ("qeax","ledger","registry"):
        if not pathlib.Path(getattr(a,name)).is_file():p.error("Input not found: "+name)
    print(json.dumps(audit(a.qeax,a.ledger,a.registry),indent=2))
