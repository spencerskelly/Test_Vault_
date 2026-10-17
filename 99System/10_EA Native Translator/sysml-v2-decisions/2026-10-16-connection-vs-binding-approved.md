# Approved rule: Connection versus Binding Connector

Date: 2026-10-16
Status: APPROVED — Option A
Scope: EA to SysML v2 to MDSE translator and Workbench

## Semantic mapping
- Ordinary connection: native SysML v2 connection definition or usage, as appropriate; connect A to B.
- Binding connector: native SysML v2 binding connector usage; bind A = B.
- Do not infer a binding from an ordinary EA connector.
- Ambiguous EA types retain source semantics and are flagged for classification.

## Workbench structural view
- Store each as a first-class model relationship with distinct native type.
- Show owner, endpoint features, related definitions/usages and source identity.
- Preserve EA GUID, original connector metadata and translation rationale.
- Changes in either view update the same underlying model.

## Workbench visual view
- Distinguish ordinary connection and binding/equality visibly.
- Selectable objects with endpoint navigation and property inspector.
- Editing endpoints updates shared structure, not only the drawing.
- Layout is separate from semantics; hiding a line never deletes the relationship.

## Validation and acceptance
- Validate endpoint resolution and owner context for both.
- For bindings, validate exactly two ends and appropriate feature compatibility.
- Round-trip serialize connection versus binding without semantic loss.
- Test with imported EA source cases, nested usages and ambiguous connector cases.

## Next decision pending
Interface versus connection versus exposed internal port/feature.
Native SysML v2 interface definition/usage is a specialized connection between ports. 'Exposure' is translation terminology, not automatically a new native SysML v2 relationship.
