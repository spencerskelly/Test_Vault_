# GitHub Repository Consolidation — Recovery Inventory and Decisions

**Recorded:** 2026-10-09
**Status:** Recovery step 1; inventory/preservation only. Not an implementation or release approval.
**Scope:** GitHub remote repositories and branches accessible to the connector at this snapshot. Uncommitted, unpushed, and other workstation-only changes have **not** been checked.

## Decisions and agreed target

The user explicitly directed the following; these decisions supersede older workspace documentation where the repository structure or repository roles conflict.

1. `Test_Vault_` is the continuing **single MDSE development/integration repository**. Incorporate `MDSE_Workbench` source, history, tests, docs and workflows into it, under `55_Workbench/`. Keep a self-contained component and its versioning, but make cross-component integration atomic.
2. The exact target workspace root layout is:

```text
Test_Vault_/
  00_Workspace/       Decisions and plans
  11_Definitions/      Reusable definitions
  22_Importer/         EA importer
  33_Base Vault/       Runtime/release builder
  44_Bootstrap/        Startup and validation
  55_Workbench/        Complete Workbench source
  66_Testing/          Integration acceptance
  88_Resources/        External information
  99_System/          Shared model authority
  .github/workflows/ Unified CI
  .obsidian/          Development vault
```

Maintain existing naming and spaces as explicitly shown. The user's `88_Resources/.` notation is interpreted as the directory `88_Resources/`, not a literal dot-suffixed name. Do **not** move `Cross-Vault/` mechanically into `88_Resources/`: determine whether it is retained internal tool development, reference history, or deferred work.

3. `PosiBattery` remains the **long-term business, market and engineering knowledge repository**. Review `Ampure_Data` and move/merge all useful nonredundant knowledge into PosiBattery, preserving source and UID provenance. User states there is nothing secure in Ampure_Data. Nevertheless `Ampure_Data` is currently private while `PosiBattery` is public; explicitly review public-disclosure suitability and collisions before publishing content. Ampure_Data may be retired after acceptance, not before.
4. `MDSE_0.8.14` and `261002083` are disposable test imports. Retain useful structure, historical compatibility fixtures, test instructions, acceptance evidence, and handoff knowledge in Test_Vault_; delete the test repositories only **after a successful replacement import** and explicit preservation review. Do not select one merely because its version string looks newer.
5. Do not delete repositories, move files, rewrite refs, or merge existing development PRs as part of Step 1.

## Remote inventory snapshot

Six repos, forty-two branch refs (including six mains), five open PRs. All listed branch refs were reported as unprotected by the branch listing endpoint at this snapshot; this does not prove effective repository ruleset status.

- `Test_Vault_` — **public**, main `19f565859e4b9fb7ae63004f1b6f0a7de1b9144e`; 10 branches; workflow: `bootstrap-candidate.yml` on main.
- `MDSE_Workbench` — **public**, main `59fc6219b1d0586900aa7d38685e7087a9d47fec`; 18 branches; 8 workflow YAML files under `.github/workflows/`.
- `PosiBattery` — **public**, main `d053f3f44bc382420937ca09497cd2b0c5ac2ae8`; 5 branches; 28 workflow YAML files.
- `Ampure_Data` — **private**, main `21c60ba50dc74ea27a65531d276d7f92f6da354f`; 5 branches; no `.github/workflows/` directory found.
- `MDSE_0.8.14` — **private**, main `b9acefeb8f356b759b5c7f1a6bc22745962d30d4`; 1 branch.
- `261002083` — **private**, main `6f6a3dee944943a14f49b0e609d01e2f49b5cb18`; 3 branches.

### Open PR preservation register

| Repository / PR | Head -> Base | State / preserve |
| --- | --- | --- |
| [Test_Vault_ #5](https://github.com/spencerskelly/Test_Vault_/pull/5) | `importer/baseline-contract-2026-10-05` -> `main` | Open; importer hardening through 0.8.19 and Workbench pin. Inspect before migration. |
| [MDSE_Workbench #6](https://github.com/spencerskelly/MDSE_Workbench/pull/6) | `workbench/local-model-0.5` -> `main` | Draft; LM 0.5 writer/editor compatibility. |
| [MDSE_Workbench #7](https://github.com/spencerskelly/MDSE_Workbench/pull/7) | `recovery/wb129-test-alignment-2026-10-08` -> `workbench/local-model-0.5` | Draft, **stacked onto #6**, test-only; not a standalone release. |
| [PosiBattery #7](https://github.com/spencerskelly/PosiBattery/pull/7) | `merge/recovery-relationship-invariants` -> `main` | Open; repairs with remaining validation findings; supersedes #4. |
| [PosiBattery #4](https://github.com/spencerskelly/PosiBattery/pull/4) | `recovery/relationship-invariants-batch-01` -> `main` | Older draft, superseded by #7. Preserve evidence before closing. |

### Selected branch comparisons versus repository main

GitHub compare results at this snapshot; `ahead` is commit count reachable from candidate but not main, and `behind` is the reverse. These are **not** tests.

| Branch | Status | Ahead | Behind |
| --- | --- | ---: | ---: |
| Test_Vault_: importer/baseline-contract-2026-10-05 | ahead | 475 | 0 |
| Test_Vault_: wb106-release-integration | diverged | 8 | 143 |
| MDSE_Workbench: workbench/local-model-0.3 | diverged | 15 | 56 |
| MDSE_Workbench: workbench/local-model-0.4 | behind | 0 | 8 |
| MDSE_Workbench: workbench/local-model-0.5 | diverged | 3 | 8 |
| MDSE_Workbench: recovery/wb129-test-alignment-2026-10-08 | diverged | 26 | 8 |
| MDSE_Workbench: proposal/bom-a14-readonly-quantity-uom | diverged | 35 | 8 |
| PosiBattery: merge/recovery-relationship-invariants | ahead | 70 | 0 |
| Ampure_Data: update/company-vault-standard-2026-09-24 | behind | 0 | 25 |

Remaining non-main branches are identified by immutable head SHAs below but have **not yet** received individual behind/ahead or semantic novelty classification. They are not candidates for deletion on the evidence gathered so far.

## Complete branch-head register (preservation; do not delete blindly)

### 261002083 (3 branches)

| Branch | Head SHA |
| --- | --- |
| `main` | `6f6a3dee944943a14f49b0e609d01e2f49b5cb18` |
| `recovery/step-03-connector-probe-2026-10-08` | `f12b67ba78e0b7e4c9635cf6cc6155314b5db2ab` |
| `wb106-acceptance` | `3f012a222975fbfd592511ae230f538157524ec1` |

### Test_Vault_ (10 branches)

| Branch | Head SHA |
| --- | --- |
| `ai/importer-v0.8-folder-cap-75` | `c82e31ccb4f665aea1f2988a28ec43630ace71b6` |
| `base-vault-2026-09-30-rel132-v04` | `5f2f6577c648ad574778da18fc2c38cd134f3466` |
| `base-vault-2026-09-30-rel133-v05` | `0df77b80138cccfb4f42be5e1296e07b532760b8` |
| `base-vault-2026-09-30-rel133-v051` | `c5a1fd4e4179c22204314502ca40b2d46c3acb1a` |
| `ci-probe-bootstrap-031` | `cf7b5e472be9b4b6fb5624337c4cf1822d4ff564` |
| `ci-probe-bootstrap-artifact` | `7369733b96f1d3db7afebb633035b64bf9efafe7` |
| `importer/baseline-contract-2026-10-05` | `0494354ec40378e119b17c61fdf6e828844035e4` |
| `main` | `19f565859e4b9fb7ae63004f1b6f0a7de1b9144e` |
| `mdse-workbench-dashboard-definition-20260930` | `1c924e3f049b136cea890a5097bc317fa9857d2b` |
| `wb106-release-integration` | `c1093cf5f7b5727beef6a0fe6b7cdfbfd39d5105` |

### MDSE_Workbench (18 branches)

| Branch | Head SHA |
| --- | --- |
| `ci-probe-runtime-architecture` | `969b1c8e6d16302b502758f67df5aae58ac09d7e` |
| `main` | `59fc6219b1d0586900aa7d38685e7087a9d47fec` |
| `proposal/bom-a14-baseline-check` | `2667965cdff6e2db8cf3129fdd0b50d4f9fd8d04` |
| `proposal/bom-a14-readonly-quantity-uom` | `87cb615876c342a34ce794beee8b5fad80b80520` |
| `recovery/wb129-ci-equals-2026-10-08` | `52b0b98f1d8416b8fb02881b79aad828cc7d2f33` |
| `recovery/wb129-ci-interface-2026-10-08` | `fc72a11e26d53f11d3f81de8ffcc1c7ce5fda921` |
| `recovery/wb129-ci-pr-probe-2026-10-08` | `94cf3a7fb2a787bbe9168bf84895dbe2e056f233` |
| `recovery/wb129-ci-real-vault-delimiter-2026-10-08` | `8097f383c41617f879eac8e4ca19fab1d0cb7657` |
| `recovery/wb129-ci-reciprocal-2026-10-08` | `47adc363e6bedcb5a199c7f69c4f2c3d32c20986` |
| `recovery/wb129-ci-reject-2026-10-08` | `78833e1e3a3089d7085dce070bb5b332bbdcbd4e` |
| `recovery/wb129-ci-source-equals-2026-10-08` | `391ca50a3caf7b64d58b4ad49be71e81cd360b7c` |
| `recovery/wb129-test-alignment-2026-10-08` | `8097f383c41617f879eac8e4ca19fab1d0cb7657` |
| `rta2-ci-probe` | `30c6f144748e865aec351d93c935599c93881933` |
| `wb106-occurrence-views` | `3a565a7abc8b60d7b3ee7e1a2152556b58e0ec59` |
| `wb106-runtime-build` | `e428116f45a114098cd9c1ff46e94af4bf367377` |
| `workbench/local-model-0.3` | `c05ede6df4f6e120d9e51a99c1b66a8af386a9ef` |
| `workbench/local-model-0.4` | `4987652c63e92f7ac16a2db33eda6feb3b5c6e49` |
| `workbench/local-model-0.5` | `7052c07b4c95212522ba4b5d274c95be0860bda3` |

### PosiBattery (5 branches)

| Branch | Head SHA |
| --- | --- |
| `chatgpt/battery-installed-reference-foundation` | `0866fccf79f2b35b5fa0a7d07cc2d1208b5c1868` |
| `claude/battery-product-categories` | `29c524588e38500666c054b1e979c2fdc15fe061` |
| `main` | `d053f3f44bc382420937ca09497cd2b0c5ac2ae8` |
| `merge/recovery-relationship-invariants` | `5beb96fe7fdd41fd30f51d9eedcad1ead6374c43` |
| `recovery/relationship-invariants-batch-01` | `0da4629eb20137713d9c8b8e159ad90de8e7c387` |

### Ampure_Data (5 branches)

| Branch | Head SHA |
| --- | --- |
| `ai/org-vault-standard-2026-09-24` | `3d6884aadd235da5589e6f6a6cf4e76dbf143941` |
| `audit/uid-compliance-2026-09-24` | `1675fc9ca486ad36390c0c8cffbb5c507c7d5b6f` |
| `main` | `21c60ba50dc74ea27a65531d276d7f92f6da354f` |
| `proposal/obsidian-pull-troubleshooting` | `a7cbf3c34a25df7c6572335b3567c38d872cf006` |
| `update/company-vault-standard-2026-09-24` | `b1d444e66fa60451965b88ee5ba8fabd1a9c25a9` |

### MDSE_0.8.14 (1 branches)

| Branch | Head SHA |
| --- | --- |
| `main` | `b9acefeb8f356b759b5c7f1a6bc22745962d30d4` |

## Known dependency and baseline hazards

- Test_Vault_ `main` currently has pre-release `mdse-release.yaml` specifying Local Model 0.2, Workbench pinned 0.1.16, and candidate 0.1.17; MDSE_Workbench `main` package version is 0.1.18; importer PR #5 is the large advanced candidate, and LM 0.5 is under draft PRs. This is a release reconciliation issue, **not** proof that any individual candidate is accepted.
- The importer candidate branch contains its own additional integration workflows and release changes. Do not assume Test_Vault_ main has all planned toolchain changes.
- MDSE_Workbench `.github/workflows/build-artifact.yml` runs `npm ci`, tests, benchmarks and build; following success on main it commits built artifacts to the source branch. During monorepo migration, redesign as a PR check and immutable build artifact followed by deliberate promotion, rather than opportunistically modifying main.
- Workbench BOM development exists on separate `proposal/bom-a14-*` branches, while LM 0.5 testing/implementation exists on several `recovery/wb129-*` branches. Treat overlapping changes as a reconciliation problem, **not** independent wholesale merges.
- PosiBattery PR #7 reports fewer relationship validation findings than main but still has remaining errors; a GitHub mergeable result does not establish a green semantic baseline.
- Ampure_Data has organization/identity/UID work. Reconcile overlapping People, Organizations, Products and other definitions against PosiBattery by stable UID/meaning; preserve evidence and avoid duplicating or silently conflating distinct elements.
- 261002083 contains `README_RUNTIME_ACCEPTANCE.md`, `README_WB106_ACCEPTANCE.md`, acceptance fixture folders, and performance/stability handoff files. Capture these before retiring the repository.
- MDSE_0.8.14 README identifies Local Model 0.3, while 261002083 README identifies Local Model 0.2. Determine whether retained compatibility fixtures cover this distinction; don't make either test repo permanent merely for this difference.

## Migration map and open placement decisions

| Current path / repository | Proposed destination | Notes |
| --- | --- | --- |
| `Test_Vault_/00_Workspace` | `00_Workspace/` | Retain roadmap, decisions, current state; update paths when migration lands. |
| `Test_Vault_/Definitions` | `11_Definitions/` | Preserve UID/link semantics. |
| `Test_Vault_/Importer` | `22_Importer/` | Use latest reconciled candidate, maintain version history. |
| `Test_Vault_/Base Vault` | `33_Base Vault/` | Update builder include lists, script paths, release manifest. |
| `Test_Vault_/Bootstrap` | `44_Bootstrap/` | Preserve definitions, tests, versioned source. |
| Entire `MDSE_Workbench` repository | `55_Workbench/` | Preserve source, tests, docs, fixtures and reachable Git history using a history-aware migration; adjust Node/CI working directories. |
| New cross-component acceptance | `66_Testing/` | Retain component-specific tests under their tool dirs, with integration orchestration here. |
| Externally acquired material | `88_Resources/` | Do not reclassify internal code or decision history as external. |
| `Test_Vault_/99_System` | `99_System/` | Shared model semantics remain authoritative. |
| `Test_Vault_/.obsidian` | `.obsidian/` | Keep as development vault; do not merge arbitrary generated/test-vault plugin settings. |
| `Test_Vault_/Cross-Vault` | **Unresolved** | Assign based on actual code/reference/deferred-work contents in the later mapping pass. |
| `Ampure_Data` unique business content | `PosiBattery`, mapped by content type | Resolve identity collisions, provenance and public disclosure. |

## Acceptance gates before any repository merge

1. Have an immutable branch-head and open-PR snapshot (this file) and back up all locally modified/untracked/unpushed work independently.
2. Determine all unmerged branch novelty, maintain a disposition ledger: **incorporate / already integrated / preserve as reference / retain open / abandon with explicit evidence**.
3. Prove the source and history migration to `55_Workbench/` on a disposable integration branch (or history-preserving local rehearsal), without replacing Test_Vault_ main.
4. Rebase/retarget CI and imports, build paths, release manifest, artifact hashes, and docs. Require one shared test matrix covering Importer -> Base Vault -> Bootstrap -> Workbench with fixture and real-model acceptance. Preserve Workbench-specific unit and stress tests.
5. Merge only after checks pass or known exceptions are separately documented and explicitly accepted. Keep the old MDSE_Workbench repo unchanged and accessible until verification is complete.
6. For PosiBattery/Ampure_Data, separate business/market content migration from engineering relationship repairs, and review public disclosure before crossing a private-to-public repository boundary.
7. Retire test imports only after successful **new** import and copy/verification of structural knowledge and fixture evidence.

## Immediate next work pass (Step 2)

- Audit workstation copies for uncommitted/unpushed changes (the GitHub connector cannot observe these).
- Compare every remaining branch with main and with its intended parent; identify unique content, particularly BOM, LM 0.5 and importer branches.
- Create a file/CI/reference migration manifest and establish a staged history-preserving Workbench import approach.
- Create only a dry-run integration branch/PR, never merge it automatically.

**Snapshot caveat:** Remote GitHub state may change after this inventory; re-read immutable refs before migration. No branch deletion or content migration is authorized by this document.
