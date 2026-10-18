# Golden Import — Aggregation and Composition

Decision date: 2026-10-17. Status: APPROVED translation policy; source-by-source validation and native parser verification pending.

- For both EA Aggregation and Composition, when explicit source evidence supports **physical assembly containment**, translate the child into a typed native SysML v2 `PartUsage` owned by the parent part/assembly/context, referencing the child's one reusable `PartDefinition`.
- Reusing the same definition across multiple parent assemblies produces separate owned usages, **not** duplicate definition notes.
- Preserve source relationship identity, EA aggregation/composition flags, endpoints, multiplicity and provenance in the local relationship ledger.
- Nonphysical grouping must not imply part ownership or generate an owned PartUsage. Preserve its original evidence and identify an independently approved native relationship if appropriate; otherwise flag review.
- EA Package/folder nesting remains organizational only; it never establishes physical containment.
- Validate orientation, parent/child typing, ownership cycles, duplicate usages and multiplicity before generating native syntax. Preserve ambiguities as review rather than inventing semantics.
- Physical containment/ownership is represented by native owned PartUsage features, not by inventing a custom SysML v2 binary Aggregation relationship.

Next relationship topic: distinguish EA nested element containment from physical assembly containment and local nested states/actions.
