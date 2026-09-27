---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Sequence"
observedEndpointOccurrences: 8
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Sequence

## Source identity

- **EA Object_Type:** `Sequence`
- **Observed relationship-endpoint occurrences:** 8

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Sequence\|No stereotype]] | 8 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Sequence | [[EA Stereotype - Module]] | 4 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Sequence | [[EA Stereotype - Module]] | 3 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Outgoing | Sequence | [[README_Object]] | 1 | 43 | Deferred | Deferred: local sequence/behavior detail |

## Canvas

[[CANVAS_Sequence]]
