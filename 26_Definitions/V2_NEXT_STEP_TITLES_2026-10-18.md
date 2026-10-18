# V2 implementation — titled steps

[Master MOC](../MOC_MDSE_V2.md) · [Scored goals](V2_PROGRAM_GOALS_AND_COMPLETION_2026-10-18.md)

These step titles are stable handoff IDs. Completion percentages are current planning estimates, not release certification.

| Step | Scope | Completion |
|---|---|---:|
| STEP-01 — Decision authority and recovery | G01 | 55% |
| STEP-02 — Native SysML mapping resolver | G02 | 45% |
| STEP-03 — Canonical graph, UID and provenance | G03 | 35% |
| STEP-04 — QEAX importer and no-loss ledger | G04 | 40% |
| STEP-05 — Native text, notes and parser | G05 | 25% |
| STEP-06 — Base Vault and plugin packaging | G06 | 30% |
| STEP-07 — Read-only Obsidian Workbench | G07 | 25% |
| STEP-08 — Golden import and release validation | G08 | 35% |
| STEP-09 — Transactional editing and reimport | G09 | 15% |
| STEP-10 — BOM import and configuration | G10 | 25% |
| STEP-11 — Team updates and Git governance | G11 | 20% |
| STEP-12 — Cross-vault and deployment lifecycle | G12 | 15% |

STEP-01–08 constitute the approved first-release scope. STEP-09–12 are later-phase work. Always search the owning definition, history, code and tests before implementing a step.

## Source reuse register

STEP-01: [Original approved native decisions](MOC_Catalogs/sysml_decisions_1.md) and [V1 recovery ledger](V1_V2_REUSE_LEDGER_INDEX.md). Decision inventory is recovered; implementation linkage is not complete.

STEP-02: [60-family approval](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md) and [12 exception cases](V2_APPROVED_EXCEPTION_HANDLING_AUDIT_2026-10-18.md). Implement exact selectors, not new mapping policy.

STEP-03: [Typed canonical graph](../24_Workbench/registry/runtime/canonical-model.mjs) and [V1 ModelRef identity contract](../100_Archive/V1/14_Workbench/WB106_IMPLEMENTATION_CONTRACT.md). Stable usage IDs, source GUIDs, aliases and review flags require writer-level integration.

STEP-04: [Reduced EA family census](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_FIRST_EXECUTION_2026-10-17.md), [Phase 8 source normalization](../24_Workbench/docs/SYSML_V2_PHASE8_CONNECTOR_NORMALIZATION.md). Reconcile source data against generated native and non-native outputs.

STEP-05: [Official parser smoke-test result](../29_SysMLv2_Translator_Workbench/Passes/PASS07_FIRST_PASSING_NATIVE_PARSER_GATE_2026-10-17.md). Real-source native emitter and note writer remain pending.

STEP-06: [Archived plugin lock baseline](../100_Archive/V1/10_Base%20Vault/Definition/Enabled%20Plugin%20Stack.md). The V2 base builder exists; plugin-ready packaging remains pending.

STEP-07: [Workbench interaction contract](../24_Workbench/docs/SYSML_V2_DRAW_TO_RELATE_AND_VAULT_DEFINITIONS_CONTRACT.md) and [historical Obsidian indexer](../100_Archive/V1/14_Workbench/src/obsidian/indexer.ts). Native read-only Obsidian integration remains pending.

STEP-08: [Scoped migration CI](../.github/workflows/v2-migration-executable-repair.yml) and [source/no-loss gates](../24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md). Synthetic CI passes; golden source→parser→GUI acceptance is not established.

STEP-09: [Archived transaction manager](../100_Archive/V1/14_Workbench/src/core/transaction.ts) and [source reconciliation](../100_Archive/V1/14_Workbench/src/core/source-reconciliation.ts) are reusable design/test sources. Transactional native-text editing follows the read-only release.

STEP-10: [BOM integration review](../24_Workbench/docs/BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md) and [XLSX adapter test work](../29_SysMLv2_Translator_Workbench/Passes/PASS06_BOM_XLSX_ADAPTER_2026-10-17.md). Real assembly, formulas, units and configuration acceptance remain open.
