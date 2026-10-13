# Branch Cleanup — Checkpoint 18: Retention and PR Decision Ledger

Date: 2026-10-12
Status: DECISION DRAFT — NO deletion, merge, PR closure or promotion authorized
Repository: spencerskelly/Test_Vault_
Candidate engineering history: `consolidation/step22-single-repo-cutover-2026-10-11`
Temporary audit documentation: `consolidate/test-vault-single-authority-20261012` (PR #41)

## Inventory reconciliation (46 remote branches in original audit)
| Category | Count | Disposition | Required gate |
|---|---:|---|---|
| `main` | 1 | KEEP protected | Never rewrite by cleanup |
| Step22 consolidation candidate | 1 | KEEP as staging candidate | All release, governance, PR and GUI gates before promotion |
| Earlier consolidation branches | 21 | RETIRE CANDIDATES | BR-02–04 prove every tip ancestor of Step22; still close/reconcile PRs and local work |
| Integration branches included in Step22 | 9 | RETIRE CANDIDATES | BR-05–06 verify ancestor tip; PR/local work and evidence checks |
| Older importer and Workbench dashboard branches included in Step22 | 3 | RETIRE CANDIDATES | BR-10–11 prove ancestry; PR/local work checks |
| Diverged integration branches | 3 | HOLD | BOM A14 rehearsal (2 branch-only commits); importer reconciliation (6); Workbench rehearsal (1); full exclusive-commit review and retention |
| Recovery consolidation branch | 1 | **PROTECT: SOURCE-ONLY DOCUMENTS** | 15 historical MD docs absent in Step22, identified BR-14; BR-15 copy blocked |
| Legacy Base Vault snapshots | 3 | HOLD | Each 1 exclusive commit; full content/retention audit needed (BR-17) |
| Temporary Bootstrap CI-probe branches | 2 | RETIRE CANDIDATES after evidence review | Branch-only 3 and 1 commits; probe notes explicitly say do not merge (BR-16) |
| Historical WB106 release branch | 1 | HOLD | 8 branch-only commits; older 0.1.17/Local Model 0.2 configuration, write-enabled CI (BR-12–13) |
| BR audit branch (PR #41) | 1 | KEEP TEMPORARILY | Move accepted plan/audit evidence into approved history, then close |
| **Total** | **46** | | |

**Ancestry-preserved earlier branches: 33 = 21 consolidation + 9 integration + 2 importer + 1 Workbench dashboard.** Step22 itself is not counted in 33. This is a statement about committed Git ancestry, not authorization to delete.

## Critical blocker — recovery documentation
BR-14 identified 15 additional `00_Workspace/GitHub Consolidation Step 04B…18…` Markdown records on `recovery/repository-consolidation-2026-10-09`. Source SHA manifest and read evidence are in BR-14 and the attempted BR-15 session. BR-15 fetched all 15 originals, but the direct GitHub content-write call was safety-blocked; **0 of 15 copies verified and no BR-15 checkpoint committed**. Preserve the recovery branch exactly as-is. Approved local procedure: restore exact files into a clean separate feature worktree, verify each `git hash-object` against source Git blob SHA, commit as historical/reference documents, register them with doc-control, re-fetch destination SHAs, then review and integrate by PR. Do not claim recovery complete until 15/15 verified at destination.

## PR and branch cleanup policy
1. **Freeze destructive work.** No bulk branch deletion, force pushes, remote renames, automatic PR closure, or unreviewed merge.
2. Inspect open PR mapping for each candidate; preserve reviews, comments and linked Actions evidence. Record PR disposition: merged / superseded-closed / remains-open and linked replacement.
3. Enumerate unique commits for held branches with `git log --oneline candidate..source`; for capped compare results use a trusted local clone `git diff --name-status candidate source`. Record exact commit SHAs, content effects and preservation/intent.
4. Require contributor review of local unpushed commits, worktrees, stashes and detached heads; GitHub remote comparisons cannot reveal them.
5. Maintain security policy for model/QEAX source and sensitive files; do not accidentally publish private files during document/history consolidation.
6. Resolve document registry governance and release pins, ensure importer+Workbench schema alignment, complete controlled Base first-open and interactive Obsidian/real-QEAX acceptance. Step22 remains pre-release.
7. Move the approved audit/retention ledger from PR #41 into surviving authority branch; do not keep two competing documentation authorities.
8. Only then propose a small reviewed deletion batch; verify archive/ref preservation, PR disposition and remote listing after each batch.

## Proposed steady state
Aim for `main` (approved), a single `develop` or equivalent integration branch **only if actual workflow needs it**, `test` only if independent staging tests need a persistent branch, and short-lived topic branches. These are target policies, NOT existing branches created by this audit. Favor fewer persistent branches and PR-controlled feature development.

## Next bounded checkpoints
- BR-19: inspect PR mapping/status and formulate non-destructive close/retire candidate batches; record safe PR dependency chains.
- BR-20: recover the 15 historical files using authorized local Git mechanism and SHA verification, before any recovery branch retirement.
- BR-21+: individual exclusive-commit review for WB106, BOM/importer/rehearsal, Base Vault/CI and final local-work/security acceptance.
- Promotion and deletion are separate approvals and must not be conflated.

Handoff: BR-18 ledger recorded; no merges/deletions.
