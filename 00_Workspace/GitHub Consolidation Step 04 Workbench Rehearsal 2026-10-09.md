# GitHub Consolidation — Step 4: Safe Workbench Import Rehearsal

**Date:** 2026-10-09
**Status:** **PASS** — GitHub Actions run `37970033542` completed successfully on the pinned source/base revisions. This proves an ephemeral history-preserving import and Workbench standalone build, **not** a persistent monorepo merge or integrated release.
**Recovery authority:** [Test_Vault_ PR #6](https://github.com/spencerskelly/Test_Vault_/pull/6)
**Staging PR:** [Test_Vault_ draft PR #7](https://github.com/spencerskelly/Test_Vault_/pull/7)
**Run:** [Rehearse Workbench subtree migration](https://github.com/spencerskelly/Test_Vault_/actions/runs/37970033542)

## Frozen inputs

- Target repository: `spencerskelly/Test_Vault_`
- Recovery branch input: `recovery/repository-consolidation-2026-10-09` at `bfefb8ee0c03dd613a8695662fbcc25112bc90c2`
- Rehearsal branch: `integration/workbench-monorepo-rehearsal-2026-10-09`
- Rehearsal workflow commit: `79dac2f69f97c3ac9ae8a1735640666e4047badb`
- Source repository: `spencerskelly/MDSE_Workbench`
- Frozen source `main` SHA: `59fc6219b1d0586900aa7d38685e7087a9d47fec`
- Intended subtree location: `55_Workbench/` — user-directed exact path.

## Execution and safety

The working container available to this assistant has Git but could not resolve `github.com` for local `git ls-remote`. Direct local rehearsal and push were therefore not available; no ordinary file-copy substitute was used.

Instead a narrowly-scoped GitHub Actions **rehearsal-only** workflow was added to the isolated staging branch at `.github/workflows/workbench-monorepo-rehearsal.yml`:
- `push` limited to the exact staging branch, optional `workflow_dispatch`; no default-branch workflow mutation;
- `permissions: contents: read`; `actions/checkout` sets `persist-credentials: false`;
- checks ancestry from frozen recovery branch and requires a clean runner checkout;
- fetches Workbench `main` and fails closed if the source head differs from frozen `59fc6219...`;
- performs `git subtree add --prefix=55_Workbench workbench/main` **without squash** in an ephemeral runner only;
- verifies the resulting Git commit has both expected parent SHAs, source commit ancestry, exact imported Git tree SHA, equal tracked-file counts, and key Workbench files;
- runs `npm ci`, `npm run typecheck`, `npm test`, `npm run build` from inside `55_Workbench/`; checks that source/fixture/package inputs were not changed by the build;
- logs the result to the Actions job summary;
- has **no GitHub push or PR-write operations**. The imported source is intentionally not committed to the GitHub staging branch by this workflow.

GitHub completed run `37970033542` with conclusion **success**. All history/tree checks, standalone TypeScript tests and build, and no-source-mutation assertions passed.

## Verified CI outcome

- Run: https://github.com/spencerskelly/Test_Vault_/actions/runs/37970033542
- Run status: **completed**, conclusion: **success**, source branch SHA: `79dac2f69f97c3ac9ae8a1735640666e4047badb`.
- History/tree proof step: **success**. Checked original Test_Vault_ ancestry, pinned source SHA, both merge parents, source commit ancestry, exact imported subtree Git tree equality, matching tracked file count and critical source paths.
- Workbench independent `npm ci`, TypeScript typecheck, `npm test`, `npm run build`: **success**; test log reports **443 passing, 0 failing**.
- Postbuild source/fixture/package diff assertion: **success**.
- No source import commit was pushed to the staging branch; temporary subtree commit vanished with the runner.
- The job logs include a Node 20 runtime deprecation warning from GitHub Actions; this did **not** fail the run but should be handled in the eventual CI migration.

## Interpretation and next promotion gate

A successful runner rehearsal establishes that the frozen Workbench source/main and its entire tracked tree can be imported beneath `55_Workbench/` with both source and destination commit histories preserved, and confirms the imported isolated package builds at that point in time. It does **not** establish an accepted combined MDSE release or carry source feature branches that are unreachable from Workbench main.

Before writing imported Workbench code to a remote staging branch:
1. Inspect the CI run conclusion and exact Git parent/tree/check evidence.
2. Verify no uncommitted, untracked or unpushed **workstation-local** work would be lost or overlooked. GitHub remote state alone cannot establish that.
3. Retain the entire source Workbench repository and all feature branch tips, notably `workbench/local-model-0.5`, WB-129 recovery, and BOM proposal.
4. Use a separate explicit write/review path for committing the subtree history into staging — an ordinary copy/squash loses ancestry.
5. Port workflows from `55_Workbench/.github/workflows` to the combined repository's root `.github/workflows`, change paths and npm working directories, and eliminate automatic artifact pushes to main.
6. Avoid editing the pinned release manifest until cross-component importer/Base/Bootstrap/Workbench acceptance passes.

**No user main branch or previously existing feature branch has been merged, deleted, or changed in Step 4.**
