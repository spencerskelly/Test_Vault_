# Golden Import — Requirement Derivation

Decision date: 2026-10-17. Status: APPROVED; implementation and pinned SysML v2 standard-library/parser conformance pending.

- Map explicit EA `«deriveReqt»` relationships to native SysML v2 standard-library **requirement derivation** semantics.
- Preserve original **derived requirement → source requirement** direction, verified against trusted EA connector roles/orientation.
- Keep derivation distinct from requirement decomposition, specialization, refinement, allocation and satisfaction. Do not infer derivation from nested requirements.
- Preserve source connector identity, type/stereotype, endpoint identities and provenance in the local-only disposition ledger.
- Only translate to native semantics when both endpoints resolve to valid requirements and the standardized derivation construct parses; otherwise retain an explicit review disposition and source evidence.
- One MDSE note per reusable requirement definition. Derivation relationships do not create extra MDSE notes.
