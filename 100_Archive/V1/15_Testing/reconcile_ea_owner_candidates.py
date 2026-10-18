"""Reconcile broad Phase 8 and strict typed EA ownership candidates.

Evidence only: no accepted native SysML v2 usages and no record-level public output.
"""
from collections import Counter
import pathlib,sqlite3
APPROVED_CANDIDATE_STEREOTYPES={"block","Hardware Component","Module","Physical Component","Physical System Variant"}
def phase8_part(o):
    if not o:return False
    t,s=o
    return t in ("Object","Part") or (t=="Class" and s!="Business Line" and "Interface" not in s)
def typed_part(o):
    if not o:return False
    t,s=o
    return t in ("Object","Part") or (t=="Class" and s in APPROVED_CANDIDATE_STEREOTYPES)
def reconcile(path):
    db=sqlite3.connect("file:"+str(pathlib.Path(path).resolve())+"?mode=ro",uri=True)
    try:
        objs={i:(t,s or "") for i,t,s in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        counts=Counter(); reasons=Counter()
        for a,b,source_agg,dest_agg,direction in db.execute("""SELECT Start_Object_ID,End_Object_ID,
            SourceIsAggregate,DestIsAggregate,Direction FROM t_connector WHERE Connector_Type='Aggregation'"""):
            o1,o2=objs.get(a),objs.get(b)
            composite=(source_agg,dest_agg) in ((0,2),(2,0))
            broad=bool(composite and phase8_part(o1) and phase8_part(o2))
            strict=bool(composite and typed_part(o1) and typed_part(o2) and a!=b and direction=="Source -> Destination")
            counts[("phase8" if broad else "not_phase8","typed" if strict else "not_typed")]+=1
            if broad and not strict:
                if not (typed_part(o1) and typed_part(o2)):reasons["stereotype_scope"]+=1
                if a==b:reasons["self_reference"]+=1
                if direction!="Source -> Destination":reasons["nonexplicit_direction"]+=1
        return {"schema":"mdse-phase8-typed-ownership-reconciliation/1",
                "totalAggregations":sum(counts.values()),
                "phase8Candidates":sum(n for (x,_),n in counts.items() if x=="phase8"),
                "typedCandidates":sum(n for (_,y),n in counts.items() if y=="typed"),
                "crossClassification":{"/".join(k):v for k,v in sorted(counts.items())},
                "gapReasons":dict(sorted(reasons.items())),"nativeCertified":0}
    finally:db.close()
