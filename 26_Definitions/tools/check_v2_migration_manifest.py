#!/usr/bin/env python3
"""Validate lossless V1 archival and V2 relocation from the staged manifest."""
from pathlib import Path
import json, subprocess, sys
root=Path(__file__).resolve().parents[2]
manifest=root/"26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json"
data=json.loads(manifest.read_text())
moves=data.get("path_moves",{})
if not moves: raise SystemExit("EMPTY_MIGRATION")
errors=[]
for source,target in moves.items():
    old=root/source; new=root/target
    if old.exists(): errors.append("SOURCE_STILL_ACTIVE: "+source)
    if not new.is_file(): errors.append("MISSING_DESTINATION: "+target)
    if not (target.startswith("100_Archive/V1/") or target.split("/")[0] in {"20_Base Vault","21_Importer","23_Bootstrap","24_Workbench","25_Testing","26_Definitions","29_SysMLv2_Translator_Workbench"}):
        errors.append("INVALID_DESTINATION: "+target)
archive=sum(v.startswith("100_Archive/V1/") for v in moves.values())
active=len(moves)-archive
if archive!=data.get("v1_archived") or active!=data.get("v2_relocated"):
    errors.append("MANIFEST_COUNT_DRIFT")
tracked=subprocess.check_output(["git","ls-files","-z"],cwd=root).decode().split("\0")
active_roots=("20_Base Vault/","21_Importer/","23_Bootstrap/","24_Workbench/","25_Testing/","26_Definitions/","29_SysMLv2_Translator_Workbench/")
bad=[p for p in tracked if p.startswith(active_roots) and "100_Archive/" in p]
if bad:errors.append("ARCHIVE_INSIDE_ACTIVE_TREE")
print(json.dumps({"status":"PASS" if not errors else "FAIL","moved":len(moves),"archived":archive,"v2_active_moved":active,"errors":errors[:30]},indent=2))
if errors:sys.exit(1)
