# Golden Import Step 2 — StateNode usages

Decision date: 2026-10-17. Status: APPROVED; implementation pending.

- Each EA `StateNode` maps to an independent native SysML v2 `StateUsage` within its owning workflow/state context, where that context can be established from source evidence.
- Multiple occurrences, even if they reference the same reusable `StateDefinition`, remain distinct local usages with their own stable identities and source provenance.
- Do not create an additional MDSE note for each usage; model usages within the owning workflow element's representation.
- Preserve original EA type/stereotype and identities in the owning model's structured provenance as appropriate.
- If owning context cannot be determined, defer that local usage with a diagnostic rather than invent an owner.
- Verify independent occurrence identities, ownership, native serialization, and repeat-import stability.
