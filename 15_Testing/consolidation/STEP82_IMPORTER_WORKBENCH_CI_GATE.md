# Step 82 — Importer Workbench compatibility gate (2026-10-14)

## Evidence / coverage classification

Inspected the active MDSE consolidated read-only integration run 38613661950; its eight jobs include importer static-contract and importer/governance smoke checks, but **none has a step invoking `66_Testing/check_importer_workbench_localmodel.py`**. The script is preserved byte-identically from historical PR #9, yet current CI did not execute it.

The current candidate source and YAML contracts match the checker's expected Local Model 0.5: release schema pin 0.5, canonical schemaVersion 0.5, writableVersion 0.5, readable [0.1–0.5], while Workbench source reader includes 0.6 and writer stays at 0.5.

## Change

Added `.github/workflows/step82-importer-workbench-contract.yml` on PR43 validation branch, commit `7626d9191558f8da170bf743fdf2953b38d50ee5`. It uses read-only sparse checkout of exactly the checker, Workbench source, release manifest, and schema; Python 3.12 with pinned PyYAML; then executes the original fail-closed compatibility checker as a blocking CI step. No historical importer merge, publication or QEAX data access.

New run `38614565590` was queued and **its conclusion was not available at checkpoint**.

## Boundary

This closes the missing *execution wiring* for the static importer/Workbench source-version check in the validation PR, subject to actual passing execution. It does **not** replace historical non-committing importer merge rehearsal, full importer acceptance, original Git ancestry proof, or macOS/Windows GUI/real-QEAX evidence. Do not merge/retire PR #9 until those are independently classified and approved.

## Step 83

Inspect the Step82 workflow result; if passed, verify fail-closed negative mode using a disposable modified schema within runner without touching tracked sources. Then decide how to curate this check into the approved main-based CI PR #42. No release/ref deletion or main promotion without review.
