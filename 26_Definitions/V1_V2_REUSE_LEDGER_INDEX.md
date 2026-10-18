# V1 → V2 Reuse Ledger — Human Navigation

[Current V2 MOC](../MOC_MDSE_V2.md) · [V1 Archive MOC](../100_Archive/MOC_V1_ARCHIVE.md) · [Machine ledger](v1_to_v2_reuse_ledger.v0.1.json) · [Deep technical audit](V1_V2_DEEP_TECHNICAL_RECOVERY_AND_PLATFORM_ARCHITECTURE_2026-10-18.md)

**Status:** 28 recoverable capabilities identified from the manifest and selected code inspection; none certified ported. This index is designed for navigation, implementation ownership and avoiding repeated reviews. The archive is immutable; reuse is via new v2 code and tests. A V2 link marks a destination or related implementation, *not* functional parity.

| Category | Count |
|---|---:|
| First-release dependencies | 21 |
| Later-phase capabilities | 7 |
| Unique entries | 28 |

## P0 — First critical path / core correctness (16)

### R01 — QEAX source fidelity and dual-stage evidence

**Goal:** G04 · **Milestone:** First release · **Disposition:** `retain_source_contract` · **Port validation:** pending

- Historical source: [Importer Operating Contract.md](../100_Archive/V1/11_Importer/Definition/Importer%20Operating%20Contract.md)
- V2 reference: [project_v2_element_candidates.py](../21_Importer/project_v2_element_candidates.py)
- **Next action:** Integrate preflight, mechanical/source ledger and independent semantic disposition; forbid silent coercion

### R02 — Model scale deterministic whole import

**Goal:** G04 · **Milestone:** First release · **Disposition:** `test_method_port` · **Port validation:** pending

- Historical source: [FULL_IMPORT_EXECUTION_STATUS.md](../100_Archive/V1/11_Importer/Testing/v0.8.19/FULL_IMPORT_EXECUTION_STATUS.md)
- V2 reference: [run_gated_phase8.py](../25_Testing/run_gated_phase8.py)
- **Next action:** Reproduce deterministic output comparisons on fresh v2 bases; v1 success does not certify native output

### R03 — Path planning performance and growth

**Goal:** G04 · **Milestone:** First release · **Disposition:** `test_method_port` · **Port validation:** pending

- Historical source: [path_planning_scalability_regression_test.js](../100_Archive/V1/11_Importer/Testing/v0.8.19/path_planning_scalability_regression_test.js)
- V2 reference: **No identified active target**
- **Next action:** Preserve no-quadratic path planner test for >27000 notes and acceptance at v2 scale

### R05 — Port/binding exposure and ambiguity

**Goal:** G02 · **Milestone:** First release · **Disposition:** `semantic_reference_not_port` · **Port validation:** pending

- Historical source: [imp011_binding_review_acceptance.py](../100_Archive/V1/11_Importer/Testing/v0.8.19/imp011_binding_review_acceptance.py)
- V2 reference: [SYSML_V2_INTERFACE_APPROVED_MAPPING.md](../24_Workbench/docs/SYSML_V2_INTERFACE_APPROVED_MAPPING.md)
- **Next action:** Protect port/binding/exposure distinctions and review cases; never import v1 equals/exposes as custom native v2 relationships

### R06 — EA connector roles and original direction

**Goal:** G03 · **Milestone:** First release · **Disposition:** `partial_recovery` · **Port validation:** pending

- Historical source: [audit_ea_connector_roles.py](../100_Archive/V1/15_Testing/audit_ea_connector_roles.py)
- V2 reference: [phase9_source_direction_bridge.py](../25_Testing/phase9_source_direction_bridge.py)
- **Next action:** Apply trusted direction audit before native semantics; reuse source validation patterns

### R07 — Stable note and occurrence identity

**Goal:** G03 · **Milestone:** First release · **Disposition:** `architecture_partial` · **Port validation:** pending

- Historical source: [WB106_IMPLEMENTATION_CONTRACT.md](../100_Archive/V1/14_Workbench/WB106_IMPLEMENTATION_CONTRACT.md)
- V2 reference: [canonical-model.mjs](../24_Workbench/registry/runtime/canonical-model.mjs)
- **Next action:** Keep definition UID and separate owner-scoped usage identity; migrate ModelRef concept, not old runtime fields

### R08 — Owned usage topology and reverse where-used

**Goal:** G03 · **Milestone:** First release · **Disposition:** `algorithm_reference` · **Port validation:** pending

- Historical source: [localmodel_topology_index_v3.py](../100_Archive/V1/15_Testing/consolidation/localmodel_topology_index_v3.py)
- V2 reference: [canonical-model.mjs](../24_Workbench/registry/runtime/canonical-model.mjs)
- **Next action:** Rebuild topology and inbound usage indexes from parsed SysML features with stable identity

### R09 — Workbench incremental indexer and hydration

**Goal:** G07 · **Milestone:** First release · **Disposition:** `missing_parity` · **Port validation:** pending

- Historical source: [indexer.ts](../100_Archive/V1/14_Workbench/src/obsidian/indexer.ts)
- V2 reference: [v2-workbench.html](../24_Workbench/v2-workbench.html)
- **Next action:** Port cooperative chunking, startup metadata burst debouncing and incremental owner hydration; v2 HTML preview is not a full Obsidian plugin

### R10 — Reverse dependency invalidation and rename safety

**Goal:** G07 · **Milestone:** First release · **Disposition:** `algorithm_reference` · **Port validation:** pending

- Historical source: [relationship-dependencies.ts](../100_Archive/V1/14_Workbench/src/core/relationship-dependencies.ts)
- V2 reference: **No identified active target**
- **Next action:** Reuse targeted re-resolution for renamed/moved notes; add >10k candidate fallback and benchmarks

### R15 — Workbench real-vault acceptance tests

**Goal:** G07 · **Milestone:** First release · **Disposition:** `test_method_port` · **Port validation:** pending

- Historical source: [Step18_Obsidian_UI_Acceptance.md](../100_Archive/V1/15_Testing/Step18_Obsidian_UI_Acceptance.md)
- V2 reference: [V2 Workbench MVP.md](../24_Workbench/V2%20Workbench%20MVP.md)
- **Next action:** Test first open and definition/usage navigation on real Obsidian host before calling GUI accepted

### R16 — Plugin lock/hash and release checker

**Goal:** G06 · **Milestone:** First release · **Disposition:** `missing_parity` · **Port validation:** pending

- Historical source: [check-release.py](../100_Archive/V1/10_Base%20Vault/Testing/check-release.py)
- V2 reference: [build_v2_test_base.py](../20_Base%20Vault/build_v2_test_base.py)
- **Next action:** Build independent v2 compatibility manifest, lock+SHA assertions and actual first-open plugin-ready base

### R23 — Cross-repository audit and review

**Goal:** G01 · **Milestone:** First release · **Disposition:** `method_reference` · **Port validation:** pending

- Historical source: [STEP89_COMPLETE_FOUR_REF_TREE_AUDIT.md](../100_Archive/V1/15_Testing/consolidation/STEP89_COMPLETE_FOUR_REF_TREE_AUDIT.md)
- V2 reference: [v2_recovery_traceability.v0.1.json](../26_Definitions/v2_recovery_traceability.v0.1.json)
- **Next action:** Reconcile retained branches/refs by identity and SHA, detect undocumented changes before implementation

### R24 — Native runtime registry and semantic gates

**Goal:** G02 · **Milestone:** First release · **Disposition:** `needs_alignment` · **Port validation:** pending

- Historical source: [Translator Definition.md](../100_Archive/V1/11_Importer/Definition/Translator%20Definition.md)
- V2 reference: [eligibility-engine.mjs](../24_Workbench/registry/runtime/eligibility-engine.mjs)
- **Next action:** Do not copy legacy relation names; align eligibility engine to October 17 approved v2 semantics (shared/composite and family-specific priority)

### R25 — Port, action, state corpus regression methods

**Goal:** G08 · **Milestone:** First release · **Disposition:** `test_method_port` · **Port validation:** pending

- Historical source: [bindingconnector_review_disposition_regression_test.js](../100_Archive/V1/11_Importer/Testing/v0.8.19/bindingconnector_review_disposition_regression_test.js)
- V2 reference: [test_v2_mapping_family_recovery.py](../25_Testing/test_v2_mapping_family_recovery.py)
- **Next action:** Create v2 semantic negative fixtures for ambiguous binding/port/owner cases

### R26 — Importer crash/rollback guards

**Goal:** G08 · **Milestone:** First release · **Disposition:** `contract_reference` · **Port validation:** pending

- Historical source: [transaction_failure_regression_test.js](../100_Archive/V1/11_Importer/Testing/v0.8.19/transaction_failure_regression_test.js)
- V2 reference: [GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md](../24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md)
- **Next action:** Assert no approved vault mutation for failed plans, invalid native text, partial writes or collisions

### R27 — Release gate and source provenance

**Goal:** G08 · **Milestone:** First release · **Disposition:** `test_method_port` · **Port validation:** pending

- Historical source: [release_gate_regression_test.js](../100_Archive/V1/11_Importer/Testing/v0.8.19/release_gate_regression_test.js)
- V2 reference: [v2-migration-executable-repair.yml](../.github/workflows/v2-migration-executable-repair.yml)
- **Next action:** Pin artifacts and attestation; separate CI synthetic pass from source/parser/GUI/release outcomes

## P1 — High-value product parity and lifecycle (11)

### R04 — Document attachment conservation

**Goal:** G04 · **Milestone:** First release · **Disposition:** `source_evidence_contract` · **Port validation:** pending

- Historical source: [FULL_IMPORT_EXECUTION_STATUS.md](../100_Archive/V1/11_Importer/Testing/v0.8.19/FULL_IMPORT_EXECUTION_STATUS.md)
- V2 reference: **No identified active target**
- **Next action:** Add explicit t_document and attachment disposition/output parity, if attachments are within first-release import scope

### R11 — Semantic cache persistence and recoverability

**Goal:** G07 · **Milestone:** First release · **Disposition:** `algorithm_reference` · **Port validation:** pending

- Historical source: [cache-persistence.ts](../100_Archive/V1/14_Workbench/src/core/cache-persistence.ts)
- V2 reference: **No identified active target**
- **Next action:** Preserve disposable indexes and quiet/burst-aware writes; parsed SysML text remains authority

### R12 — Transaction history and undo/redo engine

**Goal:** G09 · **Milestone:** Later · **Disposition:** `algorithm_reference` · **Port validation:** pending

- Historical source: [transaction.ts](../100_Archive/V1/14_Workbench/src/core/transaction.ts)
- V2 reference: **No identified active target**
- **Next action:** Adapt pure transaction manager to parser-backed SysML AST write service and atomic vault changes

### R13 — Definition migration and inbound links

**Goal:** G09 · **Milestone:** Later · **Disposition:** `algorithm_reference` · **Port validation:** pending

- Historical source: [definition-note-migrate-service.ts](../100_Archive/V1/14_Workbench/src/core/definition-note-migrate-service.ts)
- V2 reference: **No identified active target**
- **Next action:** Preserve rename/redirect and transactional multi-note review but replace YAML semantic edits with SysML text

### R14 — Stale edit and source reconciliation detection

**Goal:** G09 · **Milestone:** Later · **Disposition:** `algorithm_reference` · **Port validation:** pending

- Historical source: [source-reconciliation.ts](../100_Archive/V1/14_Workbench/src/core/source-reconciliation.ts)
- V2 reference: **No identified active target**
- **Next action:** Use dirty-state and hydration barriers before save, three-way diff and stable hashes

### R17 — Configured Obsidian runtime stack

**Goal:** G06 · **Milestone:** First release · **Disposition:** `config_reference` · **Port validation:** pending

- Historical source: [Enabled Plugin Stack.md](../100_Archive/V1/10_Base%20Vault/Definition/Enabled%20Plugin%20Stack.md)
- V2 reference: [build_v2_test_base.py](../20_Base%20Vault/build_v2_test_base.py)
- **Next action:** Reconcile approved minimum Obsidian/plugins, update ownership and install-free/offline packaging

### R18 — Bootstrap activation without silent code mutation

**Goal:** G11 · **Milestone:** Later · **Disposition:** `algorithm_reference` · **Port validation:** pending

- Historical source: [core.ts](../100_Archive/V1/13_Bootstrap/Tools/v0.3.1/src/core.ts)
- V2 reference: [README.md](../23_Bootstrap/README.md)
- **Next action:** Reuse plugin lock verification and safe activation, but implement hybrid user settings preservation

### R19 — Author registration and UID collision governance

**Goal:** G03 · **Milestone:** First release · **Disposition:** `contract_reference` · **Port validation:** pending

- Historical source: [Author Registration Spec.md](../100_Archive/V1/13_Bootstrap/Definition/Author%20Registration%20Spec.md)
- V2 reference: [APPROVED_V2_TRANSLATION_BASELINE_AND_TEST_HANDOFF_2026-10-18.md](../26_Definitions/APPROVED_V2_TRANSLATION_BASELINE_AND_TEST_HANDOFF_2026-10-18.md)
- **Next action:** Retain author UID collision checks, timezone discipline, AI identity and per-user config safely

### R20 — BOM source reader and revised source history

**Goal:** G10 · **Milestone:** Later · **Disposition:** `later_adapter_candidate` · **Port validation:** pending

- Historical source: [bom_xlsx_reader.py](../100_Archive/V1/15_Testing/bom_xlsx_reader.py)
- V2 reference: [BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md](../24_Workbench/docs/BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md)
- **Next action:** Recover spreadsheet parsing/tests, then implement effective BOM rows with separate EA and BOM identity

### R21 — BOM alternates/effectivity and numbers

**Goal:** G10 · **Milestone:** Later · **Disposition:** `proposed_parts_not_approved` · **Port validation:** pending

- Historical source: [BOM_MDSE_Vault_Implementation_Plan.md](../100_Archive/V1/14_Workbench/docs/bom/a01-a14/BOM_MDSE_Vault_Implementation_Plan.md)
- V2 reference: [BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md](../24_Workbench/docs/BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md)
- **Next action:** Separate exact-decimal quantity/unit, alternates and variant evidence from native generalization; approve pending schema

### R28 — System model property and schema vocabulary

**Goal:** G02 · **Milestone:** First release · **Disposition:** `semantic_change_boundary` · **Port validation:** pending

- Historical source: [Note Layout.md](../100_Archive/V1/16_Definitions/Note%20Layout.md)
- V2 reference: [SysML Source Ownership and Note Storage.md](../26_Definitions/SysML%20Source%20Ownership%20and%20Note%20Storage.md)
- **Next action:** Crosswalk legacy note/YAML properties to v2-native vs MDSE-only metadata; use authoritative bottom SysML v2 section

## P2 — Longer-term reuse (1)

### R22 — Variant search and metadata errors

**Goal:** G10 · **Milestone:** Later · **Disposition:** `algorithm_reference` · **Port validation:** pending

- Historical source: [variantof.ts](../100_Archive/V1/14_Workbench/src/core/variantof.ts)
- V2 reference: **No identified active target**
- **Next action:** Retain evidence-based variant comparison, not automatic specialization; test provenance

## Recovery process

1. Open the original historical contract or source and locate its tests.
2. Check the approved V2 semantic decision and the [implementation conflicts](V1_V2_DEEP_TECHNICAL_RECOVERY_AND_PLATFORM_ARCHITECTURE_2026-10-18.md) before adapting any algorithm.
3. Record a unique active V2 implementation owner and synthetic fixture; add real data/parser/GUI evidence separately.
4. Only mark a ledger item ported after active V2 tests pass. Never modify or depend on archived V1 runtime.
5. Update this index together with the [machine ledger](v1_to_v2_reuse_ledger.v0.1.json), the [program goals](V2_PROGRAM_GOALS_AND_COMPLETION_2026-10-18.md), and the [V2 MOC](../MOC_MDSE_V2.md).
