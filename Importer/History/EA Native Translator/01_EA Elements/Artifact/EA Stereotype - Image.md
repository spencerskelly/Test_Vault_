---
uid:
type: EA Element
status: Working
eaMetaclass: "Artifact"
eaStereotype: "Image"
observedEndpointOccurrences: 114
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
coverageBasis: "Observed relationship endpoints"
---
# EA Artifact — Image

## Source identity

- **EA Object_Type:** `Artifact`
- **EA stereotype:** `Image`
- **Observed relationship-endpoint occurrences:** 114

## Native-import typing rule

The r12 native importer is **source-faithful on element typing**. This note records the EA source construct as modeled. Semantic cleanup/reclassification is a later model change unless a separate import rule explicitly says otherwise.

## Coverage boundary

The r12 workbook certifies full **relationship-source** coverage and supplies element types/stereotypes observed as connector endpoints. This note therefore proves connector-facing coverage for this construct. The workbook does not contain a separate full inventory of isolated/unconnected `t_object` rows, so this note does not claim that no additional isolated EA element type exists.

## Observed connectors and opposite elements

| Direction | EA connector | Other endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---|---:|---|---|---|
| Outgoing | Dependency «trace» | [[EA Stereotype - Hardware Component]] | 103 | 24 | Settled | Map: describes / describedBy |
| Incoming | Dependency «trace» | [[README_Object]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Stereotype - System State]] | 2 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Abstraction «trace» | [[EA Stereotype - Hardware Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency | [[EA Stereotype - testCase]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| Incoming | Dependency «trace» | [[README_Action]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | Dependency «trace» | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Outgoing | Dependency «trace» | [[README_InformationItem]] | 1 | 24 | Settled | Map: describes / describedBy |
| Incoming | Dependency «trace» | [[EA Stereotype - Physical Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| Incoming | NoteLink | [[README_Note]] | 1 | 45 | Settled | No YAML relationship; preserve annotation/body detail |

## Canvas

[[CANVAS_Artifact - Image]]
