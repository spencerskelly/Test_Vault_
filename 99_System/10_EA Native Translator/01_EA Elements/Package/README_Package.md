---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Package"
observedEndpointOccurrences: 7
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Package

## Source identity

- **EA Object_Type:** `Package`
- **Observed relationship-endpoint occurrences:** 7

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Package\|No stereotype]] | 7 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Realisation | [[EA Stereotype - requirement]] | 6 | 18 | Settled | Map: Requirement appliesTo source element |
| Outgoing | Realisation | [[EA Element - No Stereotype]] | 1 | 18 | Settled | Map: Requirement appliesTo source element |

## Canvas

[[CANVAS_Package]]
