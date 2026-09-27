---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Note"
observedEndpointOccurrences: 351
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Note

## Source identity

- **EA Object_Type:** `Note`
- **Observed relationship-endpoint occurrences:** 351

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Note\|No stereotype]] | 351 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | NoteLink | [[README_UseCase]] | 159 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - requirement]] | 40 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - System Function]] | 33 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - designConstraint]] | 17 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - Module]] | 12 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - extendedRequirement]] | 10 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - Physical Component]] | 9 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | NoteLink | [[EA Stereotype - Software Component]] | 8 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | NoteLink | [[EA Stereotype - block]] | 8 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - Hardware Component]] | 8 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Element - No Stereotype]] | 7 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - System State]] | 5 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[README_Actor]] | 4 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - block]] | 4 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | NoteLink | [[EA Stereotype - Hardware Component]] | 3 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | NoteLink | [[EA Stereotype - Physical Component]] | 3 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - functionalRequirement]] | 3 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Element - No Stereotype]] | 3 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Element - No Stereotype]] | 2 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - Document]] | 2 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - Software Component]] | 2 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[README_Note]] | 2 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Association | [[EA Stereotype - block]] | 1 | 52 | Review | Review: Association endpoint pattern |
| Incoming | NoteLink | [[EA Stereotype - Business Line]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | NoteLink | [[EA Stereotype - Image]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | NoteLink | [[EA Stereotype - designConstraint]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | NoteLink | [[EA Stereotype - System State]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |

## Canvas

[[CANVAS_Note]]
