# GitHub Consolidation — Step 10: Release Registry and Canonical Workbench Fixture

**Recorded:** 2026-10-09
**Outcome:** **PASS — original release checker 0 FAIL / 4 WARN, Workbench 448 tests PASS / 0 FAIL, TypeScript/build PASS.**
**Release state:** Controlled `0.8.0` remains **pre-release**. No main branch, issued runtime, generated lock, or candidate version promoted.
**Source baseline:** `integration/importer-persisted-2026-10-09`, merge head `dcfe3e45bd45f0a3619c18ae5841a357f526347b`.
**Step 10 staging:** `integration/release-contract-step10-2026-10-09`, [draft PR #13](https://github.com/spencerskelly/Test_Vault_/pull/13).
**CI:** [Step 10 verification run 37976987887](https://github.com/spencerskelly/Test_Vault_/actions/runs/37976987887).

## Changed only on reviewable staging

1. **Release document registry:** `Base Vault/Definition/mdse-release.yaml` now includes the *four recovery documents already present on the integrated source branch* with `status: reference`, not `current`. No recovery notes became semantic authority. Future recovery records that currently live only in `recovery/repository-consolidation-2026-10-09` **are not registered on staging yet**; if moved into the integrated branch later, add each to this registry atomically.
2. **Current-state provenance:** `00_Workspace/00 - Current State.md` now begins with an October 9 candidate checkpoint, identifying WB-129 Workbench reader 0.1–0.5 / writer 0.5, importer v0.8.19 and non-issued status. The October 6 `0.4 writer` descriptions are clearly labeled the earlier baseline snapshot, not the current combined candidate. All older source evidence is preserved.
3. **Workbench model schema fixture:** `55_Workbench/test/fixtures/local-model.yaml` was stale even though it said `schemaVersion: "0.5"`. A line-wise comparison found omissions/differences in 0.2–0.4 backward-compatibility notes, canonical `equals` source semantics, explicit no-transitive-closure and exclusion of `Connection.exposes`, cross-owner review handling, and definitionless Interface validation.
   - It was replaced **only in the Workbench fixture**, directly from the governed `99_System/03_Schemas/local-model.yaml`; Git reports both files have the **identical blob SHA `361dee8269f9fbdfd16bcee33a1b808015f7ba5a`** after the fix.
   - No change was made to the canonical schema, importer algorithm, Workbench parser, or plugin binary.
4. **Automated release gate:** Added `.github/workflows/release-contract-step10.yml` for this staging branch. It checks the four reference entries and release-status/pin invariants, runs the generated `.obsidian/plugin-lock.yaml` checker in read-only `--check` mode, builds a fresh disposable Base Vault, executes the **existing authoritative** `Base Vault/Testing/check-release.py --base ... --workbench 55_Workbench`, and then Workbench `npm ci`, `typecheck`, `npm test`, and production build. The checker output is retained as a GitHub Actions log artifact.

## Evidence and honest gate distinctions

- [Initial check 37976840173](https://github.com/spencerskelly/Test_Vault_/actions/runs/37976840173) identified **1 FAIL** for Workbench's local-model fixture mismatch and **4 WARN**. The prior four *missing recovery document* failures were already resolved by the registry entries; the one fixture defect was **not ignored or silenced**.
- [Final CI run 37976987887](https://github.com/spencerskelly/Test_Vault_/actions/runs/37976987887) completed **success**. The original checker reported exactly **0 fail, 4 warn**. Workbench **448 tests passed / 0 failed**, typecheck and build passed on the exact governed fixture. `update-plugin-lock.py --check` passed with no generated changes, and the candidate Base Vault built successfully.
- The CI job being green means **pre-release contract consistency is restored**, not that the release is issued or that manual Obsidian interactions were completed.

### Four deliberately preserved warnings

1. Bootstrap generated plugin lock is `0.3.1`, matching the verified *candidate* source; canonical manifest pinned runtime remains `0.3.0`. The checker explicitly permits this state **only for pre-release**. Do not patch the pin or manually edit lock YAML before approved first-open/startup and plugin provenance checks.
2. No release-conformant importer has been formally issued, though v0.8.19 candidate has passed gated source and whole-QEAX acceptance.
3. The controlled `0.8.0` Base Vault repository has not been issued.
4. Non-current executable importer revision directories `v0.8.6`–`v0.8.18` remain under `Importer/Tools` pending controlled archive and reference audit.

## Remaining blockers

- **Workbench BOM A-14** work on `MDSE_Workbench/proposal/bom-a14-readonly-quantity-uom` still diverges from accepted WB-129 Local Model 0.5. Preserve version/history and reconcile it in a separate, testable branch without reverting 0.5 BindingConnector semantics.
- **Manual Obsidian user acceptance:** edit/restart/persistence for contextual Interface identifier, plugin startup and Bootstrap first-open are not proven by headless QEAX validation.
- **Workstation-local work audit** remains necessary before archiving the standalone Workbench source repo.
- **Numbered directory moves:** `Definitions` → `11_Definitions`, `Importer` → `22_Importer`, `Base Vault` → `33_Base Vault`, `Bootstrap` → `44_Bootstrap`; patch active release scripts/CI/links atomically before claiming a stable development vault. `55_Workbench` and `66_Testing` have already been established.
- No `main` branch, source Workbench repository, old PR or throwaway import repo was mutated/removed.

**Next bounded Step 11:** inspect the current BOM A-14 source and conflict paths against the tested WB-129 + importer staging commit, stage a read-only merge rehearsal and test its existing model invariant coverage. If BOM compatibility passes, persist it separately; do not move numbered roots at the same time.
