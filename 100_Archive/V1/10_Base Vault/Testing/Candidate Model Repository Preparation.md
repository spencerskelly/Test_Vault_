# Candidate Model Repository Preparation

**Purpose:** bridge the deterministic clean Base Vault artifact to the repository that is actually imported, opened in Obsidian and eventually promoted to the golden model. W-334.

## Stage 1 — clean build artifact

1. Build into an empty folder with `Base Vault/Tools/v0.8.0-r2/build-base.py`.
2. Run `Base Vault/Testing/check-release.py --base <folder>`.
3. Expected: zero failures. `.vault.yaml` still contains `vault_uid: UNINITIALIZED`. The folder does not need to be a Git repository.
4. Do not edit the clean artifact by hand. Rebuild it instead.

## Stage 2 — candidate model repository

**Do not enter this stage during the current 2026-10-03 stopping point.** W-337 defers the next candidate repository until Workbench WB-106 and importer v0.8.6 are aligned enough to make it a meaningful integration test.

From a validated clean artifact:

1. Make the candidate working copy.
2. Run `Initialize-Vault.sh` or `Initialize-Vault.ps1` once with the intended vault name and release-owner author code.
3. Initialize Git and connect the intended remote when sync behavior will be tested.
4. Commit the initialized clean starting point.
5. Run the Bootstrap First-Open Test Sheet.
6. Run the external importer from `Importer/Tools/<version>/` against this repository.
7. Commit import evidence/model output according to the golden-model plan.

## Stage 3 — operational/golden repository

When a candidate is accepted and the golden gates pass:

- retain the same initialized `vault_uid`;
- retain the model history/baseline;
- engineers clone this repository;
- engineers only perform Obsidian trust/enable plus Bootstrap author registration;
- engineers do **not** run Initialize-Vault or the importer.

A rejected candidate may be discarded entirely and rebuilt from Stage 1.
