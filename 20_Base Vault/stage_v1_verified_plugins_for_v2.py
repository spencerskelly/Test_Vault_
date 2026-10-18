#!/usr/bin/env python3
"""Stage verified V1 plugin artifacts as V2-owned release candidates.

V1 archive is INPUT to this one-time migration only. Generated runtime never
reads from V1. No activation, overwrites, credentials or private plugin data.
"""
import argparse,hashlib,json,pathlib,shutil,sys
ROOT=pathlib.Path(__file__).resolve().parents[2]
SOURCE=ROOT/"100_Archive/V1/10_Base Vault/Runtime/Plugins"
PLUGINS=("mdse-bootstrap","mdse-workbench","templater-obsidian","fileclass","breadcrumbs","obsidian-git","advanced-canvas")
FILES=("manifest.json","main.js","styles.css")
def stage(destination):
    destination=pathlib.Path(destination).resolve()
    if destination.exists():raise ValueError("DESTINATION_EXISTS")
    if ROOT==destination or ROOT in destination.parents:raise ValueError("DESTINATION_INSIDE_REPO")
    result={}
    for pid in PLUGINS:
        folder=SOURCE/pid
        m=folder/"manifest.json"
        if not m.is_file() or not (folder/"main.js").is_file():raise ValueError("MISSING_PLUGIN_PAYLOAD:"+pid)
        info=json.loads(m.read_text())
        if info.get("id")!=pid or not info.get("version") or not info.get("minAppVersion"):
            raise ValueError("INVALID_PLUGIN_MANIFEST:"+pid)
        result[pid]={"version":info["version"],"minAppVersion":info["minAppVersion"],"sha256":{}}
        for filename in FILES:
            f=folder/filename
            if f.is_file():result[pid]["sha256"][filename]=hashlib.sha256(f.read_bytes()).hexdigest()
    try:
        for pid in PLUGINS:
            for filename in result[pid]["sha256"]:
                target=destination/"plugins"/pid/filename
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(SOURCE/pid/filename,target)
                if hashlib.sha256(target.read_bytes()).hexdigest()!=result[pid]["sha256"][filename]:
                    raise ValueError("COPIED_HASH_MISMATCH:"+pid)
        (destination/"candidate-plugin-lock.json").write_text(json.dumps({"schema":"mdse-v2-plugin-candidate/1","status":"staged_not_activated","origin":"archived_v1_verified_payload","plugins":result},indent=2)+"\n")
    except BaseException:
        shutil.rmtree(destination,ignore_errors=True)
        raise
    return {"status":"STAGED_NOT_ACTIVATED","plugins":len(result),"output":str(destination)}
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("destination")
    a=ap.parse_args()
    try:print(json.dumps(stage(a.destination)))
    except (ValueError,OSError,json.JSONDecodeError) as e:print("BLOCKED:",e,file=sys.stderr);sys.exit(1)
