#!/usr/bin/env python3
"""Fail closed when a merged importer Local Model schema exceeds Workbench source support.

This is a compatibility gate, not a version-label check or a release promotion.
Run from a checked-out combined Test_Vault_ tree, after a candidate importer merge.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required for exact manifest/schema parsing", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parent.parent
release = yaml.safe_load((ROOT / "Base Vault/Definition/mdse-release.yaml").read_text(encoding="utf-8"))
model = yaml.safe_load((ROOT / "99_System/03_Schemas/local-model.yaml").read_text(encoding="utf-8"))
source = (ROOT / "55_Workbench/src/core/localmodel.ts").read_text(encoding="utf-8")

readable_match = re.search(r'\bREADABLE_VERSIONS\s*=\s*\[([^\]]+)\]', source)
writable_match = re.search(r'\bWRITABLE_VERSION\s*=\s*["\']([^"\']+)["\']', source)
if not readable_match or not writable_match:
    print("BLOCKED: Workbench Local Model source grammar cannot be statically resolved; review required")
    raise SystemExit(1)

readable = re.findall(r'["\']([0-9.]+)["\']', readable_match.group(1))
writable = writable_match.group(1)
schema_version = str(model.get("schemaVersion"))
manifest_version = str(release["schemas"]["localModel"])
schema_writable = str(model["compatibility"]["writableVersion"])
schema_readable = [str(v) for v in model["compatibility"]["readableVersions"]]

print("Release Local Model:", manifest_version)
print("Schema Local Model:", schema_version)
print("Schema writable/readable:", schema_writable, schema_readable)
print("Workbench source writable/readable:", writable, readable)

issues = []
if schema_version != manifest_version:
    issues.append("manifest and schema Local Model versions disagree")
if schema_writable != schema_version:
    issues.append("schema writableVersion differs from active schemaVersion")
if schema_version not in readable:
    issues.append(f"Workbench source DOES NOT READ schema {schema_version}")
if writable != schema_writable:
    issues.append(f"Workbench WRITES {writable}, but the active importer schema requires {schema_writable}")
if any(v not in readable for v in schema_readable):
    issues.append("Workbench cannot read all canonical schema backwards-compatibility versions")

if issues:
    for x in issues:
        print("BLOCKED:", x)
    print("Resolution: reconcile WB-129 Local Model 0.5 changes into 55_Workbench on a reviewed feature branch; do not change release pins just to hide incompatibility.")
    raise SystemExit(1)

print("PASS: Actual Workbench Local Model parser/writer and importer schema are compatible")
