#!/usr/bin/env python3
"""STEP-03T: approved family classification + proposed placement manifest.

No note move/rename; existing EA-ID links remain stable. No diagrams.
"""
import argparse, importlib.util, json
from collections import Counter
from pathlib import Path

def build(vault,repo_root,output):
    vault,root,dst=map(Path,(vault,repo_root,output))
    if dst.exists():raise ValueError("Manifest already exists")
    spec=importlib.util.spec_from_file_location("approved",root/"21_Importer"/"v2_approved_family_resolver.py")
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    registry=mod.load_registry(root/"24_Workbench"/"registry"/"sysml_v2_approved_family_resolver.v0.1.json")
    notes=sorted((vault/"10_Elements").glob("EA-*.md"))
    if not notes:raise ValueError("No generated notes")
    result=[];stats=Counter();seen=set()
    for note in notes:
        raw=note.read_text(encoding="utf-8")
        if not raw.startswith("---\n"):raise ValueError("Missing frontmatter: "+note.name)
        parts=raw.split("---",2)
        props={}
        for line in parts[1].splitlines():
            if ":" in line:
                k,v=line.split(":",1)
                try:props[k.strip()]=json.loads(v.strip())
                except json.JSONDecodeError:props[k.strip()]=v.strip()
        oid=props.get("eaObjectID")
        if not isinstance(oid,int) or oid in seen:raise ValueError("Invalid/duplicate source ID")
        seen.add(oid)
        family_type=props.get("eaType") or ""
        stereo=props.get("eaStereotype") or ""
        resolution=mod.resolve_element(family_type,stereo,registry=registry)
        disposition=resolution.get("disposition","review_required")
        native_kind=resolution.get("native_kind")
        # This is a classification grouping, not an authorized MDSE folder move.
        group=("01_Native_Candidates" if disposition=="native_candidate" else
               "02_MDSE_Notes" if disposition=="mdse_note" else
               "03_Reference_Only" if disposition in ("reference_only","aggregate_boundary_note") else
               "04_Folder_Metadata" if disposition=="folder_only" else
               "05_Conditional_Review" if disposition=="conditional_review" else
               "06_Other_Approved" if resolution["status"]=="approved_group" else
               "99_FlagNote_Review")
        stats[disposition]+=1
        result.append({"eaObjectID":oid,"eaGUID":props.get("eaGUID"),"sourceNote":note.name,
                       "family":resolution["family"],"disposition":disposition,
                       "nativeKindCandidate":native_kind,
                       "placementGroupProposal":group,"placementAuthorized":False,
                       "noteRenameAuthorized":False,"sysmlV2Certified":False})
    dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open("x",encoding="utf-8") as f:
        for entry in result:f.write(json.dumps(entry,ensure_ascii=False)+"\n")
    return {"notes":len(result),"dispositions":dict(sorted(stats.items())),
            "placement_authorized":False,"renames_performed":0,"diagrams_processed":False}

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("generated_vault");p.add_argument("manifest_output")
    p.add_argument("--repo-root",default=str(Path(__file__).resolve().parents[1]))
    a=p.parse_args()
    print(json.dumps(build(a.generated_vault,a.repo_root,a.manifest_output),indent=2,sort_keys=True))
