#!/usr/bin/env python3
"""Step 16 read-only native release-check diagnostic; fail unknown errors."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
proc = subprocess.run(
    [sys.executable, "Base Vault/Testing/check-release.py", "--workbench", "55_Workbench"],
    cwd=ROOT, text=True, capture_output=True, check=False,
)
lines = proc.stdout.splitlines() + proc.stderr.splitlines()
fails = [line for line in lines if line.startswith("FAIL ")]
docs = [line for line in fails if line.startswith("FAIL current tool/workspace document registered: ")]
warns = [line for line in lines if line.startswith("WARN ")]
required = [
    "Workbench user guide equals Base Vault release copy",
    "Workbench package/manifest 0.1.18 match pinned release manifest",
    "Workbench lock 0.1.18 matches pinned release manifest",
]
for phrase in required:
    if not any(re.match(r"^ok\s+", x) and phrase in x for x in lines):
        print("STEP16_ERROR=missing_native_W341_W342_evidence", phrase)
        sys.exit(1)
if len(fails) != len(docs):
    print("STEP16_ERROR=unexpected_native_release_failure")
    for line in fails:
        if line not in docs:
            print(line)
    sys.exit(1)
if (docs and proc.returncode != 1) or (not docs and proc.returncode != 0):
    print("STEP16_ERROR=unexpected_native_exit", proc.returncode)
    sys.exit(1)
if not any(re.fullmatch(r"\d+ fail, \d+ warn", line) for line in lines):
    print("STEP16_ERROR=native_summary_missing")
    sys.exit(1)
print("STEP16_W341_W342=FOCUSED_CHECKS_PASS")
print("STEP16_NATIVE_RELEASE_GATE=" + ("BLOCKED_UNREGISTERED_DOCUMENTS" if docs else "NO_FAIL"))
print("STEP16_DOCUMENT_REGISTRY_FAILURES=" + str(len(docs)))
print("STEP16_NATIVE_WARNINGS=" + str(len(warns)))
print("STEP16_RELEASE_STATUS=PRE_RELEASE_NOT_ISSUED")
