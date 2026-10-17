# APPROVED — Subclassification / EA Generalization
Date: 2026-10-16
Status: APPROVED

## Meaning and direction
For compatible definition/classifier endpoints, native SysML v2 subclassification has the same intended meaning as the project's EA Generalization: the specific element is a kind of the general element, and the inheritance arrow points from specific toward general. Adopt as the canonical relationship rule.

## Scope
- Native subclassification of suitable definitions (e.g., part, action, state, port, requirement definitions).
- Import convention already approved: EA Generalization maps to specialization/subclassification by default, with ability to repair exceptions in the SysML v2 model.
- This rule does not mean containment, configuration similarity, or function implementation.
- Native syntax: `part def ProCoreEdge specializes IndustrialCharger;` with `IndustrialCharger` a compatible definition.

## Workbench
- Structure: show parent classifier and inherited features without duplicating definitions.
- Visual: inheritance/generalization arrow points at general definition, preserving familiar EA direction.
- Edits from tree, diagram, or textual note change authoritative SysML v2 syntax in note; other views refresh.
- Validate kind compatibility and prohibited inheritance cycles.
- Reused definitions are canonical; usages do not automatically acquire separate notes.
- EA is migration-only and obsolete source connectors need not remain after successful conversion.

## Next relationship
Feature typing: how an occurrence/usage is typed by one canonical reusable definition, separate from classifier specialization.
