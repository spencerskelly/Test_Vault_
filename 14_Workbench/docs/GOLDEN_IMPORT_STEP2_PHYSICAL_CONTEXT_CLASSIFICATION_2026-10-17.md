# Golden Import Step 2 — Physical Context classification decision

Decision date: 2026-10-17. Status: user-approved conceptual classification; native representation detail pending.

EA source family: `Class:Physical Context`.

- If the source element includes/owns multiple parts, classify it as a **context** representing the composite interaction boundary and constituent parts. Do not classify it as a single external part.
- If it represents one part referenced by other model elements, map it to a reusable SysML v2 `PartDefinition` classified **external** in MDSE YAML.
- Definitions get exactly one MDSE note. Constituent/usage references do not create separate notes.
- Retain MDSE type/subtype plus original `eaType` and `eaStereotype` in YAML.
- EA packages remain organizational and are not evidence of physical composition. Require explicitly modeled constituent parts/relationships or trusted equivalent evidence.
- Do not introduce a custom SysML v2 relationship or assume a dedicated native `ContextDefinition` construct.

Pending one focused question: for a multiple-part context, should native SysML v2 serialization be a `PartDefinition` used as a context boundary, owning typed `PartUsage` references to its included parts (rather than a custom concept)? Mark such imports as review until approved.

Acceptance tests: single external part, multiple-part context, package-only grouping (must not become context), missing/ambiguous composition (review).
