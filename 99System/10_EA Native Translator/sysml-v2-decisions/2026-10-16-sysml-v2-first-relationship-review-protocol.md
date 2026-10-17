# SysML v2-first relationship review protocol
Date: 2026-10-16
Status: APPROVED REVIEW DIRECTION; individual relationship mappings pending approval

## Direction
Start with relationships defined by official SysML v2 and underlying KerML, NOT the set of EA connectors. Confirm native semantics, permissible source/target element classes or features, exact textual syntax, Workbench structural view, Workbench visual view, example and user approval. Only then map EA and legacy MDSE concepts. Native SysML v2 note syntax remains authoritative, usage notes optional, single canonical reusable definition per modeled type.

## Review sequence
1. Definition/classification: specialization, subclassification, feature typing.
2. Feature-specific relationships: subsetting, redefinition, reference subsetting, cross subsetting and related feature relationships.
3. Membership, ownership, imports and aliases; distinguishing ownership semantics from relationships.
4. Connection/interface/binding and contextual ends.
5. Port conjugation, flows, feature chaining, directional features.
6. Succession, transitions, action ordering.
7. Allocation and behavior mapping.
8. Requirement satisfaction, verification, derivation.
9. Analysis: constraints/calculations/assertions.
10. Dependency and remaining KerML/SysML native relationship kinds.

Review classes and semantic relationship metaclasses as distinct from user-visible model link types; include remaining native KerML variants in exhaustive inventory before catalog is certified complete.

## Approval template for each relationship
- Normative definition and source reference
- Valid endpoint/owner categories and cardinalities/context restrictions
- Canonical SysML v2 syntax tested in a conforming parser
- Example from industrial charger system
- Structural tree/projection
- Diagram notation, selections, edits
- Synchronized text update/read-write behavior
- Validation and bad example
- Decision status: accepted / constrained / extension / open
- EA mapping after native semantics approved

## Source references
- https://www.omg.org/spec/SysML/2.0/Language/PDF
- https://github.com/Systems-Modeling/SysML-v2-Release/tree/master/bnf

## Review notes
- Do not conflate semantic specialization metaclass with classifier subclassification, feature typing, subsetting or redefinition.
- Do not assume every underlying KerML relationship needs an explicit hand-authored connector: many appear through syntax or membership.
- Do not duplicate canonical definitions per usage.
