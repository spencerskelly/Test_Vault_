#!/usr/bin/env python3
"""Read-only exact SHA256 integrity check for pinned SysML v2 registries."""
import argparse
import hashlib
import json
from pathlib import Path

DEFAULT="24_Workbench/registry/sysml_v2_registry_pins.v0.1.json"

def verify(root, pins):
    results=[]
    for rel, expected in sorted(pins["files"].items()):
        path=root/rel
        actual=hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
        results.append({"file":rel,"match":actual==expected,"actual":actual})
    return {"status":"PASS" if results and all(r["match"] for r in results) else "BLOCKED",
            "files":results}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("root",type=Path)
    p.add_argument("--pins",type=Path)
    args=p.parse_args()
    root=args.root.resolve()
    location=args.pins or root/DEFAULT
    pin=json.loads(location.read_text(encoding="utf-8"))
    if pin.get("schema")!="mdse-v2-registry-pins/1":
        raise SystemExit("Unknown registry pin schema")
    report=verify(root,pin)
    print(json.dumps(report,indent=2))
    return 0 if report["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
