# SysML v2 Dependency — Approved Option A
Date: 2026-10-17
Status: APPROVED translation policy; implementation and normative conformance testing pending.
Authority: OMG SysML 2.0 Language and KerML metamodel. https://www.omg.org/spec/SysML/2.0

## Definition and distinctions
Dependency expresses a client-to-supplier reliance between model elements. It does not alone imply execution order, owned feature, physical connection, payload transfer, satisfaction, realization, or allocation.
- Dependency vs Allocation: reliance versus mapping between architectural elements.
- Dependency vs Succession: reliance versus temporal occurrence ordering.
- Dependency vs Connection/Interface: reliance versus modeled structural connectivity, with Interface requiring port ends.
- Dependency vs Perform/Exhibit: generic relation versus owned action/state usage.
- Dependency vs Requirement Derivation: generic reliance versus requirement-specific derivation semantics.
- Dependency vs Trace/Realization: avoid collapsing specialized provenance/realization relations into generic Dependency.

## EA translator
- Map explicit compatible EA Dependency and Usage-dependency relationships to native Dependency, preserving EA client-to-supplier orientation, source/target GUIDs, stereotypes, tags, notes and model context.
- 'Prerequisite' qualifies only when reliance rather than timing; if it defines ordered occurrences, apply Succession review.
- Preserve specialized EA Realization/Trace relations separately pending precise mappings; no indiscriminate conversion.
- Resolve model element IDs/namespaces and validate typed endpoints. Preserve unresolved source evidence, ledger disposition and repair flag; never silently discard or invent.
- Make import idempotent with rule version, complete connector reconciliation and source-target provenance.

## BOM translator
- Reuse canonical part identities where dependency endpoints refer to imported objects.
- BOM structural membership/quantity/where-used do not imply Dependency; do not infer it from BOM rows.
- Ensure reimport preserves dependency IDs and client/supplier direction; flag identity conflicts.

## Workbench
- Drag between eligible elements; after release offer Dependency when valid alongside other eligible constructs.
- Preview client, supplier, ownership/scope, exact native textual declaration and meaning, with ability to reverse direction before committing.
- Provide 'Info' action and context-local dismissible reference pane with clear compare-to links (Allocation, Succession, Connection etc.). Pane never loses current unsaved editor state.
- Visual, structural, tabular and textual projections use same canonical relation ID and native semantics; support bidirectional navigation, edit/repoint/remove, filters and undo.
- Link to in-vault semantic definition, normative reference, source mapping rule and exceptions.

## Vault definitions
- Keep a versioned relationship definition/operation catalog as files in vault, indexed by native metamodel ID and operation ID.
- Each entry states canonical name, definition, valid source/target and owning context, semantics, non-equivalences, textual/visual forms, examples, translation rules, validation rules and provenance fields.
- Documentation must distinguish 'approved intended mapping' from 'verified exact v2 syntax/semantic rule' and 'implemented'. Do not imply conformance solely because a decision document exists.

## Validation
DEP-01 EA Dependency -> v2 Dependency client-to-supplier preservation.
DEP-02 EA 'Usage' only maps when semantically a general dependency.
DEP-03 ControlFlow never becomes Dependency; incompatible specialization remains flagged.
DEP-04 Workbench reversing client/supplier is an intentional model edit.
DEP-05 View type filtering has no effect on semantic model/serialization.
DEP-06 EA+BOM reimport preserves relationships and source provenance.
DEP-07 Same-named endpoints distinguished by qualified identity.
DEP-08 Native SysML v2 conformance fixture, full mapping ledger and round-trip.

## Follow-up tasks
DEP-F01 inventory and sample EA Dependencies, Usage, Realization and Trace; classify exceptions.
DEP-F02 create normative native Dependency schema and validation rules.
DEP-F03 implement translator mapping and audit ledger.
DEP-F04 integrate Workbench chooser, inspector, preview, direction reversal.
DEP-F05 add vault-backed definition reference integration and compare-to pages.
DEP-F06 BOM identity/merge non-inference tests.
DEP-F07 conformance, round-trip, provenance and ambiguity acceptance fixtures.
DEP-F08 update consolidated relationship catalog/status and glossary.
