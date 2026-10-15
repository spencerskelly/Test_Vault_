# Step 03 — Standalone Workbench historical branch disposition and exact reference recovery

**Date:** 2026-10-10  
**Status:** SEVEN REMOTE HISTORICAL BRANCHES CLASSIFIED; FIVE UNIQUE REFERENCE BLOBS RECOVERED. **NOT an archival approval, integrated runtime acceptance, or release.**  
**Review baseline:** `spencerskelly/Test_Vault_` consolidation commit `108bd655c13c0ec9c166050eee987e41bc48681f` (plus Step 02 commit `fad82b2e30647cc483d64109f36214e756632bf2`).  
**Source:** `spencerskelly/MDSE_Workbench`, with branch tips and repository content inspected through GitHub.

## Method and limits

The Step 01 audit identified 19 remote branches, of which 12 tips are ancestors of the integration candidate and seven are not. Here the seven were compared to standalone `main` using GitHub commit/file comparisons, their relevant source/test files were fetched by branch, and critical paths were compared with the integrated `55_Workbench/` files using Git blobs, source lines and exported test names. This determines whether **obvious unported active functionality or evidence** exists; it is not a line-by-line semantic proof of every prior behavior.

All seven branches are classified as historical or superseded relative to the current candidate. **Do not cherry-pick entire branches, delete the branches, or infer that all runtime compatibility is established.** The original remote branches remain as immutable Git history if the standalone repository is later archived read-only.

## Seven branch dispositions

| Standalone branch / reviewed tip | Classification and inspected evidence | Action |
|---|---|---|
| `ci-probe-runtime-architecture` (`969b1c8e`) | Historical CI/runtime cache probe. `bench/cache-bench.ts` source blob `09658a42` is byte-identical to integrated; `src/core/cache.ts` is an older cache implementation, with newer integrated implementation present. Unique branch-only probe note preserved below. | Reference only; do not reactivate old probe. |
| `proposal/bom-a14-baseline-check` (`2667965c`) | Historical A-14 baseline test workflow. Compared older `localmodel.ts` and edit tests against integrated 0.5 writer / 0.6 read-only candidate: branch does not replace current schema compatibility. | Preserve unique workflow **in docs only**, never active GitHub Actions. |
| `recovery/wb129-ci-equals-2026-10-08` (`52b0b98f`) | Earlier canonical `equals` proof/test branch. All **67** named `localmodel-edit.test.ts` tests and all **32** named `localmodel.test.ts` tests remain by name in integrated files (integrated has 68 and 33 respectively). `test/model-edit.test.ts` has no novel nontrivial old source lines relative to integrated, while specific fixtures have evolved. | Earlier test branch superseded; keep commit history, no code cherry-pick. |
| `rta2-ci-probe` (`30c6f144`) | Temporary synchronization event probe. Cross-main comparison found only a branch-only CI probe note. | Preserve note under documentation only. |
| `wb106-occurrence-views` (`3a565a7a`) | Earlier occurrence-aware view experiments. Old `views.ts` (899 lines) uses legacy first-class `Port`, `Function`, `hasPort` and `hasFlow` model terms; integrated `views.ts` (954 lines) uses newer occurrence-aware interfaces, connections and model contract. Old `core.test.ts` has 35 named tests, integrated 40. A legacy Port graph test is not retained by name; present tests explicitly decline reinterpretation of legacy first-class Port relationships. **Do not import obsolete semantic rules.** | Earlier design superseded **with intentional legacy semantic change**; preserve Git history; verify in actual Obsidian acceptance. |
| `wb106-runtime-build` (`e428116f`) | Historical build of Workbench 0.1.17. Contains branch-only build workflow and checksum; old compiled `main.js` is not an approved current runtime. | Preserve workflow/checksum as documents; **do not** install or execute old `main.js`. |
| `workbench/local-model-0.3` (`c05ede6d`) | Legacy reader and 0.2/0.3 writer semantics. Integrated current writer is strictly 0.5 with 0.1–0.6 read compatibility; tests explicitly retain 0.3 reading/definitionless endpoints, but old 0.2/0.3 structured editing is intentionally read-only now. Older endpoint exposure editing was replaced by the current connection-level `exposes` model. | Historic migration evidence; **do not** restore old writer or endpoint exposure policy. |

## Exact historical reference blobs recovered to Test_Vault_

These five artifacts were unique paths absent from the integrated `55_Workbench/` tree. They were reproduced with identical Git blob SHA, preserving exact text bytes. Filenames were changed to `ARCHIVE_*` and placed under **`55_Workbench/docs/Reference/`**, not under any active workflow/configuration location.

| Origin branch and path | Destination in this branch | Exact original and new Git blob SHA |
|---|---|---|
| `ci-probe-runtime-architecture` / `.github/CI_PROBE_RUNTIME_ARCHITECTURE.md` | `55_Workbench/docs/Reference/ARCHIVE_CI_PROBE_RUNTIME_ARCHITECTURE.md` | `ac8d34ef04bc9afbe999b9cc4d58e648cd9ce651` |
| `proposal/bom-a14-baseline-check` / `.github/workflows/bom-a14-baseline-check.yml` | `55_Workbench/docs/Reference/ARCHIVE_BOM_A14_BASELINE_CHECK.yml` | `3c58fa778d60b7e3d425f67972c136da726b7740` |
| `rta2-ci-probe` / `docs/Architecture/CI Probe.md` | `55_Workbench/docs/Reference/ARCHIVE_RTA2_CI_PROBE.md` | `7a1f25f26c894850ad4b3177420708e5e5027a77` |
| `wb106-runtime-build` / `.github/workflows/wb106-runtime-build.yml` | `55_Workbench/docs/Reference/ARCHIVE_WB106_RUNTIME_BUILD.yml` | `8c3d71efeaa29ac7da7e843640df3d7874859e4d` |
| `wb106-runtime-build` / `WB106_BUILD_SHA256.txt` | `55_Workbench/docs/Reference/ARCHIVE_WB106_BUILD_SHA256.txt` | `02bb9a68b57ee033002e8836c8cc9d36c3c8c248` |

The historical WB-106 compiled `main.js` remains identifiable through old branch commit `e428116f45a114098cd9c1ff46e94af4bf367377` and the recovered checksum list, but its obsolete executable bytes are **not** reinstalled as an active Workbench runtime. The SHA256 checksum in that list is only historical evidence, not a current-build hash.

## Preservation and acceptance notes

- **Preserved:** the 15 exact historical handoffs recovered in Step 02; the 5 unique branch-only probe/build reference files in this step; all historical branch/commit references. No code, schema, release registry, active CI workflows, or authoring templates are modified in this step.
- **Not proved:** exact semantic equivalence of legacy first-class Port and 0.2/0.3 writer paths (these are **intentionally no longer current semantics**). Full integrated Workbench suite was not rerun for this documentation-only commit.
- **Obsidian:** prior headless checks do not replace GUI / first-open acceptance.
- **Authority:** the candidate is not merged into public `Test_Vault_/main` and the standalone repo is still active.
- **Confidentiality:** the public integrated QEAX archive still requires explicit classification and any necessary exposure response.
- **Local clones:** inspect every contributor workstation for unpushed/untracked changes before archival; remote branch inventory alone cannot rule them out.
- **BOM A-15:** isolated writer candidate ZIPs through A-15.4 are not yet committed to `55_Workbench/` and still require source-level integration and CI, without enabling unapproved Local Model 0.6 writes.

## Next bounded consolidation step

Audit remaining authority/CI references to `spencerskelly/MDSE_Workbench` and prepare a **review-only transition checklist/patch** to `Test_Vault_/55_Workbench`; do not amend manifest or merge while QEAX confidentiality, local-clone audit, and runtime gates remain unresolved.

**Disposition:** Seven historical remote branches have documented classifications and five branch-only text artifacts are preserved by content hash. This makes progress toward **eventual read-only archival**, but is **not permission to archive MDSE_Workbench yet**.
