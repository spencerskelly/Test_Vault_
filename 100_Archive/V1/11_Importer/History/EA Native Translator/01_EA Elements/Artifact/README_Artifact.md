---
uid:
type: EA Type Definition
status: Working
eaMetaclass: "Artifact"
observedEndpointOccurrences: 393
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Type — Artifact

## Source identity

- **EA Object_Type:** `Artifact`
- **Observed relationship-endpoint occurrences:** 393

## Observed variants

| Variant | Endpoint occurrences |
|---|---:|
| [[EA Stereotype - Document\|Document]] | 279 |
| [[EA Stereotype - Image\|Image]] | 114 |

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency | [[EA Stereotype - Regulatory Requirement]] | 173 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 103 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Nesting | [[README_InformationItem]] | 24 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Nesting | [[EA Stereotype - requirement]] | 16 | 33 | Deferred | Deferred: explicit EA Nesting |
| Outgoing | Dependency «refine» | [[EA Stereotype - requirement]] | 11 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «trace» | [[EA Stereotype - requirement]] | 10 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - extendedRequirement]] | 8 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[EA Stereotype - requirement]] | 7 | 24 | Settled | Map: describes / describedBy |
| Outgoing | Nesting | [[EA Stereotype - Document]] | 5 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Dependency «deriveReqt» | [[EA Stereotype - designConstraint]] | 3 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| Incoming | Dependency «trace» | [[EA Stereotype - System State]] | 3 | 50 | Review | Review: trace endpoint pattern |
| Incoming | NoteLink | [[README_Note]] | 3 | 45 | Settled | No YAML relationship; preserve annotation/body detail |
| Incoming | Abstraction «allocate» | [[EA Stereotype - requirement]] | 2 | 53 | Review | Review: allocate endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - designConstraint]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «refine» | [[EA Stereotype - designConstraint]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Incoming | Dependency «trace» | [[README_Object]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Nesting | [[EA Stereotype - requirement]] | 2 | 33 | Deferred | Deferred: explicit EA Nesting |
| Incoming | Abstraction «allocate» | [[EA Stereotype - System Function]] | 1 | 10 | Settled | Map: target Thing performs source Function |
| Incoming | Abstraction «trace» | [[EA Stereotype - Hardware Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Association | [[EA Stereotype - Hardware Component]] | 1 | 7 | Settled | Map: describes / describedBy |
| Incoming | Dependency | [[EA Stereotype - testCase]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Outgoing | Dependency «refine» | [[EA Stereotype - functionalRequirement]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| Outgoing | Dependency «satisfy» | [[EA Stereotype - extendedRequirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «satisfy» | [[EA Stereotype - System State]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| Incoming | Dependency «trace» | [[README_Action]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 1 | 24 | Settled | Map: describes / describedBy |
| Incoming | Dependency «trace» | [[EA Stereotype - Physical Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Nesting | [[README_Text]] | 1 | 33 | Deferred | Deferred: explicit EA Nesting |

## Canvas

[[CANVAS_Artifact]]
