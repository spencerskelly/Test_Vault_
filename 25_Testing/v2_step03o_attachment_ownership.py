#!/usr/bin/env python3
"""Read-only QEAX Artifact ownership evidence; no invented owners or flags."""
import argparse, json, sqlite3
from pathlib import Path
from collections import Counter,defaultdict

def analyze(qeax,ledger=None):
    db=sqlite3.connect(Path(qeax).resolve().as_uri()+"?mode=ro",uri=True)
    try:
        obj={r[0]:r for r in db.execute("SELECT Object_ID,ParentID,ea_guid,Object_Type,Stereotype,Name,Package_ID FROM t_object")}
        links=defaultdict(list)
        for cid,a,b,typ,st in db.execute("SELECT Connector_ID,Start_Object_ID,End_Object_ID,Connector_Type,Stereotype FROM t_connector"):
            links[a].append({"connector_id":cid,"other_object_id":b,"source_end":"start","connector_type":typ,"stereotype":st})
            links[b].append({"connector_id":cid,"other_object_id":a,"source_end":"end","connector_type":typ,"stereotype":st})
        counts=Counter();entries=[]
        for oid,parent,guid,kind,st,name,pkg in obj.values():
            if kind!="Artifact":continue
            valid=parent in obj and parent!=oid
            state="parent_element_candidate" if valid else ("connector_evidence_review" if links[oid] else "no_element_owner_evidence")
            counts[state]+=1
            entries.append({"artifact_object_id":oid,"artifact_guid":guid,"artifact_stereotype":st,"artifact_name":name,
                            "package_id":pkg,"parent_object_id":parent if valid else None,
                            "candidate_owner_object_id":parent if valid else None,
                            "connector_evidence":links[oid],"state":state,"ownership_confirmed":False})
        if ledger:
            p=Path(ledger)
            if p.exists():raise ValueError("Ledger exists; refuse overwrite")
            p.parent.mkdir(parents=True,exist_ok=True)
            p.write_text("".join(json.dumps(e,ensure_ascii=False)+"\n" for e in entries),encoding="utf-8")
        return {"status":"ownership_evidence_not_final_resolution","artifacts":len(entries),
                "categories":dict(sorted(counts.items())),"review_flags_created":0,"diagram_processed":False}
    finally:db.close()

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("qeax");p.add_argument("--private-ledger")
    a=p.parse_args();print(json.dumps(analyze(a.qeax,a.private_ledger),indent=2,sort_keys=True))
