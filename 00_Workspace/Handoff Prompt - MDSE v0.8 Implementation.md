# Handoff Prompt — MDSE v0.8 Implementation

**Current through W-386 / Workbench 0.1.18 release alignment, 2026-10-05.** Use this file to start the next chat. The numbered Workbench performance/stability sequence remains complete through Step 60; do not reconstruct or extend it.

## Copy-ready continuation prompt

> Continue the MDSE v0.8 golden-model/toolchain work. Authorities: `spencerskelly/Test_Vault_` for shared MDSE semantics/importer/Base/Bootstrap governance and `spencerskelly/MDSE_Workbench` for Workbench implementation. Current matched semantics are relationships 1.36, element-types 1.18 and Local Model 0.4. Importer v0.8.19 has a deterministic real-QEAX whole-model candidate with `IMPORT_COMPLETE` and completed WB-128 acceptance. Workbench 0.1.18 is merged, exact-artifact startup accepted and is the W-386 WB-106 Base pin. Do not add more standalone Workbench hardening without new regression evidence. Continue the remaining G2 path: importer release conformity, clean 0.8.0 base issuance, then Bootstrap first-open/OS acceptance before any keep/freeze decision.

## Released Workbench baseline

Workbench 0.1.18 is the W-386 controlled WB-106 baseline. WB-128 merged at `e2364cabd97118c9e9cc359ad5404620309092cc`; the controlled runtime artifact is `b0c4e2c6bdfb96d36f51d8152b17be22592ef174` and exact-artifact startup acceptance is run `37408519667`.

Exact SHA-256:
- `main.js`: `bc553fef67b5aa2cc7623b2811c05e7af8952296dd3b3ba55e663e3de5fc64aa`
- `manifest.json`: `a898ec3acce99650f18ded11235a236881ce8a8de86bfc857c70c5c4508d0e5d`
- `styles.css`: `445abe199f3dbf00724dc3cffa13aed58fc087adc9396e79de18ebe6b274b008`

Acceptance authority is `00_Workspace/Workbench Performance and Stability Roadmap.md`. Steps 55–59 retain the integrated runtime evidence; Step 60 freezes the candidate and handoff. Do not reopen Steps 18–60 unless the Workbench candidate changes or new evidence invalidates acceptance. A later code change is a new candidate and must rerun the acceptance scope affected by that change.

W-386 promotes Workbench 0.1.18 into the controlled pre-release Base payload/lock and sets `wb106Version`. This does **not** make the overall MDSE 0.8 release complete; importer release conformity, clean-base issuance and Bootstrap first-open/OS gates remain.

## Current release target

- MDSE release: **0.8.0 pre-release**
- relationships: **1.35**
- element-types: **1.17**
- Local Model: **0.2**
- importer: **v0.8.6 candidate**
- Workbench Base pin / WB-106 release: **0.1.18** (W-386); Local Model 0.1–0.3 remain readable/read-only for structured mutation and 0.4 is the governed structured-write target
- Bootstrap official runtime: **0.3.0**
- Bootstrap candidate: **0.3.1**
- Base tooling: **v0.8.0-r2**

## Stable stopping point from 2026-10-03

Bootstrap 0.3.1 builds on the development Mac and all 9 tests pass. Its candidate runtime payload and regenerated lock validated successfully. Candidate-aware release validation was added in W-335.

A clean Base Vault candidate built successfully and `Base Vault/Testing/check-release.py --base` completed with **0 fail / 4 expected pre-release warnings**. Those warnings are intentional: Bootstrap 0.3.1 is still a candidate while 0.3.0 is pinned; Workbench 0.1.16 is not yet WB-106-capable; importer v0.8.6 is not released; the clean base repository is not issued.

During initialization testing, defects in `Initialize-Vault.sh` were found before any partial identity change occurred. The release-value extraction was simplified, and `check-release.py` now runs `sh -n` against the initializer (W-336).

Per W-337, do not create another integration vault solely to continue Bootstrap testing. Finish Workbench WB-106 first, then importer v0.8.6 alignment, and use one fresh integrated candidate for Bootstrap first-open persistence, importer execution and Workbench validation.

W-338 excludes OS metadata such as `.DS_Store` and `Thumbs.db` from governed Base Vault copies. W-340 defines Internal Structure as presentation over one Local Model context, with curated Canvas geometry non-semantic. W-341 ships and cross-checks the engineer-facing Workbench guide. W-342 distinguishes the standalone 0.1.17 Workbench candidate from the still-pinned 0.1.16 Base runtime.

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

Workbench 0.1.18 is the released W-386 Base pin. The stability roadmap remains closed at Step 60; do not invent a Step 61. WB-128's bounded real-vault Gates 1–4 and the exact-artifact startup gate are the acceptance baseline for Local Model 0.4. Any later Workbench code change is a new candidate and must rerun the acceptance scope affected by that change. Use Workbench's current docs/tests as implementation authority and keep `src/core` free of Obsidian imports.

## Important governance

- Normal development occurs on `main`; version folders retain tool revisions. Branches are exceptional isolation mechanisms, not version storage.
- Importer executable stays external to operational vaults.
- Candidate and released versions must remain explicitly distinct.
- Root README is navigation, not version authority; `00 - Current State.md` and `Base Vault/Definition/mdse-release.yaml` carry current release state (W-335).
- Translator Definition only advances its W-marker when a decision changes importer/stage-1 behavior (W-335).
- Cross-vault implementation is deferred during the golden-model push.
