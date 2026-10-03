---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Text"
observedEndpointOccurrences: 51
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Text

## Source identity

- **EA Object_Type:** `Text`
- **Observed relationship-endpoint occurrences:** 51

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Text\|No stereotype]] | 51 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Incoming | Dependency «trace» | [[EA Stereotype - Module]] | 11 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_Object]] | 8 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - block]] | 7 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Abstraction «allocate» | [[EA Element - No Stereotype]] | 4 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - requirement]] | 4 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - testCase]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_InformationItem]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Abstraction «allocate» | [[README_Object]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Association | [[EA Stereotype - Module]] | 1 | 52 | Review | Review: Association endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - Hardware Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Physical Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - Software Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 1 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - System Partner]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_Object]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Nesting | [[EA Stereotype - Document]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |

## Canvas

[[CANVAS_Text]]
