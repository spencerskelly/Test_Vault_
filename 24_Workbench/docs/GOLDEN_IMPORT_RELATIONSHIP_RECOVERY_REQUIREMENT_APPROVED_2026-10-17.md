# Golden Import — EA RecoveryRequirement

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation and native library/parser verification pending.

- EA `Dependency:RecoveryRequirement` shall be translated using native SysML v2 **requirement derivation** semantics, not generic Dependency.
- Interpret the recovery requirement as the **derived requirement** and its source requirement as the derivation basis, preserving exact EA connector orientation and provenance. Confirm endpoint roles from trusted EA evidence; do not assume that raw source/target direction expresses derived-to-source without checking.
- Preserve original EA connector GUID, source type/stereotype `RecoveryRequirement`, endpoints, and normalized derivation direction in the source ledger.
- Keep derivation distinct from requirement decomposition, allocation, satisfaction, and verification; no additional MDSE note for the relationship.
- When either endpoint is incompatible with requirement derivation or source roles are ambiguous, flag for review instead of fabricating a native derivation.
- Validate syntax with pinned official SysML v2 standard library and parser before native acceptance.
