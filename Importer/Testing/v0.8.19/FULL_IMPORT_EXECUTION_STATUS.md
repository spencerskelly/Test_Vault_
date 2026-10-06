# v0.8.19 Full Import Execution Status

Status: BLOCKED — real-source semantic reconciliation failure

## Source verification

The exact project source is now available and was inspected directly as SQLite:

- File: `EA_2026_09_06_endgame.qeax`
- Size: `186036224` bytes
- SHA-256: `16c055ec1a5af57b0f4f9059d6292c5ddd3ed052124c7ef54d9af288971ae02c`
- `t_object`: 35,969
- `t_connector`: 21,822
- `t_package`: 1,387
- `t_diagramobjects`: 42,966
- `t_diagram`: 2,924
- `t_xref`: 42,052
- `t_document`: 397

The source therefore matches the approved baseline counts.

## Real-source checks passed

- 84 Activities with a function stereotype exist outside the Product Function folder; v0.8.19 must retain them as Behavior/function.
- State split from the source is 954 Product Design States and 158 other States.
- 42 `functionalRequirement` and 83 `designConstraint` Requirements occur inside Engineering Requirements; explicit semantics must override folder context.
- No raw ParentID cycles were found.
- 53 machine-generated/URL-like element names were found and are covered by the v0.8.19 filename normalization rule.
- All 79 `t_xref.Behavior = conveyed` source records resolve to a real source object and a real InformationFlow connector.

## Blocking finding

Raw xref resolution is not sufficient to prove flow preservation.

Of the 79 resolved conveyed-flow records, the initial real-source review found 62 directly allocatable and 17 blocked.

Further endpoint tracing split the 17 blockers into two categories:

- **10 Port↔Port records** were valid Interface-to-Interface topology whose Interfaces live under different child Objects. EA provides a deterministic lowest common owner: `DVS 330 E 240 Context`. The importer was too strict because it required identical immediate owners. v0.8.19 now owns these Connections at the lowest emitted common context.
- **7 Part↔Port records** remain semantically unallocated. Their Part endpoint has no explicit Interface/Port occurrence that can be selected without inventing structure.

The remaining 7 records are concentrated in the legacy DVS concept path:

`Model > IPC ! > 09 Product in Progress > Concepts > DVS Concepts > DVS 330 E 240`

The remaining records are InformationFlows whose one endpoint is directly attached to a contextual Part. Under Local Model 0.4, a Connection must bind contextual Interface occurrences. Automatically turning those Part endpoints into Interfaces would invent structure that is not explicitly present in EA.

The reviewed source records are Connector IDs `34347`, `34352`, `34353`, `34354`, `34357`, `34360`, and `34361`. They carry `ps480VACL1`, `ps480VACL2`, `ps480VACL3`, `psNeutral`, and `psPE` conveyed items.

This is therefore a real semantic reconciliation blocker, not a file-access or parser problem.

## Importer correction made during Step 12

v0.8.19 now distinguishes:

1. unresolved conveyed xref source evidence, and
2. resolved conveyed source evidence that cannot be allocated to a valid Local Model Connection.

Either condition blocks the write before generated vault content is accepted.

The aggregate release gate now includes the conveyed-flow allocation regression.

## Remaining Step 12 acceptance work

Step 12 cannot pass until the remaining 7 source records have an approved deterministic treatment. Acceptable resolution must do one of the following without silent loss:

- resolve the source endpoints to existing contextual Interfaces with deterministic evidence,
- define an approved Local Model representation for a flow terminating on a Part occurrence, or
- preserve the affected source flows as explicit governed review/model-check evidence while preventing them from being represented as completed Connection flows.

Do not freeze v0.8.19 while these 17 records remain semantically unallocated.

## Common-context ownership correction

The importer now determines Connection ownership by walking the emitted owner hierarchy and selecting the lowest common context rather than requiring both Interfaces to have the same immediate owner. This resolves the 10 cross-component Port↔Port cases without changing their Interface identity or inventing topology.
