"""Aggregate-only EA classifier/parent evidence for provisional generalizations."""
import argparse,collections,json,pathlib,sqlite3
STYLES={"Hardware Component","Physical Component","Module","Logical Signal"}
def present(v): return v is not None and str(v).strip() not in ("","0")
def evaluate(records):
 counts=collections.Counter()
 for source,target in records:
  counts["candidate_edges"]+=1
  for label,element in (("source",source),("target",target)):
   for field in ("Classifier","Classifier_guid","ParentID"):
    if present(element.get(field)): counts[label+"_"+field+"_populated"]+=1
   for field in ("IsSpec","Abstract"):
    if str(element.get(field) if element.get(field) is not None else "(null)")!="0":
     counts[label+"_"+field+"_nonzero_or_unknown"]+=1
 return {"schema":"mdse-phase9-definition-ownership-evidence/1","counts":dict(sorted(counts.items())),"native_certified":0}
def audit(qeax):
 with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
  db.row_factory=sqlite3.Row
  objects={str(r["Object_ID"]):dict(r) for r in db.execute("SELECT Object_ID,Object_Type,Stereotype,Classifier,Classifier_guid,ParentID,IsSpec,Abstract FROM t_object")}
  selected=[]
  for a,b in db.execute("SELECT Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'"):
   source=objects.get(str(a));target=objects.get(str(b))
   if not source or not target:continue
   if source["Object_Type"]!=target["Object_Type"]:continue
   if (source["Stereotype"] or "")!=(target["Stereotype"] or ""):continue
   if source["Stereotype"] not in STYLES:continue
   if source["Object_Type"] not in ("Class","Signal"):continue
   selected.append((source,target))
 return evaluate(selected)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);a=p.parse_args()
 if not pathlib.Path(a.qeax).is_file():p.error("QEAX file not found")
 print(json.dumps(audit(a.qeax),indent=2))
