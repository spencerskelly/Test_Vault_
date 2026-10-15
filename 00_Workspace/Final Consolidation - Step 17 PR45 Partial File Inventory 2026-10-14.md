# Final Consolidation — Step 17 PR45 Scope and Risk Inventory (Bounded)

Date: 2026-10-14
Review target: draft PR https://github.com/spencerskelly/Test_Vault_/pull/45
Head `7b78bf90d2d427bdbae9e3052b3e6c161a226902`.

## Correct scope statement
GitHub reports **60,611 changed files** in PR45. The paginated connector filename-list operation returned **only the first 3,000 paths**, not all 60,611. The compare API returns at most 300 file stats. Therefore **the review is 3,000/60,611 (4.95%) path coverage only**, a nonrepresentative lexically ordered sample. Never extrapolate counts to the whole PR or approve its contents as fully screened.

## First 3,000 returned paths
- `55_Workbench`: **2,911**, overwhelmingly `55_Workbench/docs` path prefixes; broad historic document set.
- `00_Workspace`: **49**.
- `.github`: **38**.
- `.obsidian`: **2**.
- Extension counts in the returned subset: Markdown **2,768**, TypeScript **113**, yml **60**, JSON **17**, mjs **10**, yaml **9**, `.DS_Store` **8**, ZIP **3**; other minor extensions.
- Three specifically visible archived files: `55_Workbench/docs/bom/a01-a14/BOM_A06_Fixtures.zip`, `BOM_A11_Canonical_Examples.zip`, `BOM_A14_Disposable_Obsidian_Vault.zip`. These are **inspection candidates**, not automatically prohibited artifacts. Must inspect contents/size/provenance and determine whether they belong in `main`.
- Visible `.DS_Store` files are OS metadata pollution candidates, not needed in a source authority tree. Track for removal on a separately reviewed cleanup branch if safe.
- Historical CI workflow files and obsolete branch triggers appear in the sample; decide which should be disabled/archived in production branch, while retaining provenance.

## Mandatory missing review
1. Acquire **full `git diff --name-status main...candidate` and complete git tree listing** through an authorized local clone or capable full-tree API/export. Github's list-PR-files limit is 3,000; do not mistake the truncated listing for all changed paths.
2. Compute extension/top-level distribution across all 60,611; enumerate binary files, sizes, Git LFS pointers, archives, QEAX/EA source models, generated vaults, caches, vendor dependencies, secret-like paths; inspect actual bytes with a security-scanning tool under approved handling rules.
3. Address retained 60k+ Workbench documents and potential historic vault/imported output scope. Do not delete model notes based on folder naming alone; decide source-of-truth vs archive vs generated using model semantics and provenance.
4. Review old and new workflow triggers/security permissions; only stable essential workflows should run by default on `main`/`develop`.
5. Reconcile main's two distinct commits and preserve three reference documents; ensure history-preserving merge instead of reset/force-push.
6. Create a versioned **full-inventory evidence attachment** and independent review approval prior to PR45 promotion; exact-head green CI does not supersede content/security review.

## Outcome
**PR45 remains draft / NO-GO for merge** pending full 60,611-file inventory and security/provenance review. Continue bounded preparation and documentation only. No deletions, merge, release or main write authorized.
