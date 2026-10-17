# Golden Import — EA StateFlow

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation and native SysML v2 parser verification pending.

- EA `StateFlow` between compatible states becomes a native SysML v2 **state transition** within its owning state machine/state context.
- Preserve the explicitly modeled source and destination state, trigger, guard and effect semantics, when available in the EA source.
- Do not invent missing triggers, guards, effects or workflow ownership. If these cannot be resolved, preserve the original evidence and flag the source relationship for review.
- Keep state definitions reusable and state usages local to the owning workflow, without generating additional MDSE notes for usages.
- Preserve EA connector identity, direction, endpoints, stereotypes and provenance in the local disposition ledger.
- Verify syntax, context, state references and repeat-import stability prior to native acceptance.
