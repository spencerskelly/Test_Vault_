# GitHub Consolidation — Step 4B: Persisted Workbench Subtree and Root CI

**Date:** 2026-10-09
**Status:** **PASS — persistent isolated history-preserving import and Workbench-specific root CI.**
**Promotion status:** DRAFT STAGING ONLY; **not merged into `main`** and **not** an accepted cross-tool MDSE release.
**Previous step:** [[GitHub Consolidation Step 04 Workbench Rehearsal 2026-10-09]]

## Persisted migration

- Destination: `spencerskelly/Test_Vault_`, branch `integration/workbench-subtree-2026-10-09`; code imported beneath `55_Workbench/`.
- Workbench source: `spencerskelly/MDSE_Workbench/main` at pinned commit `59fc6219b1d0586900aa7d38685e7087a9d47fec`.
- Recovery base (before workflow): `61633d0ea66c06928d4e457dff8d9550096164eb`.
- Stage-automation commit: `e6044d63003a1070c66d3ec150b7cc52c085323c`.
- **Imported Git commit:** [`d49cfe7679039738f3912c81db77992d44f8b0cd`](https://github.com/spencerskelly/Test_Vault_/commit/d49cfe7679039738f3912c81db77992d44f8b0cd).
- Git API independently confirms **two parents**, in order: `e6044d63003a1070c66d3ec150b7cc52c085323c`, `59fc6219b1d0586900aa7d38685e7087a9d47fec`. The second is the actual standalone Workbench source commit, so **the Workbench main history is preserved through Git ancestry**, not squash/copied files.
- The import CI asserted identical source/destination Git tree objects under the `55_Workbench` prefix, identical tracked file counts, preserved source ancestry, and key file presence.
- [Stage workflow run 37970531725](https://github.com/spencerskelly/Test_Vault_/actions/runs/37970531725): **completed / success**. The workflow ran `npm ci`, TypeScript typecheck, `npm test`, `npm run build`; logs report **443 tests passed, 0 failed**. Source/fixture/package diff check passed **before** the fast-forward-only push to the isolated branch.
- Re-triggered [stage check run 37970753112](https://github.com/spencerskelly/Test_Vault_/actions/runs/37970753112) also **succeeded**, detected existing subtree and made no new source import push.
- Source Workbench `main` confirmed unchanged after import at `59fc6219b1d0586900aa7d38685e7087a9d47fec`; Test_Vault_ `main` unchanged at `19f565859e4b9fb7ae63004f1b6f0a7de1b9144e`.

## Root-level Workbench CI

- New root workflow: `.github/workflows/mdse-monorepo-workbench-ci.yml`.
- Current staging branch HEAD after adding workflow: `32c8d4e3c1425a90b6ce329d2ec6538b3b4f69ed`.
- Paths monitored: `55_Workbench/**`, governed `99_System/03_Schemas/**`, existing Base Vault/Definition, Importer and Bootstrap paths, plus the workflow itself.
- Uses `55_Workbench/` as command working directory, with npm cache under its `package-lock.json`, and confirms package/plugin manifest versions align.
- `permissions: contents: read`, checkout without persisted push credentials; artifacts are published by the Actions artifact store **without self-committing outputs into Git**.
- [Root CI run 37970753150](https://github.com/spencerskelly/Test_Vault_/actions/runs/37970753150): **completed / success**. All check/test/build steps passed and no source/fixture diffs appeared.
- Uploaded artifact `mdse-workbench-32c8d4e3c1425a90b6ce329d2ec6538b3b4f69ed`, artifact ID `11634674148`, includes the built `main.js`, `manifest.json`, `styles.css` and checksum file; retention until 2026-10-23 (14 days), subject to GitHub policy. GitHub reported archive SHA-256 digest `f945af83c947ac5b0f0d4dddd38f2bddd1fe27ef703ae9873b7ff06a6de2efc3`.
- [Draft integration PR #8](https://github.com/spencerskelly/Test_Vault_/pull/8) targets `recovery/repository-consolidation-2026-10-09`, not `main`. Root CI is only a **Workbench component gate**, not a full importer/Bootstrap/Base Vault acceptance certification.

## Remaining important gates

1. **Local workstation protection:** inspect all active user clones for uncommitted, untracked and unpushed work; remote GitHub cannot prove their absence. Don't archive or delete standalone Workbench before this.
2. **Feature-branch reconciliation:** `workbench/local-model-0.5`, latest `recovery/wb129-test-alignment-2026-10-08` and `proposal/bom-a14-readonly-quantity-uom` are unmerged/draft. The import only brings Workbench `main` lineage. Preserve each feature head and its content/PR review history before promoting.
3. **Build artifact policy:** the copied `55_Workbench/.github/workflows/` files are historical and do not execute nested; root Workbench CI is new and read-only. Additional root integration/acceptance workflows must be adapted, and the old source workflow's automatic artifact-to-main behavior must **not** be reintroduced.
4. **Directory migration:** map `Definitions -> 11_Definitions`, `Importer -> 22_Importer`, `Base Vault -> 33_Base Vault`, `Bootstrap -> 44_Bootstrap`, and new `66_Testing` and `88_Resources`. Do not move roots without updating release manifest, scripts and references.
5. **Shared integration:** reconcile importer PR #5 and Workbench LM/BOM features, align schema versions/manifest/pinned plugins, then run Base build/importer/Bootstrap/Workbench full real-model acceptance. Current Test_Vault_ `main` release definition remains an older pre-release authority.
6. **Security/provenance:** PosiBattery / Ampure_Data content integration is a distinct later track; temporary test imports should be retired only after preserving acceptance knowledge and validating a replacement import.

## Step 4B verdict

**Completed:** non-squashed Workbench main import persisted safely to a dedicated remote integration branch, exact Git parent lineage verified, Workbench component test/build passed, unified-root Workbench CI published a checksummed immutable artifact, draft PR opened, and old repos/main/feature branches retained.

**Not completed:** cross-component release acceptance; feature PR integration; local change scan; final merge to `main`; retiring any repository.

**Next bounded unit (Step 5):** protect local-only work and start a controlled migration/alignment inventory for root paths and remaining feature branches. Prioritize the unified release contract before merging source feature branches or expanding development.
