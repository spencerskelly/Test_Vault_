# Branch Cleanup — Checkpoint BR-25: Decision-Ready Retirement Plan

**Date:** 2026-10-12  
**Repository:** `spencerskelly/Test_Vault_`  
**Engineering candidate:** `consolidation/step22-single-repo-cutover-2026-10-11` (PR #39)  
**Cleanup audit:** `consolidate/test-vault-single-authority-20261012` (PR #41)  
**State:** PLANNED / ALL DESTRUCTIVE ACTIONS BLOCKED — this document does not authorize any merges, PR closures, force pushes, branch deletions, or standalone-repository archival.

## 1. Verified scope and audit provenance

The BR-01–BR-24 sequence inventoried **46 Test_Vault_ remote branches**, checked ancestry and selected branch content, and triaged **all 36 open PRs** (#5–#39 and #41). The PR review is a classification, **not** a completed check of requested reviews, unresolved inline threads, local unpushed work, or current CI status.

**Critical correction:** The 15 historical consolidation handoffs initially described as missing in BR-14–BR-18 are in fact **all present on the Step22 tree with source-identical Git blob SHAs**, confirmed by direct per-file fetch in BR-19. Do **not** attempt duplicate recovery or use divergent Git compare's merge-base-relative changed-file list as proof of target-tip absence. BR-15's attempted copy was blocked, but no source evidence was lost.

## 2. Proposed branch batches — non-destructive first

| Batch | Branch class | Count | Decision | Required evidence before any removal |
|---|---|---:|---|---|
| B0 | `main`, Step22 candidate, BR audit branch | 3 | **KEEP** | `main` protected; PR #39 retained as pre-release; #41 retained through ledger integration |
| B1 | Earlier consolidation branches whose tips are ancestors of Step22 | 21 | **RETIRE CANDIDATE** | Recheck exact tip ancestor status against frozen candidate; map PR and linked CI/reviews; contributor local signoff; owner approval |
| B2 | Integration branches whose tips are ancestors of Step22 | 9 | **RETIRE CANDIDATE** | Same requirements; preserve diagnostic and source/test provenance |
| B3 | Earlier importer/Workbench dashboard branches whose tips are ancestors of Step22 | 3 | **RETIRE CANDIDATE** | Same requirements; verify source/head and importer/Workbench reference integrity |
| B4 | Temporary Bootstrap probe branches | 2 | **RETIRE CANDIDATE** | Explicit temporary-do-not-merge evidence BR-16; verify probe workflow/logs and no needed unpublished work |
| B5 | Diverged integration branches (BOM A14, importer reconciliation, Workbench rehearsal) | 3 | **HOLD** | Enumerate 2 / 6 / 1 exclusive commits, compare exact source content against Step22, preserve unique tests/evidence |
| B6 | Diverged recovery consolidation branch | 1 | **HOLD pending commit audit** | 15/15 handoffs already byte-identical on Step22; still enumerate 19 exclusive commits and ensure no unmatched intermediate state |
| B7 | Historical Base Vault branches | 3 | **HOLD** | Each has 1 exclusive commit; compare untruncated trees and commit diffs, document template preservation |
| B8 | Historical WB106 release branch | 1 | **HOLD** | Enumerate 8 exclusive commits; old 0.1.17 manifest and write-enabled CI must NOT be reactivated |

**Accounting:** 3 KEEP + 33 ancestry-preserved candidates + 2 probe candidates + 8 held/diverged = **46**. The 35 candidate branches are *not* approved for deletion. The held eight = 3 integration + 1 recovery + 3 Base Vault + 1 WB106.

## 3. PR batch triage / closure order

All **36 PRs remain OPEN** as of the BR-24 check; no submitted review records were returned by the review endpoint. This does not establish absence of comments, pending reviewers, or failing checks.

| PR group | Count | Proposed next handling |
|---|---:|---|
| #5–#11 | 7 | Preserve importer/Workbench lineage and negative/positive compatibility evidence; review supersession against #39 |
| #12–#18 | 7 | Preserve BOM original provenance and QEAX tests; **hold** schema proposal #16 and manual Obsidian GUI acceptance #18 |
| #19–#25 | 7 | Historical handoffs verified 15/15; **hold** QEAX security #22 and actual workstation signoff #23 |
| #26–#32 | 7 | Preserve eight byte-identical archived CI workflows and source-reference regression tests; W governance proposal #32 unapproved |
| #33–#39 | 7 | Preserve release-check/guide/plugin parity; document registry only staged, GUI not run, **keep #39** |
| #41 | 1 | Keep cleanup audit PR until findings, this correction and successor branch decision are accepted |

**Suggested individual closure procedure:** Confirm exact head/base and successor commit, review comments/threads and reviewer requests, preserve CI/artifact/decision links, confirm owner's closure approval, then close a single superseded PR with a comment linking PR #39 and the evidence checkpoint. Recheck remaining PR stack and branches after each action. Never close PR #39 or #41 as routine housekeeping.

**Do not merge all old draft PRs into `main` simply to clear the queue.** A draft that is superseded may be closed *without merge* only after its specific acceptance/evidence and PR dependency checks pass.

## 4. Release, security and deletion gates (ALL still OPEN unless separately signed)

- **S1 Public QEAX archive:** Authorized owner must classify the reported ~73 MB `EA_2026_09_06_endgame.qeax.zip` in public staging history and determine any exposure response. Branch deletion does not erase historical access; do not reproduce archive contents in public cleanup notes.
- **S2 Local work:** Each contributor checks unpushed refs, dirty worktrees, stashes and local-only histories privately. Audit scripts do not supply remote freshness or automatic workstation signoff; PowerShell runtime validation remains needed.
- **S3 Governance:** Source authority W supersession and 32 staged document registry entries (29 reference / 3 proposal) require owner approval. The 12-gate governance register from PR #32 remained NOT_APPROVED.
- **S4 Artifact/CI:** On the actual promotion tip rerun release checker, exact pinned lock and generated Base checks, importer/Workbench/Bootstrap integration, real-QEAX regression and fail-closed safety/negative tests. Earlier green staging CI is not a new release approval.
- **S5 Observed GUI:** Mac and Windows real Obsidian first-open, author setup, Workbench structured edit, save/restart, interfaces/connections/where-used and representative imported-model GUI checks need actual operator evidence. Synthetic 16-case kit and Step21 session preparation are NOT observed PASS.
- **S6 PR/repository review:** Obtain required code/document-owner reviews, resolve in-line threads/checks and confirm retention of old standalone Workbench branch/PR/source evidence. Standalone repository archival requires separate explicit approval; prefer reversible read-only archive, **not deletion**.
- **S7 Branch removal approval:** After all relevant gates, a reviewer signs the exact deletion batch/list and frozen source hashes. Delete in **small batches**, verifying remote ref listing and rollback/tag preservation between batches.

## 5. Next safe executable checks (no destructive work)

1. **BR-26**: Recheck B1/B2/B3 exact branch tips and their mapped PR head/base metadata; prepare first **small, signed, not-yet-executed** retirement batch.
2. **BR-27**: Establish commit-level evidence for all eight held/diverged branches with `git log --oneline step22..branch` in a trusted clone, including tip SHA, diff and retained successor path; do not infer preservation from merge-base-relative file listings.
3. **BR-28**: Record owner actions for S1 and S2 as private signoffs (never paste sensitive QEAX or private local paths).
4. **BR-29**: Validate PR #39 latest CI and build/GUI acceptance evidence, with no premature release declaration.
5. **BR-30**: Issue final PR/branch decision register for approval; destructive cleanup only after separate, explicit signoff.

## 6. Stop/handoff

**BR-25 outcome:** Decision-ready non-destructive plan; **0 PRs closed, 0 branches merged, 0 branches deleted** by this step.  
**NEXT:** BR-26, bounded first candidate retirement batch evidence.  
**Override rule:** This plan supersedes the BR-14–BR-18 incorrect document-absence claim; BR-19's 15/15 exact-path blob verification controls.
