#!/usr/bin/env python3
"""STEP-03P: classify source-identified artifact-owner evidence without guessing links."""
import argparse
import json
from collections import Counter
from pathlib import Path

def resolve(ledger_path, output_path):
    src, dst = Path(ledger_path), Path(output_path)
    if src.resolve() == dst.resolve() or dst.exists():
        raise ValueError("Output must be new and different from input")
    records=[]; counts=Counter(); ids=set()
    for number,line in enumerate(src.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        item=json.loads(line)
        oid=item.get("artifact_object_id")
        if oid is None or oid in ids:raise ValueError("Missing or duplicate artifact source ID")
        ids.add(oid)
        parent=item.get("parent_object_id")
        connectors=item.get("connector_evidence") or []
        if parent is not None and parent != oid:
            status="parent_owner_candidate"
            owner=parent
            reason="EA_PARENT_ELEMENT"
        elif connectors:
            status="connector_review"
            owner=None
            reason="CONNECTOR_SEMANTICS_NOT_VALIDATED"
        else:
            status="unassigned_review"
            owner=None
            reason="NO_PARENT_OR_CONNECTOR"
        counts[status]+=1
        records.append({"artifact_object_id":oid,"artifact_guid":item.get("artifact_guid"),
                        "owner_object_id":owner,"status":status,"reason":reason,
                        "evidence":{"parent_object_id":parent,"connectors":connectors},
                        "attachment_note_created":False,"flagNote_emitted":False})
    dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open("x",encoding="utf-8") as f:
        for r in records:f.write(json.dumps(r,ensure_ascii=False)+"\n")
    return {"artifacts":len(records),"categories":dict(sorted(counts.items())),
            "flags_emitted":0,"notes_created":0,"status":"ownership_candidates_staged"}
if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("source_ledger");p.add_argument("output_ledger")
    a=p.parse_args();print(json.dumps(resolve(a.source_ledger,a.output_ledger),sort_keys=True,indent=2))
