# Reference Subsetting — Supported, No Current Import Mapping
Date: 2026-10-16
Status: APPROVED — support only

## Rule
Support the native SysML v2 reference-subsetting feature relationship (`references` / `::>`) in future authored models. No existing EA elements or connectors will be mapped to reference subsetting by default. Do not infer it from Generalization, Dependency, reference part, or similarly named relationships.

## Workbench
- Recognize, parse, validate, author and export native reference-subsetting syntax in the authoritative SysML v2 note.
- Structural view displays referencing feature and target feature, separate from feature typing and composite ownership.
- Visual view displays a distinct typed relationship, not a physical connection, composition edge or `ref part`.
- Editing via text, tree or diagram updates the same owning note syntax and synchronizes other views.
- Usage notes are optional, canonical shared definitions are not duplicated.
- Any future mapping from EA requires an explicit approved rule.

## Decision context
This is a supported capability only; current imported model has no planned reference-subsetting links.

## Next review
KerML/SysML feature chaining and how a nested feature path is resolved without inventing an additional part or connection.
