# IMP-011 Rebaseline - BindingConnector Context

**Status:** Root-cause classification complete; semantic decision intentionally deferred  
**Importer:** v0.8.19  
**Real-source evidence:** bridge `37502083911`, accepted EA8647 QEAX  
**Source SHA-256:** `16c055ec1a5af57b0f4f9059d6292c5ddd3ed052124c7ef54d9af288971ae02c`

## Purpose

IMP-011 was originally based on v0.8.3 evidence that grouped 249 BindingConnectors as 47 temporary local `equals` and 202 unresolved cases. That evidence is stale after the Local Model 0.4 / W-384 changes.

This rebaseline classifies the current 249 source BindingConnectors before any further importer semantics are changed.

## Current actual disposition

The accepted v0.8.19 real import produces:

| Group | Count | Current treatment |
|---|---:|---|
| Deterministic boundary exposure | 23 | `Connection.exposes -> boundary Interface` |
| Same-owner boundary/internal, zero candidate internal Connection | 191 | temporary symmetric local `equals` review evidence |
| Not a deterministic boundary/internal exposure | 35 | no `exposes` or `equals` invented |
| **Total** | **249** | |

The 23 exposure cases are already deterministic and accepted by the Workbench gates.

## Why the 191 are not missing Connections

For each of the 191 boundary/internal cases, the importer looked for an existing Local Model Connection incident on the internal Interface and found **zero**.

Direct source-graph inspection gives:

- inner Interface has **no other connector of any kind**: **179**
- inner Interface has exactly one other connector and it is another **BindingConnector**: **12**
- inner Interface has a non-Binding Connector/InformationFlow that could supply the missing Connection: **0**

The BindingConnector graph itself has:

- connected components: **234**
- one-edge components: **219**
- two-edge components: **15**
- components larger than two BindingConnectors: **0**
- two-edge components containing any non-Binding connector: **0**

Therefore transitive BindingConnector traversal cannot recover an unmodeled internal Connection. Creating one would be synthetic topology, not reconstruction.

## Definition compatibility inside the 191

The binding evidence is nevertheless strong:

- both ends resolve to the same non-empty reusable Interface definition: **180**
- reusable Interface definition exists on only one side: **10**
- neither side has reusable Interface definition evidence: **1**
- conflicting non-empty reusable Interface definitions: **0**
- equal visible endpoint names: **154**

This supports preserving the source binding/delegation evidence, but does not by itself justify inventing a Connection.

## The remaining 35

The 35 cases that are not current boundary-to-internal exposure candidates divide cleanly:

### Same-owner nested binding — 17

Both Interfaces belong to the same Local Model owner, but both are internal: one is on a contained Part and the other is on a deeper nested Part.

- 16 / 17 have the same non-empty reusable Interface definition.
- 1 / 17 has reusable definition evidence on only one side.
- 10 participate in a two-BindingConnector component with no non-Binding connector.
- 7 are single BindingConnectors where the shallower internal Interface participates in one ordinary Connector and the deeper Interface participates in none.

These are meaningful nested delegation/binding evidence, but they are not assembly-boundary `Connection.exposes` under Local Model 0.4.

### Same-owner sibling/internal binding — 1

One PCE25 Power case binds two same-definition internal Interfaces owned by sibling Parts. One side also participates in two ordinary Connections; the other does not. There is no containment direction that makes this an exposure.

### Cross-owner binding — 17

All endpoints exist as Local Model Interfaces, but the two ends belong to different owning notes.

The population is concentrated in only two CompositeStructure diagrams:

- `Staples Button: PCE Stop Button`: **10**
- `DVS 330 E Buck Context`: **7**

All 17 pairs share the same non-empty reusable Interface definition, but the current model has no deterministic shared Local Model owner for the pair. Writing a cross-context local equality or synthesizing a Connection would therefore assert context the importer has not proved.

## Review-output defect discovered

`Review - Equals Direction.csv` does **not** currently report actual BindingConnector disposition.

It labels every pair with the same Local Model owner as `temporary local equals`, producing:

- `temporary local equals`: **232**
- `unresolved contextual owner/endpoints`: **17**

But the actual generated model is:

- `Connection.exposes`: **23**
- temporary local `equals`: **191**
- no relationship written: **35**

This is a usability problem: a reviewer cannot tell already-resolved exposure from temporary binding evidence or genuinely unresolved context.

## Safety boundary

Do not create Local Model Connections simply because a BindingConnector exists.

A Connection remains valid only when source evidence identifies two contextual Interface endpoints that form a connection under the existing Local Model rules. `Connection.exposes` remains valid only when a unique internal Connection and an assembly-boundary Interface are both deterministic.

## Next bounded step — IMP-011A

Correct `Review - Equals Direction.csv` so every BindingConnector reports its **actual disposition/root cause**, at minimum distinguishing:

1. resolved as `Connection.exposes`;
2. temporary same-owner boundary/internal `equals` because zero internal Connection exists;
3. same-owner nested internal binding;
4. same-owner sibling/non-hierarchical binding;
5. cross-owner binding.

This is evidence/output work only. After the review table is trustworthy, make the semantic decision about whether same-owner non-exposure BindingConnector evidence should remain temporary `equals` or become a governed canonical local binding relation.
