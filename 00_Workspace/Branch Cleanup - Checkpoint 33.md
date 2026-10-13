# Branch Cleanup — Checkpoint BR-33: Divergent Importer Reconciliation Verification

**Date:** 2026-10-12
**Repo:** spencerskelly/Test_Vault_
**Candidate:** consolidation/step22-single-repo-cutover-2026-10-11
**Historical branch:** integration/importer-reconciliation-2026-10-09
**Audit PR:** #41
**State:** PARTIAL — exact-path content verified, exclusive-commit enumeration open

## GitHub comparison

Comparison from Step22 candidate to historical branch returns `diverged`, historical ahead **6**, candidate ahead **644**. GitHub's branch-side comparison reports two files:
- `66_Testing/check_importer_workbench_localmodel.py`
- `.github/workflows/importer-monorepo-merge-rehearsal.yml`

**Methodology:** For diverged refs the compare file list describes branch-side diff from merge base, not necessarily the tip-to-tip file absence or differences. Direct fetches below override absence assumptions.

## Exact file preservation

| File | Historical branch | Step22 tip | Decision |
|---|---|---|---|
| `66_Testing/check_importer_workbench_localmodel.py` | Present Git blob `95c29b377ad8c7a0596e1c164db2e6bb66168b52` | Present **same Git blob** `95c29b377ad8c7a0596e1c164db2e6bb66168b52` | VERIFIED preserved byte-for-byte |
| `.github/workflows/importer-monorepo-merge-rehearsal.yml` | Present Git blob `612cc78ee5c839def7dae9b343ef9c2f8dd9b8d2` | Path absent (404) | Historical workflow evidence only; do not promote into live CI |

The legacy workflow identifies itself as a non-writing importer-to-monorepo rehearsal; it is branch-scoped and has a manual trigger. Avoid recreating/re-enabling historical CI to clear branch cleanup.

## Disposition and stop

- Keep the historical branch for now. The 6 branch-only commits have not been individually enumerated or semantically audited.
- Retain CI run links and workflow blob ref as historical evidence. The exact validator source is already present on the Step22 tip.
- No claim of clean deletion readiness until unique intermediate commits and linked PR review/comments, contributor local work, QEAX public-history security classification and release governance are addressed.
- No copy, merge, closure, branch deletion or release promotion performed.

## Handoff
STEP: BR-33
STATUS: PARTIAL; exact current validator preserved; workflow historical
NEXT: BR-34 — check the diverged BOM A14 and Workbench rehearsal branches with direct tip-to-tip file fetches; review individual unique commits using trusted Git clone before any retirement.
