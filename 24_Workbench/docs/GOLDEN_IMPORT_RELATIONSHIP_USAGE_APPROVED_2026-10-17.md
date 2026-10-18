# Golden Import — Generic EA Usage

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation and native parser verification pending.

- Generic EA `Usage` translates to native SysML v2 `Dependency`, retaining its original EA type/stereotype and source relationship identity in provenance.
- Preserve original client → supplier direction using trusted EA endpoint-role evidence.
- Do not infer physical ownership, nested PartUsage, functional performance, allocation, satisfaction or other stronger relationships from generic `Usage` alone.
- Apply a more specific approved native construct only where the EA source independently supplies explicit evidence: for example physical assembly containment → owned PartUsage; component performing a function → `perform` ActionUsage.
- Unresolved endpoints or direction remain flagged for review. Relationships do not create additional MDSE notes.
- Validate native syntax and reimport consistency before acceptance.
