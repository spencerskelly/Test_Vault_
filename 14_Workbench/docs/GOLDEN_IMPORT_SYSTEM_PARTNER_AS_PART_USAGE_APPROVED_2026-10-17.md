# Golden Import — System Partner as child PartUsage

Decision date: 2026-10-17. Status: APPROVED mapping policy; implementation and native validation pending.

An EA `System Partner` mapped to a reusable SysML v2 `PartDefinition` has **no special prohibition against being an owned physical part usage**. When an EA aggregation or composition establishes a compatible owning parent and this System Partner as its child, translate it **by exactly the same PartDefinition-to-PartUsage rules as any other part definition**: create a distinct typed owned `PartUsage` in the parent per source relationship.

- Do not downgrade, externalize, or discard ownership merely because the child definition is stereotyped `System Partner`.
- Its `external` designation is descriptive of modeling context and does not override explicitly modeled structural ownership.
- Retain one reusable definition note for the child; never clone the definition for each usage.
- Preserve each separate connector as its own usage declaration, including the source role when specified, otherwise deterministic names, and its source connector provenance.
- Explicit EA multiplicity flows to the relevant usage; missing multiplicity remains unspecified.
- Normal validity checks still apply: trusted end orientation, compatible semantic parent and child, ownership cycles, stable identities, and native SysML v2 syntax. Do not invent relationships from mere co-occurrence.

This supersedes any earlier proposed blanket distinction that would treat a System Partner child as only a contextual external participant instead of permitting owned physical PartUsage.
