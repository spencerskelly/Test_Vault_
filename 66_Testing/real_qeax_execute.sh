#!/usr/bin/env bash
# Validate deterministic EA import and real-vault Workbench 0.5 safely.
set -euo pipefail
TMP="${RUNNER_TEMP:?}/mdse-real-qeax"
QEAX="$(find "$TMP/qeax" -maxdepth 1 -name '*.qeax' -type f -size +1M -print -quit)"
test -n "$QEAX"
node Importer/Testing/v0.8.19/headless_full_import.js \
  Importer/Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html \
  "$QEAX" "$TMP/vault" "$TMP/replay" "$TMP/failure" > "$TMP/import.log" || {
    tail -n 50 "$TMP/import.log"
    exit 1
  }
python3 Importer/Testing/v0.8.19/compare_full_import_outputs.py "$TMP/vault" "$TMP/replay"
python3 Importer/Testing/v0.8.19/imp009_output_acceptance.py "$TMP/vault"
python3 Importer/Testing/v0.8.19/imp010_hierarchy_acceptance.py "$QEAX" "$TMP/vault"
python3 Importer/Testing/v0.8.19/imp010_interface_flow_acceptance.py "$QEAX" "$TMP/vault"
python3 Importer/Testing/v0.8.19/imp011_canonical_equals_acceptance.py "$QEAX" "$TMP/vault"
npm --prefix 55_Workbench ci
npm --prefix 55_Workbench run accept:real-vault:05 -- "$TMP/vault" "$TMP/workbench-result.json"
python3 - "$TMP/workbench-result.json" <<'PY'
import json,sys
r=json.load(open(sys.argv[1],encoding="utf-8"))
assert r["status"] == "PASS",r.get("failures",[])[:10]
assert r["acceptance"] == "candidate-only"
assert r["localModelVersion"] == "0.5"
assert r["sourceVaultUnmodified"] is True
print("WB-129 real-vault Local Model 0.5 acceptance PASS")
PY
if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
  echo "Full real-QEAX import, deterministic replay, semantic topology and WB-129 read/edit acceptance passed. Candidate only, not release promotion." >> "$GITHUB_STEP_SUMMARY"
fi
