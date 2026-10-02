# 09_Tools — Current status

This folder contains native importer history and vault initialization helpers.

## Current v0.8 direction

There is **no release-conformant v0.8 importer file yet**.

Use these as code/history references only:
- v0.5.2 — accepted safety/base-validation lineage;
- v0.7 — occurrence/QEAX assessment and merge evidence.

Do not use v0.7 to generate a model intended to keep.

The next issued importer is:

`EA_to_MDSE_Native_Importer_v0.8.0.html`

and it must follow:
1. `../10_Docs/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md`
2. `../10_Docs/Translator Definition.md`
3. Workspace Decision Log through W-319
4. relationships 1.35
5. element-types 1.17
6. local-model 0.2

The matched clean base must declare `mdse_release: "0.8.0"`. v0.8 is a clean import; do not migrate/patch a v0.7-generated vault in place.

## Important current rules

- source lineage: EA8647;
- one global 30-character identity-token namespace;
- Local Model Source Map authoritative on rerun;
- duplicate name marker `~2`;
- forced alteration marker `~a`;
- maximum generated repository-relative path 212;
- attachment failures non-blocking but reconciled;
- all source diagrams must reconcile although initial diagram creation is deferred.

See `MDSE v0.8 Toolchain Review - 2026-10-02.md` for the code-gap audit.

## File status (W-320)

| File | Status | Use |
|---|---|---|
| `EA_to_MDSE_Native_Importer_v0.1.html` | history | Established direct-QEAX preflight and the source-count baseline (W-273). Do not run for a model. |
| `EA_to_MDSE_Native_Importer_v0.2.html` | accepted planning baseline, immutable | Whole-model planner, passed on the real QEAX (W-274). Reference for planner behavior. |
| `EA_to_MDSE_Native_Importer_v0.3.html`, `v0.4.html`, `v0.5.html`, `v0.5.1.html` | history | Intermediate builds. Superseded by v0.5.2. |
| `EA_to_MDSE_Native_Importer_v0.5.2.html` | accepted safety lineage (fallback) | Base-vault identity checks, stale-state invalidation, `hasState/stateOf`, schema 1.35. Starting point for v0.8.0. |
| `EA_to_MDSE_Native_Importer_v0.7.html` | merge candidate, never accepted | Occurrence/QEAX code evidence. Not release-conformant (14 gaps listed in the Toolchain Review). Do not generate a model to keep. |
| `EA_to_MDSE_Native_Importer_v0.8.0.html` | planned, not built | The release importer. Build order is in the Reconciliation document. |
| `Initialize-Vault.sh`, `Initialize-Vault.ps1` | current helpers | Initialize `.vault.yaml` once in a new disposable or real vault. |

The machine-checkable version of this table is `99_System/03_Schemas/mdse-release.yaml`; run `python3 99_System/09_Tools/check-release.py` after any change to tools, schemas or docs. Registry of current files: [[00 - Current State]].


## Base build and release alignment (W-321)

- `build-base.py <output>` generates the lean runtime base from the one positive include list in `mdse-release.yaml`.
- `check-release.py --base <output>` verifies the generated base contains exactly the governed runtime set, the same schemas, and `mdse_release`.
- `check-release.py --workbench <clone>` verifies Workbench version plus current schema fixtures and the frozen Local Model 0.1 compatibility fixture.
- Current State and `mdse-release.yaml` stay in the methodology workspace; they are not duplicated into engineering vaults.
- `Initialize-Vault.sh/.ps1` preserve `mdse_release`.
- W-322 replaces the W-321 Bootstrap deferral: see the controlled plugin release section below.

## Controlled plugin release (W-322)

| File | Role |
|---|---|
| `runtime-plugins/<id>/` | Vendored plugin code for all 11 runtime plugins, plus generated governed `data.json` |
| `build-plugin-config.py` | Generates governed settings, `../06_Fileclasses/` and its link-target Base from the schemas (`--check` to verify) |
| `update-plugin-lock.py` | Generates `.obsidian/plugin-lock.yaml` (schema 2, hashes) and `.obsidian/community-plugins.json` (`--check` to verify) |
| `build-base.py` | Also copies every locked plugin into the base and writes the base `.gitignore` |
| `check-release.py` | Also runs both `--check`s, verifies payload hashes and Bootstrap/Workbench versions, and the plugins inside a built base |

Bootstrap source and docs live in `MDSE Bootstrap/` at the workspace root. How to change a plugin version: `MDSE Bootstrap/README_MDSE Bootstrap.md`.
