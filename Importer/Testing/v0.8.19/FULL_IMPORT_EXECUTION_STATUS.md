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

Of the 79 resolved conveyed-flow records:

- 62 can be allocated to the current Local Model Interface/Connection structure.
- 17 resolve to valid source Item Flow evidence but cannot currently be allocated to a valid Local Model Connection.

The 17 records are concentrated in the legacy DVS concept path:

`Model > IPC ! > 09 Product in Progress > Concepts > DVS Concepts > DVS 330 E 240`

They include InformationFlows whose endpoints are directly attached to contextual Parts or span owner contexts. Under Local Model 0.4, a Connection must bind contextual Interface occurrences. Automatically turning those Part endpoints into Interfaces would invent structure that is not explicitly present in EA.

This is therefore a real semantic reconciliation blocker, not a file-access or parser problem.

## Importer correction made during Step 12

v0.8.19 now distinguishes:

1. unresolved conveyed xref source evidence, and
2. resolved conveyed source evidence that cannot be allocated to a valid Local Model Connection.

Either condition blocks the write before generated vault content is accepted.

The aggregate release gate now includes the conveyed-flow allocation regression.

## Remaining Step 12 acceptance work

Step 12 cannot pass until the 17 source records have an approved deterministic treatment. Acceptable resolution must do one of the following without silent loss:

- resolve the source endpoints to existing contextual Interfaces with deterministic evidence,
- define an approved Local Model representation for a flow terminating on a Part occurrence, or
- preserve the affected source flows as explicit governed review/model-check evidence while preventing them from being represented as completed Connection flows.

Do not freeze v0.8.19 while these 17 records remain semantically unallocated.
