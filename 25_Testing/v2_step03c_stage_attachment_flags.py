#!/usr/bin/env python3
"""Stage attachment flagNotes onto existing graph nodes by canonical node ID."""
import argparse
import json
import os
from pathlib import Path

def patch(nodes_path, flags_path, output_path):
    nodes_path, flags_path, output_path = map(Path, (nodes_path, flags_path, output_path))
    if output_path.resolve() in {nodes_path.resolve(), flags_path.resolve()}:
        raise ValueError("Output must differ from inputs")
    flags = {}
    with flags_path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if not line.strip(): continue
            item = json.loads(line)
            uid, value = item.get("node_id"), item.get("flagNote")
            if not isinstance(uid, str) or not uid or not value or uid in flags:
                raise ValueError(f"Invalid/duplicate flag at line {i}")
            flags[uid] = value
    seen, matched, output = set(), set(), []
    with nodes_path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if not line.strip(): continue
            node = json.loads(line)
            uid = node.get("id")
            if not isinstance(uid, str) or not uid or uid in seen:
                raise ValueError(f"Missing/duplicate node ID at line {i}")
            seen.add(uid)
            if uid in flags:
                if node.get("flagNote") not in (None, "", [], flags[uid]):
                    raise ValueError(f"Conflicting flagNote on {uid}")
                node["flagNote"] = flags[uid]
                matched.add(uid)
            output.append(json.dumps(node, ensure_ascii=False, separators=(",", ":")) + "\n")
    if set(flags) != matched:
        raise ValueError(f"Unmatched attachment flag identities: {len(set(flags)-matched)}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp = output_path.with_name(output_path.name+".tmp")
    try:
        with temp.open("w", encoding="utf-8") as f: f.writelines(output)
        os.replace(temp, output_path)
    finally:
        temp.unlink(missing_ok=True)
    return {"nodes":len(seen), "attachment_flags":len(flags), "matched":len(matched)}

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("nodes")
    p.add_argument("attachment_flags")
    p.add_argument("output")
    a = p.parse_args()
    print(json.dumps(patch(a.nodes,a.attachment_flags,a.output),sort_keys=True))
