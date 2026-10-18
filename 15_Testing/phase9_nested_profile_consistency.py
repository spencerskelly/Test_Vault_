"""Read-only local nested extended-stereotype consistency audit; aggregates only."""
import argparse,collections,json,pathlib,re,sqlite3
PROFILE="Webasto MBDV Profile::Hardware Component"
PATTERN=re.compile(r'@STEREO;Name=([^;]*);FQName=([^;]*);@ENDSTEREO;')
def classify_payload(description):
    parsed=PATTERN.findall(description or "")
    if len(parsed)!=1:return "MISSING_OR_MULTIPLE_STEREOTYPES"
    name,fqname=parsed[0]
    if name=="Hardware Component" and fqname==PROFILE:return "EXPECTED_HARDWARE_PROFILE"
    return "OTHER_PROFILE_REVIEW"
def audit(path):
    counts=collections.Counter()
    with sqlite3.connect(pathlib.Path(path).resolve().as_uri()+"?mode=ro",uri=True) as db:
        db.row_factory=sqlite3.Row
        objs={r["Object_ID"]:r for r in db.execute("SELECT Object_ID,ea_guid,Object_Type,Stereotype,ParentID FROM t_object")}
        xref=collections.defaultdict(list)
        for r in db.execute("SELECT Client,Description FROM t_xref WHERE Name='Stereotypes' AND Type='element property'"):
            xref[str(r["Client"] or "").strip("{}").lower()].append(r["Description"])
        ids=set()
        for a,b in db.execute("SELECT Start_Object_ID,End_Object_ID FROM t_connector WHERE Connector_Type='Generalization'"):
            x,y=objs.get(a),objs.get(b)
            if not x or not y or x["Object_Type"]!=y["Object_Type"] or x["Stereotype"]!=y["Stereotype"]:continue
            if x["Stereotype"] not in ("Hardware Component","Physical Component","Module","Logical Signal") or x["Object_Type"] not in ("Class","Signal"):continue
            for o in (x,y):
                if o["ParentID"]:
                    ids.add(o["Object_ID"]);counts["nested_appearances"]+=1
        counts["unique_nested_elements"]=len(ids)
        for i in ids:
            r=objs[i];p=objs.get(r["ParentID"])
            counts["parent_hardware_component" if p and p["Object_Type"]=="Class" and p["Stereotype"]=="Hardware Component" else "parent_other_or_missing"]+=1
            matches=xref.get(str(r["ea_guid"] or "").strip("{}").lower(),[])
            counts["xref_"+classify_payload(matches[0]) if len(matches)==1 else "xref_MISSING_OR_MULTIPLE_RECORDS"]+=1
    return {"schema":"mdse-phase9-nested-profile-check/1","counts":dict(sorted(counts.items())),"native_certified":0}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--qeax",required=True);a=p.parse_args()
    if not pathlib.Path(a.qeax).is_file():p.error("Missing QEAX file")
    print(json.dumps(audit(a.qeax),indent=2))
