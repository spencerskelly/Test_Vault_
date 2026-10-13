# Lean Integration — Path Classification Baseline (P02)

Date: 2026-10-13
Source: uploaded Step22_Integration_Inventory.zip, `files.tsv` (complete 60,528 rows).
Status: RULE-BASED CLASSIFICATION COMPLETE; SEMANTIC ACCEPTANCE AND SECURITY OWNER REVIEW PENDING.
This file is a selection strategy, NOT permission to delete/move any data.

## Aggregate classification

| Preliminary disposition | Changed paths | A | M | D | Treatment |
|---|---:|---:|---:|---:|---|
| REFERENCE_ARCHIVE | 60,033 | 60,033 | 0 | 0 | Historical Workbench vault; exclude from new active-tree candidate until data owner classifies; never delete committed history |
| SECURITY_HOLD | 1 | 1 | 0 | 0 | QEAX ZIP historical exposure; stop public promotion pending authorized security decision |
| ACTIVE_SOURCE_CANDIDATE | 195 | 193 | 2 | 0 | Review code/build/importer source before selective integration |
| ACTIVE_TEST_CANDIDATE | 97 | 97 | 0 | 0 | Include relevant product/importer test tools after dependencies review |
| ACTIVE_DOC_CANDIDATE | 62 | 62 | 0 | 0 | Workbench docs requiring relevance review |
| GOVERNANCE_REVIEW | 53 | 7 | 25 | 21 | Explicit compatibility decisions; all 21 deletions held |
| RUNTIME_RELEASE_REVIEW | 11 | 0 | 11 | 0 | Manifest/locked plugins/base defaults require exact equality and checker run |
| CI_REVIEW | 26 | 26 | 0 | 0 | Check workflow permissions/retired dangerous jobs |
| DOCUMENT_REVIEW | 50 | 41 | 9 | 0 | Workspace evidence versus durable active docs |
| **TOTAL** | **60,528** | **60,460** | **47** | **21** | Every path assigned exactly once |

Rules executed in first-match order (a path prefix match; exact files used for QEAX and root README):
1. SECURITY_HOLD exact `EA_2026_09_06_endgame.qeax.zip`.
2. REFERENCE_ARCHIVE prefix `55_Workbench/vault/`.
3. ACTIVE_SOURCE_CANDIDATE prefix `55_Workbench/src/`.
4. ACTIVE_TEST_CANDIDATE prefix `55_Workbench/test/`.
5. ACTIVE_DOC_CANDIDATE prefix `55_Workbench/docs/`.
6. ACTIVE_SOURCE_CANDIDATE remainder prefix `55_Workbench/`.
7. ACTIVE_SOURCE_CANDIDATE prefix `Importer/`.
8. ACTIVE_TEST_CANDIDATE prefix `66_Testing/`.
9. GOVERNANCE_REVIEW prefix `99_System/` and `Definitions/`.
10. RUNTIME_RELEASE_REVIEW prefix `Base Vault/` and `.obsidian/`.
11. CI_REVIEW prefix `.github/`.
12. DOCUMENT_REVIEW prefix `00_Workspace/` and exact `README.md`.

Zero unclassified paths. These are **candidate groups, not an authoritative inclusion allowlist**. In particular, `55_Workbench/` has additional assets potentially sensitive or generated; their review is necessary. Excluding `55_Workbench/vault/` from a *new active-tree proposal* does not modify Step22, eliminate historical blobs, or decide retention.

## Decisions to make before creating lean integration branch

- Data owner classifies `55_Workbench/vault/` as reference/archive vs authoritative data; record location, ACL and retention in owner-controlled evidence.
- Security owner decides handling of historical QEAX ZIP; do not inspect archive or move it blindly.
- Review all 68 modified/deleted paths, mapping every semantic deletion to accepted replacement and regression test.
- Run source/runtime Build, Workbench, importer and governance checks using a clean, isolated proposed lean tree.
- Obtain owner approval for explicit path allowlist and exact source/target SHAs before adding files to new branch.
- Preserve all Step22 history and divergent refs during migration.

## Next: P03 semantic deletion review

Review 21 deleted paths (12 templates/fileclasses and 9 property definitions), then 47 modified paths against their replacements. Publish a path-by-path verdict matrix with `PRESERVE`, `MIGRATE`, `REMOVE_AFTER_TEST`, `HOLD` and source evidence. Do not delete anything until qualified.
