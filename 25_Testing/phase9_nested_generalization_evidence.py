"""Aggregate nested generalization endpoint evidence; no identifiers exported."""
import argparse,collections,json,pathlib,sqlite3
HIGH={"Hardware Component","Physical Component","Module","Logical Signal"}
def audit(path):
 counts=collections.Counter(); nested=set(); nested_links=collections.Counter()
 with sqlite3.connect(pathlib.Path(path).resolve().as_uri()+"?mode=ro",uri=True) as db:
  db.row_factory=sqlite3.Row
  objects={str(r["Object_ID"]):r for r in db.execute("SELECT Object_ID,ea_guid,Object_Type,Stereotype,ParentID,Classifier,Classifier_guid FROM t_object")}
  xref=set(str(r[0]).strip("{}").lower() for r in db.execute("SELECT Client FROM t_xref WHERE Name='Stereotypes' AND Type='element property'"))
  for a,b in db.execute("SELECT Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'"):
   x,y=objects.get(str(a)),objects.get(str(b))
   if not x or not y or x["Object_Type"]!=y["Object_Type"] or x["Stereotype"]!=y["Stereotype"] or x["Stereotype"] not in HIGH or x["Object_Type"] not in ("Class","Signal"):continue
   counts["candidate_edges"]+=1
   for role,r in (("source",x),("target",y)):
    if not r["ParentID"]:continue
    counts[role+"_nested_appearances"]+=1
    nested.add(str(r["Object_ID"]))
    p=objects.get(str(r["ParentID"]))
    nested_links[(role,p["Object_Type"] if p else "MISSING_PARENT",p["Stereotype"] or "" if p else "")]+=1
    if not p:counts["missing_parent_appearances"]+=1
    if r["Classifier"] or r["Classifier_guid"]:counts["nested_with_classifier_reference"]+=1
    if str(r["ea_guid"] or "").strip("{}").lower() in xref:counts["nested_with_extended_stereotype_record"]+=1
 counts["unique_nested_endpoint_elements"]=len(nested)
 return {"schema":"mdse-phase9-nested-generalization-evidence/1","counts":dict(sorted(counts.items())),"parent_type_stereotype_counts":[{"role":r,"parent_type":t,"parent_stereotype":s,"count":n} for (r,t,s),n in sorted(nested_links.items())],"native_certified":0}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);a=p.parse_args()
 if not pathlib.Path(a.qeax).is_file():p.error("QEAX file not found")
 print(json.dumps(audit(a.qeax),indent=2))
