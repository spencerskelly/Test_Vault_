# Branch Cleanup — Checkpoint BR-52: Recovery and Historical Base Vault Hold Review

**Date:** 2026-10-12
**Repository:** spencerskelly/Test_Vault_
**Audit PR:** #41
**Candidate:** consolidation/step22-single-repo-cutover-2026-10-11 @ 58ab10870f11757cf1bf367ecd5868be9b60933d
**Status:** Diverged refs remain HOLD; no deletions authorized

## Live branch discovery and comparisons

Names independently rediscovered through GitHub branch search: `recovery/repository-consolidation-2026-10-09`, `base-vault-2026-09-30-rel132-v04`, `base-vault-2026-09-30-rel133-v05`, `base-vault-2026-09-30-rel133-v051`.

| Historical ref | Compare status | Ref-only commits | Candidate-only commits | Merge base |
|---|---|---:|---:|---|
| recovery/repository-consolidation-2026-10-09 | diverged | 19 | 1804 | 61633d0ea66c06928d4e457dff8d9550096164eb |
| base-vault-2026-09-30-rel132-v04 | diverged | 1 | 2242 | 230a7846ca115971b9b46326229b547cde604607 |
| base-vault-2026-09-30-rel133-v05 | diverged | 1 | 2232 | 0978773fd3db77b76cf0e822b6dc6016b1ee8a43 |
| base-vault-2026-09-30-rel133-v051 | diverged | 1 | 2225 | 3e7d696b75793dbf46f09f573ab8c3ca7f4dfc70 |

Total of **22 branch-exclusive commits** in these four held refs, plus 17 in the four held refs investigated in BR-39 => **39 exclusive commits in eight held refs** based on current counts. This does not prove 39 unique commit *SHA identities* across branches; overlaps have not been checked, and none of these exclusive commits has been individually classified in this step.

## Exact-file checks (tip-to-tip, not merge-base assumption)

- Recovery comparison listed 15 historical handoff files as branch-added relative to common ancestor. BR-19 had previously verified all 15 exact files are already present on Step22 with byte-identical Git blob SHAs. This step independently spot-checked:
  `00_Workspace/GitHub Consolidation Step 18 Obsidian UI Acceptance Handoff 2026-10-09.md`: both recovery and candidate tips have Git blob `81a4978e0ddbc01d5ac36a27a4dada499f05a632`.
  Thus *a changed-file listing for divergent refs does not imply missing tip files*. No duplicate recovery copy justified.
- All three BaseVault historical refs contain `.vault.yaml` Git blob `9f02c8ea09e187c0f44cfc768d6d97ed6a37867b`, declaring `vault_uid: UNINITIALIZED` / `name: MDSE_Base_Vault` / `default_branch: main`.
- Step22 `.vault.yaml` uses distinct Git blob `5f96bb033a59e97ba4de19387343a64b2c8ac35f` and initialized `Test_Vault_` identity. Do **not** replace it with historic uninitialized Base metadata.
- GitHub comparison response for the BaseVault branches returned `files.length=300` each. Treat this as a possible comparison response cap, **not** evidence of a complete 300-file diff or missing hundreds of files in the current candidate.

## What remains unresolved

1. Enumerate exact SHA, parent, changed paths and purpose of 19 recovery-only commits and the one exclusive commit per BaseVault snapshot via trusted `git log Step22..ref`. Avoid loss or blind cherry-pick.
2. For each BaseVault snapshot, inspect actual full branch tips/trees rather than truncated merge-base-relative comparison and decide whether it is a historical generated clean-Base artifact worth retaining as an immutable tagged reference.
3. Preserve historical snapshot/provenance via approved retention process; confirm published-only state and contributor local signoff.
4. Apply independent S1 QEAX confidentiality, S2 local work, S3 governance, S4 release, S5 observed GUI, S6 PR review and S7 batch deletion approvals before changing remote refs.

## Safe exact-history verification

On an authorized, clean local checkout with remote refs current, separately list exact commits using `git log --format='%H %P | %s' origin/consolidation/step22-single-repo-cutover-2026-10-11..origin/recovery/repository-consolidation-2026-10-09` and the same expression for each of the three `base-vault-2026-09-30-*` refs. For branch *tree* comparison use `git ls-tree -r -z` with explicit pinned refs or `git diff --name-status <exact-candidate-sha> <exact-snapshot-sha>` and review in a private, controlled workspace. Full SHA identities and binary/file privacy must be reviewed before any public report. Do not stage model files into the public audit branch.

## Handoff
**BR-52 completed:** Confirmed all four held branch names, refreshed exact ancestry counts, verified one recovery document's identical content, and verified historical BaseVault UID differences. Recorded the large comparison-list limit honestly.
**NEXT BR-53:** Produce the minimum decision-ready preservation/classification matrix for all eight held refs (without pretending individual commits are examined), or retrieve exact commit SHAs using approved Git logs once available.
**No action:** No PR closure, branch deletion, merge, archive, release promotion or QEAX content access.
