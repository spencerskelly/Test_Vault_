# Golden Import — Explicit EA Allocation

Decision date: 2026-10-17. Status: APPROVED mapping policy; implementation, row-level role validation and official SysML v2 parser verification pending.

- Explicit EA `«allocate»` translates to native SysML v2 allocation semantics when both endpoints and their allocation roles are valid.
- Preserve original source and target roles, connector direction, identity, EA type/stereotype, and source provenance.
- Allocation represents a source-to-target mapping or assignment. It does **not** imply satisfaction, verification, specialization, containment, or execution order.
- This complements separately approved mapping of component-to-component and component-to-requirement EA Realization to allocation; do not conflate different EA source families in provenance.
- If direction, endpoint eligibility, or roles are unresolved, keep an explicit review disposition rather than fabricating an allocation.
- No extra MDSE note for relationships. Verify native syntax, source ledger disposition, and stable reimport.
