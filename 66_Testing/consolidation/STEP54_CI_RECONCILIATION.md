# Step 54 — Consolidated CI reconciliation (review-only)

Date: 2026-10-14
Working branch: `integration/p03-legacy-compat-tests-20261013`
Review PR: #43 (base: frozen Step22); companion narrow PR: #42 (base: main)
Status: PROPOSED — no workflow retired or release promoted.

## Scope and authority

Keep `Test_Vault_` as the target single development authority while PR #39 (engineering cutover), PR #41 (preservation audit), PR #42 (lean validation) and PR #43 (Step22 validation) remain independent. This step reconciles CI semantics, **not** model content, historical repositories, Git refs or release approval.

## Evidence: exact overlapping sources

| Path | PR #42 lean branch | PR #43 Step22 validation branch | Disposition |
| --- | --- | --- | --- |
| `66_Testing/consolidation/test_p03_legacy_compat.py` | blob `90b8a6d7f5cc598a42dec6a1f77b972cc0244b62` | identical blob | one logical source; do not copy twice |
| `66_Testing/consolidation/p04_full_workbench_tree.py` | blob `0ea4153a0fff131b9af902c074bdf4d5c7146a97` | identical blob | one logical source; do not copy twice |
| `.github/workflows/p03-legacy-compat-tests.yml` | lean branch push/PR to `main` | validation branch push/PR to frozen Step22 | branch triggers differ; never automatically retarget during audit |
| `.github/workflows/p04-workbench-readonly.yml` | dispatch-only; requires full Workbench files absent on lean branch | Step22-triggered, full-tree history + double-build diagnostics | retain Step22 version until full-tree evidence is accepted |
| `.github/workflows/mdse-integration-readonly.yml` | not present | multi-job integration gate on full Step22 tree | already consolidates synthetic/importer, governance and source build; don't blindly duplicate jobs |

## Target CI design after promotion is separately approved

One read-only integration workflow with independent, clearly reported jobs:

1. `synthetic-legacy-compat`: isolated P03 unit tests; failures block only schema/compatibility readiness, not data migration.
2. `workbench-tree-and-build`: run P04 tree inventory; enforce checkout completeness; `npm ci`, `npm test`, `npm run build`, double-clean-build hash consistency; check controlled `main.js` hash separately from freshly built candidate.
3. `importer-and-governance`: retain the existing static importer, Base Vault, release-policy and synthetic fixture validations currently in `mdse-integration-readonly.yml`; do not discard any gate without an explicit test-by-test mapping.
4. `evidence-summary`: record tested Git SHA, individual job results, blocked GUI/real-QEAX gates and provenance/waiver state. No publishing, syncing, promotion or rewriting controlled bundles.

## Retention and branch-target rules

- Until PR #39 engineering and #41 preservation reviews authorize cutover, leave `main` and frozen Step22 unmodified.
- PR #42 may run the synthetic-only P03 gate on its narrow branch; full P04 build cannot be treated as passing there because `55_Workbench` source is absent.
- PR #43 is the full-tree validation venue. An existing failure of `sha256sum --check artifact-sha256.txt` is **not** resolved by accepting a newly built hash; it remains a reproducibility/release hold.
- Once approved and source is on `main`, point branch filters to `main`, remove branch-specific temporary CI duplicates only after equivalent execution results are linked and reviewed.
- Sparse checkout excludes `EA_2026_09_06_endgame.qeax.zip` and historical `55_Workbench/vault/`; Actions permissions remain `contents: read` and checkouts use `persist-credentials: false`.
- The current P04 source inventory only proves tracked inputs from its allowlist; changes to that allowlist require review when adding new build inputs.

## Verification required before a workflow replacement

- [ ] Enumerate every job and test command in all three current workflow YAMLs; map each to a future job or justified hold.
- [ ] Demonstrate P03 17 synthetic tests from the target commit.
- [ ] Demonstrate P04 full-tree checkout, tests and two consistent clean-build SHA-256 results on frozen Step22.
- [ ] Diagnose and resolve governed historical `main.js` mismatch without overwriting the controlled artifact.
- [ ] Check privilege/paths (no QEAX checkout, publish/upload of model data, tokens, deploy or commit).
- [ ] Capture Linux CI evidence; independently record macOS and Windows Obsidian GUI results and real-QEAX acceptance before release.
- [ ] Reviewer sign-off on #39 and #41 before retargeting `main`, retiring duplicate workflows or deleting branches.

## Step 55 handoff

Inspect the latest actual CI run outcomes for PR #43; isolate the first failing test/build/artifact gate. Fix that failure on the validation branch only, without editing model/vault history or controlled binaries. Then map all existing integration jobs into a one-workflow candidate and run it alongside legacy jobs before removing any.
