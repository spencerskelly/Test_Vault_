# Branch Cleanup — Checkpoint BR-34: BOM and Workbench Historical Rehearsal Branches

**Date:** 2026-10-12
**Repository:** spencerskelly/Test_Vault_
**Candidate:** consolidation/step22-single-repo-cutover-2026-10-11
**Audit PR:** #41
**Status:** PARTIAL — branch-tip content verified; exclusive commit details remain open

## Git comparisons

| Source branch | Status | Branch-only commits | Candidate-only commits | Branch-side file |
|---|---|---:|---:|---|
| `integration/bom-a14-reconciliation-2026-10-09` | diverged | 2 | 128 | `.github/workflows/bom-a14-merge-rehearsal.yml` |
| `integration/workbench-monorepo-rehearsal-2026-10-09` | diverged | 1 | 1806 | `.github/workflows/workbench-monorepo-rehearsal.yml` |

Compare file lists for diverged branches are merge-base-relative and should not be interpreted as full tip-to-tip differences. Both named workflow paths were directly fetched on both refs.

## Exact verification

- BOM historical workflow: present source Git blob `cdee24fbcf33fea71f1fd297208f7467539cd5bb`; path absent (404) on Step22 tip. Source workflow is branch-scoped, manually dispatchable, `permissions: contents: read`, uses pinned imported WB-129 and BOM source SHA, and performs non-writing staging merger/test rehearsal.
- Workbench historical workflow: present source Git blob `253722a1273e9d0f30255e25299c7ec56c18684b`; path absent (404) on Step22 tip. Source workflow labels itself disposable CI proof, is branch-scoped, uses read-only `contents: read` permissions, and imports Workbench only in temporary GitHub runner checkout.

These workflows should **NOT** be copied back into active `.github/workflows`; external standalone Workbench references and old branch triggers are historical and incompatible with the single-authority CI direction.

## Current disposition

**HOLD** both remote branches until the two BOM-only and one Workbench-only commits have been enumerated and checked for intermediate behavior not visible in branch-tip comparisons, and CI artifacts/review threads are retained. No evidence from these workflow-only compare records alone establishes a missing current product runtime feature. Do not call either branch deletion-safe without local contributor, public QEAX security, PR review and owner signoffs.

Combined BR-33/34: all three divergent October 9 integration branches now have exact-path checks; the importer validator is already byte-identical on Step22 (BR-33), and the three historic-only workflows were confirmed absent from Step22.

## Handoff

STEP: BR-34
STATUS: PARTIAL — historical workflow preservation classified, unique commits pending
NEXT: BR-35 — resolve held-branch exclusive commit SHAs and meaningful changes via trusted Git log/tree audit, or investigate WB106 eight commits
NO ACTION: No merge, branch deletion, PR closure, workflow restoration, release promotion or standalone archive.
