# Branch Cleanup — Checkpoint 119 (2026-10-14)

## Source and evidence inventory
Direct `fetch_file` checks on `integration/p03-legacy-compat-tests-20261013`:
- `EA_2026_09_06_endgame.qeax.zip` exists as GitHub blob `513b2d2d4696b1502fe482424f7c05985442e2b9`. Connector fetch returned empty text because it is a binary artifact, **not proof of ZIP integrity or its extracted QEAX content**.
- `Importer/Testing/v0.8.19/imp011_binding_review_acceptance.py` available. Reads SQLite QEAX `t_connector` BindingConnector GUIDs, expected 249; reads `99_System/11_Import/Review - Equals Direction.csv` under a generated vault, requires 249 unique matching review rows with 23 exposes, 209 equals, and 17 unresolved.
- `Importer/Testing/v0.8.19/imp011_canonical_equals_acceptance.py` available. Checks Local Model 0.5 symmetry/counts (418 directed, 209 undirected equals links).
- `99_System/11_Import/Review - Equals Direction.csv` at branch root returned 404. This is consistent with the expected CSV being generated per import rather than committed as source.
- Step89 source-tree audit explicitly held real-QEAX import, GUI acceptance, and historical source approval.

## Conclusion
**Real-source acceptance cannot be claimed in this environment based on inspected evidence.** No accessible verified generated vault plus paired model was identified by these checks. The original source ZIP needs SHA-256 and extraction validation; generated vault must be paired with that exact model and importer version. Avoid interpreting the Git blob SHA as a SHA-256.

## Reproducible gate
1. Confirm source ZIP file bytes, SHA-256, archive integrity, extracted QEAX SQLite `PRAGMA integrity_check`, expected tables, source model identity, and BindingConnector GUID/count.
2. Import with pinned v0.8.19 browser importer into a disposable validated base; retain generated note files, `Review - Equals Direction.csv`, `Local Model Source Map.csv`, transaction manifest and hashes. Do not overwrite approved vault.
3. Run the original `imp011_binding_review_acceptance.py`, `imp011_canonical_equals_acceptance.py`, and candidate `imp011_topology_acceptance_v2.py` with identical `QEAX` and `vault` arguments. Save stdout, exit codes, file hashes and failing GUIDs. Every check must pass.
4. Only then consider manual Obsidian macOS/Windows GUI checks, governance signoff, merge and branch retirement.

## Next Step 120
Locate real generated outputs in other existing branch paths or approved work products, or prepare a deterministic operator execution kit for the controlled real-QEAX run. Do not infer results if the output is missing.

Holds: main unchanged; no merge, branch deletion, artifact promotion or acceptance claims.
