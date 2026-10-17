# SysML v2 Succession and Succession Flow — approved Option A
Date: 2026-10-17
Status: DECISION APPROVED; implementation pending
Normative: OMG SysML v2.0 Language §§7.13.5, 7.17.4–7.17.5 and flow sections; official transformation specification.
https://www.omg.org/spec/SysML/2.0/Language/PDF
https://www.omg.org/spec/SysML/2.0/Transformation/PDF

## Approved semantics
- Native **SuccessionUsage**: orders occurrence usages in a modeling context. Do not treat it as generic dependency, Flow, or Message.
- Native **conditional succession**: a guard expressed through a native transition usage/decision transition behavior, not merely an optional string annotation on an arbitrary connector.
- Native **SuccessionFlowUsage**: flow with succession semantics for temporal ordering and item transfer. Do not infer it simply from an EA Object Flow unless execution and transfer context are adequately supported.
- Native action decision/merge/fork/join nodes and branch semantics should be preserved, not flattened into paired arrows. Conditional cases may use `if` and `else` constructs in permitted action contexts.
- Exact grammar and metamodel conformance must be validated against the chosen official SysML v2.0 implementation, not assumed from simplified examples.

## EA translator
- Inventory UML Activity ControlFlows, ObjectFlows, source/target pins or nodes, guards, decisions, merges, forks, joins, partitions, exceptions, and ordering metadata.
- Compatible ControlFlow -> Succession or guarded native transition/succession as appropriate; preserve native control nodes and branch semantics.
- ObjectFlow -> Flow per previously approved Flow decision, or SuccessionFlow only if supported by timing/order, payload and endpoint evidence. Preserve payload/classifier and units where known.
- Do not map generic Dependencies to Succession. Resolve lexical/semantic ownership within workflow-local native action/state usages.
- Record source IDs/GUID, endpoint identities and direction, EA diagram context, original guards and tags, transform-rule version, target IDs, classification and exceptions.
- Account for every EA connector even if malformed; do not invent missing events, input/output pins, guards or parallel ordering silently.
- Idempotency, many-to-many source linkage and import-order independence are required.

## BOM translator
- Reuse canonical Part/Item/Attribute definitions and stable object identities referenced by workflow participants.
- A parts hierarchy, BOM line, cable or item quantity never implies behavioral sequencing or a succession flow.
- EA + BOM in either supported order preserves local workflows, action/event references and Canvas presentation metadata.
- Flag identity conflicts without suppressing valid workflow relationships.

## Vault-local workflow model
- One distinct workflow Markdown note with authoritative local native SysML v2 textual action/state/interactions (not a global all-connections graph).
- Explicit owned members and referenced external definitions/usages; preserve identity, scope, and typed feature chains.
- A separate linked custom Canvas view is the default projection; filtered Message/Succession/SuccessionFlow types remain in the model when hidden.
- Preserve provenance and exception overlay separately from SysML-native syntax; derived membership must be reproducible.
- Guards reference vault definitions and typed attributes/enumerations, resolving namespace and validation.
- Keep unmodeled visual ordering distinct from normative succession semantics.

## Workbench
- Draw between action/occurrence nodes in a local workflow. Filter eligible operations according to the native metamodel: Succession, guarded succession/transition, Succession Flow or other valid constructs; no generic edge storage.
- Succession selection resolves owner, source/target feature, temporal direction; preview native usage, syntax, graphical projection.
- Conditional case opens an editor for Boolean guard expression, auto-complete of vault attributes/enumerations, and appropriate decision/merge logic.
- Succession Flow selection resolves source/target transfer features, item type, time constraints and appropriate context.
- Editable in structural, textual, custom Canvas, tabular, and relationship browsers with shared stable identities; support undo, display filters, reverse navigation and explicit EA provenance.
- Never infer native ordering from arbitrary Canvas vertical position. Moving nodes changes layout only.

## Validation
1. Unguarded ordered actions generate parseable valid native succession.
2. EA guarded ControlFlow translates to compatible native guarded behavior with Boolean type-check and exact branch semantics.
3. Decision/merge/fork/join translate without serializing parallel paths.
4. ObjectFlow with explicit ordered item transfer maps to valid Succession Flow; ObjectFlow without timing evidence stays Flow or flagged candidate.
5. Missing source/target feature or Boolean guard typing produces flagged exception, preserving EA original row.
6. Unrelated dependency is never silently treated as succession.
7. Save/open workflow note, switch custom view filters, move nodes; canonical native model remains unchanged.
8. Combined EA/BOM imports preserve shared part and item identities and workflow semantics.
9. Confirm every EA connector disposition, including exceptions, via source-to-target reconciliation ledger.
10. Conformance tests against OMG-compatible SysML v2 parser/metamodel and round-trip including diagram edits.

## Follow-up tracker
- SUC-01 [EA] Extract counts and samples of EA ControlFlows, ObjectFlows, branch/control nodes, guards and event evidence.
- SUC-02 [registry] Formalize distinct mappings for SuccessionUsage, TransitionUsage guarded succession, SuccessionFlowUsage and regular FlowUsage.
- SUC-03 [EA] Implement context-aware transformation, source-to-target ledger and exceptions.
- SUC-04 [vault] Define local workflow ownership, external references and typed Boolean guard lookups.
- SUC-05 [Workbench] Draw-to-succession chooser, guard editor, and preview.
- SUC-06 [Workbench] SuccessionFlow typed endpoint/payload editor and clear disambiguation vs Flow.
- SUC-07 [Workbench] Shared canonical multi-view projection and view-only Canvas positioning.
- SUC-08 [BOM] Preserve cross-import identities and workflow links with non-inference tests.
- SUC-09 [QA] Conditional, parallel, nested, malformed and round-trip reference fixtures.
- SUC-10 [docs] Update central relationship catalog and dependency tracker; cite normative sections.
- SUC-11 [QA] Exact syntax/meta-model compliance gate for emitted v2.0 text.

## Next relationship review
Review **Transition Usage** specifically for state-machine transitions: event triggers, guards, effects, entry/exit and distinction from conditional action succession. Do not equate all state transitions to action-level successions.
