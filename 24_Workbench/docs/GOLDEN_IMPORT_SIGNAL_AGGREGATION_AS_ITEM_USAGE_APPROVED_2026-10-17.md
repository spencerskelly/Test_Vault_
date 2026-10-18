# Golden Import — Signal aggregation as nested ItemUsage

Decision date: 2026-10-17. Status: APPROVED mapping policy; source reconciliation and native SysML v2 parsing pending.

For genuine Signal → Signal composition, model the parent as a reusable SysML v2 `ItemDefinition` and create a distinct nested `ItemUsage` typed by the child's reusable `ItemDefinition` for **each** EA Aggregation connector. Do not merge separate source connectors just because the endpoints match, and do not create an additional MDSE definition note for each usage.

Preserve connector identity, aggregate end and direction, source role/name, multiplicity and provenance. Use an explicit role name when present; otherwise derive a deterministic child-based name with collision suffixes. Missing cardinality stays unspecified. Reject or flag non-compositional grouping, incompatible endpoint types and ownership cycles without silently generating native composition.

Workbench: show ItemUsage composition in both textual structural hierarchy and visual connection/containment views, with navigable parent/usage/type, validator explanations, and round-trip connector provenance. Keep ItemUsage distinct from PartUsage, ActionUsage and descriptive MDSE-only links.

Source audit context: six Signal → Signal aggregation connectors in the reduced QEAX. The approved rule does not constitute six accepted native translations; row-level evidence and parser testing remain outstanding.
