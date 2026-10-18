# Workflow-Scoped Visual Views — Workbench requirements
Date: 2026-10-17
Status: proposed implementation contract based on approved independent type filters; workflow scope recommended for detailed implementation review.

## Objective
Enable engineers to focus on a specific behavioral workflow or interaction instead of every relationship associated with a component, especially for Message, Succession, and Succession Flow.

## Three orthogonal selectors
1. Semantic scope: choose an authoritative native SysML v2 ActionDefinition/Usage, StateDefinition/Usage or supported interaction context with nested usages. Filter to model membership and references actually involved in that scope; avoid inferred membership from mere graph proximity.
2. Element/relationship visibility: independently toggle native metamodel categories and individual types. Preserve every hidden model record.
3. View presentation: layout, expanded depth, contextual references, annotations, and selected subsets. Save as vault-native presentation configuration with stable model references.

## User workflow
- Select context from navigation tree or search; Open Workflow.
- Automatically derive contained subactions, relevant event occurrences, control nodes, Messages, guarded Successions, and Succession Flows according to native ownership and reference semantics.
- Filter by nested depth, source/target actor/part, time slice, participants, active path or branch conditions where model evidence supports these.
- Show collapsed participants as swimlanes or lifelines as an optional layout; do not imply sequence solely from node positions.
- Distinguish (a) canonical members of workflow, (b) related model elements referenced as context, and (c) manually pinned view-only elements.
- Draw from one occurrence to another and choose eligible operations; preview ownership, context, event ends, conditions/guards, syntax, and model change.
- Preserve alternate paths and branches; no assumption that there is exactly one execution trace. A state machine view and action workflow view may legitimately have different sequencing semantics.
- Show a counter/indicator when relationships are hidden by scope or type; allow inspect/reveal without redefining scope.
- Support navigation to underlying native element, definition, owning action, and origin EA record.
- Save named workflow views in vault with versioned configuration, stable IDs, zoom/layout, scope ID, visibility rules and context-only pins. Keep that presentation artifact separate from SysML semantic definitions.

## Required consistency
- No synthetic ordering based solely on EA sequence diagram line placement or proximity; preserve explicit ordering/occurrence information and flag uncertain import.
- Do not treat an EA diagram as the authoritative semantic owner. Use source diagrams to seed proposed views and only create native memberships where evidence supports them.
- Hiding or isolating a workflow does not delete relationships or change exported native SysML model.
- Workbench visual, tabular and textual editors share canonical model identity and provenance.
- Message, Succession and Succession Flow stay distinct. Contained action successions may have guards and control nodes; do not collapse into arbitrary arrows.
- BOM import never infers workflows or messages from a parts hierarchy.

## EA translator
- Extract diagram IDs, diagram objects, sequence messages, connectors, activity partitions, nesting, event/fragment occurrence identifiers and documented order/guards.
- Reconcile source-defined workflows versus diagram-only visual groupings, with explicit evidence/exception flags.
- Preserve source diagram layout as a seed view where useful but not as normative behavior.
- Maintain all source element/connector dispositions and referential links to canonical model.

## BOM translator
- Reuse shared part identity to populate workflow participant references where explicitly modeled.
- Never invent message/succession/control dependencies from assembly/BOM rows.
- Preserve saved workflow views across BOM updates and flag unresolved participant links.

## Workbench
- Global relationship-type filters plus workflow-local scope filters and per-view saved settings.
- Workflow perspective with optional activity-flow, sequence/swimlane and hierarchy layouts based on same model.
- Selection chooser offers context-valid semantic operations, not a generic editable edge.
- Preview, safe edit, undo, hidden relationship warning, reverse navigation and portable view configs.

## Follow-up and acceptance
WF-01 Registry: define semantic scope queries against SysML v2 action/state/message/occurrence hierarchy.
WF-02 Workbench: scope picker and workflow explorer, recursive traversal with cycle protection.
WF-03 Workbench: type toggles + workflow scope + layout isolation; independent persistence.
WF-04 Vault: versioned saved view schema with canonical stable references and context-only pins.
WF-05 EA: extract diagram source metadata and distinguish semantics vs diagram-derived membership.
WF-06 BOM: identity/link merge and workflow view preservation.
WF-07 QA: fixture with shared component and two workflows sharing one Message type but distinct usages; verify isolation.
WF-08 QA: conditional guarded branches, nested actions, parallel paths and missing events.
WF-09 QA: toggle/hide/switch saved view without changing semantic model, serialized text or Git diff.
WF-10 Documentation: link workflow view contracts from Message/Flow/Succession reviews.

Open follow-up: select whether named workflow is generally rooted in Action Usage, State Usage, or user-defined workflow concept. Recommendation: native action/state where semantically applicable, view-only grouping elsewhere.
