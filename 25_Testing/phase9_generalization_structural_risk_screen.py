"""Read-only structural risk screening for high-volume generalization candidates.

Does not infer definitions or approve native specialization.
"""
import argparse,collections,json,pathlib,sqlite3
from phase9_high_volume_semantic_separation import classify

def cycles(edges):
    graph=collections.defaultdict(list)
    for a,b in edges:graph[a].append(b)
    color={};cyclic=set()
    def visit(n,stack):
        color[n]=1;stack.add(n)
        for m in graph[n]:
            if m in stack:cyclic.update(stack)
            elif color.get(m,0)==0:visit(m,stack)
        stack.remove(n);color[n]=2
    for n in list(graph):
        if color.get(n,0)==0:visit(n,set())
    return bool(cyclic)

def assess(evidence):
    counts=collections.Counter();edges=[]
    for a,b,source,target,direction,stereotype in evidence:
        if classify(source,target)!="SAME_STEREOTYPE_DEFINITION_CANDIDATE":continue
        counts["screened_candidates"]+=1
        if a==b:counts["self_generalization"]+=1
        if direction!="Source -> Destination":counts["direction_unverified"]+=1
        if (stereotype or "").strip():counts["connector_stereotype_review"]+=1
        if a!=b:edges.append((a,b))
    counts["candidate_graph_cycle_detected"]=int(cycles(edges))
    counts["remaining_semantic_evidence_required"]=counts["screened_candidates"]
    return {"schema":"mdse-phase9-definition-risk-screen/1","counts":dict(sorted(counts.items())),"native_certified":0}

def audit(qeax):
    with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
        nodes={str(i):(t,s or "") for i,t,s in db.execute("SELECT Object_ID,Object_Type,Stereotype FROM t_object")}
        evidence=[]
        for a,b,d,s in db.execute("SELECT Start_Object_ID,End_Object_ID,Direction,Stereotype FROM t_connector WHERE Connector_Type='Generalization'"):
            x,y=nodes.get(str(a)),nodes.get(str(b))
            if x and y:evidence.append((str(a),str(b),x,y,d,s))
        return assess(evidence)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);a=p.parse_args()
    if not pathlib.Path(a.qeax).is_file():p.error("QEAX not found")
    print(json.dumps(audit(a.qeax),indent=2))
