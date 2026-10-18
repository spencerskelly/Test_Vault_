# Golden Import — EA Use Case Extend

Decision date: 2026-10-17. Status: APPROVED translation policy; runtime implementation and official SysML v2 conformance pending.

- EA UseCase `«extend»` maps to an **optional, conditional use case usage** within the extended (base) use case, typed by the extending reusable `UseCaseDefinition`.
- Preserve explicitly modeled extension conditions and source-defined extension points where available; do not invent conditions or treat optional participation as unconditional.
- Preserve EA connector direction and roles (extending vs extended case), source connector identity, stereotype and provenance. Verify source orientation rather than assuming it from diagram layout.
- Each reusable definition has one MDSE note; contextual use case usages do not generate additional notes.
- Keep `extend` distinct from required `include`, specialization, generic Dependency, or executable control flow inferred from a diagram.
- If extension context or condition semantics cannot be represented in verified native SysML v2 constructs, flag for review and preserve evidence; do not silently reduce to generic dependency.
- Validate native syntax, guard/condition semantics, reference resolution and idempotent reimport before acceptance.
