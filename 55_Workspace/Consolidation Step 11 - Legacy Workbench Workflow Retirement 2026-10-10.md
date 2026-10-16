# Consolidation Step 11 — Historical Workbench CI workflow retirement

**Date:** 2026-10-10 Pacific time. **Status:** isolated draft-branch retirement candidate; NOT merged into public `main` and NOT permission to archive standalone Workbench.
**Source baseline:** `spencerskelly/Test_Vault_` Step 10 commit `34be43521b1579e0ced60e66cd234c87ba4c22c4`.

## Exact archive and execution boundary

Eight legacy workflows were copied to `55_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/` as the exact original Git blobs, then their runnable `.github/workflows/*.yml` entries were removed **only on this isolated consolidation branch**. All eight SHA matches were verified remotely after installation, before their active paths were removed.

Three historical workflows (BOM A-14 source Step 15, WB-129 rehearsal, Workbench subtree staging) had GitHub `contents: write` permission and Git pushes. The other five were older WB-128/WB-129 acceptance/testing routes, some manually dispatchable. None is accepted as current release evidence merely by retaining its bytes.

Moved originals and Git blob provenance:

| Former root workflow | Archived Git blob SHA |
|---|---|
| `bom-a14-source-step15.yml` | `b0a138ecdb46a3a74587aa0ba04997a06d930455` |
| `wb128-gate3-representative-views.yml` | `0bdaa3b0feb5e6917f6cb42053f93ddbcac8cb06` |
| `wb128-gate4-disposable-edits.yml` | `5afbcd3322f228889fd0ce57e66e14eb3c725598` |
| `wb128-gate5-release-alignment.yml` | `abf0174b2af10d4f9974a584bfa12530f1721b47` |
| `wb128-real-vault-acceptance.yml` | `44b4c93f413ccf0478b8cfb162692fc0f40b0004` |
| `wb129-real-qeax-local-model-05.yml` | `7c14dc88cb3cd53fc317897cd260c3ed9113c2f7` |
| `wb129-rehearsal.yml` | `7721087d6fc31cafd2390cdaa5ba8ae1fc97b09a` |
| `workbench-subtree-stage.yml` | `3e51e09147179ffed9a24c3f19b38d8705fb6fe1` |

## CI and regression gate

`66_Testing/consolidation/test_step11_retirement.cjs` checks all eight Git archive objects against content-derived SHA, proves each former active path is absent from the staged Git tree, checks the remaining root workflows do not checkout the old Workbench repo, and validates read-only preservation of the locked 0.1.18 runtime / Local Model 0.5 pre-release pins. The test opens only archived text YAML and Git metadata; it does not open the QEAX archive.

A **branch-only**, sparse-checkout GitHub Actions workflow runs those tests without write permissions or artifact uploads. Passing this workflow is limited to retirement integrity; it does not prove full Workbench/Importer/Bootstrap or real Obsidian startup acceptance.

## Safety and pending release gates

- This change does **not** modify `Test_Vault_/main`, standalone `MDSE_Workbench`, the historical workflow runs, the original released plugin lock or its generators, or past W decisions.
- Other GitHub branches or external CI could still contain/run the historical workflows. Do not claim they are globally disabled until approved promotion and explicit review.
- The Step 10 source-aware Workbench reference checker may no longer see the eight old active workflow refs, but unresolved current guidance still requires disposition. Do not suppress remaining cutover blockers.
- The public QEAX archive remains unclassified. No owner approval to disclose source-model bytes has been recorded.
- All local contributor clones and PowerShell scripts still require sign-off; full integrated tests and actual Obsidian GUI first-open/edit/restart remain open.
- The superseding W authority decision is still proposed, not formally approved. Read-only archival of the standalone Workbench repo requires **separate owner authorization**.

**Next bounded step:** re-run the provenance-aware Step 10 preflight against the post-retirement actual tree, classify remaining unknown current-document references, then prepare an explicit promotion decision with QEAX and local-clone stop gates. Keep final merge/archival blocked.
