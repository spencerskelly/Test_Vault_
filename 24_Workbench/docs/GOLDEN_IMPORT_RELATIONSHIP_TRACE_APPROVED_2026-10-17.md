# Golden Import — EA Trace

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation and native parser validation pending.

- Explicit EA `«trace»` relationships map to native SysML v2 `Dependency`, preserving original client-to-supplier source orientation and endpoint identities.
- Preserve `eaStereotype: trace` and original EA connector type, GUID and direction in provenance/evidence; retain the distinct source trace label even though native type is Dependency.
- Do not infer allocation, ownership, satisfaction, verification, derivation, refinement or execution semantics from trace.
- Specialized source relationship handling takes precedence over generic dependency handling, even when the target native construct is the same.
- Unresolved direction/endpoints are flagged for review instead of fabricating a native edge. No additional MDSE usage note is created for this relationship.
