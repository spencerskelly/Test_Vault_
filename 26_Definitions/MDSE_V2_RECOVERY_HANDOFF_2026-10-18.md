# MDSE V2 — Recovery handoff (2026-10-18)

**Status: NOT WORKING / NOT RELEASE READY.** This is the restart entrypoint, not a completion claim. An extended portable handoff with exact prototype SHA-256 values is supplied as `MDSE_V2_Recovery_Handoff_2026-10-18.zip` in the conversation.

## Actual state
Reduced QEAX SHA-256 `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822`; 11,447 objects; 14,688 connectors; 1,389 packages. 2,208 diagrams **excluded**. Exact source-family resolver recognizes 60 element and 26 connector groups, but this is not validation of native SysML v2 emission.
The recent HTML prototypes in conversation are **unverified**: `MDSE_QEAX_to_MD_Importer.html`, `MDSE_QEAX_to_MD_Importer_v2_Base_Integrated.html`, `MDSE_QEAX_to_SysMLv2_Importer.html`. The latest emits example native declarations but **does not prove complete legal native relationship/usage output, parser acceptance, browser conversion, or Obsidian first-open acceptance**. These prototypes should be migrated into a single governed source in `21_Importer`, not treated as working releases.
`20_Base Vault/build_v2_test_base.py` generates an uninitialized reference-only base with `plugin_ready=false` and `native_import_ready=false`. `20_Base Vault/stage_v2_locked_plugins.py` requires compiled certified V2 Bootstrap and Workbench plugin binaries and real test evidence; presence of staging code is **not** a runnable plugin.

## Owner-approved requirements (do not reopen)
- The **HTML importer owns first-time Base Vault creation** and native QEAX -> Markdown + SysML v2 output. On later reimport, preserve identity, annotations and configuration.
- Native SysML v2 definitions/usages/relationships wherever semantics and parser allow; no invented custom SysML relationships. Keep MDSE evidence separate.
- Copy/alias mergers only for equivalent identity; consolidate meaningful content and separately retain all connector provenance. Definition and owned usage remain distinct; shared physical parts have one definition and contextual usages.
- Packages organize folders without determining semantic owner or creating redundant Package notes. Combine Boundaries in one source-traceable descriptive note.
- Preserve full/proxy/binding ports, part/port usages and connection distinction, independent aggregation/specialization/allocate/verify/satisfy/derive/refine/trace meanings. Use approved mapping authorities rather than generic fallbacks.
- Use `flagLink` and `flagNote` for isolated unresolved connectors/usages, with source identities and explanatory note lines; don't block the functional import for a handful of outliers.
- Attachments belong to owning engineering notes. No orphan links. Authoritative native SysML note text controls Workbench; stale graph freezes and requests refresh.
- Keep source QEAX and row ledger private; deterministic reimports with stable IDs, evidence fingerprinting, diff/conflict preview and no silent edit loss.
- **EA diagram extraction/translation/Canvas seeding excluded until after tools and golden import accepted.**

Authority: [STEP-00](STEP_00_APPROVED_MODEL_HANDLING_CLARIFICATIONS_2026-10-18.md), [Diagram deferral](STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md), [Titled steps](V2_NEXT_STEP_TITLES_2026-10-18.md), [Source/vault controls](../24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md), [STEP-03Z plugin reality](STEP_03Z_LOCKED_V2_PLUGIN_PACKAGING_2026-10-18.md).

## What failed
Disconnected ledgers and source classification absorbed effort without an end-to-end native writer. Unverified conversation HTML versions drifted from the registry. Minimal Base Vault lacked Bootstrap startup. No pinned complete release linked browser libraries, semantic rules, native parser, plugin hashes, generated vault and acceptance tests. Markdown references are reported broken: **a full repository-wide broken-link inventory has not yet been produced**. Prior claims of a working importer were premature.

## Immediate execution sequence
1. Make this file and a consolidated importer README the sole active starting points; audit **all active Markdown relative links** (paths/case/anchors) and fix primary MOC navigation. Inventory historical references and archive separately; don't delete approved decisions.
2. Move one HTML importer source into `21_Importer` with pinned library versions and tests; reuse `21_Importer/v2_approved_family_resolver.py` and `24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json`.
3. Implement an actual typed canonical graph -> valid SysML v2 writer with approved relationship/usage rules; embed/link it from engineering Markdown while retaining all meaningful evidence. Exclude diagrams.
4. Enforce official pinned SysML v2 parser and total 11,447+14,688 source disposition coverage; don't turn candidates into accepted native output without proof.
5. Integrate build/test of certified V2 Bootstrap and Workbench in new-model ZIP. Opening the ZIP in Obsidian **must actually run Bootstrap**, not merely contain a folder; fail readiness if binaries missing.
6. Execute the **real HTML browser conversion** on the reduced QEAX, inspect extracted ZIP, run parser and link checker, open in Obsidian, verify first-open/Workbench, then repeat for idempotence. Only then consider full QEAX and a golden import.

## Binary acceptance
- [ ] Browser imports reduced QEAX and creates complete ZIP
- [ ] Native SysML parses with pinned official parser and key relationships/usages are present
- [ ] Every 11,447 object and 14,688 connector has one accountable disposition/target or explicit review flag
- [ ] Generated MD links, attachments and source-to-target references are valid
- [ ] First-open generated vault starts V2 Bootstrap and working Workbench
- [ ] Identical reimport makes no semantic changes and preserves annotations
- [ ] Active repository Markdown links pass automated validation
- [ ] Evidence and release manifest checked into main; proprietary model data absent

## Restart prompt
> Continue MDSE V2 from `26_Definitions/MDSE_V2_RECOVERY_HANDOFF_2026-10-18.md`. The importer is **not working**. Audit active documentation/links, then implement one actual HTML QEAX -> approved canonical graph -> parser-valid native SysML v2 + Markdown -> Bootstrap-enabled V2 Base Vault ZIP vertical slice. Use October 15 reduced QEAX (11,447 objects / 14,688 connectors), preserve approved STEP-00 semantics, don't touch EA diagrams, and use flags for isolated outliers. Do not report success before browser + parser + Obsidian verification.