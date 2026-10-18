# Golden Import — Component realizing function

Decision date: 2026-10-17. Status: APPROVED translation rule; implementation and official native parser validation pending.

- When an explicit EA Realization links a component to an Activity representing a function, translate it to native SysML v2 **perform** semantics: the component's part context performs a typed `ActionUsage` referencing the reusable function `ActionDefinition`.
- Preserve one MDSE note for each reusable component and function definition. The owned `ActionUsage` does not create another note.
- Resolve EA Realization endpoint orientation and confirm component / function endpoint kinds from trusted source evidence. Do not treat every Realization as `perform`.
- Retain original EA connector ID, stereotype, orientation and provenance in the local disposition ledger.
- If endpoints, ownership, or role evidence are insufficient, flag for review rather than inventing performance semantics.
- Other Realization cases (including requirement satisfaction) remain separate relationship categories to review.
