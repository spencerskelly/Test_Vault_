# SysML v2 Message and Visual Visibility Filters

> **Scope update (ADR-V2-05, October 18):** EA diagrams and their layout/sequence/Canvas translation are **deferred** until all tools and golden-import testing are complete. This document retains its approved semantic and future view-design decisions, but the first-release importer must use only non-diagram source elements/connectors. [Scope lock](../../26_Definitions/STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md).
Date: 2026-10-17
Status: Message option A approved; view-filter behavior approved as requirements, implementation pending.

## Message decision
- Support native SysML v2 Message usages, distinct from generic transfer flows, connections, and successions.
- Translate compatible EA sequence-diagram messages and signal interactions when source event semantics and endpoint identities support native construction.
- Preserve the original EA connector/diagram ID, send/receive event information, ordering, guards and payload definitions when present; flag unsupported or incomplete details.
- Do not reinterpret Information Flow, physical Connection, or Control Flow as a Message without source evidence.
- Maintain source-to-target reconciliation for all imported records.

## Translator impacts
### EA
- Inventory sequence messages, signal interaction records, send/accept events, endpoints, payload classifiers and ordered interaction context.
- Determine native Message semantics and feature ends; create reusable signal/item definitions only when evidence supports them.
- Map valid cases deterministically, flag missing send/receive event identity, unresolved contexts, or incompatible payloads.
- Preserve EA raw evidence and mapping version; never silently invent events or ordering.
### BOM
- Never infer messages from cables, BOM lines or device connectivity.
- Reuse shared canonical part/item identity and avoid overwriting modeled messages when merging BOM data.

## Workbench Message creation
- Draw between eligible endpoints and present Message as a filtered choice when meaningful.
- Select sending and receiving events/roles and optional typed payload using vault-backed alphabetical dropdowns; show native structure/notation preview and warnings.
- Support edit, replace payload, inspect semantics, navigation, reverse lookup, undo/redo, provenance, and round-trip across textual and visual representations.
- Validation: scope, event occurrence identities, compatible payload, ownership and ordering where modeled.

## Visual filters — mandatory
- Every graph/diagram visual view provides independent show/hide selections for model element kinds and relationship kinds.
- Filter by native SysML v2 metamodel kind/subtype, not solely presentation aliases.
- Separate toggles for Message, Flow, Connection, Perform, Exhibit, Allocation, Binding, Succession etc., and for Part, Action, State, Port, Requirement, Attribute, Item etc. Hierarchical group controls may be offered but independent leaves remain selectable.
- Filtering affects presentation only; never mutate canonical model or source provenance.
- Filtering an element hides it visually; incident connectors are hidden in that view, but remain in model and queries. Preserve visibility of orphaned relationship evidence when relevant in tabular explorer.
- Explicit indicator when a visible element has relationships suppressed by a filter; toggle to reveal without changing model.
- Filter settings may be saved per view and in named vault-backed view definitions; presets: Structural, Behavioral, Communication, Requirements, Custom. Users can reset defaults or temporarily reveal all.
- Avoid leaking view state into semantic source code or altering export. A persisted view definition is presentation metadata, not a SysML relationship.
- Views derived from the same canonical model; filters apply to diagram, relationship browser and relevant overlay/table view where appropriate, without conflating model filtering with search/query filters.
- Editing while filters are active must surface a conflict/hidden-link warning before destructive operations; added relationships should offer an option to show the relevant category.
- Support keyboard operation, search, counts, large-vault performance, stable saved filters after type renames, and per-view versioning.

## Verification
MSG-01 Parse/validate native Message with sender/receiver and payload.
MSG-02 EA Sequence Message and Signal import preserves order/evidence.
MSG-03 Missing events produce flagged mapping and no fictitious valid message.
MSG-04 EA/BOM merge does not infer or remove messages.
VIEW-01 Toggle Message off and confirm model, SysML serialization, queries, Git diff remain unchanged.
VIEW-02 Hide element type and verify incident connectors invisible without deletion.
VIEW-03 Independently toggle Flow, Connection, Message with shared endpoints.
VIEW-04 Reload saved named view in a fresh session; stable filtering.
VIEW-05 Expose hidden relationships before destructive edits.
VIEW-06 Edit via visual/table/text views, preserve stable IDs and common canonical model.

## Follow-up work
- MSG-F01 [EA translator] inventory source sequence/signal patterns and exceptions.
- MSG-F02 [registry] exact native Message semantics, event ends and payload typing.
- MSG-F03 [Workbench] Message operation/editor/preview.
- MSG-F04 [vault] reusable event and payload definitions and indexes.
- MSG-F05 [QA] conformance and provenance tests.
- VIEW-F01 [Workbench] shared typed visibility filter engine for all diagram kinds.
- VIEW-F02 [Workbench] independent element/relationship type selector with search.
- VIEW-F03 [vault] saved presets and per-view display metadata.
- VIEW-F04 [Workbench] hidden dependency badges and safe editing behavior.
- VIEW-F05 [QA] view-only visibility, persistence, performance and round-trip tests.

## Next semantics review
Succession and Succession Flow: order/control dependencies are distinct from Message communication and item transfer.
