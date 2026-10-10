# GitHub Consolidation — Step 2: Branch Reconciliation

**Recorded:** 2026-10-09
**Status:** Verified remote comparison and first-pass disposition. **No mergers or deletions approved.**
**Working PR:** [Test_Vault_ draft PR #6](https://github.com/spencerskelly/Test_Vault_/pull/6)
**Preceding register:** [[GitHub Consolidation Recovery Inventory 2026-10-09]]

## Scope and method

Queried all visible branch names and head SHAs for the six repositories. Compared every non-`main` branch with its own repository's `main` using GitHub commit comparison; performed targeted cross-branch comparisons for importer, Workbench Local Model, WB-129, BOM, older bases, PosiBattery repair, and the disposable acceptance repo.

**Snapshot totals:** six repositories; 43 remote branches including six `main` branches and this project's newly created recovery branch; 37 non-main refs; five pre-existing open PRs plus the new draft consolidation PR #6. The first recovery inventory captured 42 branch refs **before** creating the new recovery branch.

**Reading the columns:** `ahead=0` and `behind>0` means that branch's commits are ancestors/reachable from `main`, so there are no unique commits to import from that branch; it does **not** prove acceptance. `diverged` and `ahead>0` demand human/semantic review, not automatic conflict resolution. Branch names and GitHub mergeability are not release authority.

## Full branch reconciliation ledger

| Repo | Branch | Relative to main | Ahead | Behind | Initial disposition |
| --- | --- | --- | ---: | ---: | --- |
| Test_Vault_ | `ai/importer-v0.8-folder-cap-75` | behind | 0 | 210 | Ancestor; content incorporated in main history |
| Test_Vault_ | `base-vault-2026-09-30-rel132-v04` | diverged | 1 | 433 | Historical generated base snapshot; preserve provenance |
| Test_Vault_ | `base-vault-2026-09-30-rel133-v05` | diverged | 1 | 423 | Historical generated base snapshot; preserve provenance |
| Test_Vault_ | `base-vault-2026-09-30-rel133-v051` | diverged | 1 | 416 | Historical generated base snapshot; preserve provenance |
| Test_Vault_ | `ci-probe-bootstrap-031` | diverged | 3 | 88 | Probe evidence; review unique test work |
| Test_Vault_ | `ci-probe-bootstrap-artifact` | diverged | 1 | 87 | Probe evidence; review unique test work |
| Test_Vault_ | `importer/baseline-contract-2026-10-05` | ahead | 475 | 0 | ACTIVE importer integration candidate / PR #5 |
| Test_Vault_ | `mdse-workbench-dashboard-definition-20260930` | behind | 0 | 500 | Ancestor; content incorporated in main history |
| Test_Vault_ | `recovery/repository-consolidation-2026-10-09` | ahead | 1 | 0 | ACTIVE consolidation documentation / PR #6, before this new note |
| Test_Vault_ | `wb106-release-integration` | diverged | 8 | 143 | Historical release-integration changes; evaluate 8 unique commits |
| MDSE_Workbench | `ci-probe-runtime-architecture` | diverged | 3 | 920 | Old CI probe; preserve unique history; likely reference |
| MDSE_Workbench | `proposal/bom-a14-baseline-check` | diverged | 4 | 8 | BOM baseline gate, 1 commit not in richer BOM proposal |
| MDSE_Workbench | `proposal/bom-a14-readonly-quantity-uom` | diverged | 35 | 8 | ACTIVE BOM/variant/quantity/unit development; independent reconciliation |
| MDSE_Workbench | `recovery/wb129-ci-equals-2026-10-08` | diverged | 14 | 8 | WB-129 experiment; one commit outside latest recovery line |
| MDSE_Workbench | `recovery/wb129-ci-interface-2026-10-08` | diverged | 11 | 8 | WB-129 experiment; ancestor of latest recovery |
| MDSE_Workbench | `recovery/wb129-ci-pr-probe-2026-10-08` | diverged | 7 | 8 | WB-129 experiment; ancestor of latest recovery |
| MDSE_Workbench | `recovery/wb129-ci-real-vault-delimiter-2026-10-08` | diverged | 26 | 8 | ACTIVE later WB-129 recovery head; equals test-alignment SHA |
| MDSE_Workbench | `recovery/wb129-ci-reciprocal-2026-10-08` | diverged | 17 | 8 | WB-129 experiment; ancestor of latest recovery |
| MDSE_Workbench | `recovery/wb129-ci-reject-2026-10-08` | diverged | 19 | 8 | WB-129 experiment; ancestor of latest recovery |
| MDSE_Workbench | `recovery/wb129-ci-source-equals-2026-10-08` | diverged | 21 | 8 | WB-129 experiment; ancestor of latest recovery |
| MDSE_Workbench | `recovery/wb129-test-alignment-2026-10-08` | diverged | 26 | 8 | ACTIVE draft PR #7; same commit as latest real-vault-delimiter |
| MDSE_Workbench | `rta2-ci-probe` | diverged | 2 | 1041 | Old CI probe; preserve as historical evidence |
| MDSE_Workbench | `wb106-occurrence-views` | diverged | 33 | 1094 | Old WB-106 implementation; review unique history vs modern work |
| MDSE_Workbench | `wb106-runtime-build` | diverged | 2 | 1093 | Old WB-106 artifact/build probe; historical |
| MDSE_Workbench | `workbench/local-model-0.3` | diverged | 15 | 56 | Older LM development; inspect independently of 0.5 writer |
| MDSE_Workbench | `workbench/local-model-0.4` | behind | 0 | 8 | Ancestor of main, version history retained |
| MDSE_Workbench | `workbench/local-model-0.5` | diverged | 3 | 8 | ACTIVE draft PR #6; base of WB-129 recovery and BOM proposal |
| PosiBattery | `chatgpt/battery-installed-reference-foundation` | diverged | 1 | 2275 | Legacy unique commit; review before closure |
| PosiBattery | `claude/battery-product-categories` | behind | 0 | 2270 | Ancestor; no unique branch commits |
| PosiBattery | `merge/recovery-relationship-invariants` | ahead | 70 | 0 | ACTIVE recovery PR #7; remaining validation defects |
| PosiBattery | `recovery/relationship-invariants-batch-01` | diverged | 68 | 2 | Superseded draft PR #4; ancestor of PR #7 head |
| Ampure_Data | `ai/org-vault-standard-2026-09-24` | behind | 0 | 21 | Ancestor; no independent branch commits |
| Ampure_Data | `audit/uid-compliance-2026-09-24` | behind | 0 | 17 | Ancestor; no independent branch commits |
| Ampure_Data | `proposal/obsidian-pull-troubleshooting` | behind | 0 | 27 | Ancestor; no independent branch commits |
| Ampure_Data | `update/company-vault-standard-2026-09-24` | behind | 0 | 25 | Ancestor; no independent branch commits |
| 261002083 | `recovery/step-03-connector-probe-2026-10-08` | ahead | 1 | 0 | Single GitHub connector probe; optionally preserve evidence |
| 261002083 | `wb106-acceptance` | behind | 0 | 126 | Ancestor; fixture work reachable from test-main |

## High-priority ancestry and collisions

### Importer / Test_Vault_

- `importer/baseline-contract-2026-10-05` is **475 ahead / 0 behind** `Test_Vault_ main`, with 161 reported changed files. It is an active integration candidate under [Test_Vault_ PR #5](https://github.com/spencerskelly/Test_Vault_/pull/5). Preserve and treat as the source candidate to validate, not as an accepted release or as an automatic merge.
- `wb106-release-integration` is **8 ahead / 143 behind** main; compared directly against the importer candidate, it is **8 behind / 618 ahead** when the importer candidate is the head (diverged). Inspect the eight unique integration commits for workflow/manifest changes not carried forward.
- `ci-probe-bootstrap-031` has three non-main commits; `ci-probe-bootstrap-artifact` has one. Their CI probe files should be examined for retained acceptance knowledge rather than mechanically merged.
- The three September 30 base-vault branches each have a unique branch commit relative to main and hundreds of path differences because they are generated bases/snapshots, not equivalent methodology-source branches. GitHub's compare file output reached 300 entries for these, so the file listing is truncated. Preserve source lineage and useful tests but do not merge snapshot roots wholesale.
- `ai/importer-v0.8-folder-cap-75` and `mdse-workbench-dashboard-definition-20260930` have **zero** unique commits relative to main.

### Workbench: Local Model, WB-129, and BOM are not one line

- `workbench/local-model-0.4` is an ancestor of Workbench main (0 ahead / 8 behind). Do not reapply it.
- `workbench/local-model-0.5` is 3 ahead / 8 behind main and remains draft [Workbench PR #6](https://github.com/spencerskelly/MDSE_Workbench/pull/6).
- `recovery/wb129-test-alignment-2026-10-08` is **23 commits ahead and zero behind** the Local Model 0.5 branch. It points to the **same SHA** `8097f383c41617f879eac8e4ca19fab1d0cb7657` as `recovery/wb129-ci-real-vault-delimiter-2026-10-08`. Its draft [Workbench PR #7](https://github.com/spencerskelly/MDSE_Workbench/pull/7) is stacked on PR #6.
- Most WB-129 CI experiment heads are ancestors of that later recovery head. **Exception:** `recovery/wb129-ci-equals-2026-10-08` compared to the later recovery head is **1 behind / 13 ahead** (diverged). Thus it contains one commit not in the latest recovery line; inspect its patch and intent separately. Do not assume the latest head contains every experimental change.
- `proposal/bom-a14-readonly-quantity-uom` is **32 ahead and zero behind** `workbench/local-model-0.5`, but compared to the later WB-129 recovery head it is **32 ahead / 23 behind** (diverged). It includes shared Local Model base work and adds separate BOM, `variantOf`, quantity/unit, fixtures, verification, and documentation. **Reconcile after choosing a validated LM 0.5 integration baseline.**
- `proposal/bom-a14-baseline-check` has **one unique commit not present** in the richer BOM branch, so audit that baseline CI/test commit before superseding it.
- Workbench's older `wb106-*`, `rta2-*` and `ci-probe-runtime-architecture` branches are very far behind modern main but retain independent historical commits. Preserve until unique intent/test content is classified. Do not attempt their wholesale merge.

### PosiBattery relationship repair

- `merge/recovery-relationship-invariants` is 70 commits ahead and zero behind main; current work tracked in [PosiBattery PR #7](https://github.com/spencerskelly/PosiBattery/pull/7).
- `recovery/relationship-invariants-batch-01` is **four commits behind and zero ahead** PR #7's head; its history is contained in the newer recovery line, although the newer PR still needs semantic validation.
- `claude/battery-product-categories` has zero unique commits against main. `chatgpt/battery-installed-reference-foundation` retains one unique legacy commit, 2,275 behind main. Inspect it for useful content before retirement.

### Ampure_Data migration and temporary import repos

- All four `Ampure_Data` non-main branches are already ancestors of `Ampure_Data main`; no individual remote feature branch requires integration. Next migrate useful **unique content on main** into PosiBattery by meaning/UID/provenance; don't blindly copy vault settings, separate duplicate authority, or publish unexpected confidential contents merely because the user expects none.
- `261002083/wb106-acceptance` is an ancestor of its own main. The unique `recovery/step-03-connector-probe-2026-10-08` commit adds `recovery-evidence/STEP-03-GITHUB-CONNECTOR-PROBE.txt`, which is a probe, not a required runtime change. The test vault's main still holds the WB-106 acceptance fixtures and startup/cache acceptance guidance; retain reusable evidence in `66_Testing/` before deleting the disposable repo.
- `MDSE_0.8.14` has only main, with its own legacy base structure and Local Model 0.3 evidence. Defer deletion until a new import is accepted and structural knowledge is retained.

## Proposed import/disposition order (not yet executed)

1. **Preservation gate.** For each workstation clone of Test_Vault_, MDSE_Workbench, PosiBattery and Ampure_Data, capture `git status --porcelain=v1 -uall`, `git branch -vv`, `git remote -v` and `git log --oneline @{u}..HEAD` on each locally active branch (if upstream is set). Protect local-only files and commits before migration.
2. **Recovery evidence.** Review the one-off differences noted above: WB-129 equals experiment, BOM baseline probe, WB106 release-integration 8 commits, old Workbench probes, Test base snapshots, PosiBattery legacy reference branch. Record **incorporate / already included / evidence-only / unresolved**, with commit and path rationale.
3. **New monorepo staging branch.** Bring the current Workbench source under `55_Workbench/` with Git lineage intact (e.g., non-squashed subtree), while preserving the existing `Test_Vault_` tree. Do not overwrite `main`; defer moving the other folders until source history and paths are verified.
4. **Unify CI and release contracts.** Create path-aware Workbench source/test/build commands, authoritative schema contract checks, importer acceptance, Base Vault build, Bootstrap startup checks, and integrated runtime/real-vault tests. Rework automatic artifact commits to a reviewable deterministic promotion workflow.
5. **Decide single integration baseline.** Stage LM 0.5 + WB-129 after resolving the outlier commit; then reconcile BOM from its own branch and importer v0.8.19. Keep distinct component versions but a single verified integrated release manifest/commit.
6. **Approve migration gate.** Only after build and integration evidence, retire independent Workbench source authority; keep old repo read-only/archive until links, history, issues, tags and downstream CI references are accounted for.
7. **Separate PosiBattery path.** Validate PR #7's relationship repairs; then migrate Ampure_Data's nonredundant knowledge into PosiBattery with UID matching and content review.
8. **Delete disposable imports last.** Retain fixtures and structural knowledge; wait for successful new import and confirmed receipt of acceptance evidence.

## Result and explicit limitations

**Completed:** compared all current remote non-main branches and the key overlapping lines; classified immediate ancestors and high-risk divergent heads; established a defensible ordering for integration.

**Not completed:** local dirty/unpushed audit, commit-by-commit patch intent review, Git history migration, CI execution, file relocation, business-content migration or repository deletion. This step is strictly recovery planning with immutable refs preserved in the preceding register.

**Next bounded unit (Step 3):** audit the unique WB-129 equals commit and BOM baseline-check commit, assemble the exact Workbench source/CI migration manifest, and prepare the initial history-preserving staging instructions. No direct merges to main.
