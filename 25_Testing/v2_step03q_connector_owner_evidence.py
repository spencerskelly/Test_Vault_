#!/usr/bin/env python3
"""STEP-03Q: classify connector ownership evidence using approved family registry.

No connector is treated as proof of attachment ownership without row evidence.
"""
import argparse
import importlib.util
import json
from collections import Counter
from pathlib import Path

def inspect(ledger_path, output_path, repository_root):
    source=Path(ledger_path).resolve()
    dest=Path(output_path).resolve()
    if source==dest or dest.exists():
        raise ValueError("Output must be new and different from input")
    root=Path(repository_root)
    module_path=root/"21_Importer"/"v2_approved_family_resolver.py"
    spec=importlib.util.spec_from_file_location("family_resolver_for_step03q",module_path)
    resolver=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(resolver)
    registry=resolver.load_registry(root/"24_Workbench"/"registry"/"sysml_v2_approved_family_resolver.v0.1.json")
    stats=Counter()
    families=Counter()
    records=[]
    seen=set()
    for line in source.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record=json.loads(line)
        oid=record.get("artifact_object_id")
        if oid is None or oid in seen:
            raise ValueError("Missing or duplicate artifact object ID")
        seen.add(oid)
        evidence=record.get("evidence") or {}
        connections=evidence.get("connectors") or []
        evaluated=[]
        for conn in connections:
            kind=conn.get("connector_type") or ""
            stereo=conn.get("stereotype") or ""
            if kind:
                rule=resolver.resolve_connector(kind,stereo,registry=registry)
            else:
                rule={"status":"review_required","reason":"MISSING_CONNECTOR_TYPE","emission_authorized":False}
            family=kind+(":"+stereo if stereo else "")
            families[family]+=1
            evaluated.append({"connector_id":conn.get("connector_id"),
                              "other_object_id":conn.get("other_object_id"),
                              "source_end":conn.get("source_end"),
                              "family":family,"approved_family_review":rule})
        status=record.get("status")
        if status=="connector_review":
            if not evaluated:
                raise ValueError("Connector review missing evidence")
            outcome="connector_owner_unconfirmed"
        elif status=="parent_owner_candidate":
            outcome="parent_owner_candidate"
        elif status=="unassigned_review":
            outcome="unassigned_review"
        else:
            raise ValueError("Unknown candidate status: "+str(status))
        stats[outcome]+=1
        records.append({"artifact_object_id":oid,"artifact_guid":record.get("artifact_guid"),
                        "owner_object_id":record.get("owner_object_id") if status=="parent_owner_candidate" else None,
                        "status":outcome,"connector_evidence":evaluated,
                        "ownership_confirmed":False,"flagNote_emitted":False})
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open("x",encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record,ensure_ascii=False)+"\n")
    return {"artifacts":len(records),"categories":dict(sorted(stats.items())),
            "connector_families":dict(sorted(families.items())),
            "owner_confirmations":0,"flagNotes_created":0,
            "status":"connector_family_evidence_classified"}
if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("candidate_ledger")
    p.add_argument("output_ledger")
    p.add_argument("--repo-root",default=str(Path(__file__).resolve().parents[1]))
    a=p.parse_args()
    print(json.dumps(inspect(a.candidate_ledger,a.output_ledger,a.repo_root),indent=2,sort_keys=True))
