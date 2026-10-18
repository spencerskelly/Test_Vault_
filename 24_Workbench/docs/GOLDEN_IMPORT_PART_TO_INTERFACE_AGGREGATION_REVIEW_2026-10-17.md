# Golden Import — Part child of Interface exception

Decision date: 2026-10-17. Status: APPROVED for source review; native mapping **not approved**.

The reduced QEAX audit identified one EA Aggregation connector whose child is classified as Part and whose aggregate parent is classified as Interface. Do not automatically reverse the connector or convert it into an owned PartUsage or InterfaceUsage. Flag the row for targeted source inspection and preserve its original direction, aggregate-end flag, source identifiers and provenance in the local-only reconciliation ledger.

Review the EA endpoint subtypes, stereotypes, roles, connector notes, any owning port semantics, and contextual diagram/model evidence before proposing a native SysML v2 construct. The fact that an InterfaceDefinition does not necessarily own a physical PartDefinition makes this an exception rather than an automatic mapping. Keep this distinct from the separately approved Interface-child → Part-parent mapping. Do not assert native validation until completed.

Workbench: surface a review diagnostic, show the source connector without inventing ownership, and support navigation to both endpoints and original evidence. Round-trip/provenance must remain intact.
