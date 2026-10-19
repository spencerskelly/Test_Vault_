#!/usr/bin/env python3
"""STEP-03Y: read-only V2 staged-base integrity and runtime readiness audit."""
import argparse,hashlib,json
from pathlib import Path

REQUIRED_PLUGIN_IDS=("mdse-bootstrap","mdse-workbench")
def audit(base):
    root=Path(base)
    manifest=root/".mdse_v2_test_base.json"
    if not manifest.is_file():raise ValueError("Missing V2 test-base manifest")
    data=json.loads(manifest.read_text(encoding="utf-8"))
    if data.get("schema")!="mdse-v2-test-base/1":raise ValueError("Unexpected base schema")
    mismatches=[]
    for rel,digest in data.get("files",{}).items():
        file=root/rel
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest()!=digest:
            mismatches.append(rel)
    pins=root/"99_System/registry/sysml_v2_registry_pins.v0.1.json"
    semantic_pins=bool(pins.is_file())
    plugins={}
    for pid in REQUIRED_PLUGIN_IDS:
        location=root/".obsidian/plugins"/pid
        manifest_file=location/"manifest.json"
        runtime=location/"main.js"
        plugins[pid]={"manifest":manifest_file.is_file(),"runtime":runtime.is_file()}
    plugin_ready=all(all(v.values()) for v in plugins.values())
    return {"base_schema":data["schema"],"files_checked":len(data.get("files",{})),
        "hash_failures":mismatches,"registry_present":semantic_pins,
        "plugins":plugins,"plugin_ready":False,
        "native_import_ready":False,"status":"BLOCKED_RUNTIME" if not mismatches else "FAIL_BASE_INTEGRITY",
        "reason":"Runtime plugin version/hash locks, native parser and editor acceptance not certified",
        "diagrams_imported":False}
if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("base");a=p.parse_args()
    print(json.dumps(audit(a.base),indent=2))
