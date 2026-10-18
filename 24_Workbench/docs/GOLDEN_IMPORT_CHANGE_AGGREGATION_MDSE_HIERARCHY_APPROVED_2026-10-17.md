# Golden Import — Change to Change aggregation

Decision date: 2026-10-17. Status: APPROVED; translation implementation pending.

For the twelve EA Change → Change aggregation connectors in the reduced QEAX, preserve the parent–child hierarchy as **MDSE-specific descriptive relationships** between Change notes. Change remains an MDSE note rather than a native SysML v2 definition; do not invent a custom SysML v2 relationship or translate these as native PartUsages.

Each distinct connector must remain independently traceable, even if endpoints repeat. Store parent and child references, source connector identity, aggregation end/direction, explicit roles and multiplicity where provided, and EA provenance in the MDSE model/evidence. Keep absent multiplicity unspecified. Workbench structural hierarchy and visual views must display and navigate this relationship clearly and distinguish it from native SysML v2 ownership. Validate endpoints, cycles and round-trip stability; retain ambiguity diagnostics rather than silently dropping source relationships.

Approval is a policy decision, not proof that all twelve rows are successfully translated. Local connector-level reconciliation and Workbench verification remain pending.
