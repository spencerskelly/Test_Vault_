---
title: MDSE — Complete Repository Note Census
type: map-of-contents
status: indexed-coverage-not-content-certified
updated: 2026-10-18
---
# Complete repository note census

[Master V2 MOC](../MOC_MDSE_V2.md) · [Historical V1 archive MOC](../100_Archive/MOC_V1_ARCHIVE.md) · [Approval exception audit](V2_APPROVED_EXCEPTION_HANDLING_AUDIT_2026-10-18.md)

**Purpose:** a stable fallback search index. Every Markdown note present in pinned commit `5eea630bee387213b1bc1c511b90cc0f679ea6a3` was linked in one of the 13 catalogs below. The pinned tree contained **917 Markdown notes** and was neither truncated nor limited to the prior relocation manifest. The catalogs cover **all directory areas including 99System and 99_System**, which are distinct directories.

**Important:** inventorying a note is **not** an assessment that it contains an approved decision, a working implementation, unique content, or valid SysML syntax. Treat catalog entries as `indexed_only` until assessed. Approved historical decisions retain their original provenance.

| Area | Notes in pinned snapshot | Catalog |
|---|---:|---|
| V1 archive and archive MOC | 465 | [1](MOC_Catalogs/archive_1.md) · [2](MOC_Catalogs/archive_2.md) · [3](MOC_Catalogs/archive_3.md) · [4](MOC_Catalogs/archive_4.md) · [5](MOC_Catalogs/archive_5.md) |
| V2 Workbench and decisions | 125 | [1](MOC_Catalogs/workbench_1.md) · [2](MOC_Catalogs/workbench_2.md) |
| Translator work history | 122 | [1](MOC_Catalogs/translator_history_1.md) · [2](MOC_Catalogs/translator_history_2.md) |
| Workspace, release and decision history | 58 | [Workspace](MOC_Catalogs/workspace_1.md) |
| **99System native SysML v2 decisions** | **35** | [October 16–17 native decisions](MOC_Catalogs/sysml_decisions_1.md) |
| 99_System schemas, templates and records | 65 | [System](MOC_Catalogs/legacy_system_1.md) |
| Other program files, MOC, tools and definitions | 47 | [Other](MOC_Catalogs/other_1.md) |
| **Total** | **917** | **13 catalogs** |

## Newly surfaced authority — do not recreate it

The `99System/10_EA Native Translator/sysml-v2-decisions/` directory contains already-approved definitions for binding, connections, reference part usages, dependencies, requirement decomposition/derivation/satisfaction/verification, attributes/units, calculation, constraints, and other relationships. It was **not surfaced as an authority in the original curated MOC**. This is a key cause of repeated discussions; use the [full decision catalog](MOC_Catalogs/sysml_decisions_1.md) and link these original approvals into their active v2 owner notes.

Useful examples:
- [Referential part usage](../99System/10_EA%20Native%20Translator/sysml-v2-decisions/2026-10-16-referential-part-usage-approved.md)
- [Binding connector](../99System/10_EA%20Native%20Translator/sysml-v2-decisions/2026-10-17-binding-connector-approved.md)
- [Attributes and units](../99System/10_EA%20Native%20Translator/sysml-v2-decisions/2026-10-17-attributes-valuetypes-units-approved.md)
- [Requirement decomposition](../99System/10_EA%20Native%20Translator/sysml-v2-decisions/2026-10-17-requirement-decomposition-approved.md)
- [12-point relationship documentation standard](../99System/10_EA%20Native%20Translator/sysml-v2-decisions/2026-10-16-relationship-documentation-standard-approved.md)

## Consolidation evidence and no-delete rule

The pinned snapshot had **one known pair of byte-identical Markdown notes** based on git blob SHA:
- `100_Archive/V1/10_Base Vault/Definition/MDSE Workbench User Guide.md`
- `100_Archive/V1/14_Workbench/docs/User Guide/MDSE Workbench User Guide.md`

They are **candidates** for eventual consolidation or redirect, not authorized for deletion. Before changing paths, check Obsidian wikilinks, Markdown links, Canvas, Bases, YAML links, importer config and historical tags; preserve UID/id and run a backlinks and build regression. Two copies can intentionally serve different release contexts.

## Automated maintenance

- [Repository-wide note coverage checker](../25_Testing/test_repository_note_moc_coverage.py) is designed to compare current tracked Markdown notes with catalog links and explicitly linked newer MOC notes. A new Markdown file without MOC entry is a CI finding, not grounds for automatic deletion.
- [Central MOC](../MOC_MDSE_V2.md) contains curated authorities; these 13 catalogs provide exhaustive **findability**.
- When creating or retiring a note, update its owning MOC/catalog in the same PR and use an explicit replacement/redirect rather than moving historical material silently.
- Distinguish `approved` (rule), `implemented` (runtime), `verified` (fixture/parser/UI), `released` (versioned toolchain), and `indexed_only` (navigation).
- Do not clean up `99System` vs `99_System` or other similar folder names by guessing; use source-context and exact dependencies first.
