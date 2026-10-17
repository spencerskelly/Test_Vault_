# APPROVED — SysML v2 Binding Connector
Date: 2026-10-17
Status: APPROVED — Relationship #13

## Meaning
A native binding connector asserts equality/equivalence between its two bound features in the relevant context. Binding does not, by itself, mean physical connectivity, communication, allocation, or dependency.

## User-readable example
A Charger exposes outputVoltage and its internal controller exposes measuredVoltage. `bind outputVoltage = controller.measuredVoltage;` constrains them to equivalent values. It does not describe a wire.

## Correct use
- Equality of compatible feature values or identity references, with resolvable feature paths.
- Explicit use of native SysML v2 binding semantics.
- Do not infer a binding merely because two ports are connected or have same type/name.

## EA mapping
Map genuine EA Binding Connectors directly to native SysML v2 bindings, maintaining the bound ends and owner context. Normal EA Connector remains a Connection Usage unless evidence establishes different semantics. Resolve canonical alias identities before translating endpoints. Invalid or ambiguous sources must produce validation findings, not misleading bindings.

## Workbench
- Structural view: independent binding usage listed in its owning context with two navigable endpoints and equality meaning.
- Visual view: distinguish from ordinary connection and interface using explicit equality-specific styling; user can select endpoints and binding itself.
- Inspector: canonical feature paths, compatible types/values, scope, validation and native binding syntax.
- Editing from note/tree/diagram alters authoritative SysML v2 text in owning Obsidian note, then refreshes both projections.
- Validate exactly two resolvable ends, compatibility, and context/visibility; do not create an extra part or link ownership.
- Reusable definitions remain canonical; usage notes optional.
- Documentation must include formal meaning, accessible explanation, valid/invalid examples, contrast with adjacent connections and interface concepts.

## Example
```sysml
part def Charger {
    attribute outputVoltage : Real;
    part controller : Controller;
    bind outputVoltage = controller.measuredVoltage;
}
```
Example assumes Controller has compatible measuredVoltage attribute and requisite namespaces are resolvable. Confirm full syntax/compatibility using conforming SysML v2 parser before production output.

## Next native relationship
Flow / item flow, distinguished from Connection and Interface. Review formal semantics and Workbench representation.
