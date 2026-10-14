# Final Consolidation — Step 5 Unique Change Disposition

Date: 2026-10-14. Compare base `integration/p03-legacy-compat-tests-20261013`.

## Verified GitHub comparisons
1. `integration/bom-a14-reconciliation-2026-10-09`: 2 commits ahead, 261 behind; one net unique path: `.github/workflows/bom-a14-merge-rehearsal.yml`. Workflow is branch-specific historical non-writing rehearsal, fetching a pinned old Workbench BOM proposal. **Preserve as evidence; do not blindly enable in new development branch.**
2. `integration/importer-reconciliation-2026-10-09`: 6 ahead, 777 behind; two net unique paths: `.github/workflows/importer-monorepo-merge-rehearsal.yml` and `66_Testing/check_importer_workbench_localmodel.py`. Despite compare showing checker added relative to an older common ancestor, direct fetch verified the checker already exists in the candidate. Workflow is pinned to old merger refs; preserve history without activating obsolete CI.
3. `main`: 2 ahead, 1942 behind; net comparison shows `.obsidian/community-plugins.json`, `.obsidian/core-plugins.json`, plus `Reference/SysML v2 integration.md`, `Reference/resolve.md`, `Reference/separation.md`. Direct fetch of the two plugin configurations from main and candidate showed matching displayed contents; inspect exact blob equality at promotion. All three reference Markdown files are **absent** on candidate (404) and should be copied from main to the new integration staging branch without overriding main or modifying source.
4. Main's two unique commits must be reconciled or explicitly documented. File diffs alone do not prove ancestry reconciliation.

## Promotion blockers / next task
- Stage the three missing Reference documents on a new preservation branch from the current candidate, with provenance to main; maintain file paths unchanged.
- Do not activate stale branch-targeted workflows. Save their tip refs/tags or audit evidence before approved retirement.
- Run exact-head CI after staging and review old check dependencies.
- No merge, delete, main change, release approval, or real QEAX signoff implied.
