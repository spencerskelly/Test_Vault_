#!/usr/bin/env python3
"""Read-only EA-to-graph identity reconciliation; never guesses names."""
import argparse
import json
import sqlite3
from collections import defaultdict
from pathlib import Path

GUID_KEYS = ("eaGUID", "ea_guid", "eaGuid", "sourceGuid", "source_guid")
ID_KEYS = ("eaObjectID", "ea_object_id", "eaObjectId", "sourceObjectID")

def normalize_guid(value):
    return str(value).strip().strip("{}").lower() if value is not None else ""

def reconcile(db_path, nodes_path):
    db = sqlite3.connect("file:" + Path(db_path).resolve().as_posix() + "?mode=ro", uri=True)
    try:
        rows = db.execute("SELECT Object_ID,ea_guid,Object_Type FROM t_object").fetchall()
    finally:
        db.close()
    ids = {str(oid): (oid, guid, kind) for oid, guid, kind in rows}
    guids = defaultdict(list)
    for row in rows:
        guids[normalize_guid(row[1])].append(row)
    assigned, unknown, graph_ids, duplicate_ids = defaultdict(list), [], set(), set()
    node_count = 0
    with open(nodes_path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if not line.strip():
                continue
            node = json.loads(line)
            nid = str(node.get("id") or "")
            if not nid or nid in graph_ids:
                duplicate_ids.add(nid or "<missing>")
            graph_ids.add(nid)
            node_count += 1
            candidates = set()
            for key in GUID_KEYS:
                if node.get(key):
                    candidates.update(str(row[0]) for row in guids.get(normalize_guid(node[key]), []))
            for key in ID_KEYS:
                if node.get(key) is not None and str(node[key]) in ids:
                    candidates.add(str(node[key]))
            if nid in ids:
                candidates.add(nid)
            candidates.update(str(row[0]) for row in guids.get(normalize_guid(nid), []))
            if len(candidates) == 1:
                assigned[next(iter(candidates))].append(nid)
            else:
                unknown.append({"graph_node_id": nid, "line": lineno,
                                "candidate_count": len(candidates),
                                "reason": "ambiguous" if candidates else "no_verified_source_identity"})
    missing = [{"object_id": int(key), "ea_guid": row[1], "type": row[2]}
               for key, row in ids.items() if key not in assigned]
    multi = [{"object_id": int(key), "graph_node_ids": found}
             for key, found in assigned.items() if len(found) > 1]
    result = {"source_objects": len(rows), "graph_nodes": node_count,
              "uniquely_matched_source_objects": len(assigned),
              "source_without_verified_node": missing,
              "graph_without_unique_source": unknown,
              "multiply_represented_source_objects": multi,
              "duplicate_graph_ids": sorted(duplicate_ids)}
    result["status"] = ("review_required" if
                        (missing or unknown or multi or duplicate_ids) else "reconciled")
    return result

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("qeax")
    p.add_argument("nodes_jsonl")
    p.add_argument("--output", required=True)
    args = p.parse_args()
    target = Path(args.output)
    if target.resolve() in (Path(args.qeax).resolve(), Path(args.nodes_jsonl).resolve()):
        p.error("Output must differ from inputs")
    result = reconcile(args.qeax, args.nodes_jsonl)
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: len(value) if isinstance(value, list) else value
                      for key, value in result.items()}, indent=2))
    raise SystemExit(0 if result["status"] == "reconciled" else 2)
