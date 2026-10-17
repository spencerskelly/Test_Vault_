# Golden Import — MDSE flagLink fallback for questionable relationships

Decision date: 2026-10-17. Status: APPROVED policy; implementation and round-trip testing pending.

## Policy

When an EA relationship cannot be confidently mapped to an approved native SysML v2 relationship or usage, preserve it as an **MDSE `flagLink`** for later semantic correction. Do not invent native SysML v2 semantics or silently discard the relationship. This fallback applies to *all remaining questionable relationship families*, including the five State-child → Activity-parent aggregations and the one previously flagged Part-child → Interface-parent aggregation, unless subsequent evidence supports a native construct.

- Store one separately identifiable flagLink record per original EA connector; do not merge repeated connectors based only on endpoints.
- Retain source connector ID/GUID where available, source and destination element IDs, original endpoint orientation, connector family and stereotype, role names, aggregation flags, explicit multiplicity, EA package/context, and provenance.
- Keep `flagLink` **MDSE-only** in a clearly separated relationship section; it is not a custom SysML v2 relationship and must not appear as native ownership, flow, or connection syntax.
- Include a machine-readable reason/validation status (`unresolved_semantics`, `incompatible_endpoint_kinds`, `ambiguous_direction`, etc.), review notes and optionally proposed mappings. Missing multiplicity stays unspecified.
- Workbench structural and visual views must show an explicitly flagged link with navigable endpoints, editable review/disposition, clear distinction from native relationships, and source traceability. An unresolved flagLink must not imply containment in hierarchy or physical ownership.
- Later correction replaces/resolves the flagLink by an explicitly approved native or MDSE relationship while retaining its source connector identity and disposition history. Never leave a second active relationship accidentally representing the same source connector.
- Preserve detailed source-model evidence in local-only reconciliation ledgers; only rules, tools, synthetic tests and aggregate findings are committed to the methods repo.
- Acceptance tests: deterministic identity across reimport; repeated connectors stay distinct; endpoints and directions unchanged; unresolved links survive round-trip; corrected disposition is reversible and traceable; no accidental native serialization.

This policy does not override any already approved direct mappings: use a native construct when endpoint semantics and evidence support it, and reserve flagLink for genuinely unresolved cases.

## Approved clarification — YAML link and explanation in note (2026-10-17)

The `flagLink` is stored as an **MDSE YAML link on the relevant note**, rather than merely an external exception ledger. The note body must contain a human-readable explanation of why that specific link is flagged, the observed source relationship, and what decision or evidence is required to resolve it. The YAML link carries stable target reference and original connector provenance; when multiple EA connectors target the same element, represent each independently and preserve connector identity. Show the YAML link and explanatory note text together in Workbench, with navigation and a clear unresolved indicator. This remains MDSE-only (not native SysML v2 syntax). Later replacement with an approved relationship must retain audit history and remove the active unresolved flag without silently losing provenance.

Illustrative shape only; final YAML schema and note section names require integration tests:

```yaml
flagLink:
  - target: "<MDSE-target-UID>"
    eaConnectorGUID: "<source-connector-GUID>"
    reason: "ambiguous_semantics"
```

In the note body, explain the source relationship and why its native interpretation is unresolved. Do not add model-specific source data to the methods repository.
