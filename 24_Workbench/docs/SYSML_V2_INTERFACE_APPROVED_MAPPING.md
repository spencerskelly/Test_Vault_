# SysML v2 Interface — Approved Option A
Date: 2026-10-17
Status: Approved architecture and mapping policy; code implementation and corpus-level verification pending.
Authority: OMG SysML v2.0 Language and Transformation: https://www.omg.org/spec/SysML/2.0

## Normative semantics
- Native InterfaceDefinition is a specialized ConnectionDefinition; its interface ends are PortUsages.
- Native InterfaceUsage is a specialized ConnectionUsage with ends restricted to PortUsages. Preserve ownership, typing, multiplicity, direction and exact role/port-end references.
- Interface != generic Connection, Flow, Binding, Message or Allocation. Connecting two graphical port symbols does not alone establish interface semantics.
- PortDefinition/PortUsage and conjugated port semantics stay distinct. Conjugation reverses in/out directional features under normative rules, not arbitrary line direction.
- Existing EA ProxyPort and FullPort categorization follows previously approved distinct treatment; neither kind alone dictates the relationship type. A physical/full port may still be a genuine native PortUsage, not reduced to a simple connector.
- Standard SysML v2 definitions and usages are separate. Referencing an InterfaceDefinition does not replicate its reusable definition per occurrence.
- Provided/Required interface relationships in EA are evidence of contract/compatibility, NOT automatically native InterfaceUsage. Translate compatible typed features, port direction/conjugation and interface end constraints as supported by source data; otherwise preserve source metadata and flag.

## Translation matrix
| EA source | v2 mapping | gate |
|---|---|---|
| Explicit EA port-to-port interface interaction | InterfaceUsage, optionally typed by InterfaceDefinition | Both resolved ends correspond to PortUsages; valid context and type compatibility |
| EA interface classifier/contract | InterfaceDefinition or other compatible native type/feature construct | Must match interface-end and ownership semantics; no name-only guessing |
| Port-to-port EA connector with ordinary connectivity semantics | ConnectionUsage | Do not reclassify as interface just from port endpoints |
| EA Provided/Required relationships | Compatible port feature typing, directional/conjugated contract where justified | Preserve original roles; flag unsupported translation |
| EA Binding Connector | Native Binding per separate approved rule | Never convert merely because both ends are ports |
| EA item/information flow through ports | Native Flow per approved Flow rule | Does not by itself imply InterfaceUsage |

## EA translator
1. Inventory t_object ports, stereotypes, classifier references; t_connector connector types/stereotypes, ends, direction; t_xref, tagged values, conveyance and provided/required info as available.
2. Resolve original connector endpoints to canonical PortDefinition/PortUsage, with correct containing PartDefinition/PartUsage and full/proxy port distinction in provenance.
3. Identify explicit interface semantics; map only compatible candidates to native InterfaceDefinition and InterfaceUsage, with correctly typed port ends and end references.
4. Resolve conjugation/in-out features and validate two-sided compatibility in model context, including nested interface layers.
5. Preserve original EA GUID, connector direction/roles, classifier and tag evidence, source packages/diagrams and transformation rule version.
6. Every source connector/element gets a disposition, stable target identity or explicit exception record. No silent coercion, omissions, manufactured ports or inferred direction.

## BOM translator
- Reuse canonical parts, assemblies, hardware connector/port identities and unit/attribute definitions from vault.
- BOM hierarchy and physical cabling do not by themselves create a native interface or directional contract.
- Preserve existing ports/interface usages across BOM updates and independently version BOM-specific quantity, UOM and revision history.
- Flag incompatible duplicate part identities or assumptions; EA->BOM and BOM->EA import order should reconcile without changes to native interface semantics.

## Workbench
- Draw from one port (or participant with selectable port) to another; then display filtered eligible choices, including Interface only when semantic validity passes.
- Offer native InterfaceDefinition selection using alphabetically ordered vault-defined dropdown, plus filtered port-end role selector, feature directions and possible conjugated port presentation.
- Preview owner, both ends, typed usage, exact native syntax and actual meaning before commit; no auto-creation from gestures without choice.
- Structural view: port contract/interface containment, roles and feature typing; graphical view: correct interface/port display; tabular view: endpoints, direction, definition, provenance, validation; textual view: native SysML.
- Custom Canvas and saved per-view element/relationship filters can hide Interface independently from Connection/Flow/Binding without deleting semantics.
- Editing and removing interfaces must preserve referential integrity and warn if hidden relationships are impacted. Navigation supports participants, ports, interface definition, usage, inherited properties and source EA evidence.

## Vault definitions
- Store reusable PortDefinitions, conjugated forms as native semantics, InterfaceDefinitions, typed PortUsages/InterfaceUsages, attributes, enumerations, flow payloads and quantity/unit definitions in vault.
- Distinguish standard-library definitions from user-owned vault definitions and custom extensions; stable canonical IDs and qualified names.
- No hardcoded engineering dropdown values or duplicate port definition per usage.

## Validation
1. Parse/semantic conform native v2 InterfaceDefinition/Usage with valid port ends.
2. Conjugated ports and in/out directions agree across interface.
3. EA port-to-port interface imports as InterfaceUsage with correct owning context and original source GUID.
4. Generic connection between ports does not get silently turned into InterfaceUsage.
5. Provided/Required legacy contract without resolvable port does not fabricate an interface and retains a visible exception.
6. Reusable interface definition shared across independent usages, no unintended copies.
7. Full/proxy provenance preserved and actual PortUsage types valid.
8. BOM reimport preserves ports/interface references and does not manufacture interfaces.
9. Workbench draw/edit/repoint/delete updates canonical text/structure/Canvas with stable IDs; hide/show no semantic changes.
10. All source EA records accounted for with explicit mapping exceptions and original evidence.

## Follow-up tracker
INT-01 [EA] inventory port-to-port links, interfaces, provided/required relationships and source classifier cases.
INT-02 [Registry] create normative mapping table of InterfaceDefinition/Usage and PortDefinition/Usage, role/direction/conjugation constraints.
INT-03 [EA] implement context-aware port-end resolution and source evidence ledger.
INT-04 [Vault] reusable definition and usage index supporting qualified identity and native conjugation.
INT-05 [Workbench] draw-to-interface chooser, contract selector and native preview.
INT-06 [Workbench] structural/visual/text/table projections and independent type filters.
INT-07 [BOM] part/connector identity merge and non-inference tests.
INT-08 [QA] native parser/semantic tests including port contracts and inherited/nested interfaces.
INT-09 [QA] EA exception, round-trip, saved-view and import-order verification.
INT-10 [Docs] incorporate exact mapping in central catalog with normative reference and implementation status.

## Next reviewed relationship candidate
Dependency: general native SysML v2 dependency semantics versus allocations, interfaces, typing and specialization. EA Dependency must retain weaker dependency semantics rather than be automatically interpreted as allocation or physical connection.
