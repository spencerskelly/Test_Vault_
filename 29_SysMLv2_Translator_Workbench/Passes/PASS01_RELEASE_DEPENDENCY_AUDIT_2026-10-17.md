# Pass 01 — Release dependency audit (completed)

**Scope:** Audit only. No release manifest, plugin payload, plugin lock, source model, or live vault mutated.  
**Result:** BLOCKED for combined v2 release; evidence and targeted Pass 02 remediation ready.

## Verified from current Test_Vault_ main via connected GitHub
1. **Path migration drift.** The release manifest `10_Base Vault/Definition/mdse-release.yaml` contains **104 textual old-prefix occurrences**: `Base Vault/` 15, `Importer/` 15, `Bootstrap/` 6 and `00_Workspace/` 68. This is an occurrence census **including comments and historical registered documents**, **not** 104 broken runtime paths. Separate active paths before patching; historical and human prose are not bulk-rewritten.
2. **Active entrypoints at risk.** `tools.cleanBase.builder` and `runtimePlugins.payload/configGenerator/lockGenerator` reference old unnumbered paths; runtimeBase include/mapped paths also need per-path existence validation. Existing `10_Base Vault/Tools/v0.8.0-r2/build-base.py` uses manifest paths directly, so its output cannot be declared verified without fixing source paths.
3. **Bootstrap version mismatch.** Vendored `10_Base Vault/Runtime/Plugins/mdse-bootstrap/manifest.json` = **0.3.1**; root `.obsidian/plugin-lock.yaml` pins **0.3.1**; release YAML tools.bootstrap.version = **0.3.0**. Lock and payload version agree with each other; active release declaration does not. Do not downgrade or blindly promote to reconcile.
4. **Workbench binary remains legacy.** `14_Workbench/package.json` and shipped plugin manifests report **0.1.18**, while latest `14_Workbench/src/main.ts` has new popup code not proven built into shipped `main.js`. Native SysML v2 editor and four real navigation dropdowns are still incomplete.
5. **CI migration drift.** `.github/workflows/importer-candidate.yml` watches `Importer/**` but not `11_Importer/**`; its release command still invokes `Base Vault/Testing/check-release.py`. Its green status cannot be inferred from past v1 logs or empty commit-status API data.
6. **Missing release authority for native v2.** YAML tools.importer.candidate still points at historical v0.8.19 EA→MDSE HTML; there is no accepted v2 importer/parser release pin. Keep legacy profile and v2 candidate lane separate.
7. **Reproducibility limits.** External command-line checkout from this execution environment was not possible (GitHub DNS unavailable); current-root full-tree execution of `15_Testing/check_v2_import_kit.py` and `10_Base Vault/Testing/check-release.py` is **NOT CLAIMED**. Audit evidence is remote source fetches, not a successful build or CI validation. Preserve that distinction.

## Step 01 exit checklist
- [x] Identify release manifest authority and current numbered directories.
- [x] Inspect importer/base/Bootstrap/Workbench manifests and lock versions.
- [x] Detect old CI paths and identify affected v2 triggers.
- [x] Separate old documentation references from operational path breakage.
- [x] Record fail-closed checker entrypoint and source-specific source-profile risks.
- [x] Leave all release pins, lock hashes and live model data untouched.
- [ ] Complete checkout-level release checker execution (first action after Pass 02 paths repaired).

## Pass 02 handoff — precise action
**Repair only active, machine-consumed references.** Patch path fields in release YAML for builder, runtimePlugin payload/generators, importer candidate/source profile locations and runtime-base include/mapped files; preserve historical documents and published v1 mappings. Update the base release-check script and affected current CI path triggers/commands for numbered layout. Add a focused synthetic/structural negative-path check; do not alter plugin versions or mark v2 ready. Pass only when a fresh base candidate can be generated and its release check produces actionable results in a checkout.

**Pass status:** COMPLETE as remote audit and documentation. **Release gate:** BLOCKED. **Next response requires user `y`**.
