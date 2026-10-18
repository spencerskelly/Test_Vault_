# Golden Import — Shared and composite EA aggregation

Decision date: 2026-10-17. Status: APPROVED translation policy; fixture row validation and parser verification pending.

- EA shared aggregation (`1`) and composite aggregation (`2`) **both create an owned native SysML v2 usage** when source endpoints and trusted evidence establish a valid semantic parent–child relationship.
- Select usage type according to approved parent/child semantic kinds: physical assembly → owned `PartUsage`; nested states → `StateUsage`; nested actions → `ActionUsage`. Do **not** force every aggregation into physical containment.
- Reference a single reusable definition; no new MDSE note for the usage.
- Preserve original EA shared/composite flag, direction, endpoints, connector identity, and provenance. Do not silently merge distinct aggregation source records.
- Organizational grouping alone, including EA package hierarchy, must not create semantic usage. Invalid or ambiguous parent–child types remain reviewable.
- Test explicit orientation, compatible usage kind, multiple parents/reuse, ownership cycles, multiplicity, and reimport stability. Native parser acceptance is not yet claimed.

Next audit: generalization child-to-parent source orientation and endpoint compatibility.
