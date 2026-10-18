# Golden Import — Interface to Part aggregation

Decision date: 2026-10-17. Status: APPROVED mapping policy; row-level eligibility and native parser validation pending.

For EA Interface → Part aggregation where the interface is the child and the part is the owner, translate the source-defined ownership using the appropriate **native SysML v2 PortUsage or InterfaceUsage** based on the underlying interface classification and the approved port/interface taxonomy. Do not collapse ports and interfaces into one generic bucket. In particular, independently modeled full ports that are parts must preserve their appropriate physical/port semantics instead of being blindly reclassified.

Each EA Aggregation connector represents a distinct modeled usage even when endpoints repeat. Retain one note per reusable definition, with independent nested usages in the owning part definition. Preserve explicit EA role names, otherwise use deterministic derived names and collision suffixes. Carry applicable explicit multiplicity and retain unspecified multiplicity as unspecified. Retain original direction, aggregate-end flag, connector identity, subtype and round-trip provenance.

Workbench must show separate PortUsage and InterfaceUsage semantics in structural and visual views, including owned/connected behavior, navigable typing, validation and round-trip trace. Ambiguous interface classifications or incompatible ownership stay reviewable; do not force conversion. Verify actual native syntax before marking accepted.

Source audit context: 11 Interface → Part aggregation connectors in reduced QEAX classification; count is not native translation acceptance.
