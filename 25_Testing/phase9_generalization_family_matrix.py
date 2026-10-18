"""Independent, conservative EA generalization kind matrix; no native certification."""
import collections,json,pathlib,sqlite3,argparse

# Candidates describe endpoint families, not permission to emit native SysML.
DEFINITIONS={
 ("Class","block"):"PartDefinition",
 ("Activity",""):"ActionDefinition",
 ("State",""):"StateDefinition",
 ("Requirement",""):"RequirementDefinition",
 ("Signal",""):"ItemDefinition",
 ("InformationItem",""):"ItemDefinition",
 ("Class","Hardware Component"):"PartDefinition",
 ("Class","Physical Component"):"PartDefinition",
 ("Class","Module"):"PartDefinition",
 ("Signal","Logical Signal"):"ItemDefinition",
}
def ea_kind(type_,stereotype):
 return DEFINITIONS.get((type_,(stereotype or "").strip()),"UNRESOLVED")

def assess(source,target,direction,connector_stereotype=""):
 if (connector_stereotype or "").strip():return "CONNECTOR_STEREOTYPE_REVIEW"
 if direction!="Source -> Destination":return "DIRECTION_REVIEW"
 a,b=ea_kind(*source),ea_kind(*target)
 if "UNRESOLVED" in (a,b):return "ENDPOINT_KIND_REVIEW"
 if a!=b:return "CROSS_KIND_REVIEW"
 if source[1].strip() in ("Hardware Component","Physical Component","Module","Logical Signal") or target[1].strip() in ("Hardware Component","Physical Component","Module","Logical Signal"):
  return "STEREOTYPE_MAPPING_REVIEW:"+a
 return "SAME_DEFINITION_FAMILY_CANDIDATE:"+a

def audit(qeax):
 counts=collections.Counter()
 with sqlite3.connect(pathlib.Path(qeax).resolve().as_uri()+"?mode=ro",uri=True) as db:
  objects={str(r[0]):(r[1],r[2]) for r in db.execute("SELECT Object_ID,Object_Type,COALESCE(Stereotype,'') FROM t_object")}
  for _,sty,direction,start,end in db.execute("SELECT Connector_Type,Stereotype,Direction,Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'"):
   a=objects.get(str(start));b=objects.get(str(end))
   counts[assess(a,b,direction,sty) if a and b else "MISSING_ENDPOINT"]+=1
 return {"schema":"mdse-phase9-generalization-family-matrix/1","total":sum(counts.values()),"categories":dict(sorted(counts.items())),"native_certified":0}

if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);a=p.parse_args()
 if not pathlib.Path(a.qeax).is_file():p.error("QEAX file not found")
 print(json.dumps(audit(a.qeax),indent=2))
