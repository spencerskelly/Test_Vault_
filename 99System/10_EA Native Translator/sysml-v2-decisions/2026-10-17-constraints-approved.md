# APPROVED — Native SysML v2 Constraints
Date: 2026-10-17
Status: APPROVED — Relationship review #22

## Explanation
A constraint is an evaluable condition over model values, commonly Boolean. A reusable constraint definition specifies the rule, a constraint usage applies it in a context, and an assertion expresses that the condition is intended to hold. A constraint is not automatically a requirement, verification case, or observed pass/fail result.

## Scope
- Support native SysML v2 Constraint Definitions, Constraint Usages, and asserted constraints, along with other conforming constraint forms supported by the language.
- Store expressions and referenced features in authoritative SysML v2 syntax in Obsidian notes.
- Verify complete emitted syntax and model validity with a conforming SysML v2 parser.
- No blanket reinterpretation of text descriptions as mathematical constraints.

## EA migration
Translate only EA elements or relationships that explicitly model compatible constraint semantics and resolvable parameters, expressions, and owning context. Keep ambiguous legacy 'Design Constraint' entries as pending review; they may be prose requirements rather than formal evaluable constraints. Do not silently invent numerical thresholds or formulas.

## Workbench
- Structural view: definition, usage, owning context, parameters, referenced attributes, expression, and assertion status.
- Visual view: distinct constraint node/relationship with navigable parameter or attribute references (parametric representation); separate from physical connection.
- Inspector/editor: modify formula, parameters, bindings, type/units and assertion kind; any view edits authoritative note syntax and refreshes structure/diagrams.
- Validate expression parse, feature reference resolution, Boolean result for constraints, units/dimensional consistency where available, contextual ownership, and circular expressions.
- Support reuse: one canonical definition per type, multiple usages, without requiring per-usage Markdown notes.
- Documentation includes plain explanation, compatible examples and nonexamples, plus distinction from requirements, satisfaction, binding and calculation.

## Example (conceptual)
Current regulation condition: actualCurrent <= maximumCurrent. A reusable constraint may be applied in many charger contexts without defining another constraint type.

## Next native concept
Calculation Definitions/Usages, distinguished from Boolean constraints and assertion semantics; review exact native expression/result semantics.
