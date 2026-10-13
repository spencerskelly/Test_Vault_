# Branch Cleanup — Checkpoint BR-42: Release Manifest Authority Gate

**Date:** 2026-10-12
**Repository:** spencerskelly/Test_Vault_
**Audit PR:** #41
**Engineering candidate:** consolidation/step22-single-repo-cutover-2026-10-11
**Reference manifest:** `Base Vault/Definition/mdse-release.yaml` Git blob `6d06db25ed50ff390460c567b8fa769981aacc9e`
**Status:** PRE-RELEASE — governance proposals remain proposals

## Confirmed source facts, not inferred

Directly fetched the Step22 candidate manifest (not relying on old PR summaries). It declares:
- `manifestVersion: 2`
- `mdseRelease: "0.8.0"` and `releaseStatus: pre-release`, dated 2026-10-05
- `sourceModelId: EA8647`
- `schemas.relationships: "1.36"`, `schemas.elementTypes: "1.18"`, `schemas.localModel: "0.5"`
- `tools.importer.release: null`; importer **candidate** v0.8.19 at `Importer/Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html`
- `tools.workbench.repo: "spencerskelly/Test_Vault_"`, version `0.1.18`, `requiredForRelease: true`, `nextGate: Golden-model integration / Bootstrap first-open`
- `tools.bootstrap.version: "0.3.0"` active; `candidateSource: Bootstrap/Tools/v0.3.1` not promoted.
- `repos.authority` and `repos.workbench` both point at `spencerskelly/Test_Vault_`, expressing repository *development authority* but not a release promotion.
- Controlled `runtimePlugins.lock: ".obsidian/plugin-lock.yaml"`, mapped runtime Base inputs and forbidden copy-outs, and `Base Vault/Testing/check-release.py` as the described checker.

## The governance separation is concrete

In the same manifest's `documents` list, the following remain explicitly **status: proposal**:
- `00_Workspace/Consolidation Step 15 - Exact Registry Redline and Promotion Stops 2026-10-10.md`
- `00_Workspace/Consolidation Step 15 - Proposed W Decision and Authority Signoff 2026-10-10.md`
- `00_Workspace/MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md`

The manifest also includes current authority rows, including `00_Workspace/00 - Current State.md`, `00_Workspace/Workspace Decision Log.md`, `Importer/Definition/Translator Definition.md`, `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`, and several active Bootstrap/Base documents. Proposed continuation contract does **not** supersede those by being registered.

The Step22 cutover document `66_Testing/consolidation/STEP22_SINGLE_REPO_CUTOVER.md` explicitly states moving **new development location** to `Test_Vault_/55_Workbench/` does **not** ratify W/Workbench source-authority decisions, Local Model 0.6 writing, BOM quantity/units/`variantOf` authoring, a release or GUI acceptance.

## Small reviewer decision packet

1. **Development location:** Accept the staged source-location policy subject to PR review; do not treat `main` as promoted.
2. **Document/W governance:** Review the three proposals under existing current authority, record specific approvals/rejections and any registry changes separately.
3. **Schema changes:** Keep relationship 1.36, elements 1.18 and Local Model 0.5 pinned until governed change approval and tests; do not silently ship Local Model 0.6 or BOM authoring.
4. **Importer release:** Null release + v0.8.19 candidate is not a published importer release.
5. **Release gate:** On an exact agreed promotion SHA, run pinned check-release, Workbench/importer/Bootstrap compatibility, generated Base and fail-closed negatives, and obtain real UI acceptance. Do not convert `pre-release` to release merely because historical Step22 CI was green.
6. **Safety gates:** Separately resolve QEAX public-history data-owner decision (BR-37), contributors' private local worktree signoffs (BR-38), and any standalone repo archive authorization.

## Handoff

**BR-42 completed:** Verified actual controlled source-of-truth manifest and explicit proposal rows, clarifying development-home change versus release authority. No governance signoff, runtime test, archive or deployment was performed.

**NEXT BR-43:** Trace one concrete outstanding release gate using actual checks in `Base Vault/Testing/check-release.py` and CI configuration; produce a compact exact-tip test matrix rather than another global summary.

**NO ACTION:** No PR closing, merging, branch deletion, workflow promotion, manifest modification or standalone archive.
