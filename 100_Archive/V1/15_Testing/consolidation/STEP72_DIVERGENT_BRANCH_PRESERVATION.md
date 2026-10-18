# Step 72 — Divergent branch preservation audit (2026-10-14)

Status: **read-only comparison complete; all four branches remain on HOLD**. Compared each source branch against frozen `consolidation/step22-single-repo-cutover-2026-10-11` via GitHub compare, not merely dated ledger estimates.

| Branch | Candidate-only commits | Step22-only commits | Distinct changed paths observed | Action |
|---|---:|---:|---|---|
| `integration/bom-a14-reconciliation-2026-10-09` | 2 | 128 | `.github/workflows/bom-a14-merge-rehearsal.yml` | Preserve reproducible BOM rehearsal before retirement |
| `integration/importer-reconciliation-2026-10-09` | 6 | 644 | `.github/workflows/importer-monorepo-merge-rehearsal.yml`; `66_Testing/check_importer_workbench_localmodel.py` | Preserve substantive importer/Workbench compatibility check and rehearsal |
| `integration/workbench-monorepo-rehearsal-2026-10-09` | 1 | 1806 | `.github/workflows/workbench-monorepo-rehearsal.yml` | Preserve historical source migration CI provenance; decide whether active CI is redundant |
| `recovery/repository-consolidation-2026-10-09` | 19 | 1804 | 19 original `00_Workspace/GitHub Consolidation Step ...` handoff/history documents (file list in compare) | Retain historical documentation/provenance; reconcile with current records before archival |

These compare counts are branch-exclusive commit ancestry counts, **not** counts of unique functionality or inaccessible work. A file-path difference can be reproduced elsewhere; content equivalence has not yet been exhaustively shown. The compare's file list includes historical rename/change semantics and should not be treated as a complete current-tree manifest.

Representative source blobs inspected:
- BOM workflow `cdee24fbcf33fea71f1fd297208f7467539cd5bb`
- Importer compatibility checker `95c29b377ad8c7a0596e1c164db2e6bb66168b52`
- Workbench rehearsal workflow `253722a1273e9d0f30255e25299c7ec56c18684b`
- Recovery step18 handoff `81a4978e0ddbc01d5ac36a27a4dada499f05a632`, explicitly says manual Obsidian GUI **not run** in that historical evidence.

## Recommended reconciliation sequence

1. For each of the four branches, freeze exact tip SHA in a machine-generated register; compare its exclusive file blobs with current main, Step22, PR #41 and PR #43, with content-level identity and documentation links.
2. Classify each exclusive path as implemented elsewhere, historical-only and archival, still-needed executable gate, or superseded/unsafe automation. For the importer compatibility checker especially, do not mistake a new CI workflow for semantic-equivalent coverage without reading assertions.
3. Preserve any unmatched substantive file in a separately reviewed archive or implementation PR; retain permanent ancestry via an approved durable ref/tag where needed.
4. Reconfirm branch dependencies and obtain explicit owner approval for each branch SHA before deletion.
5. Never merge a historical CI rehearsal blindly; it has hardcoded old source SHAs and may trigger obsolete actions.

**No branch deletion, merge, tag, release, controlled artifact modification, QEAX conversion or model rewrite occurred.**

## Next Step 73

Inspect exact current tip SHA and cross-reference importer compatibility script versus current `66_Testing/` and CI gates; distinguish unique active function from archival-only provenance. Prepare a concrete per-path disposition matrix.
