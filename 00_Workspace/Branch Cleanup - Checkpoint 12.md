# Branch cleanup — checkpoint BR-12: WB-106 release integration branch

Date: 2026-10-12
Status: PARTIAL — net tree/version review complete; eight unique commits not individually enumerated
Source: `wb106-release-integration`
Candidate: `consolidation/step22-single-repo-cutover-2026-10-11`

## Live compare and inspected files

GitHub compare base=Step22, head=WB106 returned `diverged`, ahead=8 (WB106-only), behind=1952 (Step22-only). Seven net changed files:
- `.github/workflows/wb106-runtime-integration.yml` — added on WB106
- `.obsidian/plugin-lock.yaml` — modified
- `00_Workspace/00 - Current State.md` — modified
- `00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md` — modified
- `Base Vault/Definition/mdse-release.yaml` — modified
- `Base Vault/Runtime/Plugins/mdse-workbench/main.js` — modified
- `Base Vault/Runtime/Plugins/mdse-workbench/manifest.json` — modified

Fetched both versions of release manifest, plugin lock and Current State. Evidence:
- WB106 manifest blob `9793b4becbc19d138753549c86c37f4eb2b0d7b2`; Step22 manifest blob `6d06db25ed50ff390460c567b8fa769981aacc9e`.
- WB106 Workbench 0.1.17, importer candidate 0.8.6, relationships 1.35, element types 1.17, Local Model 0.2; standalone Workbench repo listed as authority.
- Step22 Workbench 0.1.18, importer candidate 0.8.19, relationships 1.36, element types 1.18, Local Model 0.5; Test_Vault_ listed as Workbench authority.
- Both release statuses are `pre-release`.
- WB106 plugin-lock Workbench 0.1.17; Step22 plugin-lock Workbench 0.1.18.
- Step22 Current State explicitly labels its October 9 integration as staging only, not released or GUI accepted.

## Preliminary disposition

**HOLD as historical release candidate. DO NOT BULK-MERGE into Step22.** The source tree carries older schema/runtime/pinning and would risk configuration regression. Preserve historical branch/workflow provenance pending individual commit review, PR disposition, local-work signoff and release approvals.

This pass does not establish that all eight unique commit effects are stale, nor that Step22 is acceptable for promotion to main.

## Handoff

STEP: BR-12
STATUS: PARTIAL — content-level source comparison and version differences verified; unique commit audit remains
SOURCE: GitHub compare and six branch-specific file fetches, 2026-10-12
OUTPUT: this checkpoint on PR #41
CHECK: WB106 ahead 8, Step22 ahead 1952, seven changed files, release pins verified
NEXT: BR-13 — reconcile unique commits and cleanup/PR retention gates in a bounded batch, beginning with WB106 commit identification or recovery branch
OPEN: all unique-commit identities/diffs, PR closures, local branches/worktrees/stashes, security, document control, GUI acceptance.
