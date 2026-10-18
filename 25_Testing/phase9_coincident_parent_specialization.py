"""Read-only, aggregate-only review of coincident EA lexical parent and supertype."""
import argparse,collections,json,pathlib,sqlite3
def qualify(child,parent,edges):
 if not child or not parent:return "MISSING_CONTEXT_REVIEW"
 if str(child.get("ParentID"))!=str(parent.get("Object_ID")):return "NOT_LEXICAL_PARENT"
 if child.get("Object_Type")!="Class" or parent.get("Object_Type")!="Class":return "NON_CLASS_CONTEXT_REVIEW"
 if child.get("Stereotype")!="Hardware Component" or parent.get("Stereotype")!="Hardware Component":return "DIFFERENT_STEREOTYPE_REVIEW"
 forward=[d for a,b,d in edges if str(a)==str(child["Object_ID"]) and str(b)==str(parent["Object_ID"])]
 reverse=[d for a,b,d in edges if str(a)==str(parent["Object_ID"]) and str(b)==str(child["Object_ID"])]
 if reverse:return "REVERSE_PARENT_GENERALIZATION_REVIEW"
 if not forward:return "NO_PARENT_GENERALIZATION"
 if len(forward)!=1 or forward[0]!="Source -> Destination":return "MULTIPLE_OR_UNVERIFIED_DIRECTION_REVIEW"
 return "COINCIDENT_PARENT_AND_SUPERTYPE_REVIEW"
def audit(path):
 counts=collections.Counter()
 with sqlite3.connect(pathlib.Path(path).resolve().as_uri()+"?mode=ro",uri=True) as db:
  db.row_factory=sqlite3.Row
  nodes={str(r["Object_ID"]):dict(r) for r in db.execute("SELECT Object_ID,ParentID,Object_Type,Stereotype FROM t_object")}
  edges=[(str(a),str(b),d) for a,b,d in db.execute("SELECT Start_Object_ID,End_Object_ID,Direction FROM t_connector WHERE Connector_Type='Generalization'")]
  nested={n for a,b,_ in edges for n in (a,b) if n in nodes and nodes[n]["ParentID"] and nodes[n]["Stereotype"]=="Hardware Component"}
  counts["unique_nested_hardware_endpoints"]=len(nested)
  for n in nested:
   c=nodes[n];counts[qualify(c,nodes.get(str(c["ParentID"])),edges)]+=1
 return {"schema":"mdse-phase9-coincident-parent-specialization/1","counts":dict(sorted(counts.items())),"native_certified":0,"may_emit_native":False}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);a=p.parse_args()
 if not pathlib.Path(a.qeax).is_file():p.error("QEAX file not found")
 print(json.dumps(audit(a.qeax),indent=2))
