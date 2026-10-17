# Golden Import — Nested states and activities

Decision date: 2026-10-17. Status: APPROVED translation policy; source-specific validation and parser conformance pending.

- Direct EA element nesting, even without an Aggregation or Composition connector, is evidence of **local semantic ownership** for nested States and Activities.
- Translate nested States to native SysML v2 local `StateUsage` in the owning state/workflow context; translate nested Activities to local `ActionUsage` in the owning action/workflow context, using reusable definitions where supported by source evidence.
- Do not create separate MDSE notes for the local usages; retain original EA type/stereotype, IDs and provenance in the owning model representation.
- Physical Parts are **not** automatically treated as owned PartUsages solely because one EA element is nested under another; require explicitly supported physical containment evidence.
- EA Package hierarchy remains purely organizational and does not establish semantic ownership.
- Flag missing/invalid parent, conflicting ownership, or ownership cycles for review; avoid invented owners or native constructs.

Next relation topic to resolve separately: EA nesting of non-State/non-Activity elements and ownership of generic behavior/ports.
