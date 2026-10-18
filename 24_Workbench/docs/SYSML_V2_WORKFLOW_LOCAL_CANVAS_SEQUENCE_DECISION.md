# Workflow-local SysML v2 models and Obsidian Canvas sequence views

> **Scope update (ADR-V2-05, October 18):** EA diagrams and their layout/sequence/Canvas translation are **deferred** until all tools and golden-import testing are complete. This document retains its approved semantic and future view-design decisions, but the first-release importer must use only non-diagram source elements/connectors. [Scope lock](../../26_Definitions/STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md).
Decision date: 2026-10-17
Status: USER-APPROVED architectural requirements; sequence renderer/editor implementation pending

## Accepted decisions
1. One discrete Obsidian Markdown note per workflow.
2. The workflow's authoritative behavior model is LOCAL to that workflow note and follows native SysML v2 syntax. External reusable elements are referenced, not cloned. Workflow membership is derived from explicit native ownership/membership and references; merely being pictured does not constitute membership.
3. Every workflow has a distinct visual view (linked .canvas) with DEFAULT=custom, seeded from the local workflow model but able to select a subset of its occurrences, relations and context participants. Models and views are separate artifacts and must remain synchronizable.
4. Canvas sequence-style rendering needs to accomplish sequence communication and ordering goals; it need not exactly reproduce formal SysML graphical notation. Any non-normative visual convention must not be misrepresented as native notation.
5. Workbench independently filters types of elements and relations and scope/membership; hide/show changes view only, not canonical SysML or provenance.

## File layout example
Workflow_Name/
  Workflow_Name.md
  CANVAS_Workflow_Name.canvas
No repeated definitions for shared participant objects; note references stable IDs/qualified SysML names.

## Canvas implementation assessment
- Native Obsidian Canvas JSON 1.0 supports node types text/file/link/group; nodes have coordinates and dimensions, and directed labeled edges link NODE IDs. It does not natively support precise event-relative anchors on continuous UML-style lifelines, native combined-fragment constraints, or SysML v2 semantic validation.
- Sequence renderer strategy: participant header/file nodes; generated repeated event/occurrence nodes at chronological vertical positions; draw message edges between event nodes; lifeline rails and guarded fragment boxes via presentation nodes/groups or Workbench CSS/plugin enhancement. All event, message, succession, and operand identities are stable mappings to canonical SysML constructs, not just edge coordinates.
- Renderer must use original JSON Canvas semantics and preserve unrelated hand-authored layout where possible; external plugin extensions optional. Never depend solely on unknown/custom JSON fields surviving every Canvas editor.
- Workbench interprets intentful canvas edge gestures; choose native Message/Succession/Flow etc. from eligible choices and compile to proper local SysML constructs after validation. Raw Canvas edges do NOT automatically become SysML relationships.
- Support branching, concurrent paths, loops and guards as modeled, not inferred from vertical placement. If semantics unavailable, render visual only with a diagnostic.
- Preserve manually included participants as context-only references, visually distinguished from owned workflow actions/events.
- Sequence and activity-style views can be alternative projections of same local workflow, each with independent saved custom visibility settings.

## EA translator
- Map relevant EA Activity/Sequence/Interaction structure into workflow-local SysML when semantic ownership is evidenced.
- Preserve EA diagram source and layout to seed an initial custom view, not as authoritative semantics.
- Retain EA element/connector GUIDs, diagram IDs, messages, guards, and event ordering with explicit exception flags for uncertain mappings and complete reconciliation.
- Avoid inventing workflow membership solely because objects are on the same EA diagram.

## BOM translator
- Resolve participant part identity via canonical vault object/part registry.
- Do not infer local workflows, ordering, or messages from BOM hierarchy, cable existence, or quantity.
- Preserve workflow links and saved Canvas views through BOM reimport.

## Workbench and vault
- Index workflow ID, local owning action/state/context, nested usages, message usages, event occurrences and successions.
- Provide Open Workflow, sequence/activity-style layout selector, custom scope filters, native relationship creation by drawing, preview and apply, edit/repoint/delete, undo/redo, and provenance/flags.
- Linked Canvas owns presentation layout, pinned context and visibility settings only. Markdown model owns SysML semantics. Stable canonical IDs connect them.
- Define recovery path if note and Canvas drift: compare metadata, regenerate projection with explicit preservation of customized positions and manual context pins, never silently override semantic model.

## Acceptance tests
- Two workflows share same part participants but have distinct message usages: opening one shows only local membership by default.
- Hide all Messages: serialized SysML and Git diff for semantic model remain unchanged.
- Drag event A -> event B, select Message: generated native usage has valid event ends and ownership; canvas updated and reopened.
- Model branches, loops and parallel occurrences remain semantically valid across layout changes.
- Move participant/layout nodes: no semantic change.
- Reimport EA and BOM: deterministic workflow identity and no unexpected rewritten views.
- Missing event identity preserved as provenance-backed exception, not an invented valid native message.
- Run on supported Obsidian version and plugin baseline before relying on custom lifeline styles.

## Follow-up items
WF-C01: Author native workflow note schema and identity/ownership rules.
WF-C02: Define .canvas projection format with stable links to canonical identities and separate view-only metadata.
WF-C03: Prototype generated sequence Canvas from local actions/events/messages.
WF-C04: Decide lifeline and fragment rendering strategy with current Advanced Canvas baseline.
WF-C05: Workbench gesture to semantic operation conversion and validation.
WF-C06: Model-local membership resolver and independent type/view filters.
WF-C07: EA Activity/Sequence diagram importer mapping and source layout preservation.
WF-C08: BOM participant cross-link stability and no invented flows.
WF-C09: Round-trip and hand-edited Canvas conflict detection.
WF-C10: User acceptance testing of multiple workflows with shared participants.
