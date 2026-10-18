# V2 import kit integration checkpoint

Status: **BLOCKED for runnable integrated release**; tools and preflight tests can continue.

## Target package
1. Self-contained, offline, single-file HTML importer with EA/QEAX and BOM Excel source adapters, generated embedded versioned semantic rulesets, source-profile drift detection, staged vault output and full local diagnostic export. A second HTML importer is acceptable only if it shares generated code and rules. Full-source scale/memory tests required.
2. Uninitialized controlled **base vault** produced by the governed `10_Base Vault/Tools/v0.8.0-r2/build-base.py`; includes all mapped runtime files, Obsidian plugin manifests, plugin lock, bootstrap and Workbench payloads. Initialization and author registration proceed using existing controlled base workflow. Build/import must target fresh copies, not existing human vaults.
3. **Workbench** Obsidian plugin with note-first SysML v2 authority and popup (Links, Structure, Behavior, Requirements dropdowns; Note Actions, Link Actions and collapsed Advanced Actions). Default automatic popup OFF, manually accessible command. Selected-item editing must source-rewrite the note's bottom SysML v2 section atomically, reparse and refresh all projections. Current popup launcher source exists but editable v2 code and runtime QA are not complete.
4. **Bootstrap** prebuilt/locked and governed by release manifest, capable of checking all plugin file hashes and author registration. Must be tested with the exact staged Workbench build, not older payload.
5. Release manifest is the single alignment gate for importer version and embedded rules hash, exact parser version, base builder, Workbench artifact version, Bootstrap artifact version, plugin lock hashes, and tests.

## Repository findings in current main
- `10_Base Vault/Definition/mdse-release.yaml` still names MDSE release 0.8.0, importer v0.8.19 (old EA-to-MDSE candidate), Workbench 0.1.18, and Bootstrap **0.3.0** with 0.3.1 candidate. This is not a SysML v2 release manifest.
- The vendored `10_Base Vault/Runtime/Plugins/mdse-bootstrap/manifest.json` is **0.3.1** while manifest active version is **0.3.0**; this is an explicit alignment failure to resolve with lock regeneration and promotion/test, not manual version-string patching.
- Vendored `mdse-workbench/manifest.json` is 0.1.18, pre-v2. The recent popup addition modifies `14_Workbench/src/main.ts` but has no documented newly compiled, locked runtime artifact or Obsidian test.
- Base builder exists and is positive-include/locked-plugin-driven. Previous candidate base checks do not certify the present v2 setup.
- Importer preflight tests validated reduced QEAX source (11,447 objects, 14,688 connectors); real Excel alternates-review workbook is not complete assembly BOM. Original `ALL_BOMs` workbook still needed for BOM structural acceptance. Native v2 parser and serializer not accepted.

## New executable release check
Run `python 15_Testing/check_v2_import_kit.py PATH_TO_TEST_VAULT_CHECKOUT --json`. This read-only validator flags known release discrepancies and missing v2 release declarations. It is intentionally fail-closed, and a GO requires more than merely fixing the visible string mismatches; supply actual parser and Workbench runtime test evidence.

## Execution path
A. Implement serializer, native parser and both source adapters with exact UID/ruleset policies; dry-run and reconcile every source record.
B. Build Workbench bundle with popup and note editing, run source/unit tests, and test inside Obsidian.
C. Build/promote Bootstrap and Workbench pinned payloads, regenerate lock and config, update release manifest with versions and hashes.
D. Generate fresh base vault using builder; run release validator and Bootstrap end-to-end startup check.
E. Import reduced QEAX into disposable base copy; independently import complete BOM workbook into another disposable base copy; check notes, sections, UIDs, relationships, counts, log output, second identical run, and Workbench UX.
F. Repeat on full EA QEAX and expanded Excel formats, testing performance and source-drift errors; only then label integrated kit ready.

Never put raw model rows or original spreadsheets into Test_Vault_. No claims of packaged runnable v2 importer or shipped updated plugin until those outputs exist.
