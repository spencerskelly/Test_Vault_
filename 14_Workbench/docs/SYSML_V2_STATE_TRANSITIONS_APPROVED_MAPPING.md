# SysML v2 State Transitions — Approved Mapping
Date: 2026-10-17
Status: Approved translation policy; implementation and conformance testing pending
Normative authority: OMG SysML v2.0 Language and KerML; validate against official textual syntax and metamodel.

## Decision
Adopt native SysML v2 TransitionUsage for EA state-machine Transitions, including explicit source state, target state, trigger/accepter, guard, and effect semantics when modeled. Preserve entry/do/exit behaviors with appropriate native state semantics. Do not collapse transitions into generic Succession, Message, Flow or an untyped directed edge. Reusable state definitions and locally owned usages remain distinct. Designs modeled as states and allocated to objects translate through the separately approved ExhibitStateUsage rule.

## EA translator
- Inventory EA StateMachine/State, Transition connectors, event triggers, guard expressions, effects, entry/do/exit actions, composite substates and owners.
- Determine owning state-machine/state context and source/target state usages; resolve transition scopes and aliases.
- Translate explicit triggers, guards and effects using native constructs only when semantically and type-compatible. Do not manufacture missing event identities or Boolean semantics.
- Preserve transition EA GUID, source/target GUID and original direction, event specification, guard, effect, tags, notes, source diagram identifier, mapping rule version.
- Flag ambiguity or illegal native placement; account for every imported EA relationship in source coverage ledger. Preserve copies of source data when interpretation is uncertain.
- Ensure nested states remain nested state usages, not false relationships to top-level unrelated states.

## BOM translator
- Reuse canonical identities for parts exhibiting states; retain stable references across EA/BOM import.
- Do not derive state transitions or behavior order from BOM structure, cable connectivity or quantity.
- Preserve state behavior/provenance and custom views when BOM updates part records; flag identity collisions.

## Workbench
- Inside workflow-local note or state-machine context, draw between state usages; eligible operation chooser offers Transition only when context permits.
- Provide trigger/event, Boolean guard and effect editors with autocomplete from vault-native type, attribute and enumeration registries; preview exact native v2 structure, direction, owner, and generated text.
- Support entry/do/exit, hierarchical substates, reverse navigation, editing/repointing, versioned stable references and undo.
- Custom workflow/state Canvas is a separate presentation file; filtering hides transitions without changing model.
- Distinguish native state-machine transitions from guarded action successions and message exchanges.

## Vault
- State/transition model is local to a workflow/state-machine note where appropriate; external definitions referenced without duplicating their identity.
- Keep readable textual SysML v2 alongside stable element IDs and dedicated provenance/exception metadata.
- Canvas views default custom, with relationship/element visibility choices stored as view-only data.

## Validation tests
1. Simple Standby -> Charging transition; parse and semantic validation.
2. Triggered guarded transition with a native effect action.
3. Transition absent trigger/guard/effect where valid; no false mandatory inference.
4. Nested state and transitions scoped to the proper composite state.
5. Several part usages exhibiting the same reusable state definition without cloning it.
6. EA transition with malformed or unresolved endpoints/guards is flagged with source evidence.
7. Edit transition in Canvas and textual view and confirm one canonical native model.
8. EA+BOM reimport preserves identities, local ownership, and views.
9. Source-to-target EA transition reconciliation counts complete.

## Follow-up tasks
- TRN-01 EA inventory of state machine transitions and source fields.
- TRN-02 Semantic registry mapping of EA State/Transition/Trigger/Guard/Effect to exact native v2 constructs.
- TRN-03 Importer implementation with deterministic state ownership and original evidence retention.
- TRN-04 Vault-local state/transition note model and reusable definition registry.
- TRN-05 Workbench draw-to-transition chooser, editors and validation.
- TRN-06 Graphical/structural/textual/tabular synchronized projections.
- TRN-07 BOM identity integration and non-inference regression.
- TRN-08 State hierarchy, guard typing, event and effect conformance fixtures.
- TRN-09 Round-trip, malformed source, and complete mapping-ledger tests.
- TRN-10 Update central catalog of approved mappings and next-review backlog.

## Next review candidate
SysML v2 InterfaceDefinition / InterfaceUsage and interface ends (including port roles and conjugation), distinct from Connection and Flow. Review EA Provided/Required Interfaces and realization/dependency relationships with care.
