#!/usr/bin/env python3
"""STEP-03Z: stage hash-locked V2 plugin artifacts into a fresh generated test base.

Inputs must be compiled, explicitly V2-certified external build artifacts.
Never substitutes V1 plugins or marks native importer certified.
"""
import argparse,hashlib,json,shutil
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec

IDS=("mdse-bootstrap","mdse-workbench")
REQUIRED=("manifest.json","main.js")
def digest(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def stage(base,artifacts,out,attestation):
    base=Path(base).resolve();artifacts=Path(artifacts).resolve();out=Path(out).resolve()
    if out.exists():raise ValueError("Output exists")
    if not (base/".mdse_v2_test_base.json").is_file():raise ValueError("Not a V2 test base")
    evidence=json.loads(Path(attestation).read_text(encoding="utf8"))
    if evidence.get("schema")!="mdse-v2-plugin-evidence/1" or evidence.get("v2_editor_tests_passed") is not True or evidence.get("bootstrap_tests_passed") is not True:
        raise ValueError("V2 runtime evidence missing or not passed")
    pins=evidence.get("plugins",{})
    checks={}
    for pid in IDS:
        folder=artifacts/pid
        metadata=json.loads((folder/"manifest.json").read_text(encoding="utf8"))
        if metadata.get("id")!=pid:raise ValueError("Plugin ID mismatch: "+pid)
        pin=pins.get(pid,{})
        if pin.get("version")!=metadata.get("version"):raise ValueError("Plugin version pin mismatch: "+pid)
        hashes={}
        for name in REQUIRED:
            file=folder/name
            if not file.is_file():raise ValueError("Missing compiled payload: "+str(file))
            actual=digest(file)
            if pin.get("sha256",{}).get(name)!=actual:raise ValueError("Hash mismatch: "+pid+"/"+name)
            hashes[name]=actual
        checks[pid]={"version":metadata["version"],"sha256":hashes}
    try:
        shutil.copytree(base,out)
        for pid in IDS:
            target=out/".obsidian/plugins"/pid;target.mkdir(parents=True,exist_ok=True)
            for filename in REQUIRED:shutil.copy2(artifacts/pid/filename,target/filename)
        lock={"schema":"mdse-v2-plugin-lock/1","plugins":checks,
              "plugin_artifacts_verified":True,"native_import_ready":False,
              "runtime_observed_in_obsidian":False}
        (out/".mdse_v2_plugin_lock.json").write_text(json.dumps(lock,indent=2)+"\n")
        return {"plugins_staged":len(IDS),"plugin_artifacts_verified":True,
                "native_import_ready":False,"runtime_observed_in_obsidian":False}
    except BaseException:
        if out.exists():shutil.rmtree(out)
        raise
if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for field in ("test_base","compiled_plugin_artifacts","output_base","evidence_json"):p.add_argument(field)
    a=p.parse_args();print(json.dumps(stage(a.test_base,a.compiled_plugin_artifacts,a.output_base,a.evidence_json),indent=2))
