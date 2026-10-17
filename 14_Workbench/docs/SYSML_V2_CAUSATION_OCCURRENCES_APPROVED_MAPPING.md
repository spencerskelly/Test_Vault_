# Approved: SysML v2 Occurrences and Standard-Library Causation
Date: 2026-10-17
Status: Option A APPROVED for native MDSE v2 capability. Implementation / full conformance pending.
Normative baseline: OMG SysML v2.0 Language and KerML; see https://www.omg.org/spec/SysML/2.0/Language/PDF, Occurrences §7.9.2–7.9.3; Cause-and-Effect Domain Library (standard machine-readable library).

## Exact classification, not a generic "causes" connector
- OccurrenceDefinition / OccurrenceUsage: native SysML v2 occurrences, with featuring context and duration; actions and states are related specialized occurrence concepts.
- EventOccurrenceUsage: native event-occurrence modeling where events are actually modeled; do not mistake raw log rows for semantic events.
- Time slice: native occurrence usage with time-slice portion kind; represents a portion of an occurrence over a temporal interval and must be scoped to a featuring occurrence.
- Snapshot: native occurrence usage with snapshot portion kind; represents an instantaneous portion of an occurrence and must be scoped accordingly.
- Causation: expressed using the official SysML v2 Cause-and-Effect Domain Library's supported constructs, not a newly invented built-in generic connector. Pin exact library metaclasses, definitions, declarations and grammar to the project library version before implementing editors.

## Distinctions
- Succession describes temporal ordering; A precedes B does not assert A causes B.
- Cause-and-effect modeling asserts a causal explanation/relationship with domain-library semantics; A causes B is a stronger engineering statement.
- Dependency means reliance (client/supplier), not causation, ordering, containment or transport.
- Message describes communicative event semantics; Flow describes transfer. Neither automatically implies causation.
- State Transition captures source/target state, trigger, guard and effect semantics; its existence does not automatically assert an independent causal relation.
- Time slices and snapshots refer to portions of modeled occurrences, not arbitrary diagram annotations or the same thing as enum operating states.

## EA translator
- Inventory explicitly compatible UML occurrences/events, signals, transitions, state-machine event specifications, activity behavior and temporal tagged evidence.
- Map compatible explicitly modeled elements only when semantic scope, identity and direction are available; preserve raw EA GUIDs, tags, notes, diagram and owner evidence.
- Do not infer causes from ControlFlow, Transition, Dependency, InformationFlow, temporal proximity, diagram layout, issue occurrence, or event log correlation.
- No automatic time slice, snapshot or causation mappings from unlabeled temporal values; flag unresolved source semantics.
- Every source element/connector has exact mapping ledger disposition, including exceptions and source copies.

## BOM translator
- Reuse canonical part and item identities referenced by occurrences.
- BOM quantity, revision, serials, product alternatives or part hierarchy do not imply events, duration, temporal relations or causation.
- Preserve authored native occurrence and causal models across imports and flag source identity conflicts.

## Vault model and Workbench
- Store reusable occurrence definitions and context-local usages, time-slice/snapshot declarations and validated library causation constructs as native SysML text and indexed model IDs.
- Workflows remain one note each with native local model and separate custom Canvas. Other occurrence-based notes may use the appropriate owner and related views.
- Drag-to-relate menu offers causal relationships ONLY if eligible under standard library's defined constructs; never auto-select from temporal layout. Temporal occurrence editors use type-correct operations (not force a binary edge).
- Enable separate filters for Event, Occurrence, Time Slice, Snapshot, Causation, Succession, Transition, Message, Flow.
- The dismissible in-editor Definitions panel shows canonical name, standard vs library status, scope and ownership, comparable semantics, eligible end roles, native syntax, constraints, concrete engineering examples and provenance.
- Context-specific timeline, activity/state, fault investigation and causal network layouts may be offered as projections; visuals do not manufacture native semantics.

## Validation
1. Parse/semantic test native occurrence definitions and usages with featuring context and stable IDs.
2. Time-slice and snapshot must refer to valid featuring occurrence and obey portion constraints.
3. Event occurrence typing/scope and source provenance remain correct.
4. Cause-and-effect constructs use exact pinned standard domain library types and validate causal-end typing.
5. A followed by B via succession MUST NOT create a causal claim.
6. Events in logs or BOM evidence MUST NOT manufacture native causation or snapshots.
7. EA source reconciliation exact and exception flags preserve contradictory/incomplete data.
8. EA/BOM import order preserves canonical participant identities and authored causal assertions.
9. Workbench view filtering changes visualization, not canonical text/semantic graph; round trip edits validated.
10. Scenario with overtemperature event and protection actuation includes explicit claimed causal link only when modeled/approved.

## Follow-up tracker
OCC-01 Pin exact OMG v2.0 + Cause-and-Effect Domain Library version and names (normative conformance).
OCC-02 Extract EA occurrence/event patterns and count candidates and exceptions.
OCC-03 Implement explicit EA import with stable identities, provenance and exception ledger.
OCC-04 Add canonical occurrence definition/usage, event, slice/snapshot and causal-library indexing in vault.
OCC-05 Add Workbench semantic eligibility, native editors, occurrence viewer, definitions drawer and filters.
OCC-06 Extend workflow-local sequence and time context projections without using Canvas location as semantics.
OCC-07 BOM non-inference and identity-preservation regressions.
OCC-08 Conformance fixtures for causation versus succession, events versus messages and snapshots versus states.
OCC-09 Native text/graph/tabular view round-trip and cross-import stability.
OCC-10 Central decision matrix and all relation metadata updates.

## Next Group 3 review (NOT approved)
Analysis cases, objective and subject structure, evaluation, trade studies, and analysis results. Keep previously approved calculation, constraint, requirement, quantity and unit types unchanged. A trade study is supported by the standard Analysis Domain Library; model its evaluation criteria and alternatives distinctly from product Variation/Variant choices, satisfaction assertions, and test results.
