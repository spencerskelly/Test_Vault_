# EA Generalization import audit — 2026-10-16

Status: Analysis and proposed refinement, NOT an approved change to Option A.

Source: uploaded EA_2026_10_15_endgame_mini.qeax; SQLite t_object and t_connector.

## Evidence
- Elements: 11,447; connectors: 14,688; Generalization: 3,735.
- Generalizations with different EA Object_Type: 46.
- Generalizations with different stereotype text (including blank): 782; overlaps other counts.
- All generalization endpoints resolve to t_object.
- Leading endpoint groups: Hardware Component→Hardware Component 767; Logical Signal→Logical Signal 579; System State→System State 218; UseCase→UseCase 216; Activity(blank)→Activity(blank) 189; System Function→System Function 187; Physical Component→Physical Component 181; Module→Module 150; Data Interface→Electrical & Material Interface 108.
- 45 EA Object→Class generalizations include specific software versions and physical cable/transformer occurrences, candidates for typing rather than subclassification.
- One State→Activity generalization exists and requires manual review.

## Proposed import policy
Keep all source connectors, GUIDs, endpoints, stereotypes, direction and owning context in a source-evidence graph. Do not apply an unconditional Generalization→specialization conversion.
Classify each edge: definition subclassification; usage typing (which is not an explicit generalization in the target); usage subsetting; usage redefinition; decomposition/containment; ambiguous/invalid.
Classification requires endpoint kind, definitions vs usages, EA typing and parentage, stereotypes and neighboring relations; avoid treating names alone as semantics.
Don't invent v2 syntax. Emit native constructs only after validation. For unresolved edges, retain source-only links in a separate provenance/translation section and produce a finding. Preserve original EA generalization even when the target relation changes.

## Workbench structural and visual requirements
Separate original EA relationship from resolved native v2 relationship. Make proposed/confirmed/unresolved status filterable. Source graph and target model should be separately queryable.
Definitions and usages must have distinct icons/tree nodes; tree shows real containment, not fictitious parentage caused by an EA Generalization.
Diagrams: native inheritance for confirmed subclassification; reference/typing link for usage to definition; distinct subset/redefinition; actual containment for nested state/action usages; warning or dashed 'unresolved source generalization' edge for unmapped cases. Never render an unresolved edge as confirmed v2 inheritance.
Inspector shows source endpoint IDs, object types, stereotypes, owner context, rationale, confidence and chosen v2 syntax; source and transformed relation selectable. Summary counts, decision log and reversible overrides.
Golden tests from real QEAX: two matching hardware component defs, signal defs, state defs, use cases, activities, mixed interface stereotypes, software-version Object→Class, one State→Activity edge.

## Suggested next approval
A. Conditional transformation with source evidence kept separate; no blanket specialization.
B. Blanket specialization for definition-to-definition and review other cases.
C. Manual review of all 3,735 prior to translation.
