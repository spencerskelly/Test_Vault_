#!/usr/bin/env python3
"""Repair executable references after the numbered V2 migration. Idempotent, fail closed."""
from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[2]
tracked=[Path(x) for x in subprocess.check_output(["git","ls-files","-z"],cwd=ROOT).decode().split("\0") if x]
active={"20_Base Vault","21_Importer","23_Bootstrap","24_Workbench","25_Testing","26_Definitions","29_SysMLv2_Translator_Workbench"}
code={".py",".mjs",".js",".ts",".json",".yml",".yaml"}
old="14_Workbench/registry/"
changed=[]
for path in tracked:
    if path.parts[0] not in active or path.suffix not in code:continue
    if path.name in {"V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json","V2_FOLDER_MIGRATION_REFERENCE_AUDIT_2026-10-18.json"}:continue
    full=ROOT/path
    if not full.exists(): continue
    try: content=full.read_text()
    except UnicodeDecodeError:continue
    if old not in content:continue
    revised=content.replace(old,"24_Workbench/registry/")
    if path.as_posix()=="24_Workbench/registry/sysml_v2_registry_pins.v0.1.json":
        # Hash values are unchanged. Paths are identifiers; only keys are renamed.
        before=json.loads(content)["files"]
        after=json.loads(revised)["files"]
        if sorted(before.values())!=sorted(after.values()):
            raise SystemExit("PIN_HASH_CHANGED")
    full.write_text(revised)
    changed.append(str(path))
remaining=[]
for path in tracked:
    if path.parts[0] not in active or path.suffix not in code:continue
    full=ROOT/path
    if not full.exists():continue
    try: content=full.read_text()
    except UnicodeDecodeError:continue
    if old in content and path.name not in {"V2_FOLDER_MIGRATION_REFERENCE_AUDIT_2026-10-18.json","V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json"}:
        remaining.append(str(path))
print(json.dumps({"changed":changed,"remaining_executable_old_registry_references":remaining},indent=2))
if remaining:sys.exit(1)
