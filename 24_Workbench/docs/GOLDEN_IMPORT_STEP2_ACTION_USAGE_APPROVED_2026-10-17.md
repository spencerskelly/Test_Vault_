# Golden Import Step 2 — EA Action

Decision date: 2026-10-17. Status: APPROVED; implementation and native SysML v2 parser validation pending.

- EA `Action` maps to a native SysML v2 `ActionUsage` owned by its containing action or workflow, not a separate reusable definition.
- No separate MDSE note is created for this local usage; preserve source EA type, stereotype, identity and provenance in the owning model representation.
- Allow **untyped ActionUsage** where the source has no reusable `ActionDefinition` classifier. Add explicit `UNRESOLVED_ACTION_TYPE` review flag; do not fabricate an action definition.
- Retain source-defined control, input/output and workflow relationships using their separately approved rules; do not infer behavior from package nesting or diagram position alone.
- If owning action/workflow cannot be established, preserve source evidence and defer with diagnostic rather than invent an owner.
- Acceptance: valid native syntax, stable local usage identity, no usage notes, visible unresolved-type flags, and repeat-import stability.
