---
title: MDSE v1 archive — Master Map of Contents
type: map-of-contents
status: archive-reference
updated: 2026-10-18
source: V2_FOLDER_MIGRATION_MANIFEST_2026-10-18
---
# MDSE v1 — Archive Map of Contents

[Current v2 MOC](../MOC_MDSE_V2.md) · [V2 program goals](../26_Definitions/V2_PROGRAM_GOALS_AND_COMPLETION_2026-10-18.md) · [Full archived path manifest](../26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json)

**Read-only historical knowledge.** The v1 archive is a value-recovery source, **not** an executable or semantic dependency for v2. Do not overwrite v1, import its scripts into v2 directly, or treat provisional notes as approved rules. Source: the recorded relocation manifest; 1,165 archived paths (includes code, assets, tests, documentation, and binaries). The per-area indexes below explicitly link every listed archived path.

## 00 — Full archive file directory

| Area | Indexed files | Complete link inventory |
|---|---:|---|
| Base Vault | 48 | [Base Vault files](MOC_V1_base_vault_1.md) |
| EA importer | 666 | [1](MOC_V1_importer_1.md) · [2](MOC_V1_importer_2.md) · [3](MOC_V1_importer_3.md) · [4](MOC_V1_importer_4.md) · [5](MOC_V1_importer_5.md) |
| Bootstrap | 28 | [Bootstrap files](MOC_V1_bootstrap_1.md) |
| Workbench | 217 | [1](MOC_V1_workbench_1.md) · [2](MOC_V1_workbench_2.md) |
| Testing and consolidation | 166 | [1](MOC_V1_testing_1.md) · [2](MOC_V1_testing_2.md) |
| Definitions and property contracts | 40 | [Definitions files](MOC_V1_definitions_1.md) |
| **Total** | **1,165** | [Migration manifest](../26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json) |

## 10 — Importer: source ingestion, safety, mapping and release

- [Importer operating contract](V1/11_Importer/Definition/Importer%20Operating%20Contract.md) — two-stage source-faithful import, read-only source, fresh-vault staging, separate semantic acceptance.
- [Translator definition](V1/11_Importer/Definition/Translator%20Definition.md) — mechanical translation rules and approval authority.
- [Importer full execution status](V1/11_Importer/Testing/v0.8.19/FULL_IMPORT_EXECUTION_STATUS.md) — recorded result; compare fixture/release assumptions before reuse.
- [Importer tools v0.8.19](V1/11_Importer/Tools/v0.8.19/README.md) — mature HTML importer experience.
- [Historically modeled EA elements and their source notes](MOC_V1_importer_1.md) · [continuation](MOC_V1_importer_2.md) — detailed family-level source examples and documentation retained.
- [Source extraction and import test corpus](MOC_V1_importer_5.md) — regression assets and prior release guards.

## 20 — Base Vault, release, plugins and startup
- [Base Vault README](V1/10_Base%20Vault/README.md)
- [Approved enabled plugin stack and settings ownership](V1/10_Base%20Vault/Definition/Enabled%20Plugin%20Stack.md)
- [Release manifest](V1/10_Base%20Vault/Definition/mdse-release.yaml)
- [Initialization scripts and bundled runtime plugins](MOC_V1_base_vault_1.md)
- [Base release checker](V1/10_Base%20Vault/Testing/check-release.py)

## 30 — Bootstrap and user identity
- [Author registration policy and collision checks](V1/13_Bootstrap/Definition/Author%20Registration%20Spec.md)
- [Bootstrap historical README](V1/13_Bootstrap/README.md)
- [Bootstrap versions, source, artifacts, tests](MOC_V1_bootstrap_1.md)

## 40 — Workbench and model editing
- [WB-106 implementation contract](V1/14_Workbench/WB106_IMPLEMENTATION_CONTRACT.md) — ModelRef note/local identities, parser, schema gates, transaction boundaries.
- [Workbench release notes](V1/14_Workbench/RELEASE_NOTES.md)
- [Workbench docs index](V1/14_Workbench/docs/INDEX.md)
- [Workbench decisions](V1/14_Workbench/docs/Definition/02%20-%20Workbench%20Decision%20Log.md)
- [Workbench source, regression and UI tests](MOC_V1_workbench_2.md)
- [Workbench documentation and BOM integration](MOC_V1_workbench_1.md)

## 50 — BOM and where-used / configuration
- [BOM implementation plan A01–A14](V1/14_Workbench/docs/bom/a01-a14/BOM_MDSE_Vault_Implementation_Plan.md) — note the proposal/approval boundaries.
- [BOM persistence audit](V1/14_Workbench/docs/bom/A01-A14_GIT_PERSISTENCE_AUDIT.md)
- [BOM recovery status](V1/14_Workbench/docs/bom/A01-A14_RECOVERY_STATUS_2026-10-09.md)
- [BOM reader and variant checkpoint inventory](MOC_V1_workbench_1.md)
- [v2 target integration review](../24_Workbench/docs/BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md)

## 60 — System tests, CI and prior consolidation
- [Archived tests, evidence and consolidation records](MOC_V1_testing_1.md) · [continuation](MOC_V1_testing_2.md)
- [Original source profile checker](V1/15_Testing/check_qeax_source_profile.py)
- [Connector role evidence auditor](V1/15_Testing/audit_ea_connector_roles.py)
- [Local-model topology analysis and tests](V1/15_Testing/consolidation/localmodel_topology_index_v3.py)
- [Four-ref historical repository audit](V1/15_Testing/consolidation/STEP89_COMPLETE_FOUR_REF_TREE_AUDIT.md)

## 70 — Modeling definitions and source provenance
- [Full property / definition reference inventory](MOC_V1_definitions_1.md)
- [Note layout](V1/16_Definitions/Note%20Layout.md)
- [EA source section](V1/16_Definitions/EA%20Source%20Section.md)
- [Author identity change process](V1/16_Definitions/Changing%20Your%20Author%20Code.md)

## 80 — Reuse candidates and overlooked value
[**V1 → v2 recovery opportunity register**](../26_Definitions/V1_ARCHIVE_VALUE_RECOVERY_GAPS_2026-10-18.md) records what is reusable, the target v2 owner, validation needed, and approved/proposed status. High-priority examples: staged import ledger and rollback gates; per-occurrence ModelRef identity and local model indexing; reproducible plugin lock/config ownership; author identity collisions; BOM exact-decimal and alternates; release provenance/reproducible CI.

## 90 — Maintenance and decision precedence
1. Find here and in the [v2 MOC](../MOC_MDSE_V2.md) before recreating a feature.
2. Read original v1 contract and original tests, then compare to **approved v2** contract. Copy values/algorithms as new v2 implementations only after independent v2 tests; no archived runtime imports.
3. Keep v1 archived and unchanged. New recovery findings live in active `26_Definitions/`, not the frozen archive.
4. Machine index derives from the archived path manifest; run the v1 MOC coverage test when the archive manifest changes. Re-index new archived files rather than silently omitting them.
5. Metadata/Markdown links are navigation, never formal SysML semantics.
