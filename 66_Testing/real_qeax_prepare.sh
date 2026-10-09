#!/usr/bin/env bash
# Prepares exactly pinned importer and schema-compatible Workbench in CI only.
set -euo pipefail
TMP="${RUNNER_TEMP:?}/mdse-real-qeax"
mkdir -p "$TMP/qeax"
git merge-base --is-ancestor 8097f383c41617f879eac8e4ca19fab1d0cb7657 HEAD
git config user.name "MDSE acceptance"
git config user.email "mdse-acceptance@users.noreply.github.com"
git fetch --no-tags origin refs/heads/importer/baseline-contract-2026-10-05
test "$(git rev-parse FETCH_HEAD)" = 0494354ec40378e119b17c61fdf6e828844035e4
git merge --no-ff --no-commit FETCH_HEAD
python3 66_Testing/check_importer_workbench_localmodel.py
test -f EA_2026_09_06_endgame.qeax.zip
unzip -j EA_2026_09_06_endgame.qeax.zip -d "$TMP/qeax" >/dev/null
QEAX="$(find "$TMP/qeax" -maxdepth 1 -name '*.qeax' -type f -size +1M -print -quit)"
test -n "$QEAX"
test "$(sha256sum "$QEAX" | cut -d' ' -f1)" = 16c055ec1a5af57b0f4f9059d6292c5ddd3ed052124c7ef54d9af288971ae02c
test "$(sqlite3 "$QEAX" 'SELECT count(*) FROM t_object;')" = 35969
test "$(sqlite3 "$QEAX" 'SELECT count(*) FROM t_connector;')" = 21822
for target in "$TMP/vault" "$TMP/replay" "$TMP/failure"; do
  python3 "Base Vault/Tools/v0.8.0-r2/build-base.py" "$target"
  printf 'vault_uid: 20261006000000000skellyspencer\nname: MDSE_05_CANDIDATE\ndefault_branch: main\nmdse_release: "0.8.0"\n' > "$target/.vault.yaml"
done
echo "Frozen QEAX verified, schema compatible, disposable bases created."
