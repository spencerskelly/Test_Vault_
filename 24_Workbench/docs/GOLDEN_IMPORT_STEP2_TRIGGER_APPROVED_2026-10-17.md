# Golden Import Step 2 — EA Trigger mapping

Decision date: 2026-10-17. Status: APPROVED; implementation and native parser validation pending.

- EA `Trigger` maps to a native SysML v2 transition trigger within its owning state machine/state-transition context.
- No separate MDSE note is created for a local trigger usage; preserve source identity, EA type/stereotype and provenance in the owning model metadata.
- Preserve explicit event, guard and transition association when present; do not invent triggers or owners from naming or diagram proximity.
- When owner or transition cannot be reliably resolved, disposition is deferred review with source evidence retained.
- Validate native syntax/semantics against pinned SysML v2 parser and verify reimport stability.
