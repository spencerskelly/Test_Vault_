# Golden Import — EA Use Case Include

Decision date: 2026-10-17. Status: APPROVED translation policy; runtime implementation and native SysML v2 parser verification pending.

- EA UseCase `«include»` maps to a **required nested use case usage** in the including case, typed by the reusable `UseCaseDefinition` of the included case, rather than an ordinary generic Dependency.
- Preserve original including -> included endpoint roles and connector direction from trusted EA evidence; don't infer inclusion from naming or package location.
- The reusable included definition retains a single MDSE note. Its contextual usage within the including case does not create a separate note.
- Preserve original EA connector identity, type, stereotype, endpoint identities and provenance; unresolved ownership/target typing stays reviewable.
- Do not silently treat `include` as optional participation, `extend`, specialization or arbitrary nesting. Verify the exact native use-case usage form against pinned SysML v2 parser/library prior to declaring acceptance.
