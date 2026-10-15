# Step 15 — Owner Approval Proposal: One Repository, Main + Develop, Branch Reduction

Date: 2026-10-14
Repository: `spencerskelly/Test_Vault_`
Status: **PROPOSAL ONLY — no merge, deletion or release approval**

## Current confirmed snapshot
- **49 remote branches** (48 in earlier inventory plus new `integration/final-preservation-stage-20261014`).
- **19 open PRs**, including latest draft [#44](https://github.com/spencerskelly/Test_Vault_/pull/44). PRs #5–18 are earlier stacked chain; #39, #41–44 are later drafts.
- Exact staging commit: `7b78bf90d2d427bdbae9e3052b3e6c161a226902`. All eight jobs of [consolidated Actions run 38659103199](https://github.com/spencerskelly/Test_Vault_/actions/runs/38659103199) passed, and all nine workflows on that commit succeeded.
- Three main-only references restored in staging at identical Git blob IDs; primary consolidated CI triggers extended for staging + prospective main/develop.
- Stage remains pre-release and is **not** QEAX/GUI acceptance. Historic release artifacts and audit refs remain preserved.

## Desired sustainable Git structure
- `main`: protected approved engineering baseline, **not** a golden generated-model or MDSE release declaration.
- `develop`: protected working integration branch for new importer, Workbench, Bootstrap, schema and test improvements.
- Short-lived feature/fix branches with PR to `develop`, then reviewed PR to `main`; immutable tags for notable preserved historical refs; retain release branches only with justified support lifecycle.
- One authoritative code workspace: `Test_Vault_`; retired standalone repo may remain read-only reference after local unpublished-work clearance.

## Proposed promotion sequence (requires explicit owner authorization at merge/cleanup gates)
1. Freeze and record exact `main` and staging SHAs. Reconfirm current branch tip and protections; ensure `main` two distinct commits are integrated or their payloads preserved with documented provenance. The three Reference files are already blob-identical in staging; plugin configs appeared identical by content. **Do not force-push or reset main.**
2. Compare candidate to `main` as a proper reviewed PR; audit complete file set, generated/QEAX payload, binary risks, licensing/confidentiality, release manifests, checkout assumptions, and historical migrations. Since history is divergent, **PR #44 is a validation PR against Step22, not the direct promotion PR.**
3. Confirm the release-checker observations (not just job exit code), governance approvals, branch protections, test names, and sign-off. Explicitly choose whether outstanding real-QEAX/Obsidian GUI gates are required for the *development baseline*; they **remain mandatory before real-model/golden-vault or release signoff**.
4. On owner's separate approval: merge candidate to `main` using a history-preserving reviewed merge (never overwrite/force-push), rerun CI at final merge SHA; stop if validation regresses.
5. Create `develop` from the approved `main` commit; register required CI on both protected targets and run a smoke validation. Do **not** start new tool updates on obsolete integration branches.
6. Write permanent handoff / branch policy at an approved `main` path; if needed cherry-pick *only a curated summary* from audit PR #41, not all checkpoint documents.

## Open PR disposition proposal
| PR | Proposed disposition after approved integration | Condition |
|---|---|---|
| #44 staging validation | Preserve validation evidence; close as superseded by promotion PR | Only once main approval PR is reviewed / final history retained |
| #43 earlier P03 integration validation | Close superseded | Tests/history represented and checks recorded |
| #42 isolated lean CI | Close superseded, not independently merge | Needed test files checked in staged source, workflow differences reviewed |
| #41 180+ checkpoint audit | Curate decisions into accepted branch policy, preserve PR as audit; then close | Key decisions and links retained |
| #39 historical Step22 cutover | Close superseded | Cutover code/refs proven within accepted merged baseline |
| #5–18 stacked historical PRs | Batch-review references + content before closure | Preserve any unique work; don't equate 'old' with safe to discard |

**Closing a PR never deletes its head branch or historical commits by itself.** Avoid mass-closing until approved new baseline is accessible.

## Branch reduction in risk groups
- **Retain indefinitely initially**: `main`, new `develop`, staging until approved main merge, audit branch until curated, and all historically divergent refs until content disposition.
- **Low-risk candidate set**: the 34 pre-staging branches found to have zero ahead commits relative to the integration head; many `consolidation/step02`–`step22` and earlier importer/BOM/workbench steps. Before deleting: create immutable preservation refs where required, verify SHA/reachability and no active PR/open local work. The zero-ahead classification indicates *ancestry only*, not authorization.
- **Hold for individual preservation decision**: `recovery/repository-consolidation-2026-10-09`, `consolidate/test-vault-single-authority-20261012`, `wb106-release-integration`, `integration/lean-test-infrastructure-20261013`, three `base-vault-` releases, two `ci-probe-` branches, BOM and importer reconciliation, rehearsal and any newly changed branches. Their unique histories should be tagged or retained as archival refs until review and actual tool changes are captured.
- **Main must NEVER be treated as cleanup target**. `develop` does not exist yet and must not be implied to exist.
- Separate explicit owner approval for **each branch deletion batch**, with exact list, pinned commit ID, protected-ref check, contributor local unpublished-work check, PR dependency audit, and rollback path. Begin with small reversible batches and re-audit remote refs.

## Readiness and stop/go
GO (preparation): choose main/develop policy, create direct main promotion PR **when authorized**, gather review/security acceptance, CI on exact proposed promotion head; proposal may advance without production QEAX acceptance if clearly limited to engineering development.
NO-GO (currently): no owner authorization to merge to main or delete historical refs; no final post-merge checks; real-QEAX schema 0.5 regeneration and interactive UI acceptance not signed off.
This proposal does not change any branch except its audit-document checkpoint.
