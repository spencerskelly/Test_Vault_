# Handoff Prompt — MDSE v0.8 Implementation

**Current through W-338, 2026-10-03.** Use this file to start the next chat. **Workbench WB-106 is complete and pinned as 0.1.17.** The immediate priority is now **importer v0.8.6 alignment**, then one fresh integrated candidate vault.

## Copy-ready continuation prompt

> Continue the MDSE v0.8 golden-model/toolchain work. Authorities: `spencerskelly/Test_Vault_` (main) for shared MDSE semantics, importer, Bootstrap, Base/release tooling and golden-model governance; `spencerskelly/MDSE_Workbench` (main) for Workbench implementation and its product-definition docs. Read first: `Test_Vault_/00_Workspace/00 - Current State.md`; `Test_Vault_/00_Workspace/MDSE Plan - Path to a Golden Model.md`; `Test_Vault_/00_Workspace/MDSE Tool Definitions and Boundaries.md`; `Test_Vault_/00_Workspace/Workspace Decision Log.md` through W-338; `Test_Vault_/99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`; `Test_Vault_/Importer/Definition/Translator Definition.md`; and the current Workbench docs under `MDSE_Workbench/docs/Definition/`. Workbench WB-106 is complete in 0.1.17: occurrence-aware Structure, Interfaces, Where Used and Requirements; read-only Local Model occurrence details; Review integration; exact local block targeting; Local Model 0.1/0.2 read compatibility. Its built runtime is vendored, hashed and pinned as `wb106Version: "0.1.17"`. Preserve the settled occurrence model: reusable definitions are notes; contextual uses are Local Model records; no fake notes; occurrence clicks open occurrence details; inheritance comes from subtypeOf/instanceOf/occurrence→definition, never partOf. Next align importer v0.8.6 against this runtime contract. Do not create a throwaway vault; once importer alignment is ready, build the one fresh integration candidate required by W-337 for Bootstrap first-open persistence + importer + Workbench validation.

## Current release target

- MDSE release: **0.8.0 pre-release**
- relationships: **1.35**
- element-types: **1.17**
- Local Model: **0.2**
- importer: **v0.8.6 candidate**
- Workbench runtime: **0.1.17**; **WB-106 complete and pinned**
- Bootstrap official runtime: **0.3.0**
- Bootstrap candidate: **0.3.1**
- Base tooling: **v0.8.0-r2**

## Stable stopping point from 2026-10-03

Bootstrap 0.3.1 builds on the development Mac and all 9 tests pass. Its candidate runtime payload and regenerated lock validated successfully. Candidate-aware release validation was added in W-335.

A clean Base Vault candidate previously built successfully and `Base Vault/Testing/check-release.py --base` completed with **0 fail / 4 expected pre-release warnings**. Workbench is no longer one of those warnings: 0.1.17 is now the WB-106-capable pinned runtime. The remaining pre-release blockers are Bootstrap 0.3.1 promotion/integrated persistence testing, importer v0.8.6 acceptance/release, and issuance of the clean base repository.

During initialization testing, defects in `Initialize-Vault.sh` were found before any partial identity change occurred. The release-value extraction was simplified, and `check-release.py` now runs `sh -n` against the initializer (W-336).

Per W-337, do not create another integration vault solely to continue Bootstrap testing. WB-106 is now complete; align importer v0.8.6 next, then use one fresh integrated candidate for Bootstrap first-open persistence, importer execution and Workbench validation.

W-338 excludes OS metadata such as `.DS_Store` and `Thumbs.db` from governed Base Vault copies.

## Settled Base/Bootstrap lifecycle

1. `build-base.py` creates a deterministic raw artifact with `vault_uid: UNINITIALIZED` and no Git requirement.
2. `check-release.py --base` validates the raw artifact.
3. Release owner initializes the candidate identity once, initializes/connects Git, and commits the clean starting point.
4. External importer writes the model; importer executable is never shipped in the operational vault.
5. Bootstrap verifies locked runtime files/config and performs only safe activation repair; changed/missing locked plugins remain disabled and are reported.
6. Engineers eventually clone the initialized golden repository; they do not initialize the vault or run the importer.

## Bootstrap 0.3.1 promotion gate

Still required in the integrated candidate vault:

- community plugin disabled → Bootstrap re-enables → restart → remains enabled;
- Canvas disabled → Bootstrap enables → restart → remains enabled;
- core Templates enabled → Bootstrap disables → restart → remains disabled;
- damaged locked plugin stays disabled and reports drift;
- governed `data.json` drift is detected and not overwritten;
- extra community plugin warns but is not disabled/uninstalled.

## Workbench continuation

Current runtime 0.1.17 completes WB-106: Local Model 0.1/0.2 parsing, durable `ModelRef`, incremental occurrence indexing/findings, occurrence-aware Structure/Interfaces/Where Used/Requirements, derived Canvas occurrence cards with native block links, read-only Local Model details, Review integration, and Obsidian-style link writing. The standalone Workbench tests/build pass, its built artifacts are vendored in `Base Vault/Runtime/Plugins/mdse-workbench/`, the plugin lock is regenerated, `mdse-release.yaml` records `wb106Version: "0.1.17"`, and release checks pass.

Do not expand this milestone into structured Local Model editing yet. Configuration persistence/topology variation and other W-314 follow-on work remain deferred until the importer/integrated candidate proves the read/navigation foundation.

## Important governance

- Normal development occurs on `main`; version folders retain tool revisions. Branches are exceptional isolation mechanisms, not version storage.
- Importer executable stays external to operational vaults.
- Candidate and released versions must remain explicitly distinct.
- Root README is navigation, not version authority; `00 - Current State.md` and `Base Vault/Definition/mdse-release.yaml` carry current release state (W-335).
- Translator Definition only advances its W-marker when a decision changes importer/stage-1 behavior (W-335).
- Cross-vault implementation is deferred during the golden-model push.
