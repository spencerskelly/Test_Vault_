#!/usr/bin/env python3
"""Report V2 references to pre-migration paths; never rewrite approved documentation."""
from pathlib import Path
import json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
ACTIVE={"20_Base Vault","21_Importer","23_Bootstrap","24_Workbench","25_Testing","26_Definitions","29_SysMLv2_Translator_Workbench"}
EXT={".md",".py",".mjs",".js",".ts",".json",".yaml",".yml",".html"}
PATTERN=re.compile(r"(?<![\w/])(?:10_Base Vault|11_Importer|13_Bootstrap|14_Workbench|15_Testing|16_Definitions)/[^\s\x60'\"<>)]*")
files=[Path(p) for p in subprocess.check_output(["git","ls-files","-z"],cwd=ROOT).decode().split("\0") if p]
results=[]
for rel in files:
    if rel.parts[0] not in ACTIVE or rel.suffix not in EXT:continue
    if rel.name in {"V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json","V2_FOLDER_MIGRATION_REFERENCE_AUDIT_2026-10-18.json","audit_v2_legacy_references.py"}:continue
    f=ROOT/rel
    if not f.is_file():continue
    try:lines=f.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:continue
    for line_no,line in enumerate(lines,1):
        for match in PATTERN.finditer(line):
            value=match.group(0).rstrip(".,;:")
            classification="historical_reference" if any(t in line.lower() for t in ("historical","archive","legacy","old path","prior path","previous path","superseded")) else "review_active"
            # Docs can mention old paths for historical discussion. Do not alter them automatically.
            results.append({"file":rel.as_posix(),"line":line_no,"reference":value,"class":classification})
summary={"schema":"mdse-v2-migration-reference-audit/1","total":len(results),"review_active":sum(x["class"]=="review_active" for x in results),"historical_reference":sum(x["class"]=="historical_reference" for x in results),"findings":results}
print(json.dumps(summary,indent=2))
if "--strict" in sys.argv and any(x["class"]=="review_active" and Path(x["file"]).suffix in {".py",".mjs",".js",".ts",".json",".yaml",".yml",".html"} for x in results):
    sys.exit(1)
