#!/usr/bin/env python3
"""STEP-03U: validate note identities and unresolved placement targets."""
import argparse, json
from pathlib import Path
from collections import Counter

def build(vault, manifest, output):
    root=Path(vault)
    dest=Path(output)
    if dest.exists():
        raise ValueError("Output already exists")
    items=[json.loads(s) for s in Path(manifest).read_text().splitlines() if s.strip()]
    ids=set()
    guids=set()
    statuses=Counter()
    results=[]
    for item in items:
        oid=item["eaObjectID"]
        key=item.get("eaGUID")
        if oid in ids or (key and key in guids):
            raise ValueError("Duplicate source identity")
        ids.add(oid)
        if key:guids.add(key)
        source=root/"10_Elements"/item["sourceNote"]
        if not source.is_file():
            raise ValueError("Missing source note")
        disposition=item["disposition"]
        status=("folder_mapping_pending" if disposition=="folder_only" else
                "boundary_merge_pending" if disposition=="aggregate_boundary_note" else
                "identity_and_placement_pending")
        statuses[status]+=1
        item["targetNoteUID"]=None
        item["targetPath"]=None
        item["migrationStatus"]=status
        results.append(item)
    if not items:
        raise ValueError("No notes")
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open("x",encoding="utf8") as f:
        for item in results:
            f.write(json.dumps(item,ensure_ascii=False)+"\n")
    return {"identities":len(results),"statuses":dict(sorted(statuses.items())),
            "moves":0,"new_uids":0,"diagrams_processed":False}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("vault");p.add_argument("manifest");p.add_argument("output")
    a=p.parse_args()
    print(json.dumps(build(a.vault,a.manifest,a.output),indent=2))
