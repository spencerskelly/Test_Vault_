# Golden Import Step 2 — EA Port

Decision date: 2026-10-17. Status: APPROVED; runtime implementation and native parser validation pending.

- EA `Port` translates to native SysML v2 `PortUsage` within its owning part/context.
- When the source identifies a reusable port type, reference its `PortDefinition` rather than duplicating a definition.
- Allow an untyped `PortUsage` where no type is established; mark it with `UNRESOLVED_PORT_TYPE` and preserve source provenance. Do not fabricate a `PortDefinition`.
- No separate MDSE note for a local port usage. Retain original EA type/stereotype and stable source identity in the owning model's metadata.
- Preserve explicit port connections and roles under separately approved connector translation rules; do not infer ownership from EA package placement.
- Validate ownership, typing where present, syntax, unresolved flag visibility and repeat-import stability.
