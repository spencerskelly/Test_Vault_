# SysML v2 Flow — approved mapping and implementation backlog
Decision date: 2026-10-17
Status: Approved option A; implementation and corpus verification pending
Normative authority: OMG SysML 2.0 Part 1 Language §7.16.2 and Part 2 Transformation. https://www.omg.org/spec/SysML/2.0/Language/PDF

## Decision
Adopt native SysML v2 Flow definitions and usages. Translate compatible EA Information Flows, Item Flows, and Activity Object Flows while preserving conveyed item definitions and original EA records. Keep ordinary Connections separate. Control Flows are NOT translated into generic streaming Flow; review under Succession / Succession Flow. Messages remain distinct, reviewed next.

## Semantics and shape
- A native flow usage models a transfer of payload from a source output feature to a target input feature. Resolve feature chains and direction, not merely parent element IDs.
- A flow definition is reusable; flow usages occur in an owning model context. Preserve payload type, features, multiplicity and qualified model identities.
- Flow must not be conflated with Connection, Message, Succession, Succession Flow or Bindings; those have distinct constraints.
- Textual syntax reference: `flow source.outputFeature to target.inputFeature;` in a valid owning context. Typed payload and flow definition when supported and resolvable.
- Flag absent or incompatible input/output features and missing conveyed item typing, retaining original evidence; do not fabricate details silently.

## EA translator
1. Extract EA connector type/subtype/stereotype, direction, client/supplier, conveyed items, connector tags, Activity Object Flow edge roles, source/target element types and owning contexts.
2. Map EA Information Flow and Item Flow to Flow usage only when semantics and required endpoints can be resolved; if not, map to flagged candidate with original records and a repair work item.
3. Translate Activity Object Flow only when transferable payload and action-facing features can be resolved; distinguish control flow and guard semantics.
4. Build or resolve reusable item/attribute definitions in vault; preserve EA data typing, notes and classifier IDs.
5. Record source EA GUID, original direction, all mapped feature IDs, target flow usage IDs, rule version, original tags and exception flags; reconcile every original connector, including 1:N mappings.

## BOM translator
- BOM hierarchy, quantity, units, cable/part existence never imply an active item/information flow.
- Reuse shared item/quantity/unit and physical part definitions registered in vault.
- Preserve independently imported flows when merging canonical part identities. Flag competing type/port assumptions; no guessed direction based on BOM connectivity.
- Regression checks: EA->BOM and BOM->EA import order equivalence for stable identities, flows, and provenance.

## Workbench
- Drag line source to target; offer Flow only when eligible, together with other valid operations.
- Flow selection opens source output feature and target input feature selection (filtered by context/type/direction); optional payload definition/usage dropdown, alphabetically ordered from vault.
- Preview exact flow definition/usage, direction, owner, resulting SysML text and graphical notation; confirm/cancel; preserve atomic edit/undo.
- Support editing payload type, feature ends, definition usage, navigation, delete/repoint, reverse "where flows" query and distinct graphical visualization.
- Structural view: typed item transfers, feature endpoints and ownership; visual view: flow indications with graphical notation; tabular view: source/target/payload/flags; textual view: parseable native syntax. All views share same canonical IDs.
- Unresolved input/output features are surfaced as flags; do not create an invalid native flow masquerading as valid.

## Vault-native model registry
- Canonical reusable flow, item and attribute definitions; typed feature ports/inputs/outputs, quantity kinds, units, enum definitions/literals, qualified names, stable IDs.
- Definitions stored as editable versioned vault artifacts, indexed for Workbench menus; no hardcoded item choices. Keep standard libraries / extension concepts distinguishable.
- Preserve EA raw connector information as provenance and the mapping rule ID separately from native SysML constructs.

## Validation
- Native parse and semantic conformance to OMG SysML v2.0.
- Feature chain endpoints resolved with source output and target input; directed compatibility and payload type.
- Verify multiplicity, owner namespace/context, item definition/usage, no detached/missing source records.
- EA mapping ledger counts every element/connector with target IDs, native-with-evidence, flagged exception or excluded-with-rationale disposition.
- Test multi-source flow usages, payload mismatch, reversed direction, missing conveyed class, Activity Object Flow vs Control Flow, imported native Flow vs Connection, BOM merge and update idempotency, graphical/text/table synchronized edit, round-trip preservation.

## Follow-up tracker
- FLOW-01: Inventory EA Information Flows, Item Flows and Object Flows; sample and count, identify presence of conveyed classifier and guard data. [EA translator]
- FLOW-02: Define exact source classifier and edge mapping table to v2 Flow metamodel. [semantic registry]
- FLOW-03: Build vault reusable Item/Flow Definition and typed feature registries with stable identity. [vault]
- FLOW-04: Implement flow creation, editing and endpoint chooser after drag gesture. [Workbench]
- FLOW-05: Add flow-specific visual/textual/structural/tabular projections. [Workbench]
- FLOW-06: Reconcile BOM aliases/parts and shared quantity-unit definitions without inferring flows. [BOM translator]
- FLOW-07: Implement validation, error flags and EA evidence source-to-target ledger. [QA]
- FLOW-08: Add conformance and regression suite including control/flow separation and round-trip. [QA]
- FLOW-09: Update central relationship catalog and guide with the exact native specification mappings. [docs]
- FLOW-10: Verify actual source data from complete EA exports before declaring transformation exact. [integration]

## Next review
Message: native SysML v2 Message usage, event occurrences and optional payloads, distinct from streaming Flow.
