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
# First-run dependency audit: check source tree, lockfile and release path migration
LEGACY_TO_CONSOLIDATED = {
    "Base Vault/": "10_Base Vault/",
    "Importer/": "11_Importer/",
    "Bootstrap/": "13_Bootstrap/",
    "00_Workspace/": "55_Workspace/",
    "55_Workbench/": "14_Workbench/",
}
def audit_paths(paths, category):
    stale=[]
    missing=[]
    for label, src in paths:
        if not isinstance(src,str) or not src:
            continue
        if (root/src).exists():
            continue
        mapped=next((new + src[len(old):] for old,new in LEGACY_TO_CONSOLIDATED.items() if src.startswith(old)),None)
        if mapped and (root/mapped).exists():
            stale.append((label,src,mapped))
        else:
            missing.append((label,src))
    if stale:
        examples="; ".join(f"{old} -> {new}" for _,old,new in stale[:3])
        emit("BLOCKER" if category=="runtime" else "WARNING",
             "STALE_"+category.upper()+"_PATHS",
             f"{len(stale)} stale {category} paths. Examples: {examples}")
    if missing:
        examples="; ".join(p for _,p in missing[:3])
        emit("BLOCKER" if category=="runtime" else "WARNING",
             "MISSING_"+category.upper()+"_PATHS",
             f"{len(missing)} unresolved {category} paths. Examples: {examples}")

base=m.get("runtimeBase",{})
runtime=[]
runtime += [(f"includeFiles:{x}",x) for x in base.get("includeFiles",[])]
runtime += [(f"includeTrees:{x}",x) for x in base.get("includeTrees",[])]
runtime += [(f"mappedFiles:{x.get('source')}",x.get("source")) for x in base.get("mappedFiles",[])]
runtime += [("cleanBase.builder",tools.get("cleanBase",{}).get("builder"))]
runtime += [("runtimePlugins.payload",m.get("runtimePlugins",{}).get("payload"))]
runtime += [(f"runtimePlugins.{key}",m.get("runtimePlugins",{}).get(key))
            for key in ("configGenerator","lockGenerator")]
audit_paths(runtime,"runtime")
docs=[(d.get("status","unknown"),d.get("path")) for d in m.get("documents",[]) if isinstance(d,dict)]
audit_paths(docs,"documentation")

lock_text=read(".obsidian/plugin-lock.yaml")
if lock_text:
    try:
        lock=yaml.safe_load(lock_text) or {}
        for pid, entry in (("mdse-workbench",workbench),("mdse-bootstrap",bootstrap)):
            pinned=(lock.get("plugins") or {}).get(pid,{})
            if pinned.get("version")!=entry.get("version"):
                emit("BLOCKER","PLUGIN_LOCK_VERSION_MISMATCH",
                     f"{pid}: locked={pinned.get('version')}, release={entry.get('version')}")
            files=pinned.get("sha256") or {}
            import hashlib
            for name,expected in files.items():
                file=root/"10_Base Vault/Runtime/Plugins"/pid/name
                if not file.is_file():
                    emit("BLOCKER","LOCKED_RUNTIME_FILE_MISSING",str(file.relative_to(root)))
                elif hashlib.sha256(file.read_bytes()).hexdigest()!=expected:
                    emit("BLOCKER","LOCKED_RUNTIME_HASH_MISMATCH",f"{pid}/{name}")
    except (ValueError,TypeError) as exc:
        emit("BLOCKER","INVALID_PLUGIN_LOCK",str(exc))

# Detect legacy CI paths that may stop current changes from triggering checks.
ci=root/".github/workflows/importer-candidate.yml"
if ci.exists():
    workflow=ci.read_text(encoding="utf-8")
    if ('"Importer/**"' in workflow and '"11_Importer/**"' not in workflow):
        emit("WARNING","STALE_CI_IMPORTER_TRIGGER",
             "Importer candidate workflow watches Importer/** but not 11_Importer/**")
    if 'run: python "Base Vault/' in workflow:
        emit("WARNING","STALE_CI_RELEASE_COMMAND",
             "Importer candidate workflow still invokes legacy Base Vault/ paths")
# Old v1 compatibility docs remain relevant history, but are not v2 release authority.
status="BLOCKED" if any(v["severity"]=="BLOCKER" for v in findings) else "GO"
report={"status":status,"blockers":sum(x["severity"]=="BLOCKER" for x in findings),"warnings":sum(x["severity"]=="WARNING" for x in findings),"findings":findings}
print(json.dumps(report,indent=2) if a.json else "\n".join([f"{x['severity']} {x['code']}: {x['message']}" for x in findings]+[f"RESULT: {status}"]))
sys.exit(1 if status=="BLOCKED" else 0)
