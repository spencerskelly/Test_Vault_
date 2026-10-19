#!/usr/bin/env python3
"""STEP-03B: fail if exported graph loses flagNotes or breaks graph identity."""
import argparse
import json

def rows(path):
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                obj = json.loads(line)
                if not isinstance(obj, dict):
                    raise ValueError("Non-object JSONL record")
                yield obj

def audit(nodes_path, edges_path, expected_notes, expected_links=None):
    nodes = set()
    notes = 0
    for node in rows(nodes_path):
        uid = node.get("id")
        if not isinstance(uid, str) or not uid or uid in nodes:
            raise ValueError("Missing or duplicate node id")
        nodes.add(uid)
        value = node.get("flagNote")
        notes += len(value) if isinstance(value, list) else int(bool(value))
    edges = set()
    links = 0
    for edge in rows(edges_path):
        uid = edge.get("id")
        if not isinstance(uid, str) or not uid or uid in edges:
            raise ValueError("Missing or duplicate connector id")
        edges.add(uid)
        if edge.get("source") not in nodes or edge.get("target") not in nodes:
            raise ValueError("Broken endpoint: " + uid)
        explicit = edge.get("flagLink")
        legacy = edge.get("type") == "flagLink" or any(s in str(edge.get("disposition", "")).lower() for s in ("flaglink", "unresolved", "review"))
        links += len(explicit) if isinstance(explicit, list) and explicit else int(bool(explicit) or legacy)
    if notes != expected_notes:
        raise ValueError(f"flagNote export loss: expected {expected_notes}; actual {notes}")
    if expected_links is not None and links != expected_links:
        raise ValueError(f"flagLink export loss: expected {expected_links}; actual {links}")
    return {"nodes": len(nodes), "edges": len(edges), "flagNotes": notes, "flagLinks": links}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("nodes")
    p.add_argument("edges")
    p.add_argument("--expected-flag-notes", required=True, type=int)
    p.add_argument("--expected-flag-links", type=int)
    args = p.parse_args()
    print(json.dumps(audit(args.nodes, args.edges, args.expected_flag_notes, args.expected_flag_links), sort_keys=True))
