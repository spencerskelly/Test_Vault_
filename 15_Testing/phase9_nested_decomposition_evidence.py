"""Aggregate-only physical-decomposition evidence for nested generalization endpoints."""
import argparse,collections,json,pathlib,sqlite3
STYLES={"Hardware Component","Physical Component","Module","Logical Signal"}
def audit(qeax):
 c=collections.Counter()
 with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
  objs={r[0]:(r[1],r[2],r[3] or "",r[4] or 0) for r in db.execute("SELECT Object_ID,ParentID,Object_Type,Stereotype,Classifier FROM t_object")}
  edges=list(db.execute("SELECT Connector_Type,Start_Object_ID,End_Object_ID FROM t_connector"))
  selected=set()
  for typ,a,b in edges:
   if typ!="Generalization":continue
   x,y=objs.get(a),objs.get(b)
   if not x or not y or x[1:3]!=y[1:3] or x[2] not in STYLES or x[1] not in ("Class","Signal"):continue
   for identifier,elem in ((a,x),(b,y)):
    if elem[0]:selected.add(identifier)
  c["nested_elements"]=len(selected)
  child_count=collections.Counter(x[0] for x in objs.values() if x[0])
  for identifier in selected:
   parent=objs[identifier][0]
   if child_count[identifier]:c["nested_with_children"]+=1
   for typ,a,b in edges:
    if identifier not in (a,b):continue
    other=b if a==identifier else a
    if typ=="Aggregation":c["incident_aggregation"]+=1
    if typ=="Generalization":c["generalization_to_parent" if other==parent else "generalization_other"]+=1
    if typ not in ("Generalization","Aggregation"):c["other_incident_"+typ]+=1
 return {"schema":"mdse-phase9-nested-decomposition-evidence/1","counts":dict(sorted(c.items())),"native_certified":0}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);a=p.parse_args()
 if not pathlib.Path(a.qeax).is_file():p.error("QEAX not found")
 print(json.dumps(audit(a.qeax),indent=2))
