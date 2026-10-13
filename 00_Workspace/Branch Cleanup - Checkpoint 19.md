# Branch cleanup — checkpoint BR-19: PR inventory and critical recovery correction

Date: 2026-10-12
Status: PASS — inventory + exact recovery blob verification, NO PR closure/merge/deletion
Repo: spencerskelly/Test_Vault_
Candidate: `consolidation/step22-single-repo-cutover-2026-10-11`
Audit: PR #41

## Critical correction to BR-14 through BR-18

Earlier branch compare output suggested 15 recovery Markdown documents were absent from Step22. **That conclusion was wrong.** A direct GitHub file fetch of each of the 15 exact `00_Workspace/GitHub Consolidation Step 04B..18.. 2026-10-09.md` paths on Step22 returned all 15, and **all 15 destination Git blob SHA values exactly matched** the originals fetched from `recovery/repository-consolidation-2026-10-09` during BR-15.

This is a critical verified correction. BR-15's file copying failure did **not** lose any documents; it was unnecessary for the Step22 candidate because the documents were already there. No copying was performed by this step. Do not leave the previous “15 files missing from Step22” assertion uncorrected in future retention decisions.

Exact source/candidate SHA manifest:
| Step document | Verified Git blob SHA | On Step22 |
|---|---|---|
| 04B Persisted Workbench Import | 7c3dc3a51495d5e9edbb2bd60f58f5de106ae2eb | MATCH |
| 05 Release Contract and Path Audit | 774d3959507a8684533f2717f16d244c5a4efcab | MATCH |
| 06 Importer Workbench Compatibility | cf7d17034f2ed32b29e59bd5bd67bfeaa84cc626 | MATCH |
| 07 WB129 Local Model 05 Staging | 531531f475c106efb5e1617edf8626bbf83f0847 | MATCH |
| 08 Importer WB129 Acceptance | 2db622f6bfb6f5cb81fb627674d7553dc20fb68c | MATCH |
| 09 Persisted Importer WB129 | 268071d83c800577924bbe92056a9fb6d330904d | MATCH |
| 10 Release Registry and Fixture | c18cc684ff41d4460fdee18d55361900988f24c4 | MATCH |
| 11 BOM Reconciliation | 854872ddf504e7252ca70d0d90bd0a52f78d68e3 | MATCH |
| 12 BOM Artifacts Recovery | ed276a95778ca3f70da469870d98567b3eff0d21 | MATCH |
| 13 Original BOM Archive Verification | 63a401913fcfc10758f7a04550d993ac8decb0ee | MATCH |
| 14 BOM Original Git Integrity Complete | 51cd4cdf6cb7f443ae4751f1d4ab233bb2a325ed | MATCH |
| 15 BOM Staged Source Integration | 85f6e0d0db3d90eb8744f90b71ff6641611224db | MATCH |
| 16 BOM Schema Governance Proposals | a73dc7707cbe03d1e554db16ea00f7bad661a09e | MATCH |
| 17 Post-BOM Real QEAX | 566a380eb3bac153be31787f611e5764daa8eaaf | MATCH |
| 18 Obsidian UI Acceptance Handoff | 81a4978e0ddbc01d5ac36a27a4dada499f05a632 | MATCH |

## Live PR inventory

GitHub open-PR search returned 36 open PRs: #5–#39 (35) plus #41 (one). Two broad sequences:
- #5–#18: initial importer/Workbench/BOM feature history and acceptance, to reconcile with later staging.
- #19–#39: recovery and sequential single-authority consolidation, including #19's explicit preserved handoffs and #39's Step22 cutover candidate.
- #41: active branch cleanup and audit documentation; do not close until accepted records and this correction are integrated.

## Proposed non-destructive sequence

1. Confirm PR #19’s provenance and file hashes (Step22 content parity is now verified).
2. Keep PR #39 as the consolidation candidate; block promotion to main until appropriate permissions, data security, document registry, CI, local work, and manual Obsidian tests pass.
3. Review superseded PRs in small dependency-aware batches. Classify per PR as historical/superseded, independently required, or blocker. Preserve links to accepted successor commits and comments. Do not close/merge any PR in this pass.
4. Correct preceding BR14–BR18 status in the final decision ledger; their exploratory net comparison should not override exact-path file fetches.
5. Revisit whether other “net additions” from diff endpoints really are absent from Step22 by exact blob fetch before determining missing code.
6. Confirm unpushed contributor work/worktrees/stashes and unique branch-exclusive commits before *any* branch deletion.

## Handoff
STEP: BR-19
STATUS: PASS — critical preservation verification and PR count
CHECK: 15/15 historical documents exist byte-identically on Step22, 36 open PRs identified
NEXT: BR-20 — classify PR #5–#18 or #19–#25 in first bounded PR review batch, and confirm base/head and review gates using PR details
OPEN: PR metadata and reviewer statuses, full unique-commit reconciliation, main promotion gates
