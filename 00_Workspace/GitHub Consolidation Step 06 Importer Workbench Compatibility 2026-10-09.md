# GitHub Consolidation — Step 6: Importer and Workbench Reconciliation Gate

**Recorded:** 2026-10-09
**Status:** Completed remote branch comparison, clean ephemeral Git merge rehearsal, importer and Workbench standalone component tests, and an **intentional compatibility-blocking check**.
**Promotion:** NOT APPROVED; no importer merge committed or pushed. No main branch changed.
**Plan predecessor:** [[GitHub Consolidation Step 05 Release Contract and Path Audit 2026-10-09]]

## Exact immutable input refs

- Existing Workbench-integrated staging input: `spencerskelly/Test_Vault_` `integration/workbench-subtree-2026-10-09` @ `75eff6007af46e19f36f76b38df44658ac381ba5`.
- Importer development candidate: `spencerskelly/Test_Vault_` `importer/baseline-contract-2026-10-05` @ `0494354ec40378e119b17c61fdf6e828844035e4`; tracked by [importer PR #5](https://github.com/spencerskelly/Test_Vault_/pull/5).
- Standalone Workbench main source currently imported under `55_Workbench/`: `spencerskelly/MDSE_Workbench` @ `59fc6219b1d0586900aa7d38685e7087a9d47fec`.
- Workbench Local Model 0.5 recovery candidate: `spencerskelly/MDSE_Workbench` `recovery/wb129-test-alignment-2026-10-08` @ `8097f383c41617f879eac8e4ca19fab1d0cb7657`; draft [Workbench PR #7](https://github.com/spencerskelly/MDSE_Workbench/pull/7).
- Rehearsal-only branch: `integration/importer-reconciliation-2026-10-09`.
- [Clean-merge + component-test run 37972109329](https://github.com/spencerskelly/Test_Vault_/actions/runs/37972109329) — **success** for the guarded merge and component-level checks, while legacy release checker was a separately recorded failing diagnostic.
- [Detailed-diagnostic run 37972267943](https://github.com/spencerskelly/Test_Vault_/actions/runs/37972267943) — **success** for the merge/component tests; prints the exact 4 failed release checks and 4 warnings.
- [Compatibility gate run 37972437540](https://github.com/spencerskelly/Test_Vault_/actions/runs/37972437540) — **intentional failure on source/schema incompatibility**, not a Git conflict.

## What the dry-run proved

GitHub Actions fetched the **exact pinned importer SHA** and used `git merge --no-ff --no-commit` in an ephemeral runner. The merge had **zero Git file conflicts** and did not change the remote branch. The importer would contribute 475 unique commits relative to the original Test_Vault_ main, including release manifest, schemas, importer v0.8.19 tool chain, tests, mapping schemas, templating, and several root CI workflows; preserve all source ancestry in an eventual non-squashed merge.

The noncommitting merged tree passed:

- version consistency of the importer release manifest vs `99_System/03_Schemas`: relationships 1.36, elementTypes 1.18, Local Model 0.5;
- imported Workbench **package/manifest version** 0.1.18, matching the importer release manifest and Workbench entry in generated plugin lock;
- importer v0.8.19 governed source-profile check, headless-script syntax, release-gate regressions and IMP-009 output-acceptance selftest;
- construction of the fresh candidate Base Vault;
- imported Workbench standalone npm typecheck, **443 tests passed, 0 failed**, and build, on the merged tree.

**These do not establish importer/Workbench semantic compatibility.** They do not prove a Workbench 0.5 edit/read of an imported real-QEAX vault.

## Critical newly verified release blocker — Workbench Local Model 0.5

The importer branch's manifest and `local-model.yaml` both require **Local Model 0.5** to write, with 0.1–0.5 readable. Yet imported Workbench `55_Workbench/src/core/localmodel.ts` at the source SHA states:

```typescript
export const READABLE_VERSIONS = ["0.1", "0.2", "0.3", "0.4"] as const;
export const WRITABLE_VERSION = "0.4";
```

The Workbench recovery candidate `8097f383...` instead has:

```typescript
export const READABLE_VERSIONS = ["0.1", "0.2", "0.3", "0.4", "0.5"] as const;
export const WRITABLE_VERSION = "0.5";
```

Thus **Workbench plugin version 0.1.18 alone is insufficient compatibility evidence**. The same product/version label is present on a source commit whose parser does not understand the new importer-written schema. Importing schema 0.5 notes into that Workbench would disable their governed structured interaction.

Implemented a **fail-closed** source/schema validator `66_Testing/check_importer_workbench_localmodel.py` on the importer rehearsal branch. It reads the actual source `READABLE_VERSIONS` and `WRITABLE_VERSION`, active schema version and compatibility section, and manifest; it does not trust product version strings alone. [Run 37972437540](https://github.com/spencerskelly/Test_Vault_/actions/runs/37972437540) correctly produced:

- `BLOCKED: Workbench source DOES NOT READ schema 0.5`
- `BLOCKED: Workbench WRITES 0.4, but the active importer schema requires 0.5`
- `BLOCKED: Workbench cannot read all canonical schema backwards-compatibility versions`

This is an **expected, actionable red gate**, preventing any promotion of the incompatible pair. Workbench 0.5 recovery and BOM remain separate and should be reconciled without reducing compatibility for earlier schema versions.

## Existing release-checker findings after dry-run merge

`Base Vault/Testing/check-release.py --base <fresh candidate>` exits 1 with **4 FAIL / 4 WARN**. The failures are all unregistered **new cross-repo consolidation documents** on the older staging baseline; they are not unresolved merge conflicts:

1. `00_Workspace/GitHub Consolidation Recovery Inventory 2026-10-09.md`
2. `00_Workspace/GitHub Consolidation Step 02 Branch Reconciliation 2026-10-09.md`
3. `00_Workspace/GitHub Consolidation Step 03 Workbench Migration Manifest 2026-10-09.md`
4. `00_Workspace/GitHub Consolidation Step 04 Workbench Rehearsal 2026-10-09.md`

Each must be added to the correct `documents` status registry in the **existing authoritative** `mdse-release.yaml` after the candidate merge, including later Step 4B/5/6 documents as applicable; do not suppress the checker and do not edit an unrelated manifest on the wrong branch.

Its four release warnings were:
- Bootstrap generated plugin lock 0.3.1 matches candidate source, while manifest still pins 0.3.0;
- importer is not yet release-conformant;
- clean 0.8.0 Base Vault not issued;
- superseded v0.8.7–0.8.18 importer executable revisions still in `Importer/Tools` pending archive before release.

Additional stale documentation to reconcile: importer branch's `00_Workspace/00 - Current State.md` retains some Local Model **0.4 writer** text despite `local-model.yaml` and manifest being **0.5**. Importer PR #5 description starts as if through v0.8.14 despite current v0.8.19 head. Treat the manifest and source at the exact commit, not old narrative snapshots, as evidence.

## GitHub changes made in Step 6

- Created isolated remote branch `integration/importer-reconciliation-2026-10-09` from the frozen combined Workbench integration baseline.
- Added root `.github/workflows/importer-monorepo-merge-rehearsal.yml`: permission `contents: read`, no credentials for push, pinned source checks and ephemeral no-commit merge; exercises importer contract, Base build, Workbench standalone tests, and legacy release checker diagnostics.
- Added `66_Testing/check_importer_workbench_localmodel.py` and inserted it as a hard gate before claiming integrated Workbench acceptance. Explicit blocked status is the intended output for the present source mismatch.
- CI workflow refinements fixed two **test-harness** errors (shell `-e` propagation on nonzero diagnostic release check; SIGPIPE from truncating a large `git diff`), without changing importer/model runtime behavior.

**No importer source merge persisted**, no existing feature PR merged/closed and no repository deleted.

## Required integration order from here

1. Integrate the reviewed WB-129 **Local Model 0.5 recovery code** into a new **WorkBench-feature staging branch** of Test_Vault_ under `55_Workbench/`, preserving unique code/history, and reconcile the single ancestral CI probe identified in Step 3.
2. Resolve any overlap with BOM A-14 (which independently branched from LM 0.5) without dropping either functionality or broadening schemas silently; the BOM source is **not** accepted automatically by a WB-129 fix.
3. On the combined Workbench 0.5 source, rerun the source/schema compatibility check, Workbench tests, importer regression and real-QEAX Local Model 0.5 acceptance against exact pinned sources. A parser check **passing** alone is not full semantics or interactive Obsidian acceptance.
4. Then persist the importer branch history with an explicitly reviewed **non-squashed merge** on a separate integration branch and register all current/reference workspace docs. Preserve branch refs until the merged head/CI evidence is verified.
5. With importer + Workbench semantics aligned, carefully relocate `Importer/` to `22_Importer/` and `Base Vault/` to `33_Base Vault/`, patching all current runtime scripts, manifest pointers, CI and Obsidian links atomically.

**Next bounded Step 7:** WB-129 version-0.5 source/history migration preparation and integrated compatibility gate; do **not** delete source repo, merge current importer PR #5 to main, or promote version 0.8.0 yet.
