# Golden Import — Repeated aggregation connections represent distinct usages

Decision date: 2026-10-17. Status: APPROVED clarification; implementation pending.

- Do **not** collapse multiple EA Aggregation/Composition connectors between the same parent and child definition solely because their endpoints match.
- Each independently modeled connector can represent a distinct use/role of that same part. Preserve each as a **separate owned PartUsage declaration (a separate line within the owning parent definition)**, referencing the same reusable PartDefinition.
- Still create only **one MDSE note for the reusable PartDefinition**; do not create a new reusable definition or note per relationship.
- Preserve separate source connector IDs, roles/names, multiplicities and provenance. Keep omitted multiplicity unspecified.
- Do not infer that identical endpoint pairs are duplicate modeling errors. Deduplication requires affirmative evidence that source relationships are truly redundant, not just matching endpoints.
- Validate distinct, deterministic usage identities and names; if usage names collide, disambiguate without changing the reused definition or silently merging occurrences.
- Apply previously approved ownership-cycle checks, compatible owner/child kinds and native parser validation.
