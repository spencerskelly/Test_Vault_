---
title: MDSE v2 — Master Map of Contents
type: map-of-contents
status: active-navigation
owner: MDSE v2 program
updated: 2026-10-18
scope: toolchain-development-repository
---
# MDSE v2 — Master Map of Contents

> **Start here.** This note indexes the tools, approved semantics, source translators, workstreams, verification and retained project history. Links point to the owning document or folder; this map **does not supersede** those authorities. This is the development repository, **not a complete generated engineering model**. Imported model content and private QEAX/BOM ledgers remain local.

## 00 — Program status and next work
- [Program goals, subwork, evidence-based completion estimates](26_Definitions/V2_PROGRAM_GOALS_AND_COMPLETION_2026-10-18.md)
- [Program workbench and navigation home](26_Definitions/V2_PROGRAM_HOME.md)
- [Approved first-release scope and architecture decisions](26_Definitions/V2_RELEASE_ARCHITECTURE_DECISIONS_2026-10-18.md)
- [Approved v2 translation baseline](26_Definitions/APPROVED_V2_TRANSLATION_BASELINE_AND_TEST_HANDOFF_2026-10-18.md)
- [Program recovery, architecture questions and gaps](26_Definitions/V2_FULL_PROGRAM_RECOVERY_AND_ALIGNMENT_2026-10-18.md)
- [Workstream-level implementation traceability](26_Definitions/V2_IMPLEMENTATION_TRACEABILITY_AUDIT_2026-10-18.md)
- [Why the prior aggregation work must not be repeated](26_Definitions/V2_PRIOR_WORK_RECOVERY_AUDIT_2026-10-18.md)
- [Current approved-to-runtime mismatch report](26_Definitions/V2_EXECUTABLE_CANDIDATE_GAP_REVIEW_2026-10-18.md)

## 10 — Model language, definitions and relationships
- [Definitions area](26_Definitions/README.md)
- [Native connector/semantic operation definition index](26_Definitions/V2_CONNECTOR_DEFINITIONS_INDEX.md)
- [Reviewed SysML v2 relationship concepts and Workbench help](24_Workbench/docs/SYSML_V2_RELATIONSHIP_REFERENCE_AND_HELP_PANEL.md)
- [Central operation eligibility contract](24_Workbench/docs/SYSML_V2_PHASE3_CENTRAL_RELATIONSHIP_REGISTRY.md)
- [60 EA element families: approved individual dispositions](24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md)
- [26 EA relationship families: approved individual dispositions](24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md)
- [Aggregation: approved shared and composite semantics](24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_SHARED_COMPOSITE_USAGE_APPROVED_2026-10-17.md)
- [Aggregation: all 2,267 source classifications](24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_RECONCILIATION_2026-10-17.md)
- [Aggregation: stable role/usage naming](24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_USAGE_NAMING_APPROVED_2026-10-17.md)
- [Flow definition](24_Workbench/docs/SYSML_V2_FLOW_APPROVED_MAPPING.md)
- [Interface definition](24_Workbench/docs/SYSML_V2_INTERFACE_APPROVED_MAPPING.md)
- [State-transition definition](24_Workbench/docs/SYSML_V2_STATE_TRANSITIONS_APPROVED_MAPPING.md)
- [Dependency definition](24_Workbench/docs/SYSML_V2_DEPENDENCY_APPROVED_MAPPING.md)
- [Allocation, Perform and Exhibit distinction](24_Workbench/docs/SYSML_V2_EA_ALLOCATION_ELEMENT_TYPE_DECISION.md)
- [Text/source ownership and note storage (historical proposal; see approved bottom-section rule)](26_Definitions/SysML%20Source%20Ownership%20and%20Note%20Storage.md)

## 20 — Source adapters, identity and modeling data
- [EA importer home](21_Importer/README.md)
- [Source reconciliation, privacy and staged write safeguards](24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md)
- [Read-only element candidate projector](21_Importer/project_v2_element_candidates.py)
- [Read-only connector candidate projector](21_Importer/project_v2_relationship_candidates.py)
- [Connector-end evidence audit](21_Importer/v2_connector_end_evidence.py)
- [Connector evidence validation](21_Importer/v2_validate_connector_evidence.py)
- [EA phase 8 normalization](24_Workbench/docs/SYSML_V2_PHASE8_CONNECTOR_NORMALIZATION.md)
- [Source-bound direction bridge](25_Testing/phase9_source_direction_bridge.py)
- [BOM → SysML v2 integration, quantity and identity contracts](24_Workbench/docs/BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md)

## 30 — Software tools, base and human interface
- [Base Vault tools](20_Base%20Vault/README.md) · [Test-base builder](20_Base%20Vault/build_v2_test_base.py)
- [Importer tools](21_Importer/README.md)
- [Bootstrap and managed configuration](23_Bootstrap/README.md)
- [Workbench tools](24_Workbench/README.md) · [Read-only prototype](24_Workbench/v2-workbench.html) · [MVP](24_Workbench/V2%20Workbench%20MVP.md)
- [Workbench readiness and UX gates](24_Workbench/docs/SYSML_V2_BUILD_READINESS_STABILITY_UX_GATE_2026-10-17.md)
- [Cross-vault resolver planning and retained history](66_Cross-Vault/README.md)

## 40 — Testing, parser, release and source integrity
- [Testing home](25_Testing/README.md)
- [Golden Charger SysML fixture](25_Testing/Fixtures/Golden%20Charger%20v2/README.md)
- [Official parser runner](25_Testing/sysml2_parser_runner.py)
- [Official parser attestation](25_Testing/sysml2_parser_attestation.py)
- [Phase 8 full-row source verification](25_Testing/verify_phase8_rows_against_qeax.py)
- [V2 recovery register checks](25_Testing/test_v2_recovery_traceability.py)
- [60+26 family completeness checks](25_Testing/test_v2_mapping_family_recovery.py)
- [Candidate runtime coverage check](25_Testing/test_v2_executable_candidate_crosswalk.py)
- [Main v2 workflow](.github/workflows/v2-migration-executable-repair.yml)
- [First-run dependency and release audit](29_SysMLv2_Translator_Workbench/FIRST_RUN_FAST_TRACK_DEPENDENCY_RULES_DOC_AUDIT_2026-10-17.md)
- [SysML v2 project history and sequential passes](29_SysMLv2_Translator_Workbench/README_SysMLv2_Translator_Workbench.md)

## 50 — Machine-readable registers
- [Workstream recovery and implementation status](26_Definitions/v2_recovery_traceability.v0.1.json)
- [60 element + 26 connector approval records](26_Definitions/v2_mapping_family_recovery.v0.1.json)
- [Provisional candidate-selector crosswalk](26_Definitions/v2_executable_candidate_crosswalk.v0.1.json)
- [Pinned semantic registry](24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json)
- [Native-candidate decision register](24_Workbench/registry/sysml_v2_semantic_decisions.v0.1.json)
- [Family disposition registry](24_Workbench/registry/family_disposition_registry.v0.2.json)

## 60 — Project background and retained knowledge
- [Workspace governance and older decisions](55_Workspace/README.md)
- [Earlier development and approvals: historic reference only](26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json)
- [Shared tool/runtime model schemas (check v2 authority before use)](99_System/)
- [Cross-cutting reference and research](88_Reference/)
- [V2 research / Phase 5–9 passes](29_SysMLv2_Translator_Workbench/README_SysMLv2_Translator_Workbench.md)

## 70 — Known missing coverage / avoid duplicated work
| Gap | Why it matters | Next action |
|---|---|---|
| Individual native definitions for Binding, ports/conjugation, requirement operations, attributes/units, analysis and causation | Reviewed in prior discussions but not all individually linked and verified in active catalog | Find existing approval first; add exact link + status, not a duplicate decision |
| Approved vs provisional runtime rules | Only 2 exact element selectors, 26 wildcard and 32 unmatched in provisional candidate registry | Reuse October 17 60-family approval, implement exact precedence without changing approved semantics |
| Native emission, note writer, parser acceptance | Rules and evidence exist; first-release generated output not accepted | Integrate existing graph and parser to a disposable v2 base |
| Read-only Workbench integration | Prototype exists, but imported model end-to-end UX unverified | Exercise generated model and linked definitions/where-used |
| Release configuration and CI | Versioned paths and workflows exist; current CI pass not independently confirmed | Pin checkout and verify results, upgrade and rollback contracts |
| Full repository file coverage | This curated MOC is **not yet every file** | Generate a full repository inventory locally, link every major folder to its index, and report orphans automatically |
| Historical external assets | Older conversations, branches and other repos may contain useful work | Inventory by source and reconcile with active authority; never overwrite approved rules |

## Maintenance contract — always apply
1. **Find before creating:** search this MOC → authoritative mapping/decision → machine-readable register → existing implementation/test → archive/reference if necessary.
2. Never call a file `complete` merely because it exists; track approved, implemented, synthetic-tested, real-source-tested, parser-accepted, GUI-accepted and released separately.
3. Each new approved operation must be linked from its owning concept definition, the 60/26 family register where applicable, its runtime operation and test, and this MOC.
4. New folder or workstream must have an index/README and an entry here. Document supersession instead of maintaining multiple competing copies.
5. Do not embed raw QEAX, proprietary model elements, BOM data or private disposition ledgers in this public development repository.
6. Run [the MOC link integrity test](25_Testing/test_v2_master_moc.py) on CI and review its findings alongside implementation traceability.
