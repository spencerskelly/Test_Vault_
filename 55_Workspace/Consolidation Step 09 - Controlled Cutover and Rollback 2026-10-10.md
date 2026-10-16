# Step 09 — Controlled Workbench authority/CI rehearsal and rollback

**Status:** Isolated draft PR candidate only; the changed manifest and current docs describe a **proposed** future source authority, not an issued release.  
**Parent commit:** `256330788ba03a17596112ecd5f9a9b406359cfa`; target draft branch `consolidation/step09-authority-ci-rehearsal-2026-10-10`.

## Exact application scope

- `Base Vault/Definition/mdse-release.yaml`: only the two governing repo owner fields `tools.workbench.repo` and `repos.workbench` change to `spencerskelly/Test_Vault_`. The release version, `releaseStatus: pre-release`, all three semantic schema pins, plugin release pins, runtime manifest policy, and other repositories are not changed.
- Six current navigation/ownership documents: root `README.md`, `00_Workspace/README.md`, `00_Workspace/00 - Current State.md`, `00_Workspace/MDSE Tool Definitions and Boundaries.md`, `55_Workbench/docs/INDEX.md`, and `55_Workbench/docs/Definition/04 - Architecture and Model Boundary.md`. These now point to `55_Workbench/` but retain an explicit **candidate pending approval** marker in the responsible boundary notes.
- Two root workflow files: `.github/workflows/mdse-monorepo-workbench-ci.yml` and `.github/workflows/mdse-release-alignment-preflight.yml`. Both acquire a `main` push trigger and the *exact* Step 09 candidate branch trigger; PR base covers `main` and the Step 08 staging branch. Workbench CI has additional path triggers for current docs and `66_Testing/consolidation/**` plus a new read-only Node rehearsal gate after `actions/setup-node`.
- A new `66_Testing/consolidation/test_step09_cutover.cjs` regression script asserts two correct repository-owner values, unchanged release pins, byte-exact plugin lock / generator / original Workspace decisions, Workbench package/manifest pairing, source/CI paths, read-only workflow permissions and no Git push. It reads no QEAX data and changes no repository files.
- The accompanying proposed W decision is **not** placed in the authoritative Workspace Decision Log.

## Safety constraints and negative gates

- Zero changes permitted to `.obsidian/plugin-lock.yaml`, `Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py`, any schema, Workbench writer, importer, QEAX, or runtime payload.
- Historical root workflows continue to contain old refs and are intentionally not rewritten in this patch. The Step 08 strict preflight is therefore **expected to remain NOT READY**. Never weaken the original history-sensitive scanner merely to make the candidate appear green.
- If CI fails for unrelated pre-existing source/version alignment, distinguish that from failure of this targeted cutover rehearsal. **Do not call full integration accepted** without the complete passing suite.
- Before any merge, run `python3 "Base Vault/Testing/check-release.py" --workbench "55_Workbench"`, both root CI checks, source/schema/plugin hashes, and real Obsidian GUI acceptance. A green source build alone is insufficient.

## Rollback and merge strategy

This draft branch starts at Step 08 commit `256330788ba03a17596112ecd5f9a9b406359cfa`. Review its GitHub compare against that SHA for the exact changed file allowlist; absent reviewed approval it can simply be left unmerged or closed. If later merged and found defective, revert the **specific approved cutover commit**, preserving historical Git ancestry and avoiding force pushes. Restore the original repository fields and root CI branch triggers only in coordination with the controlled owner/CI team; never reset/clean contributor clones to solve divergent Git states.

Avoid changing production `main` or archiving `MDSE_Workbench` while QEAX data classification, local clone sign-off, tested runtime release and Obsidian GUI first-open remain open.

**Next bounded step (Step 10):** Evaluate the real GitHub CI results for this rehearsal, fix only candidate defects, prepare the root release-preflight transition so generated lock provenance is informational rather than a false active clone dependency, and record the gates remaining before archive. No public-main merge without owner approval.
