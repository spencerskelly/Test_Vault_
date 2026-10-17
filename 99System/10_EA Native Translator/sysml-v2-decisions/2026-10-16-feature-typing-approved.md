# APPROVED: Native SysML v2 Feature Typing
Date: 2026-10-16
Status: APPROVED — relationship review #2

## Definition
A feature typing relationship constrains the values of a feature/usage using an applicable type (definition). This is distinct from subclassification: typing a usage does not introduce a new subtype.

## Example
```sysml
part def CANTransceiver;
part def Controller {
    part canA : CANTransceiver;
    part canB : CANTransceiver;
}
```
Both usages have the same canonical reusable type definition, with independent contexts and identities.

## Permitted examples and constraints
- Part usage typed by compatible part definition.
- Action, state, port, attribute usages typed by compatible respective definitions.
- Validate type compatibility and reference resolution; reject dangling or incompatible type references.
- SysML v2 syntax in Obsidian owning note is semantic authority.
- A usage is represented in owning note syntax; separate Markdown note for every usage is NOT required.
- One canonical reusable definition for each modeled type.

## Workbench
- Structural: usages show owners, type labels, and navigation to canonical definition. Do not conflate a usage with a specialized definition.
- Visual: display usage as `usageName : DefinitionName`; selecting its type navigates to shared definition; optional typed-by edge in trace view only, not as a mandatory physical connection.
- Editing type in text/tree/diagram updates the canonical note's `: Type` syntax and refreshes synchronized views.
- Where-used reports are reverse queries, not duplicated links in the definition.
- Validate change impact on endpoints, multiplicities, specialized constraints and other affected usages; avoid creating new notes merely to represent usage.

## EA migration
EA Object imports as reusable `part def` by default; later genuine usages may be reclassified. EA Generalization defaults to subclassification; feature typing is a separate native relationship. Old EA source relationships are not permanent authoritative records.

## Next relationship: Subsetting
Evaluate SysML v2 feature subsetting as a precise subset-of-values relation, including allowed feature kinds, inherited context, and Workbench display. Do not confuse with nesting/part-of.
