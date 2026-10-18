#!/usr/bin/env python3
"""Enforce V2-only runtime ownership and fail closed on archive execution references."""
from pathlib import Path
import json,re,subprocess,sys
root=Path(__file__).resolve().parents[2]
active=("20_Base Vault","21_Importer","23_Bootstrap","24_Workbench","25_Testing","26_Definitions","29_SysMLv2_Translator_Workbench")
runtime_suffix={".py",".js",".mjs",".ts",".html",".json",".yaml",".yml",".sh",".ps1"}
tracked=[Path(s) for s in subprocess.check_output(["git","ls-files","-z"],cwd=root).decode().split("\0") if s]
issues=[]
for rel in tracked:
    if rel.parts[0] not in active or rel.suffix not in runtime_suffix: continue
    if rel.name in {"check_v2_archive_runtime_boundary.py","V2_FOLDER_MIGRATION_REFERENCE_AUDIT_2026-10-18.json","V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json"}: continue
    try: lines=(root/rel).read_text(encoding="utf-8").splitlines()
    except (UnicodeDecodeError,OSError):continue
    for no,line in enumerate(lines,1):
        if "100_Archive/" not in line:continue
        # A comment, documentation text in a JSON description, or quoted error message
        # can mention archives harmlessly; actual executable path use is blocked.
        if re.search(r"(?:require\s*\(|import\s+|from\s+|readFile|open\s*\(|Path\s*\(|resolve\s*\(|join\s*\(|source\s*[:=]|payload\s*[:=]|builder\s*[:=]|runtime\s*[:=]|subprocess|run:|node\s+|python\s+).{0,150}100_Archive/",line):
            issues.append({"file":rel.as_posix(),"line":no,"reason":"ACTIVE_ARCHIVE_DEPENDENCY"})
summary={"status":"PASS" if not issues else "BLOCKED","active_runtime_files":sum(p.parts[0] in active and p.suffix in runtime_suffix for p in tracked),"archive_execution_references":len(issues),"findings":issues}
print(json.dumps(summary,indent=2))
if issues:sys.exit(1)
