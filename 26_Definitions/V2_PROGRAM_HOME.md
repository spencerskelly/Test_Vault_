# MDSE v2 — Program Navigation

**Start here for all v2 work.** This is a link/index page, not a new semantic rulebook. The independent v2 workspace stays in numbered folders; historical assets are references, never v2 runtime dependencies.

## Program and approval
- [Goals, major tasks, estimated completion, and acceptance](V2_PROGRAM_GOALS_AND_COMPLETION_2026-10-18.md)
- [Approved phased release and architecture decisions](V2_RELEASE_ARCHITECTURE_DECISIONS_2026-10-18.md)
- [Approved translation baseline and golden test handoff](APPROVED_V2_TRANSLATION_BASELINE_AND_TEST_HANDOFF_2026-10-18.md)
- [Full-program recovery and strategic gaps](V2_FULL_PROGRAM_RECOVERY_AND_ALIGNMENT_2026-10-18.md)
- [Prior work audit and avoidance of duplicate analysis](V2_PRIOR_WORK_RECOVERY_AUDIT_2026-10-18.md)
- [Detailed implementation traceability and gaps](V2_IMPLEMENTATION_TRACEABILITY_AUDIT_2026-10-18.md)

## Definitions and conversions — approved authority
- [Connector and native construct definition index](V2_CONNECTOR_DEFINITIONS_INDEX.md)
- [October 17 approval: 60 element families](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md)
- [October 17 approval: 26 relationship families](../24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md)
- [Aggregation disposition: all 2,267 connectors](../24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_RECONCILIATION_2026-10-17.md)
- [Common eligibility and Workbench operation policy](../24_Workbench/docs/SYSML_V2_PHASE3_CENTRAL_RELATIONSHIP_REGISTRY.md)
- [Help/definitions panel specification](../24_Workbench/docs/SYSML_V2_RELATIONSHIP_REFERENCE_AND_HELP_PANEL.md)

## Data and implementation register
- [Approved semantic rules vs active runtime divergence register](v2_approved_runtime_divergences.v0.1.json)
- [V1→V2 reusable capability ledger (28 entries)](V1_V2_REUSE_LEDGER_INDEX.md)
- [Detailed technical analysis, known mismatches, and target Obsidian architecture](V1_V2_DEEP_TECHNICAL_RECOVERY_AND_PLATFORM_ARCHITECTURE_2026-10-18.md)
- [Machine-readable reuse ledger](v1_to_v2_reuse_ledger.v0.1.json)
- [Machine-readable 60+26 family inventory](v2_mapping_family_recovery.v0.1.json)
- [Approved family versus provisional selector crosswalk](v2_executable_candidate_crosswalk.v0.1.json)
- [Workstream traceability register](v2_recovery_traceability.v0.1.json)
- [Executable selector mismatch and gaps](V2_EXECUTABLE_CANDIDATE_GAP_REVIEW_2026-10-18.md)
- [Source reconciliation and vault write contract](../24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md)
- [BOM-to-v2 integration review](../24_Workbench/docs/BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md)

## Tools, validation and delivery
- [Base Vault](../20_Base%20Vault/README.md)
- [EA importer](../21_Importer/README.md)
- [Bootstrap and team configuration](../23_Bootstrap/README.md)
- [Workbench](../24_Workbench/README.md)
- [Testing](../25_Testing/README.md)
- [SysML v2 translator history and passes](../29_SysMLv2_Translator_Workbench/README_SysMLv2_Translator_Workbench.md)
- [Phase 8/9 trusted direction and canonical evidence](../24_Workbench/docs/SYSML_V2_PHASE8_CONNECTOR_NORMALIZATION.md)
- [First-run fast track and release audit](../29_SysMLv2_Translator_Workbench/FIRST_RUN_FAST_TRACK_DEPENDENCY_RULES_DOC_AUDIT_2026-10-17.md)

## How to find the right authority
1. Product priority and percentages → goals file.
2. Whether a semantic conversion is approved → dedicated October 17 definition file, then 60/26-family reconciliation.
3. Runtime availability → executable crosswalk, actual implementation file and test (not approval wording alone).
4. Current release status → CI/parser/UI evidence at an exact commit; do not infer from file presence.
5. Proposal conflicts → retain original proposal as historical; subsequent explicit approval takes precedence. Record a discrepancy instead of silently changing a rule.

## Vault linking and maintenance
Use Markdown relative links for GitHub compatibility and Obsidian readability; they may be converted to vault wikilinks by the governed link resolver later. Do not duplicate definitions across pages. New approved concepts must be added to the dedicated definition, the family/register trace, the workstream owner, and the validation/test record. If an existing concept is found, **update its link and status instead of recreating it**.

Last inventory date: 2026-10-18. Exact UI/CI acceptance is not yet confirmed.
