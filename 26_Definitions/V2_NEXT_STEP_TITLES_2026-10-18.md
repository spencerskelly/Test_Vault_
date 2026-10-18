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
