#!/usr/bin/env python3
"""STEP-03N read-only QEAX attachment identity audit (aggregate output only)."""
import argparse
import json
import sqlite3
from collections import Counter
from pathlib import Path

def guid(value):
    return str(value or "").strip().strip("{}").casefold()

def audit(source):
    db = sqlite3.connect(Path(source).resolve().as_uri() + "?mode=ro", uri=True)
    try:
        objs = db.execute("SELECT Object_ID,ea_guid,Object_Type,Stereotype FROM t_object").fetchall()
        docs = db.execute("SELECT ElementID,ElementType,DocType FROM t_document").fetchall()
        links = db.execute("SELECT Start_Object_ID,End_Object_ID FROM t_connector").fetchall()
        by_guid = {}
        for row in objs:
            by_guid.setdefault(guid(row[1]), []).append(row)
        linked = set()
        for a,b in links:
            linked.add(a);linked.add(b)
        artifacts = [x for x in objs if x[2] == "Artifact"]
        matched = Counter()
        missing = Counter()
        ambiguous = 0
        for reference,etype,dtype in docs:
            targets = by_guid.get(guid(reference), [])
            if len(targets) == 1:
                kind = targets[0][2] + ":" + str(targets[0][3] or "")
                matched[kind] += 1
            elif len(targets) == 0:
                missing[str(etype) + ":" + str(dtype)] += 1
            else:
                ambiguous += 1
        return {
            "status":"attachment_identity_inventory_not_ownership_acceptance",
            "artifact_elements":len(artifacts),
            "artifact_image_elements":sum(x[3]=="Image" for x in artifacts),
            "artifact_document_elements":sum(x[3]=="Document" for x in artifacts),
            "artifact_elements_without_connectors":sum(x[0] not in linked for x in artifacts),
            "embedded_document_records":len(docs),
            "matched_document_target_types":dict(sorted(matched.items())),
            "unmatched_document_record_types":dict(sorted(missing.items())),
            "ambiguous_document_guid_matches":ambiguous,
            "diagrams_processed":False,
            "review_flags_created":0
        }
    finally:
        db.close()

if __name__ == "__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("qeax")
    args=p.parse_args()
    print(json.dumps(audit(args.qeax),indent=2,sort_keys=True))
