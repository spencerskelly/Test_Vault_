---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Actor"
observedEndpointOccurrences: 254
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Actor

## Source identity

- **EA Object_Type:** `Actor`
- **Observed relationship-endpoint occurrences:** 254

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[README_Actor\|No stereotype]] | 254 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Association | [[README_UseCase]] | 210 | 34 | Settled | Map: participants on the Use Case endpoint |
| Outgoing | Aggregation | [[EA Stereotype - Physical Context]] | 10 | 4 | Settled | Map: participants on the Context endpoint |
| Incoming | Association | [[README_UseCase]] | 5 | 34 | Settled | Map: participants on the Use Case endpoint |
| Outgoing | Generalization | [[README_Actor]] | 5 | 1 | Settled | Map: subtypeOf / supertypeOf |
| Incoming | NoteLink | [[README_Note]] | 4 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Outgoing | Aggregation | [[EA Stereotype - Hardware Component]] | 3 | 51 | Review | Review: Aggregation endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_Issue]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Association | [[EA Element - No Stereotype]] | 2 | 52 | Review | Review: Association endpoint pattern |
| Outgoing | Sequence | [[EA Stereotype - System Partner]] | 2 | 43 | Deferred | Deferred: local sequence/behavior detail |
| Incoming | Abstraction «allocate» | [[README_Change]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Abstraction «allocate» | [[README_InformationItem]] | 1 | 53 | Review | Review: allocate endpoint pattern |
| Outgoing | Association | [[README_Issue]] | 1 | 6 | Settled | Map: affects / affectedBy |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[README_InformationItem]] | 1 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Generalization | [[EA Stereotype - System Partner]] | 1 | 1 | Settled | Map: subtypeOf / supertypeOf |

## Canvas

[[CANVAS_Actor]]
