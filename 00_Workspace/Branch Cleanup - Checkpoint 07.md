# Branch cleanup — checkpoint BR-07: BOM A14 reconciliation divergence

Date: 2026-10-12
Status: PARTIAL — net tree analyzed, individual two exclusive commits not yet enumerated
Reference branch: `integration/bom-a14-reconciliation-2026-10-09`
Candidate branch: `consolidation/step22-single-repo-cutover-2026-10-11`

## Live comparison

Compare base=Step 22, head=BOM A14 returned `diverged`, ahead=2, behind=128, and exactly one reported net file difference:
- Added on BOM A14 branch: `.github/workflows/bom-a14-merge-rehearsal.yml` (115 changed lines)

This is a *net tree comparison*, not evidence that both distinct commits were individually read. Commit IDs/parent graph still need enumeration. Avoid treating 2 commits as 2 missing functions.

## Source inspection

Fetched branch file (blob SHA `cdee24fbcf33fea71f1fd297208f7467539cd5bb`), GitHub path:
`https://github.com/spencerskelly/Test_Vault_/blob/integration/bom-a14-reconciliation-2026-10-09/.github/workflows/bom-a14-merge-rehearsal.yml`

Workflow:
- Triggers on the historical integration branch and manual dispatch; read-only GitHub permissions.
- Pins staged source, BOM and WB129 SHA values and fetches `spencerskelly/MDSE_Workbench.git` branch `proposal/bom-a14-readonly-quantity-uom`.
- Rehearses `git subtree pull --prefix=55_Workbench` in CI runner and records conflict files, localmodel diff and status.
- On clean merge, checks Local Model 0.5 write / 0.6 read presence, runs BOM focused regression tests and other npm tests, uses an ephemeral test-only schema-version edit, then builds.
- Requires `55_Workbench/docs/bom/a01-a14/BOM_SOURCE_MANIFEST.json` to be present to consider promotion successful.

## Preliminary policy disposition

**DO NOT PROMOTE** this historical branch-specific workflow into a self-contained Test_Vault_ runtime, because it requires fetching the standalone Workbench repository. It may remain accessible in Git history and branch/PR records. Preserve its diagnostic rationale in this checkpoint. A future in-repo-only BOM regression test should be developed against approved source rather than resurrecting the external fetch.

**HOLD branch deletion:** confirm the 2 exclusive commit identities, compare any intermediate commit effects, map PR and approvals, and verify immutable preservation of the diagnostic source if policy requires it. The fact that the Step 22 tree lacks the workflow is not by itself evidence of lost production functionality.

## Handoff
STEP: BR-07
STATUS: PARTIAL — tree impact inspected; exclusive commits still require enumeration
SOURCE: GitHub compare, fetched workflow at blob cdee24fbcf33fea71f1fd297208f7467539cd5bb
OUTPUT: this file on PR #41
CHECK: 2 commits ahead of Step 22, 128 behind, 1 net added file
NEXT: BR-08 — enumerate BOM branch-exclusive commits and review the 6 importer-reconciliation branch-only commits in bounded batches
BLOCKERS: no merge/deletion until content, PR closure, local-work, security and governance checks conclude.
