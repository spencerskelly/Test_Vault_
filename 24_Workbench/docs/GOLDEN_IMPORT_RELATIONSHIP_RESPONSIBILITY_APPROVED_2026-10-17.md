# Golden Import — EA Usage:Responsibility

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation, evidence and native parser validation pending.

- EA `Usage:Responsibility` maps to native SysML v2 allocation (`allocate`) **when the source identifies an element responsible for a function or requirement**.
- Preserve the responsible element, responsibility target, EA source/target orientation, connector identity, type/stereotype and provenance. Normalize allocation roles from trusted source metadata rather than diagram layout.
- Do not infer satisfaction, verification, ownership, specialization, or execution order from responsibility assignment.
- Cases with insufficient evidence of who is responsible for what, or incompatible endpoints, receive an explicit review disposition; do not silently downgrade to generic Dependency or fabricate an allocation.
- Keep reusable definitions as single MDSE notes and relationships/usages within the owning semantic model without additional usage notes.
- Validate syntax, role eligibility, and idempotent import against the pinned native SysML v2 implementation.
