# Step 01 — Workbench remote-branch coverage and consolidation freeze

**Date:** 2026-10-10  
**Status:** REMOTE INVENTORY VERIFIED; CONSOLIDATION NOT YET ACCEPTED OR MERGED.  
**Scope:** `spencerskelly/MDSE_Workbench` remote branches versus `spencerskelly/Test_Vault_` integrated candidate; local workstations are **not** covered.

## Immutable starting points

- Destination authoritative development repository: `spencerskelly/Test_Vault_`.
- Destination current `main` before consolidation: `19f565859e4b9fb7ae63004f1b6f0a7de1b9144e`.
- Integrated candidate (former PR #18 head): `602fc8e7a023cb102bf06dc0bf30bb092ada200f`.
- New consolidation branch: `consolidation/single-authority-2026-10-10`, branched from that exact candidate SHA.
- Standalone Workbench `main`: `59fc6219b1d0586900aa7d38685e7087a9d47fec`.
- Standalone Workbench recovered BOM branch: `50e78c6924a1615d865e763ffdb39d1d2f338bad`.
- Do not add new features or merge into either `main` until the coverage and security gates are reviewed. This is a coordination instruction, **not** GitHub-enforced freeze or archival.

## Remote coverage checks completed

1. Listed **all 19 current remote branches** in standalone Workbench.
2. GitHub commit-graph comparison against the integrated Test_Vault_ candidate confirmed **12 branch tips are ancestors**, including standalone `main`, Local Model 0.4/0.5, WB-129 and BOM A-01–A-14 original recovery.
3. **Seven older branch tips are not present as ancestors** of the integrated candidate; GitHub cross-repository compare returned 404 for those tips. Their file trees were inspected against the integrated Workbench tree instead. Do **not** call these seven fully recovered until unique artifacts or significant differences are classified.
4. Exact Git blob comparison of standalone recovered BOM branch tree against integrated `55_Workbench/`: standalone has **60,234 files**; integrated has **60,235 files**. **60,218 same-path files have identical blobs**, **16 same-path files have different blobs**, **0 standalone-only paths**, **1 integrated-only path** (`scripts/real-vault-05-acceptance.ts`). The 16 differences include code, fixtures, docs, workflow and generated artifacts; never overwrite integrated candidate wholesale with older standalone content.
5. Tested integrated branch already contains `55_Workbench/` with Git ancestry, Importer v0.8.19, Local Model **0.5 authoritative writer**, and experimental **read-only 0.6** plus `variantOf` proposals. GitHub CI: Step 17 full frozen QEAX headless test **PASS** ([run 38012181833](https://github.com/spencerskelly/Test_Vault_/actions/runs/38012181833)); Step 18 packaging/fixture test **PASS** ([run 38013751270](https://github.com/spencerskelly/Test_Vault_/actions/runs/38013751270)). **Real Obsidian GUI and first-open NOT RUN**; release status remains pre-release.

### Every standalone Workbench branch tip accounted for

| Branch | Commit prefix | Result |
|---|---|---|
| `ci-probe-runtime-architecture` | `969b1c8e` | NOT ancestor; CI probe |
| `main` | `59fc6219` | Ancestor |
| `proposal/bom-a14-baseline-check` | `2667965c` | NOT ancestor; experimental BOM CI |
| `proposal/bom-a14-readonly-quantity-uom` | `87cb6158` | Ancestor |
| `recovery/bom-a01-a14-artifacts-2026-10-09` | `50e78c69` | Ancestor |
| `recovery/wb129-ci-equals-2026-10-08` | `52b0b98f` | NOT ancestor; historical equals test |
| `recovery/wb129-ci-interface-2026-10-08` | `fc72a11e` | Ancestor |
| `recovery/wb129-ci-pr-probe-2026-10-08` | `94cf3a7f` | Ancestor |
| `recovery/wb129-ci-real-vault-delimiter-2026-10-08` | `8097f383` | Ancestor |
| `recovery/wb129-ci-reciprocal-2026-10-08` | `47adc363` | Ancestor |
| `recovery/wb129-ci-reject-2026-10-08` | `78833e1e` | Ancestor |
| `recovery/wb129-ci-source-equals-2026-10-08` | `391ca50a` | Ancestor |
| `recovery/wb129-test-alignment-2026-10-08` | `8097f383` | Ancestor |
| `rta2-ci-probe` | `30c6f144` | NOT ancestor; CI probe |
| `wb106-occurrence-views` | `3a565a7a` | NOT ancestor; older design branch |
| `wb106-runtime-build` | `e428116f` | NOT ancestor; older runtime/build branch |
| `workbench/local-model-0.3` | `c05ede6d` | NOT ancestor; older LM 0.3 branch |
| `workbench/local-model-0.4` | `4987652c` | Ancestor |
| `workbench/local-model-0.5` | `7052c07b` | Ancestor |

### Distinct paths found on seven non-ancestor branches

These paths are **absent from the integrated** `55_Workbench/` tree (other source/fixture files already exist by path but can differ in content):

- `ci-probe-runtime-architecture`: `.github/CI_PROBE_RUNTIME_ARCHITECTURE.md`
- `proposal/bom-a14-baseline-check`: `.github/workflows/bom-a14-baseline-check.yml`
- `rta2-ci-probe`: `docs/Architecture/CI Probe.md`
- `wb106-runtime-build`: `.github/workflows/wb106-runtime-build.yml`, `WB106_BUILD_SHA256.txt`

Other three non-ancestor branches expose **no unique paths** versus integrated, but still have differing code/fixtures. Review semantics and historical evidence before declaring superseded. Do not reinstate obsolete probes as active root CI without explicit intent.

### Outstanding integration items

- The recovery branch `recovery/repository-consolidation-2026-10-09` contains **15 later recovery handoff files (Step 04B through Step 18)** under `00_Workspace/` that are missing by path from the integrated branch. Carry their documentation across in a bounded, verified step. Its ancestry is divergent; **do not merge the entire recovery branch blindly**.
- Full branch and blob audit is a **remote-only** check. On every computer developing in either repository, inspect `git status --porcelain`, `git branch -vv`, and unpushed/local-only commits before retiring the standalone repo. Do not claim a complete worldwide freeze based on GitHub.
- Public integrated candidate currently tracks `EA_2026_09_06_endgame.qeax.zip` (~73.2 MB). **BLOCKER for public-main merge pending owner classification of source-data confidentiality and distribution policy.** Moving branches does not undo previous public exposure; if sensitive, use an appropriate exposure/remediation plan rather than a simple deletion commit.
- Existing standalone PRs and integrated Test_Vault_ draft PR chain remain open. **No merge/close/archive/delete has occurred in this step.**
- Active `Test_Vault_` README and current-state references to standalone Workbench will require one coordinated authority update at main promotion; keep one canonical `55_Workbench/` implementation and one root-level CI trigger.

## Decision and next bounded step

**Decision for now:** Use `Test_Vault_/consolidation/single-authority-2026-10-10` as sole staging branch for consolidation and designate `55_Workbench/` as the target source home; standalone `MDSE_Workbench` is preserved read-only **by working convention only**, not yet archived.

**Next: Step 02 — Recover missing handoffs and classify historical branches.** Copy/reconcile the 15 recovery-only documents without overwriting the integrated implementation. Preserve the five historical/probe-only files as evidence only if needed; compare the seven non-ancestor branches' unique logic before declaring them superseded. Record SHA/path comparisons and tests. Maintain explicit stop conditions for sensitive QEAX source and unverified local changes.

**Success condition for Step 01:** 19/19 remote Workbench branches inventoried, exact integration candidate named, missing-branch evidence recorded and stored in Git, no change to either `main`.