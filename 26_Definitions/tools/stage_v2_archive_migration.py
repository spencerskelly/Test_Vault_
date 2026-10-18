#!/usr/bin/env python3
"""Stage V2-first folder separation on a disposable checkout. Never deletes content."""
from pathlib import Path
import subprocess, sys, json, re
root=Path(__file__).resolve().parents[2]
def tracked():
    return [Path(p) for p in subprocess.check_output(["git","ls-files","-z"],cwd=root).decode().split("\0") if p]
files=tracked()
legacy=("10_Base Vault","11_Importer","13_Bootstrap","14_Workbench","15_Testing","16_Definitions")
moves={}
for p in files:
    if not p.parts or p.parts[0] not in legacy: continue
    old=p.parts[0]
    s=p.as_posix()
    active=False
    dest=None
    if old=="14_Workbench":
        if len(p.parts)>1 and p.parts[1]=="registry":
            active=True; dest=Path("24_Workbench")/Path(*p.parts[1:])
        elif len(p.parts)>2 and p.parts[1]=="docs" and (re.search(r"SYSML.V2|GOLDEN_IMPORT|BOM_TO_SYSMLV2",p.name,re.I)):
            active=True; dest=Path("24_Workbench")/"docs"/p.name
    elif old=="15_Testing":
        if re.search(r"(phase[4-9]|sysml.v2|v2_|parser|canonical.graph)",p.name,re.I) and p.parts[1]!="consolidation":
            active=True; dest=Path("25_Testing")/Path(*p.parts[1:])
    elif old=="11_Importer" and re.search(r"sysml.v2|v2_",p.name,re.I):
        active=True;dest=Path("21_Importer")/Path(*p.parts[1:])
    elif old=="10_Base Vault" and re.search(r"^V2_|sysml.v2",p.name,re.I):
        active=True;dest=Path("20_Base Vault")/Path(*p.parts[1:])
    if not active:
        dest=Path("100_Archive")/"V1"/p
    if (root/dest).exists() or dest in moves.values():
        raise SystemExit(f"PATH COLLISION: {p} -> {dest}")
    moves[p]=dest
if not moves: raise SystemExit("No legacy files found; refusing empty migration")
# copy of source tree retained in Git history; git mv preserves full contents
for src,dst in moves.items():
    (root/dst).parent.mkdir(parents=True,exist_ok=True)
    subprocess.check_call(["git","mv","--",str(src),str(dst)],cwd=root)
# Build a machine-readable manifest, not source data
summary={"schema":"mdse-v2-separation/1","v1_archived":sum(str(x).startswith("100_Archive/") for x in moves.values()),"v2_relocated":sum(not str(x).startswith("100_Archive/") for x in moves.values()),"path_moves":{str(k):str(v) for k,v in sorted(moves.items())}}
out=root/"26_Definitions"/"V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json"
out.write_text(json.dumps(summary,indent=2)+"\n")
# Stop on active v2 references to legacy source roots; do not attempt unsafe global replacement.
findings=[]
for p in tracked():
    if p.parts[0] not in ("20_Base Vault","21_Importer","23_Bootstrap","24_Workbench","25_Testing","26_Definitions","29_SysMLv2_Translator_Workbench"):continue
    real=root/p
    if not real.is_file() or real.suffix not in (".py",".mjs",".js",".ts",".json",".yaml",".yml",".md",".html"):continue
    try: val=real.read_text()
    except UnicodeDecodeError:continue
    for i,line in enumerate(val.splitlines(),1):
        if any(x in line for x in ("14_Workbench/registry/","15_Testing/phase","11_Importer/Definition/SysML","10_Base Vault/Testing/V2_")):
            findings.append({"path":str(p),"line":i,"text":line[:170]})
report=root/"26_Definitions"/"V2_FOLDER_MIGRATION_REFERENCE_AUDIT_2026-10-18.json"
report.write_text(json.dumps({"stale_active_references":findings},indent=2)+"\n")
print(json.dumps({"archive":summary["v1_archived"],"v2":summary["v2_relocated"],"stale_reference_count":len(findings)}))
if findings: sys.exit("Blocked: active V2 references require rewriting and validation before merging")
