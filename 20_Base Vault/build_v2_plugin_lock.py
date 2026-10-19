#!/usr/bin/env python3
"""Generate or validate the V2-owned plugin lock from packaged V2 bytes only."""
from pathlib import Path
import argparse,hashlib,json,sys
BASE=Path(__file__).resolve().parent/"Runtime/Plugins"
IDS=("mdse-bootstrap","mdse-workbench","templater-obsidian","fileclass","breadcrumbs","obsidian-git","advanced-canvas")
def build():
  entries={}
  for pid in IDS:
    root=BASE/pid
    m=json.loads((root/"manifest.json").read_text())
    if m.get("id")!=pid or not m.get("version") or not m.get("minAppVersion"):
      raise ValueError("INVALID_MANIFEST:"+pid)
    files={}
    for name in ("manifest.json","main.js","styles.css"):
      p=root/name
      if name!="styles.css" and not p.is_file():raise ValueError("MISSING_FILE:"+pid+"/"+name)
      if p.is_file():files[name]=hashlib.sha256(p.read_bytes()).hexdigest()
    entries[pid]={"version":m["version"],"minAppVersion":m["minAppVersion"],"sha256":files}
  return {"schema":"mdse-v2-vendored-plugin-lock/1","status":"unverified_v2_runtime","plugins":entries}
def main():
  ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");a=ap.parse_args()
  try:
    data=build();out=BASE/"plugin-lock.v2.json"
    rendered=json.dumps(data,indent=2)+"\n"
    if a.check:
      if not out.is_file() or out.read_text()!=rendered:raise ValueError("LOCK_MISSING_OR_STALE")
    else:out.write_text(rendered)
    print(json.dumps({"status":"PASS","pluginCount":len(data["plugins"]),"lock":str(out)}))
  except (OSError,ValueError,json.JSONDecodeError) as e:
    print("BLOCKED:",e,file=sys.stderr);return 1
  return 0
if __name__=="__main__":sys.exit(main())
