#!/usr/bin/env python3
"""Reconcile V2 registry pins after a path-only migration; fail closed on semantic changes."""
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=Path("24_Workbench/registry")
PIN=ROOT/BASE/"sysml_v2_registry_pins.v0.1.json"
OLD=("14_"+"Workbench/registry/").encode("ascii")
NEW=b"24_Workbench/registry/"
def digest(data):return hashlib.sha256(data).hexdigest()
def run(write=False):
    pins=json.loads(PIN.read_text(encoding="utf-8"))
    if pins.get("schema")!="mdse-v2-registry-pins/1" or pins.get("status")!="candidate_not_release":
        raise RuntimeError("UNEXPECTED_PIN_MANIFEST")
    expected={
        f"{BASE}/family_disposition_registry.v0.2.json",
        f"{BASE}/sysml_v2_semantic_rules.v0.2.json",
        f"{BASE}/sysml_v2_semantic_decisions.v0.1.json",
    }
    if set(pins["files"])!=expected:raise RuntimeError("UNEXPECTED_REGISTRY_SET")
    amended={}
    for rel,old_hash in pins["files"].items():
        data=(ROOT/rel).read_bytes()
        actual=digest(data)
        if actual==old_hash:
            amended[rel]=old_hash
            continue
        if NEW not in data or digest(data.replace(NEW,OLD))!=old_hash:
            raise RuntimeError("NON_PATH_REGISTRY_DRIFT: "+rel)
        amended[rel]=actual
    changed=sum(amended[k]!=pins["files"][k] for k in amended)
    if write and changed:
        pins["files"]=amended
        PIN.write_text(json.dumps(pins,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    return {"status":"PASS" if write or amended==pins["files"] else "REPIN_REQUIRED",
            "registry_count":len(expected),"path_only_repin":changed,
            "write":write}
if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--write",action="store_true")
    a=arg.parse_args()
    try:
        result=run(a.write)
        print(json.dumps(result))
        raise SystemExit(0 if result["status"]=="PASS" else 2)
    except (OSError,ValueError,KeyError,RuntimeError) as ex:
        print(json.dumps({"status":"BLOCKED","reason":str(ex)}))
        raise SystemExit(1)
