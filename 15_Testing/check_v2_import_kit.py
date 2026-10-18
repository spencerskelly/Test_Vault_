#!/usr/bin/env python3
"""Read-only MDSE v2 import-kit consistency gate. Exit nonzero if release prerequisites are unmet."""
import argparse, json, pathlib, re, sys
try:
    import yaml
except ImportError:
    sys.exit("BLOCKER PY_YAML_MISSING: pip install pyyaml")

p=argparse.ArgumentParser()
p.add_argument("root",type=pathlib.Path,help="Test_Vault_ checkout")
p.add_argument("--json",action="store_true")
a=p.parse_args()
root=a.root.resolve()
findings=[]
def emit(level,code,message):
    findings.append({"severity":level,"code":code,"message":message})
def read(rel):
    file=root/rel
    if not file.is_file():
        emit("BLOCKER","MISSING_FILE",rel)
        return None
    return file.read_text(encoding="utf-8")
raw=read("10_Base Vault/Definition/mdse-release.yaml")
m=yaml.safe_load(raw) if raw else {}
tools=m.get("tools",{})
workbench=tools.get("workbench",{})
bootstrap=tools.get("bootstrap",{})
importer=tools.get("importer",{})
for pid,entry in (("mdse-workbench",workbench),("mdse-bootstrap",bootstrap)):
    data=read(f"10_Base Vault/Runtime/Plugins/{pid}/manifest.json")
    if not data: continue
    try: version=json.loads(data)["version"]
    except (ValueError,KeyError): emit("BLOCKER","BAD_PLUGIN_MANIFEST",pid);continue
    declared=entry.get("version")
    if version!=declared:
        emit("BLOCKER","PLUGIN_VERSION_MISMATCH",f"{pid}: vendored={version}, release manifest={declared}")
for key in ("sourceProfile","candidate"):
    ref=importer.get(key)
    if ref:
        mapped=ref.replace("Importer/","11_Importer/")
        if not (root/mapped).is_file():
            emit("WARNING","LEGACY_MANIFEST_PATH",f"Importer {key} path needs checkout-specific validation: {ref}")
if not importer.get("sysmlV2Release"):
    emit("BLOCKER","NO_V2_IMPORTER_RELEASE","Release manifest does not declare a verified, self-contained SysML v2 importer")
if not workbench.get("sysmlV2NoteEditorVerified"):
    emit("BLOCKER","V2_WORKBENCH_UNVERIFIED","Note-first SysML v2 editing not built and tested in Obsidian")
if not m.get("sysmlV2ParserPin"):
    emit("BLOCKER","NO_PINNED_V2_PARSER","Missing independent native SysML v2 parser/library pin and acceptance evidence")
for path in ["10_Base Vault/Tools/v0.8.0-r2/build-base.py","10_Base Vault/Runtime/Plugins/mdse-bootstrap/main.js","10_Base Vault/Runtime/Plugins/mdse-workbench/main.js"]:
    if not (root/path).is_file():
        emit("BLOCKER","MISSING_RELEASE_PAYLOAD",path)
status="BLOCKED" if any(v["severity"]=="BLOCKER" for v in findings) else "GO"
report={"status":status,"blockers":sum(x["severity"]=="BLOCKER" for x in findings),"warnings":sum(x["severity"]=="WARNING" for x in findings),"findings":findings}
print(json.dumps(report,indent=2) if a.json else "\n".join([f"{x['severity']} {x['code']}: {x['message']}" for x in findings]+[f"RESULT: {status}"]))
sys.exit(1 if status=="BLOCKED" else 0)
