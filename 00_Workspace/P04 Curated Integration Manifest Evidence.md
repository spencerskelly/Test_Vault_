# P04 — Curated Integration Manifest: Executed Path Inventory

Date: 2026-10-13
Repository: spencerskelly/Test_Vault_
Current main: 19f565859e4b9fb7ae63004f1b6f0a7de1b9144e
Frozen Step22: 58ab10870f11757cf1bf367ecd5868be9b60933d
Status: REVIEW MANIFEST GENERATED LOCALLY; NO INCLUSION OR DELETION APPROVED.

## Actual artifact evidence

The user-supplied Step22_Integration_Inventory.zip was read locally. Its SHA-256 was `7fe98c8e89a4885720fda21cc1edd2a03849d83a4ddc1990de07b66739ad7435`. The `files.tsv` had 60,528 changed paths: 60,460 A, 47 M, 21 D.

Generated a six-column, 60,528-row CSV `Step22_Curated_Integration_Manifest.csv` with `git_status,path,review_class,proposed_active_tree,preservation,approval`. Its SHA-256: `21e4295fdc4b9e1b0cc01ad45c9e66907d9f6231f43080ffbeace9673587c87a`. The complete CSV was delivered as a downloadable chat artifact; it was NOT committed into GitHub.

| Review class | Paths |
|---|---:|
| REFERENCE_ARCHIVE_REVIEW (`55_Workbench/vault/`) | 60,033 |
| SOURCE_REVIEW | 147 |
| WORKBENCH_ASSET_REVIEW | 48 |
| TEST_REVIEW | 97 |
| DOC_REVIEW | 62 |
| GOVERNANCE_REVIEW | 53 |
| RUNTIME_RELEASE_REVIEW | 11 |
| CI_REVIEW | 26 |
| DOC_HISTORY_REVIEW | 50 |
| SECURITY_HOLD (historical QEAX ZIP) | 1 |
| TOTAL | 60,528 |

Classification rules are prefix-based: historical Workbench vault is review-only; QEAX ZIP is security hold; source candidates include importer and Workbench/src; tests include Workbench/test and 66_Testing; other Workbench files require asset review; schema, fileclass and Definitions require governance review; Base/.obsidian require runtime review; workflows CI review; Workspace/README doc review. **All 60,528 rows require review/approval**. All 21 D rows are `BLOCK_DELETE_PENDING_MIGRATION`. Every row identifies preservation of source commit history.

## Exact-source CI status

The new `.github/workflows/p03-legacy-compat-tests.yml` at `integration/p03-legacy-compat-tests-20261013` commit `28c3f3af3e3ecfbf371056ccd8f31f3059230e53` is present. The connected workflow-run API filters to PR-triggered runs and returned no runs, and the combined status API returned no entries. The public GitHub workflow page was inaccessible from this execution environment. Thus CI is **NOT VERIFIED**. Do not report a pass.

## Decision to unblock actual curated integration

1. Owner/security disposition: 60,033 Workbench vault paths and public historical QEAX material; no archive contents accessed.
2. Review 21 deleted definitions for legacy compatibility and approve migrations explicitly; P03 synthetic triage test branch is only diagnostic.
3. Review 47 modified files for semantic/runtime compatibility.
4. Approve exact active-tree inclusion set (not prefix guesses alone), verify source dependencies, and create one curated branch from fresh main **after** review. Do not merge 1,809 commits wholesale or silently copy historic vault data.
5. Run controlled build, importer smoke tests, Workbench tests and real GUI checks appropriate for touched runtime. Require explicit merge approval.
6. Consolidate into main, then retire ancestry-preserved branches with exact ref and local-work signoff; keep divergent histories until accounted for.

## Practical next action

Review the **195 Workbench/source asset** candidates (147 SOURCE_REVIEW and 48 WORKBENCH_ASSET_REVIEW) to separate required runtime/source/package dependencies from generated caches and snapshots. Do not create another branch until inclusion decisions are better established.

No branch merge/deletion, PR closure, source change, release promotion or Workbench archival occurred; only this audit document was added.
