"""Aggregate-only source stereotype review; no model identifiers or rows emitted."""
import collections,pathlib,sqlite3
TYPED={"block","Hardware Component","Module","Physical Component","Physical System Variant"}
def broad(o):
    return bool(o and (o[0] in ("Object","Part") or (o[0]=="Class" and o[1]!="Business Line" and "Interface" not in o[1])))
def typed(o):
    return bool(o and (o[0] in ("Object","Part") or (o[0]=="Class" and o[1] in TYPED)))
def audit(path):
    c=sqlite3.connect("file:"+str(pathlib.Path(path).resolve())+"?mode=ro",uri=True)
    try:
        objs={k:(t,s or "") for k,t,s in c.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        sets=collections.Counter(); endpoints=collections.Counter(); total=0
        for a,b,sa,da,d in c.execute("SELECT Start_Object_ID,End_Object_ID,SourceIsAggregate,DestIsAggregate,Direction FROM t_connector WHERE Connector_Type='Aggregation'"):
            x,y=objs.get(a),objs.get(b)
            baseline=(sa,da) in ((0,2),(2,0)) and broad(x) and broad(y)
            accepted_candidate=baseline and typed(x) and typed(y) and a!=b and d=="Source -> Destination"
            if not baseline or accepted_candidate:continue
            total+=1
            deferred=tuple(sorted({(o[1] or "<blank>") if o[0]=="Class" else o[0] for o in (x,y) if not typed(o)}))
            sets[" + ".join(deferred) or "<non-type-reason>"]+=1
            for o in (x,y):
                if not typed(o):endpoints[(o[1] or "<blank>") if o[0]=="Class" else o[0]]+=1
        return {"schema":"mdse-deferred-ea-ownership-stereotypes/1","deferredConnectors":total,
                "deferredConnectorCategorySets":dict(sorted(sets.items())),
                "deferredEndpointOccurrences":dict(sorted(endpoints.items())),
                "nativeCertified":0,"status":"REVIEW_REQUIRED"}
    finally:c.close()
