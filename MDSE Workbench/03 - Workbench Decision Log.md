# Workbench Decision Log

## Purpose

This log consolidates the decisions that define the MDSE Workbench and dashboard direction.

It intentionally distinguishes:

- **interface/product decisions** that belong to Workbench;
- **supporting architecture decisions** needed to make the interface reliable;
- **model-mechanics questions** that are outside the Workbench scope unless separately governed.

The guiding correction made during the discussion was:

> Workbench is primarily a good interface to the existing model. It should not become a vehicle for redesigning model mechanics.

## Status legend

- **Settled** — use as the current Workbench direction.
- **V1** — implement in the first useful release.
- **Future path** — preserve the design path, but not required for V1.
- **Open** — not yet decided.
- **Out of scope** — belongs to model/schema governance, not Workbench interface design.

---

## A. Product and architecture

### D-001 — Generic Workbench, vault-defined configuration
**Status:** Settled

Workbench is a generic MDSE engine. Vault configuration defines element types, relationship vocabulary, validation, view profiles, and other model-specific behavior.

Ampure-specific semantics should not be hard-coded into the plugin.

### D-002 — One primary everyday plugin
**Status:** Settled

The engineer should experience one main **MDSE Workbench** plugin.

Other responsibilities remain separate:

- Bootstrap for setup/config verification;
- Translator for EA/import/migration;
- Cross-Vault Resolver for cross-vault infrastructure.

Workbench may be internally modular.

### D-003 — Core behavior owned by Workbench
**Status:** Settled

Workbench owns the critical user experience and should not require community plugins for:

- indexing;
- schema-driven validation;
- creation;
- traversal;
- view generation;
- semantic Canvas editing;
- review/model health.

Other plugins may enhance the experience but are not required for correctness.

### D-004 — Dashboard implementation
**Status:** V1

Use a dedicated custom Obsidian Workbench view.

A Markdown landing/help note may be added later but is not the primary interactive dashboard.

### D-005 — Interface, not metamodel
**Status:** Settled

Workbench consumes the existing MDSE schema and rules. Questions such as property inheritance, cardinality policy, and other metamodel mechanics are not Workbench decisions unless separately governed.

---

## B. Dashboard and navigation

### D-006 — Dashboard is the primary V1 entry point
**Status:** V1

Do not crowd note/file context menus with MDSE actions in V1.

Engineers intentionally open Workbench when they want to perform MDSE actions.

### D-007 — Task-oriented dashboard
**Status:** V1

Organize the dashboard around:

- **Create**
- **Explore**
- **Review**

Do not make the user navigate the metamodel taxonomy before knowing what task they want to perform.

### D-008 — Future deeper workspaces
**Status:** Future path

Task areas may later open richer dedicated workspaces while keeping the simple task-oriented home screen.

### D-009 — Personal dashboard presentation
**Status:** Future path

Allow local favorites/hide/reorder of actions.

Personal presentation must not change shared semantics or model state.

### D-010 — Personal settings local by default
**Status:** Settled

Workbench personal settings should be stored locally rather than committed through Git by default.

Design for later export/import/sync.

---

## C. Create experience

### D-011 — Compact modal creation in V1
**Status:** V1

Create actions use compact modal forms.

### D-012 — Path to richer workflows
**Status:** Future path

Complex creation/planning activities may later use full Workbench workflow screens while reusing the same creation service.

### D-013 — Open new note after creation
**Status:** V1

After successful creation, automatically open the new Markdown note.

### D-014 — Rapid-entry mode later
**Status:** Future path

Add a future option to remain in Workbench for repeated creation.

### D-015 — Schema-defined validity
**Status:** Settled

Creation should block only on information required for a valid element according to the current model rules.

Recommended/completeness information may be surfaced without turning every useful creation into a long form.

### D-016 — Context-aware relationship suggestion
**Status:** Future path / supporting behavior

When creation is launched from a model context, Workbench may suggest a likely relationship, but the engineer confirms, changes, or chooses none.

Never silently infer semantic relationships.

### D-017 — Placement assistance
**Status:** Settled

Workbench may show a default location and allow the engineer to choose another folder or create a folder.

Folder placement is organizational, not semantic.

### D-018 — Unique note names
**Status:** Settled supporting constraint

Duplicate model note names are blocked. Workbench may suggest meaningful alternatives.

Naming nomenclature remains advisory rather than a strict Workbench gate unless separately governed.

---

## D. Explore experience

### D-019 — Select element(s) first
**Status:** V1

The primary Explore workflow is:

```text
select element(s) → choose view
```

### D-020 — Simple V1 picker
**Status:** V1

Element picker supports:

- fast unique-name search;
- optional type filter;
- multi-select.

### D-021 — Richer picker later
**Status:** Future path

Possible later additions:

- recent elements;
- favorites;
- richer filters;
- saved searches;
- view-first selection flow.

### D-022 — One-click standard view generation
**Status:** V1

Selecting a standard view immediately generates it using governed defaults.

### D-023 — View Options
**Status:** V1

Provide an adjacent **View Options...** path for engineers who want to override defaults before generation.

### D-024 — Starting set
**Status:** V1

Views may start from one or multiple selected notes.

Future query/filter starting sets are deferred.

### D-025 — Multiple selected elements
**Status:** V1

Show shared/connecting context first. Local context around each selected element remains expandable.

### D-026 — Bounded semantic traversal
**Status:** V1

View Profiles define sensible default traversal depth and allowed semantic paths.

Engineers may request deeper traversal.

### D-027 — All valid bounded paths
**Status:** Settled

Within the chosen bounds, show all valid connecting paths rather than arbitrarily picking one shortest path.

### D-028 — Oversized view handling
**Status:** V1

Render a useful bounded view and explicitly show omitted branches, such as “+N additional”.

Never silently imply that omitted model connections do not exist.

---

## E. View Profiles and generated views

### D-029 — Governed standard profiles + personal variants
**Status:** Settled

Shared standard View Profiles define approved engineering views.

Personal variants may change presentation/traversal choices but not redefine model semantics.

### D-030 — Standard engineering layouts
**Status:** V1

Use deterministic engineering-oriented layouts for standard profiles.

Custom profiles may use a generic fallback layout.

### D-031 — Generated views are disposable
**Status:** V1

Generated quick views are refreshable/disposable working views.

### D-032 — Save as Curated View
**Status:** V1

Allow an engineer to promote a generated view into an intentional curated Canvas that Workbench will not automatically overwrite.

### D-033 — Generated refresh behavior
**Status:** V1

Refresh may rebuild the generated Canvas and discard manual Canvas-only layout/annotations.

If manual work matters, save as a Curated View first.

### D-034 — Staleness detection
**Status:** V1

Generated views should indicate when relevant model changes make the view out of date.

Do not continuously redraw the Canvas.

### D-035 — Deterministic generated view identity
**Status:** V1

Reuse the generated view for the same starting set + View Profile rather than creating repeated numbered duplicates.

### D-036 — Generated view storage
**Status:** V1

Use a vault-configured Generated Views location excluded from Git.

Curated views are saved to a normal engineer-selected vault location.

### D-037 — Curated views are frozen snapshots in V1
**Status:** V1

V1 does not synchronize curated views automatically with model changes.

Preserve metadata needed for future non-destructive update-from-model behavior.

---

## F. Canvas editing

### D-038 — View Mode by default
**Status:** V1

Generated Canvas opens in View Mode.

### D-039 — Explicit Model Edit mode
**Status:** V1

The engineer explicitly enables Model Editing on the same Canvas when they want to change the model.

### D-040 — Edit mode is temporary per Canvas
**Status:** V1

Closing the Canvas or restarting Obsidian returns it to View Mode.

Do not persist edit mode as durable Canvas state.

### D-041 — V1 relationship creation
**Status:** V1

Select two nodes, then choose **Create Relationship**.

For multi-select, support one-to-many or many-to-one operations through the same relationship service.

### D-042 — Future native drag-to-connect
**Status:** Future path

Native Canvas drag gestures may later call the same relationship service.

Do not make the V1 service depend on a particular gesture.

### D-043 — Batch relationship preview
**Status:** V1

For batch operations, preview valid and invalid pairs before commit.

Allow creation of the valid subset only after explicit confirmation.

Do not silently skip invalid pairs.

### D-044 — Avoid automatic many-to-many
**Status:** Settled

Initial batch behavior should not create all-to-all relationships implicitly.

### D-045 — Relationship display direction
**Status:** V1

Display the relationship name that matches the visual reading direction while storing the canonical owner-side relationship required by the model.

### D-046 — Immediate write on confirmation
**Status:** V1

Once the engineer confirms a valid relationship, update authoritative note/YAML content immediately.

### D-047 — Delete semantic edge confirmation
**Status:** V1

Deleting a semantic edge prompts:

- Remove from this view only;
- Remove relationship from model;
- Cancel.

### D-048 — Delete node affects Canvas only
**Status:** V1

Deleting a Canvas node does not delete or retire the underlying model element.

### D-049 — Inherited/contextual edges read-only
**Status:** V1

Contextual/inherited visual edges are not directly editable as though they were explicit stored relationships.

Workbench should trace to the source and may offer actions such as opening the source relationship or adding an explicit relationship.

### D-050 — Undo/Redo
**Status:** V1

Maintain an in-session semantic transaction stack.

A batch edit should be one undoable transaction.

Git remains durable history/audit.

### D-051 — Groups visual by default
**Status:** V1

Canvas groups carry no model semantics by default.

A future bound semantic group may propose schema-defined relationships, never create them silently.

### D-052 — Ordinary property editing
**Status:** V1 / Future path

V1: open the note to edit ordinary properties.

Long term: direct Canvas property editing is a goal.

---

## G. Relationship safety

### D-053 — Strict relationship validation
**Status:** Settled

Relationship picker shows only relationships valid for the selected endpoints according to the current schema.

### D-054 — `newRelationship` escape hatch
**Status:** Settled

A provisional `newRelationship` may be used when the engineer knows two elements are related but no approved relationship is known.

It is not treated as normal semantic reasoning until resolved.

No explanation is mandatory.

### D-055 — `newRelationship` is engineer-usable
**Status:** Settled

Engineers may use `newRelationship` without AI intervention.

Workbench must make unresolved instances easy to review later.

### D-056 — Resolve to existing valid relationship
**Status:** V1

Review of `newRelationship` allows replacement with an existing valid relationship.

If none fits, leave it unresolved. Do not turn the review modal into a schema-authoring tool.

### D-057 — Model endpoints must be model elements
**Status:** Settled supporting constraint

Semantic MDSE relationships connect typed MDSE elements.

If an engineer attempts a semantic relationship to an ordinary note, Workbench may offer explicit **Convert to MDSE Element...** rather than silently converting it.

---

## H. Review experience

### D-058 — Categorized dashboard queues
**Status:** V1

Dashboard shows concise categories/counts rather than a full governance table.

### D-059 — Whole-vault default
**Status:** V1

Review represents the actual whole-vault model state.

Do not default to personnel/task-assignment semantics.

### D-060 — Filters
**Status:** V1

Allow filtering by useful model dimensions such as finding type, element type, folder, product/system context, or relationship type where available.

### D-061 — Dedicated Review screen
**Status:** V1

Clicking a dashboard Review category opens a dedicated Review screen inside Workbench.

### D-062 — Focused finding modal
**Status:** V1

Clicking an individual finding opens a focused modal that explains the finding, presents relevant resolution actions, and allows opening source/target notes.

### D-063 — Sequential Review
**Status:** Open

Question paused before decision:

Should the focused Review experience support Previous/Next navigation and automatic movement to the next unresolved finding?

Recommendation at pause point: yes, without introducing bulk-edit behavior.

---

## I. Model/index reliability

### D-064 — Stable identity handling
**Status:** Settled

Human-authored YAML remains readable; Workbench should resolve model identity robustly using durable IDs/UIDs internally where practical.

### D-065 — Ambiguous links are errors
**Status:** Settled

Do not guess when a model link is ambiguous.

Require resolution.

### D-066 — Relationship fields are lists
**Status:** Existing model constraint consumed by Workbench

Workbench must respect the vault's approved relationship storage form rather than inventing a different storage layer.

### D-067 — Simple relationship edges
**Status:** Settled supporting principle

Do not add arbitrary metadata objects to every edge.

When a connection needs identity, rationale, evidence, lifecycle, or history, represent that using an appropriate first-class model element when the methodology requires it.

### D-068 — Disposable local index
**Status:** Settled

Workbench may maintain a local cache/index for speed.

The cache is rebuildable and not authoritative.

“The index may be cached. The model may not.”

### D-069 — Plugin/schema compatibility
**Status:** Settled

Schema/configuration should declare compatibility/version information.

If Workbench is too old for the vault schema, preserve note readability but disable unsafe semantic edit/view actions with a clear message.

---

## J. Scope corrections and deferred mechanics

### D-070 — Property inheritance discussion paused
**Status:** Out of scope for Workbench

The discussion reached a question about schema-defined property inheritance.

The user explicitly redirected the effort:

> “this is getting into model mechanics and i really only want a good interface to the model”

No Workbench implementation should assume a new property-inheritance policy from that unfinished discussion.

### D-071 — No schema redesign through UI design
**Status:** Settled

When an interface requirement exposes a real schema gap, record it for separate methodology review. Do not silently solve it inside Workbench.

---

## How to use this log

When a future proposal conflicts with a settled decision:

1. identify the conflicting decision number;
2. explain why new information justifies reopening it;
3. record the revised decision and date;
4. update affected build/interface documents;
5. preserve the old decision in history rather than erasing it.
