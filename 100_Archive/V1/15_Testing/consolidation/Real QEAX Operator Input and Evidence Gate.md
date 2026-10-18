# Real QEAX Acceptance — Operator Input and Evidence Gate (2026-10-14)

**Status: BLOCKED ON PAIRED REAL DATA — NOT APPROVED.** Static/synthetic CI succeeded for validation commit `298271bee000cc3a4820e134ad81778dcb0a56d5` ([run 38648119715](https://github.com/spencerskelly/Test_Vault_/actions/runs/38648119715)); its artifacts API returned **no artifacts**. Passing CI does not provide a real imported vault.

## Inputs required (one reproducible pair)
1. The **extracted, unmodified EA source `.qeax`** in a local read-only source directory. Optionally preserve the exact downloaded source ZIP for integrity attestation; do not infer an extraction from filename alone.
2. A **complete generated Obsidian vault** produced from *that exact QEAX* by the approved importer candidate; keep its original generated output and logs. Do not substitute a synthetic fixture, an old sample, or an unrelated model.
3. In that vault: `99_System/11_Import/Review - Equals Direction.csv` and `99_System/11_Import/Local Model Source Map.csv`, plus generated Markdown carrying Local Model regions.
4. A distinct results directory, outside both source QEAX and output vault, for failure/success reports.

## Read-only command
From a local checkout of the **same validation commit**:

```sh
python3 66_Testing/consolidation/step120_real_qeax_operator_gate.py \
  --qeax "/absolute/path/source.qeax" \
  --vault "/absolute/path/generated-vault" \
  --source-zip "/absolute/path/original-source.zip" \
  --results "/absolute/path/acceptance-results"
```

Omit `--source-zip` only when no authoritative source ZIP exists; record its absence in the evidence handoff. The operator gate checks SQLite integrity and **249** source BindingConnectors, hashes input evidence, verifies the two CSVs exist, and runs IMP-011 review, canonical symmetric-equals, and topology acceptance validators. It writes `qeax_imp011_acceptance.json`, returning nonzero on failure. **It does not execute the importer or create a vault**; generate and pair the vault before running it.

## Acceptance interpretation
- **PASS:** all input hashes recorded, QEAX integrity `ok`, BindingConnector count 249, review CSV and source map present, and all three validators exit zero. Retain the JSON report, generated vault snapshot, importer provenance/version, model SHA256, ZIP SHA256 if supplied, and exact source/output pairing.
- **FAIL / missing:** any input missing, damaged, mismatch, or validator failure. Inspect report and correct the underlying importer/data issue. Never relabel synthetic checks as a real import pass.
- Even PASS only closes the **real-QEAX IMP-011 gate**. Separate full-model, Obsidian GUI, release-governance and merge/branch-retirement approvals remain required.

## Next actionable handoff
Locate the actual complete generated vault produced from `EA_2026_09_06_endgame.qeax` and matching authoritative source QEAX. If this pair does not exist or cannot be shared, arrange a controlled operator import using the v0.8.19 candidate, with a captured importer log and exact hashes; then run this gate. **Do not commit the large QEAX or generated vault merely to satisfy CI.** Use a controlled, separately stored evidence bundle and record stable artifact identifiers instead.

This note makes no modifications to main, merges, branch deletion, release promotion, or QEAX signoff.
