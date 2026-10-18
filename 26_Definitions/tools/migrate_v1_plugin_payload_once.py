#!/usr/bin/env python3
"""One-time copy of approved plugin payloads into V2-owned source directories.

Migration-only tool. Generated V2 releases never refer to the archive.
Run in checkout, commit the copied files and their inventory separately.
"""
from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).resolve().parents[2]
old=root/"100_Archive/V1/10_Base Vault/Runtime/Plugins"
new=root/"20_Base Vault/Runtime/Plugins"
names=("mdse-bootstrap","mdse-workbench","templater-obsidian","fileclass","breadcrumbs","obsidian-git","advanced-canvas")
files=("manifest.json","main.js","styles.css")
manifest={"schema":"mdse-v2-vendored-plugin-lock/1","status":"unverified_v2_runtime","plugins":{}}
for name in names:
    folder=old/name
    meta=json.loads((folder/"manifest.json").read_text())
    if meta.get("id")!=name or not meta.get("version") or not (folder/"main.js").is_file():
        raise SystemExit("INVALID_SOURCE_PLUGIN:"+name)
    dest=new/name
    if dest.exists():raise SystemExit("REFUSE_EXISTING_V2_PLUGIN:"+name)
    expected={}
    for fn in files:
        if (folder/fn).exists():expected[fn]=hashlib.sha256((folder/fn).read_bytes()).hexdigest()
    manifest["plugins"][name]={"version":meta["version"],"minAppVersion":meta["minAppVersion"],"sha256":expected}
# Only copy after all inputs validated
for name,data in manifest["plugins"].items():
    dest=new/name;dest.mkdir(parents=True)
    for fn,expected in data["sha256"].items():
        shutil.copyfile(old/name/fn,dest/fn)
        if hashlib.sha256((dest/fn).read_bytes()).hexdigest()!=expected:raise SystemExit("HASH_MISMATCH:"+name)
(new/"plugin-lock.v2.json").write_text(json.dumps(manifest,indent=2)+"\n")
print("Copied",len(names),"plugin packages into V2-owned runtime; remains unverified for V2.")
