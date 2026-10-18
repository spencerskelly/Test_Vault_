# V2 connector and semantic operation definitions — authority index

Purpose: find the approved construct before modifying code. This index links to the original decision document; it is NOT a separate definition or authorization of syntax. [Program home](V2_PROGRAM_HOME.md) · [26-family source mapping](../24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md) · [Workbench help requirements](../24_Workbench/docs/SYSML_V2_RELATIONSHIP_REFERENCE_AND_HELP_PANEL.md)

## Governing semantic model
Native SysML v2 constructs can be feature ownership, usage, reference, typing, allocation, connection, binding, temporal succession or behavioral semantics rather than a generic binary edge. User-approved source mapping and per-row evidence are separate from grammar conformance and released implementation. Drawn line → eligible operation preview, not silent creation.

## Dedicated approved decisions (October 17)
| Concept | Definition / decision | Distinction and current implementation gate |
|---|---|---|
| General dependency | [Dependency](../24_Workbench/docs/SYSML_V2_DEPENDENCY_APPROVED_MAPPING.md) | Reliance, not arbitrary connection, ownership or timing |
| Flow and payload | [Flow](../24_Workbench/docs/SYSML_V2_FLOW_APPROVED_MAPPING.md) | Directed transfer, not Connection or ControlFlow |
| Interfaces and ports | [Interface](../24_Workbench/docs/SYSML_V2_INTERFACE_APPROVED_MAPPING.md) | Interface ends are port usages, not any drawn port line |
| State transition | [Transition](../24_Workbench/docs/SYSML_V2_STATE_TRANSITIONS_APPROVED_MAPPING.md) | State change with trigger/guard/effect, not generic Succession |
| Allocation / Perform / Exhibit | [EA allocation typed-endpoint decision](../24_Workbench/docs/SYSML_V2_EA_ALLOCATION_ELEMENT_TYPE_DECISION.md) | Action↔Object Perform, State↔Object Exhibit, Object↔Object Allocation with evidence |
| Shared/composite | [Owned usage decision](../24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_SHARED_COMPOSITE_USAGE_APPROVED_2026-10-17.md) | Shared/composite flags retained; typed usage not generic edge |
| Composition | [Physical aggregation and composition](../24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_AGGREGATION_COMPOSITION_APPROVED_2026-10-17.md) | Physical PartUsage only for valid physical source evidence |
| Repeated occurrence | [Distinct repeated usages](../24_Workbench/docs/GOLDEN_IMPORT_REPEATED_AGGREGATION_DISTINCT_USAGES_APPROVED_2026-10-17.md) | Same endpoints may represent distinct usages |
| Usage name | [Stable deterministic naming](../24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_USAGE_NAMING_APPROVED_2026-10-17.md) | Role/name first, deterministic collision handling, stable identity |
| Aggregate corpus | [Reconciliation](../24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_RECONCILIATION_2026-10-17.md) | 2,267 reviewed: 1,959 Part, 148 Action, 76 State, 10 UseCase, 6 Item, 12 Change hierarchy, 56 flagged |

## Reference catalog of additional approved native categories
[Full relationship reference and help-panel index](../24_Workbench/docs/SYSML_V2_RELATIONSHIP_REFERENCE_AND_HELP_PANEL.md) describes Message, Succession, SuccessionFlow, Connection, Binding, PortDefinition/PortUsage/Conjugation, verification, derivation, decomposition, constraints, calculations, quantity/units, nested actions/states and other native semantics. Dedicated approvals for many of these exist elsewhere in the October 17 corpus; **their exact separate definitive paths and parser attestations still require exhaustive linking**. Do not treat the summary index as native grammar proof.

## EA mapping coverage
- [All 26 source connector families, approved review dispositions](../24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md).
- [60 EA element families, exact approved source handling](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md).
- [Central operation registry contract](../24_Workbench/docs/SYSML_V2_PHASE3_CENTRAL_RELATIONSHIP_REGISTRY.md).
- [Machine-readable recovered source families](v2_mapping_family_recovery.v0.1.json).
- [Candidate selector coverage and divergences](v2_executable_candidate_crosswalk.v0.1.json).

## Definition completion requirements
Each native operation's eventual vault definition should include: unique ID, native SysML version/section, plain-language meaning, legal owner/endpoint kinds, direction and multiplicity, typing, native example independently parsed, visual/structural presentation, source translation families, negative comparisons, diagnostic codes, provenance/round-trip, Workbench help text, and state in {approved policy, runtime implemented, parser accepted, UI accepted, released}. Never label it fully implemented merely because a design document exists.

## Known documentation work
- Recover exact authoritative files for Binding, ports/full/proxy/binding distinctions, Requirement derivation/decomposition/verify, Constraint/Calculation/Attribute/Unit, Message/Succession/SuccessionFlow, State/Action nesting, Causation and Analysis/Trade studies.
- Check approved dedicated files for clashes with preliminary generic registries. Specific later approved policy prevails; record code mismatch, not reopening approval.
- Implement one shared machine-readable catalog for Workbench help, EA/BOM selector, validation and navigator; unit-test referential integrity and no duplicative IDs.
- Keep official parser conformance and GUI tests separate from documenting approval.

This index is navigation, not a substitute for original semantic authority.
