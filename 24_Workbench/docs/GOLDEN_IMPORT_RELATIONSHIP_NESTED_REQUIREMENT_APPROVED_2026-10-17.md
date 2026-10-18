# Golden Import — Nested requirement decomposition

Decision date: 2026-10-17. Status: APPROVED; implementation and native parser conformance pending.

- Direct nesting of an EA Requirement within another EA Requirement is sufficient evidence of requirement decomposition even when no explicit connector exists.
- Translate the nested child as a native SysML v2 requirement usage within the owning parent requirement context, referring to the child's reusable `RequirementDefinition`.
- One MDSE note per reusable requirement definition. Do not create separate MDSE notes for contextual requirement usages.
- Preserve the child and parent source identities, original EA type/stereotype, hierarchy and provenance. Organizational EA Package/folder nesting alone does not imply requirement decomposition.
- Requirement decomposition remains distinct from requirement derivation; do not infer deriveReqt from nesting.
- Flag invalid owners, cyclic decomposition, unresolved child definition references or conflicting semantics for review rather than fabricating relationships.
- Native serialization, reference typing and repeat import acceptance remain pending.
