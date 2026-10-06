# IMP-010 Rebaseline — Folded Non-Object Parts

**Status:** current-source classification complete; semantic decision required  
**Importer:** v0.8.19  
**Local Model:** 0.4  
**Real-source evidence:** bridge `37492673084`  
**Source:** `EA_2026_09_06_endgame.qeax`  
**SHA-256:** `16c055ec1a5af57b0f4f9059d6292c5ddd3ed052124c7ef54d9af288971ae02c`

## Purpose

Rebaseline IMP-010 against the accepted v0.8.19 real-QEAX output before changing the importer or Local Model schema.

The important conclusion is that these source rows are **not one semantic class**. Allowing Local Model Part records to point to any MDSE type would make physical structure, behavior/state decomposition and interface flow properties indistinguishable. That is not an acceptable fix.

## Current count

`Review - Semantic and Connectors.csv` contains **438** warnings of the form:

`Folded EA Part ... resolves to <type>; it remains note-level/source evidence and is not emitted as a Local Model part occurrence.`

Those 438 rows represent only **219 unique source Part GUIDs**. Every affected GUID appears exactly twice.

| Target MDSE type | Unique Parts | Distinct referenced definitions | Current source pattern |
|---|---:|---:|---|
| Behavior | 142 | 130 | Activity-owned reference to another Activity |
| Condition | 61 | 59 | 60 State-owned references to another State; 1 Hardware Component-owned reference to a State |
| Item Flow | 16 | 2 | Port-owned instance copy of a FlowProperty/Physical Signal |
| **Total** | **219** | **191** | three different semantic patterns |

The previous v0.8.3 IMP-010 baseline was 244 unique Parts: 142 Function + 61 Design + 25 Port + 16 Item Flow. W-384 removed the 25 Port-target cases by making EA Ports contextual Local Model Interfaces. The remaining counts are otherwise the same source population under the current Behavior/Condition taxonomy.

## Source evidence

### A — Behavior references: 142

All 142 source rows are EA `Part` objects that:

- are unnamed;
- have no Note;
- have no Multiplicity;
- have no `PDATA2`;
- have no classifier or classifier GUID;
- have no object-property/tag rows;
- touch no connector;
- appear in no diagram object row;
- are owned by an Activity;
- point through `PDATA1` to another Activity.

Owner breakdown:

- System Function Activity: 55
- Hardware Function Activity: 43
- Software Function Activity: 35
- no-stereotype Activity: 9

Referenced target breakdown:

- Hardware Function Activity: 73
- Software Function Activity: 33
- System Function Activity: 29
- no-stereotype Activity: 7

These rows carry no occurrence-specific engineering data. They behave as EA reference/containment carriers for behavior decomposition, not physical Part occurrences.

### B — Condition references: 61

All 61 source rows are unnamed EA `Part` objects with the same zero-data pattern as group A.

Targets:

- 61 × State / System State → MDSE Condition

Owners:

- 60 × State / System State
- 1 × Class / Hardware Component

The one Object-owned case is:

- owner: `Circuit - Comms_Universal BMID`
- target: `WiFi 802.11 Interface`
- target source type: State / System State
- source Part GUID: `{F82059BA-4249-4db8-A19B-426004EB5E9C}`

The 60 State→State rows behave like state/design hierarchy references. The one Object→Condition row is structurally different. Its target `WiFi 802.11 Interface` is under `05 Product Design`, so the current W-149/W-291/W-292 ownership rule resolves it as `hasDesign` / `designOf`, not `hasState` / `stateOf`.

### C — Interface flow-property instances: 16

These 16 are not equivalent to groups A/B.

All 16:

- are unnamed EA `Part` objects;
- are owned by an EA Port;
- have no Note, Multiplicity, tag, connector or diagram-object evidence;
- have a populated `Classifier` / `Classifier_guid`;
- point through `PDATA1` to a Physical Signal;
- classify to a `Part` whose stereotype is `FlowProperty`.

Only two definitions are involved:

1. Port definition `iCan`
   - FlowProperty: `can`
   - Physical Signal: `psCan`
   - affected contextual copies: 2

2. Port definition `i3V3Analog`
   - FlowProperty: `3.3V`
   - Physical Signal: `ps3V3Analog`
   - affected contextual copies: 14

This is interface/property semantics. Encoding these as Local Model physical Parts would be misleading.

## Why the warning count is doubled

`buildLocalOccurrenceModel()` calls `foldedPartOccurrence()` in two passes. Successful structural Parts are cached in `partBySource`; rejected non-Object definitions return `null` without a rejected-result cache entry. The second pass therefore emits the same warning again.

This is an evidence-quality defect, not 438 separate semantic problems. It should be removed when IMP-010 handling is finalized, or grouped under IMP-014 if the semantic work is intentionally separated.

## Governing-rule conflict exposed by the rebaseline

W-137 originally described these 219 rows as `hasPart` references. That decision predates W-384 and the current Behavior/Condition/Interface taxonomy.

Current v0.8.19 has two relevant mechanisms:

1. Local Model `Part` records require a reusable MDSE Object definition.
2. The note-level relationship graph is type-aware:
   - Behavior → Behavior resolves through generic hierarchy ownership (`hasChild` / `childOf`);
   - Condition → Condition likewise resolves as hierarchy except governed special cases;
   - Object → Condition resolves as `hasDesign` / `designOf` when the Condition subtype is `design`; otherwise it resolves as `hasState` / `stateOf`. The single current IMP-010 case is a design.

Therefore the current Local Model rejection is not evidence that all 219 need a broader Part schema. For groups A/B, a Local Model Part would likely be the wrong representation.

## Recommended semantic split

### IMP-010A — Behavior hierarchy, 142

Do **not** create Local Model Parts. Verify on real output that each deterministic Activity→Behavior reference is already represented by the intended note-level hierarchy relationship. If it is, treat these as successfully translated reference/containment evidence and remove the Local Model warning.

### IMP-010B — Condition hierarchy/state ownership, 61

Split further:

- 60 State→Condition references: verify the intended Condition hierarchy relationship.
- 1 Object→Condition/design reference: verify `hasDesign` / `designOf`.

Do **not** make either case a physical Local Model Part merely because EA stored the carrier row as `Object_Type=Part`.

### IMP-010C — Interface flow-property instances, 16

Treat these as a distinct Interface problem.

Before changing schema, determine whether the existing definition chain already gives the needed information:

`contextual Port/Interface occurrence → reusable interface Object → FlowProperty → Physical Signal/Item Flow`

If that chain is sufficient for engineering use, no local record is needed; preserve traceability and stop warning. If the 16 source rows carry local variation that must be addressable independently, add an explicit Interface/flow-property representation rather than abusing Local Model Part.

## Next acceptance step

Add a focused IMP-010 classifier/validator that proves, on the current real source and generated output:

1. exactly 219 unique affected source Parts;
2. exact subgroup counts 142 / 61 / 16;
3. the 142 Behavior and 60 State-owned Condition references resolve to their intended canonical note-level hierarchy links;
4. the single Object-owned design Condition resolves through `hasDesign` / `designOf`;
5. the 16 Port-owned Signal copies are traceable through their Port definition and FlowProperty classifier;
6. no non-Object target is emitted as a Local Model Part;
7. one source Part produces at most one actionable review finding.

Only after that evidence should the governing rule be updated and implementation behavior changed.


## Current acceptance gate

`imp010_hierarchy_acceptance.py` is the focused real-source acceptance for groups A/B. It is intentionally stricter than checking aggregate relationship counts:

- reads the accepted QEAX directly;
- requires exactly 203 Activity/State-targeted Part carrier rows (142 Activity, 61 State);
- requires the State-target owner split 60 State / 1 Class;
- verifies each folded Part ledger row resolves to the exact target note UID;
- proves none of the 203 source GUIDs is emitted as a Local Model physical Part;
- finds the actual owner and target Markdown notes by UID;
- requires the forward and inverse canonical YAML relationships on every source case;
- expects 202 source rows to resolve through `hasChild` / `childOf`, with one duplicate owner-target pair producing 201 unique links;
- expects the single Object→design case to resolve through `hasDesign` / `designOf`;
- fails if a required link or inverse is missing.

The synthetic self-test reproduces all 203 cases including the one duplicate pair and proves the validator fails closed when one required `hasChild` link is removed. The real-QEAX bridge now runs this gate against the complete generated vault before Workbench acceptance.


## Real-QEAX hierarchy acceptance — PASS

Bridge `37498212847` is the governing proof for IMP-010A/B after the folded-Part ownership fix.

Gate 1b ran fail-closed against the complete generated vault and reported:

- source Parts checked: **203**
- target counts: **142 Activity / 61 State**
- State-target owner counts: **60 State / 1 Class**
- expected relationship rows: **202 `hasChild` / 1 `hasDesign`**
- unique relationship pairs: **201 `hasChild` / 1 `hasDesign`**
- generated owner/target note pairs checked: **203**
- Local Model Part occurrences for these source GUIDs: **0**
- result: **PASS**

Representative hierarchy evidence:

- `Product Durability` → `Lifecycle Abuse Durability` through `hasChild` / `childOf`
- `Circuit - Comms_Universal BMID` → `WiFi 802.11 Interface` through `hasDesign` / `designOf`

The first fail-closed real run exposed the single Object→design ownership defect. The folded-Part graph builder passed `childSubtype` into the `ownerSubtype` argument and omitted the real child subtype, preventing `ownerField()` from choosing `hasDesign`. Commit `3d8657f2510f0a71387a005f58621ed18cbc2d03` corrects that call and adds `folded_part_relationship_regression_test.js` to the aggregate release gate.

**Conclusion:** the 142 Behavior and 61 Condition carrier rows are not Local Model structural-Part defects. Their source semantics are preserved through governed note-level ownership. IMP-010A/B are complete.

## Remaining IMP-010 scope

Only **16 unique Port-owned flow-property carrier Parts** remain a semantic decision:

- 2 contextual copies of `iCan` / FlowProperty `can` / Physical Signal `psCan`;
- 14 contextual copies of `i3V3Analog` / FlowProperty `3.3V` / Physical Signal `ps3V3Analog`.

These must be resolved as Interface semantics, not by widening Local Model Part.

Separately, the importer currently emits duplicate folded-Part warning rows because a rejected non-Object structural Part can be visited in both Local Model passes without a rejected-result cache entry. Once the 16-case semantic rule is settled, IMP-010 cleanup must emit no more than one actionable finding per source Part while retaining exhaustive machine traceability.


## IMP-010C implementation — W-397

The remaining 16 source rows do not carry independent occurrence semantics. Each is an unnamed Port-owned EA `Part` with no Note, Multiplicity, tag, connector or diagram evidence. Its `Classifier` is a reusable `FlowProperty` Part, its parent Port points to the Interface Class that owns that FlowProperty, and its `PDATA1` exactly matches the FlowProperty definition's `PDATA1`.

W-397 therefore treats them as contextual copies of the reusable FlowProperty definition rather than local structural Parts.

Recognition is intentionally strict. A carrier folds to the FlowProperty Item Flow only when all of these are true:

1. the source row is a non-FlowProperty EA `Part`;
2. its owner is an EA Port;
3. `Classifier` / `Classifier_guid` resolves to an EA Part stereotyped `FlowProperty`;
4. that FlowProperty is owned by an interface Class;
5. the owner Port points to that same interface Class;
6. carrier `PDATA1` equals FlowProperty-definition `PDATA1`;
7. the typed target resolves to a Signal or Class.

Any future row that differs fails that exact-copy recognition and remains visible for review rather than being silently collapsed.

### Reusable definition layer

The current model has 760 FlowProperty Item Flow definitions. **752** are owned by reusable interface Classes. Those definitions now use the current generic ownership vocabulary:

`Object/interface hasChild Item Flow` / `Item Flow childOf Object/interface`

This restores the useful ownership intent of historical W-133 without restoring first-class Port notes or the retired `hasFlow/flowOf` vocabulary.

The 1 package-owned and 7 ownerless FlowProperties are not assigned artificial interface owners.

### Direction and typed Signal/Class

Local Model flow occurrences remain connection-owned under W-294. A FlowProperty definition is not itself a connection-carried local flow occurrence.

The reusable Item Flow note retains:

- EA FlowProperty `direction` as `- Direction: ...` in `Source: EA`;
- its exact `PDATA1` type as `- FlowProperty type: [[...]]` when resolvable.

These are source evidence, not new canonical relationships. The current schema has no governed `typedBy` relation, so W-397 does not invent one.

### Warning behavior

Behavior/Condition carriers already accepted by W-396 and exact FlowProperty copies accepted by W-397 are handled semantic carriers, not Local Model warnings. They are cached as non-structural results so a second Local Model pass cannot emit duplicate warnings.

Unsupported future folded Parts that resolve to a non-Object definition still produce a review warning, but warning keys are source-Part scoped so one source Part cannot create duplicate actionable findings.

### Acceptance

`imp010_interface_flow_acceptance.py` is wired as real-QEAX Gate 1c and must prove:

- exactly 16 exact contextual copies;
- grouping 14 `3.3V` / `ps3V3Analog`, 2 `can` / `psCan`;
- no occurrence-specific data on those 16;
- each copy folds in Ledger to its FlowProperty Item Flow UID;
- zero Local Model Part records for those source GUIDs;
- all 752 interface-owned FlowProperty definitions have `hasChild` / `childOf`;
- direction and typed-target source evidence are retained;
- zero exact-copy Local Model warning rows;
- no folded-Part source GUID has duplicate review rows.


## Real-QEAX acceptance — closed

IMP-010 is closed by bridge run `37502083911` on head `2492b64f3e6caf9acf7745c8936b6a43040e964f`.

Acceptance results:

- both full imports: **WRITE PASS**
- deterministic output comparison: **PASS**
- Local Model Parts: **2,055** actual emitted records
- Gate 1b Behavior/Condition hierarchy acceptance: **PASS**
- Gate 1c Interface FlowProperty acceptance: **PASS**
- exact contextual copies: **16**
- interface-owned FlowProperty definitions checked: **752**
- copy GUIDs emitted as Local Model Parts: **0**
- exact-copy Local Model warnings: **0**
- duplicate folded-Part review GUIDs: **0**
- Workbench read-only, semantic and structured-edit Gates 2–4: **PASS**

The first Gate 1c attempt failed only because the acceptance validator had not loaded typed-target notes for every FlowProperty definition. That same run also revealed an accounting defect: handled semantic carriers cached as `null` were included in the displayed Local Model Part statistic. Neither defect changed the emitted Local Model. The accounting fix now counts `partsByOwner` records, restoring the authoritative 2,055-part result, and Gate 1c verifies that count directly from the Local Model Source Map.
