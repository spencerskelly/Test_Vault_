# GitHub Consolidation — Step 3: Workbench Migration Manifest

**Date:** 2026-10-09
**Status:** Read-only source inspection and approved-target migration design. **NO source or repository merge executed.**
**Tracking:** [Test_Vault_ draft PR #6](https://github.com/spencerskelly/Test_Vault_/pull/6).
**Inputs:** [[GitHub Consolidation Recovery Inventory 2026-10-09]] and [[GitHub Consolidation Step 02 Branch Reconciliation 2026-10-09]].

## Step 3 findings: exceptions resolved at the file/intent level

### WB-129 equals branch — one non-ancestral commit

- Branch `MDSE_Workbench/recovery/wb129-ci-equals-2026-10-08`: `52b0b98f1d8416b8fb02881b79aad828cc7d2f33`.
- Comparing the latest WB-129 recovery head `8097f383c41617f879eac8e4ca19fab1d0cb7657` **to** this equals branch produces 1 ahead / 13 behind. GitHub identifies the one unique commit as `52b0b98` (message: `fix(ci probe): include endpoint finding label for exact recovery source`).
- The commit's sole patch adds `const label = \`endpoint "${r.identifier}"\`;` under endpoint validation in `src/core/localmodel.ts`.
- **Verified:** the exact `const label` statement is **also present** in the later WB-129 recovery head, together with additional 0.5 `equals` validation for malformed values, self-equality, and symmetry. Thus this is **unique ancestry, not missing effective source behavior** at the inspected location.
- **Disposition:** preserve commit reference as history/evidence; do **not** cherry-pick this old commit wholesale. Reconfirm with the full 0.5 test matrix before declaring equivalent runtime behavior.

### BOM A-14 baseline branch — one non-ancestral CI commit

- Branch `MDSE_Workbench/proposal/bom-a14-baseline-check`: `2667965cdff6e2db8cf3129fdd0b50d4f9fd8d04`.
- Comparing richer `proposal/bom-a14-readonly-quantity-uom` head `87cb615876c342a34ce794beee8b5fad80b80520` to that branch produces **1 ahead / 32 behind**. GitHub identifies the unique commit `2667965` (`A-14: measure untouched Workbench 0.5 test baseline in isolated branch`).
- Its sole patch creates `.github/workflows/bom-a14-baseline-check.yml` with `npm ci`, `npm run typecheck`, `npm test`, scoped only to that baseline-check branch.
- The richer BOM proposal has its own `.github/workflows/bom-a14-verify.yml`, also running `npm ci`, `typecheck`, focused BOM tests and historical `npm test`.
- **Disposition:** baseline-check workflow is a historical comparator, **not** a missing product feature. Preserve its SHA and, if useful, test-run URL in the evidence register; build a unified root CI check instead of importing the branch-specific trigger verbatim. This does **not** establish that either branch's tests pass.

### Branch integration consequence

`workbench/local-model-0.5` (`7052c07b...`) is the shared ancestry for two active development tracks:
- WB-129 latest head `8097f383...` adds **23 commits** above LM 0.5.
- BOM A-14 head `87cb6158...` adds **32 commits** above LM 0.5.
- Their latest heads diverge (32 / 23). **Do not merge both blind or silently select the later-date branch.** Bring the accepted source snapshot into the monorepo, then reconcile WB-129 versus BOM as separate feature PRs against that common baseline, with path-aware conflict resolution and all affected tests.

## Scope of the first Workbench import

**Source repository:** `spencerskelly/MDSE_Workbench`
**Source main at inspection:** `59fc6219b1d0586900aa7d38685e7087a9d47fec`
**Destination repository:** `spencerskelly/Test_Vault_`
**Initial destination staging branch:** `integration/workbench-monorepo` (create **later**, not in this step)
**Destination root:** `55_Workbench/`
**Base for rehearsal:** `recovery/repository-consolidation-2026-10-09` (contains the recovery registers), after locally confirming latest branch SHA.
**History policy:** preserve reachable source-main Git ancestry with **non-squashed `git subtree add`**; keep original Workbench repo readable, including its active branches, until candidate feature history and issues/PRs are safely accounted for. The subtree import of **main alone does not transport unreachable feature branch histories**.

### Source path -> destination path

| Source in MDSE_Workbench | Destination | Action |
| --- | --- | --- |
| `src/` | `55_Workbench/src/` | Preserve unchanged in initial import |
| `test/` | `55_Workbench/test/` | Preserve tests, fixtures and historical-version coverage |
| `bench/` | `55_Workbench/bench/` | Preserve performance / generator harness |
| `scripts/` | `55_Workbench/scripts/` | Preserve real-vault read/edit/reload acceptance programs |
| `docs/`, `README.md`, `RELEASE_NOTES.md`, `WB106_IMPLEMENTATION_CONTRACT.md` | `55_Workbench/` | Retain Workbench-specific authority; later link common model decisions in `00_Workspace/` |
| `package.json`, `package-lock.json`, `tsconfig.json`, `esbuild.config.mjs` | `55_Workbench/` | Continue running Node/TS/esbuild with working directory set to `55_Workbench` |
| `manifest.json`, `styles.css`, `versions.json` | `55_Workbench/` | Keep independent Obsidian plugin metadata and version |
| `main.js`, `artifact-sha256.txt`, `vault/.obsidian/plugins/mdse-workbench/` | `55_Workbench/` **at import** | Keep historical artifacts; later make release artifact publishing deterministic, with hashes and explicit promotion |
| `vault/` | `55_Workbench/vault/` | Preserve Workbench integration fixture, **not** as the source of the next generated Base Vault |
| `ci-workflows/`, `.github/workflows/` | Under `55_Workbench/` **historically** | GitHub will not run workflows nested there. Port *selected* active workflows to **root** `.github/workflows/` and correct paths; leave originals as history/reference until validated |
| `.devcontainer/`, `.gitattributes`, `.gitignore` | `55_Workbench/` | Review scoped ignore/attributes and devcontainer path behavior |
| `.DS_Store` | Retain history only; remove from current tracked tree in follow-up | Unnecessary binary system file; don't alter source history |
| `Test_Vault_/Definitions` | `11_Definitions/` | Separate subsequent workspace directory migration |
| `Test_Vault_/Importer` | `22_Importer/` | Separate migration; importer PR #5 has advanced source and CI |
| `Test_Vault_/Base Vault` | `33_Base Vault/` | Separate migration; update hardcoded `Base Vault/` references and release paths |
| `Test_Vault_/Bootstrap` | `44_Bootstrap/` | Separate migration |
| `Test_Vault_/99_System` | `99_System/` | Preserve model authority |
| `Test_Vault_/Cross-Vault` | Not yet decided | Classify as current tool work, deferred historical work, or external reference; do not silently put in `88_Resources/` |

## Integration workflow manifest

**Current Workbench main GitHub workflows inspected at the root:**
- `build-artifact.yml`
- `integration-candidate-startup.yml`
- `integration-cold-start.yml`
- `integration-live-edit.yml`
- `integration-plugin-overlap.yml`
- `integration-recovery.yml`
- `integration-restart-cycles.yml`
- `integration-view-capability.yml`

**Current Test_Vault_ main:** `bootstrap-candidate.yml`. Importer candidate PR #5 includes additional workflows; evaluate that candidate as the likely future cross-tool CI input rather than treating current `main` as complete.

**Required path changes when moved:** run `npm ci`, `npm test`, `npm run typecheck`, `npm run build`, and Workbench benchmarks from `55_Workbench/`; in GitHub Actions use `defaults.run.working-directory: 55_Workbench` or explicit `working-directory`, set `actions/setup-node cache-dependency-path: 55_Workbench/package-lock.json`, and update `paths`/artifact paths to include `55_Workbench/**`.

**Special hazards checked in source files:**
- `esbuild.config.mjs` writes `main.js` relative to the current directory and resolves `src/main.ts`. Do **not** invoke from repo root unchanged.
- `tsconfig.json` includes `src/**/*.ts`, `test/**/*.ts`, and `bench/**/*.ts`, relative to package root.
- `build-artifact.yml` currently writes plugin payloads and uses a bot `git push` back to main on successful push. Disable this self-mutating behavior in the monorepo migration; publish immutable artifacts and promote a verified payload through a separate review/commit instead.
- The Workbench recovery workflow uses `vault/99_System`, generated `main.js`, and `bench/` paths; adjust their working directory and file transfers together rather than just renaming the workflow.
- `Test_Vault_/Base Vault/Tools/v0.8.0-r2/build-base.py` derives repository root by climbing three directories and hardcodes `Base Vault/Definition/mdse-release.yaml`. Moving `Base Vault/` to `33_Base Vault/` requires updating this and related build/release scripts and manifests. **Do not relocate Base Vault in the initial Workbench-source import PR.**
- `Test_Vault_` release manifest currently references standalone `spencerskelly/MDSE_Workbench`, has old pinned versions and copies vendored plugin artifacts. Update repository/path/version references only after integrated test evidence. Monorepo layout alone does not approve LM 0.5 or importer v0.8.19.

## Reproducible history-preserving staging recipe — NOT EXECUTED

Use a **clean local clone** with Git installed, an authenticated GitHub account, and enough disk for both histories. Never run inside the user's active Obsidian vault until local changes are captured. Confirm `git status --porcelain=v1 -uall` is empty and scan all local clones for unpushed commits/untracked files first.

```bash
git clone https://github.com/spencerskelly/Test_Vault_.git mdse-monorepo-staging
cd mdse-monorepo-staging
git fetch origin
git switch -c integration/workbench-monorepo origin/recovery/repository-consolidation-2026-10-09
git remote add workbench https://github.com/spencerskelly/MDSE_Workbench.git
git fetch --no-tags workbench '+refs/heads/*:refs/remotes/workbench/*'
git log -1 --format='%H %s' workbench/main
git status --short
git subtree add --prefix=55_Workbench workbench/main -m "Import Workbench main history under 55_Workbench"
git log -1 --format='%H %P %s'
git -C 55_Workbench status --short
```

Before the subtree add, verify that `workbench/main` equals the intended source SHA; if it moved, re-evaluate source and do not blindly reuse this guide. Verify the merge commit has both expected parent ancestries; there must be **no `--squash`**. If `git subtree` is unavailable, stop and select an equivalently history-preserving procedure; do not fall back to an ordinary file copy and claim history preservation. `git -C 55_Workbench status` is just a convenience check in the same outer Git worktree, not a nested Git repository requirement.

**Do not push or open this staging PR until the local-work preservation gate is checked and root paths/CI plan are agreed.** Do not delete the remote Workbench repo. Preserve every old branch and PR reference until accepted feature code and issue/decision context have been mapped.

## Step 3 completion and Step 4 boundary

**Completed:** inspected both special historical commits down to their changes and compared them with modern heads; documented why neither requires blind cherry-picking. Inspected actual Workbench package/build/CI structure; produced a source-to-destination inventory and non-squashed Git history migration procedure; enumerated build/release alignment hazards.

**Not completed:** local workstation status, subtree operation, build/test execution, artifact promotion, importer PR integration, PR migration, root folder moves, remote deletion, or release acceptance.

**Next bounded step (Step 4):** make a non-destructive source-history-preserving staging implementation/rehearsal, verify both Git parent histories and preserved file inventory, and prepare path-adjusted CI on the staging branch. If no Git-capable clean worktree is accessible, deliver a tested patch/script and stop before remote mutation instead of silently switching to an unhistoried file copy.
