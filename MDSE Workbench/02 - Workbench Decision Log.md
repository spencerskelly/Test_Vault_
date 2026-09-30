# Workbench Decision Log

> IDs use the `WB-` prefix (renamed 2026-09-30 from `D-`, same numbers) so they cannot be confused with the Workspace Decision Log (`W-`) or the EA migration Decision Register. Former open items `O-001`…`O-009` are now `WB-063` and `WB-072`…`WB-079` (mapping at the end). This note replaces the separate Open Decisions, Continuation Handoff and Change Log notes.

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
- **Proposed** — a recommendation written for approval. It is **not** direction until Spencer approves it; if approved, change the status and date in place and record any decision it supersedes.
- **Out of scope** — belongs to model/schema governance, not Workbench interface design.

---

## A. Product and architecture

### WB-001 — Generic Workbench, vault-defined configuration
**Status:** Settled

Workbench is a generic MDSE engine. Vault configuration defines element types, relationship vocabulary, validation, view profiles, and other model-specific behavior.

Ampure-specific semantics should not be hard-coded into the plugin.

### WB-002 — One primary everyday plugin
**Status:** Settled

The engineer should experience one main **MDSE Workbench** plugin.

Other responsibilities remain separate:

- Bootstrap for setup/config verification;
- Translator for EA/import/migration;
- Cross-Vault Resolver for cross-vault infrastructure.

Workbench may be internally modular.

### WB-003 — Core behavior owned by Workbench
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

### WB-004 — Dashboard implementation
**Status:** V1

Use a dedicated custom Obsidian Workbench view.

A Markdown landing/help note may be added later but is not the primary interactive dashboard.

### WB-005 — Interface, not metamodel
**Status:** Settled

Workbench consumes the existing MDSE schema and rules. Questions such as property inheritance, cardinality policy, and other metamodel mechanics are not Workbench decisions unless separately governed.

---

## B. Dashboard and navigation

### WB-006 — Dashboard is the primary V1 entry point
**Status:** V1

Do not crowd note/file context menus with MDSE actions in V1.

Engineers intentionally open Workbench when they want to perform MDSE actions.

### WB-007 — Task-oriented dashboard
**Status:** V1

Organize the dashboard around:

- **Create**
- **Explore**
- **Review**

Do not make the user navigate the metamodel taxonomy before knowing what task they want to perform.

### WB-008 — Future deeper workspaces
**Status:** Future path

Task areas may later open richer dedicated workspaces while keeping the simple task-oriented home screen.

### WB-009 — Personal dashboard presentation
**Status:** Future path

Allow local favorites/hide/reorder of actions.

Personal presentation must not change shared semantics or model state.

### WB-010 — Personal settings local by default
**Status:** Settled

Workbench personal settings should be stored locally rather than committed through Git by default.

Design for later export/import/sync.

---

## C. Create experience

### WB-011 — Compact modal creation in V1
**Status:** V1

Create actions use compact modal forms.

### WB-012 — Path to richer workflows
**Status:** Future path

Complex creation/planning activities may later use full Workbench workflow screens while reusing the same creation service.

### WB-013 — Open new note after creation
**Status:** V1

After successful creation, automatically open the new Markdown note.

### WB-014 — Rapid-entry mode later
**Status:** Future path

Add a future option to remain in Workbench for repeated creation.

### WB-015 — Schema-defined validity
**Status:** Settled

Creation should block only on information required for a valid element according to the current model rules.

Recommended/completeness information may be surfaced without turning every useful creation into a long form.

### WB-016 — Context-aware relationship suggestion
**Status:** Future path / supporting behavior

When creation is launched from a model context, Workbench may suggest a likely relationship, but the engineer confirms, changes, or chooses none.

Never silently infer semantic relationships.

### WB-017 — Placement assistance
**Status:** Settled

Workbench may show a default location and allow the engineer to choose another folder or create a folder.

Folder placement is organizational, not semantic.

### WB-018 — Unique note names
**Status:** Settled supporting constraint

Duplicate model note names are blocked. Workbench may suggest meaningful alternatives.

Naming nomenclature remains advisory rather than a strict Workbench gate unless separately governed.

---

## D. Explore experience

### WB-019 — Select element(s) first
**Status:** V1

The primary Explore workflow is:

```text
select element(s) → choose view
```

### WB-020 — Simple V1 picker
**Status:** V1

Element picker supports:

- fast unique-name search;
- optional type filter;
- multi-select.

### WB-021 — Richer picker later
**Status:** Future path

Possible later additions:

- recent elements;
- favorites;
- richer filters;
- saved searches;
- view-first selection flow.

### WB-022 — One-click standard view generation
**Status:** V1

Selecting a standard view immediately generates it using governed defaults.

### WB-023 — View Options
**Status:** V1

Provide an adjacent **View Options...** path for engineers who want to override defaults before generation.

### WB-024 — Starting set
**Status:** V1

Views may start from one or multiple selected notes.

Future query/filter starting sets are deferred.

### WB-025 — Multiple selected elements
**Status:** V1

Show shared/connecting context first. Local context around each selected element remains expandable.

### WB-026 — Bounded semantic traversal
**Status:** V1

View Profiles define sensible default traversal depth and allowed semantic paths.

Engineers may request deeper traversal.

### WB-027 — All valid bounded paths
**Status:** Settled

Within the chosen bounds, show all valid connecting paths rather than arbitrarily picking one shortest path.

*Amendment proposed 2026-09-30: [[#WB-082 — Node cap outranks depth]] (bounds include a node cap that wins over depth).*

### WB-028 — Oversized view handling
**Status:** V1

Render a useful bounded view and explicitly show omitted branches, such as “+N additional”.

Never silently imply that omitted model connections do not exist.

---

## E. View Profiles and generated views

### WB-029 — Governed standard profiles + personal variants
**Status:** Settled

Shared standard View Profiles define approved engineering views.

Personal variants may change presentation/traversal choices but not redefine model semantics.

### WB-030 — Standard engineering layouts
**Status:** V1

Use deterministic engineering-oriented layouts for standard profiles.

Custom profiles may use a generic fallback layout.

### WB-031 — Generated views are disposable
**Status:** V1

Generated quick views are refreshable/disposable working views.

### WB-032 — Save as Curated View
**Status:** V1

Allow an engineer to promote a generated view into an intentional curated Canvas that Workbench will not automatically overwrite.

### WB-033 — Generated refresh behavior
**Status:** V1

Refresh may rebuild the generated Canvas and discard manual Canvas-only layout/annotations.

If manual work matters, save as a Curated View first.

### WB-034 — Staleness detection
**Status:** V1

Generated views should indicate when relevant model changes make the view out of date.

Do not continuously redraw the Canvas.

### WB-035 — Deterministic generated view identity
**Status:** V1

Reuse the generated view for the same starting set + View Profile rather than creating repeated numbered duplicates.

### WB-036 — Generated view storage
**Status:** V1

Use a vault-configured Generated Views location excluded from Git.

Curated views are saved to a normal engineer-selected vault location.

### WB-037 — Curated views are frozen snapshots in V1
**Status:** V1

V1 does not synchronize curated views automatically with model changes.

Preserve metadata needed for future non-destructive update-from-model behavior.

---

## F. Canvas editing

### WB-038 — View Mode by default
**Status:** V1

Generated Canvas opens in View Mode.

### WB-039 — Explicit Model Edit mode
**Status:** V1

The engineer explicitly enables Model Editing on the same Canvas when they want to change the model.

### WB-040 — Edit mode is temporary per Canvas
**Status:** V1

Closing the Canvas or restarting Obsidian returns it to View Mode.

Do not persist edit mode as durable Canvas state.

### WB-041 — V1 relationship creation
**Status:** V1

Select two nodes, then choose **Create Relationship**.

For multi-select, support one-to-many or many-to-one operations through the same relationship service.

### WB-042 — Future native drag-to-connect
**Status:** Future path

Native Canvas drag gestures may later call the same relationship service.

Do not make the V1 service depend on a particular gesture.

### WB-043 — Batch relationship preview
**Status:** V1

For batch operations, preview valid and invalid pairs before commit.

Allow creation of the valid subset only after explicit confirmation.

Do not silently skip invalid pairs.

### WB-044 — Avoid automatic many-to-many
**Status:** Settled

Initial batch behavior should not create all-to-all relationships implicitly.

### WB-045 — Relationship display direction
**Status:** V1

Display the relationship name that matches the visual reading direction while storing the canonical owner-side relationship required by the model.

### WB-046 — Immediate write on confirmation
**Status:** V1

Once the engineer confirms a valid relationship, update authoritative note/YAML content immediately.

### WB-047 — Delete semantic edge confirmation
**Status:** V1

Deleting a semantic edge prompts:

- Remove from this view only;
- Remove relationship from model;
- Cancel.

### WB-048 — Delete node affects Canvas only
**Status:** V1

Deleting a Canvas node does not delete or retire the underlying model element.

### WB-049 — Inherited/contextual edges read-only
**Status:** V1

Contextual/inherited visual edges are not directly editable as though they were explicit stored relationships.

Workbench should trace to the source and may offer actions such as opening the source relationship or adding an explicit relationship.

### WB-050 — Undo/Redo
**Status:** V1

Maintain an in-session semantic transaction stack.

A batch edit should be one undoable transaction.

Git remains durable history/audit.

### WB-051 — Groups visual by default
**Status:** V1

Canvas groups carry no model semantics by default.

A future bound semantic group may propose schema-defined relationships, never create them silently.

### WB-052 — Ordinary property editing
**Status:** V1 / Future path

V1: open the note to edit ordinary properties.

Long term: direct Canvas property editing is a goal.

---

## G. Relationship safety

### WB-053 — Strict relationship validation
**Status:** Settled

Relationship picker shows only relationships valid for the selected endpoints according to the current schema.

### WB-054 — `newRelationship` escape hatch
**Status:** Settled

A provisional `newRelationship` may be used when the engineer knows two elements are related but no approved relationship is known.

It is not treated as normal semantic reasoning until resolved.

No explanation is mandatory.

### WB-055 — `newRelationship` is engineer-usable
**Status:** Settled

Engineers may use `newRelationship` without AI intervention.

Workbench must make unresolved instances easy to review later.

### WB-056 — Resolve to existing valid relationship
**Status:** V1

Review of `newRelationship` allows replacement with an existing valid relationship.

If none fits, leave it unresolved. Do not turn the review modal into a schema-authoring tool.

### WB-057 — Model endpoints must be model elements
**Status:** Settled supporting constraint

Semantic MDSE relationships connect typed MDSE elements.

If an engineer attempts a semantic relationship to an ordinary note, Workbench may offer explicit **Convert to MDSE Element...** rather than silently converting it.

---

## H. Review experience

### WB-058 — Categorized dashboard queues
**Status:** V1

Dashboard shows concise categories/counts rather than a full governance table.

### WB-059 — Whole-vault default
**Status:** V1

Review represents the actual whole-vault model state.

Do not default to personnel/task-assignment semantics.

### WB-060 — Filters
**Status:** V1

Allow filtering by useful model dimensions such as finding type, element type, folder, product/system context, or relationship type where available.

### WB-061 — Dedicated Review screen
**Status:** V1

Clicking a dashboard Review category opens a dedicated Review screen inside Workbench.

### WB-062 — Focused finding modal
**Status:** V1

Clicking an individual finding opens a focused modal that explains the finding, presents relevant resolution actions, and allows opening source/target notes.

### WB-063 — Sequential Review
**Status:** Open (recommendation: B)

When a user opens a Review finding, should Workbench support moving through the current filtered queue?

- **A — Manual selection:** resolve/close, return to the list, choose another.
- **B — Previous / Next:** show `← Previous   4 of 17   Next →`; after a successful resolution, optionally advance to the next unresolved finding.
- **C — Batch resolution:** multi-select and bulk semantic correction.

Recommendation: **B**, without broad batch editing in V1. It improves cleanup sessions and needs no new model concept. The roadmap previously listed it as V1.x; if approved, it is V1 (small cost, high cleanup value).

---

## I. Model/index reliability

### WB-064 — Stable identity handling
**Status:** Settled

Human-authored YAML remains readable; Workbench should resolve model identity robustly using durable IDs/UIDs internally where practical.

### WB-065 — Ambiguous links are errors
**Status:** Settled

Do not guess when a model link is ambiguous.

Require resolution.

### WB-066 — Relationship fields are lists
**Status:** Existing model constraint consumed by Workbench

Workbench must respect the vault's approved relationship storage form rather than inventing a different storage layer.

### WB-067 — Simple relationship edges
**Status:** Settled supporting principle

Do not add arbitrary metadata objects to every edge.

When a connection needs identity, rationale, evidence, lifecycle, or history, represent that using an appropriate first-class model element when the methodology requires it.

### WB-068 — Disposable local index
**Status:** Settled

Workbench may maintain a local cache/index for speed.

The cache is rebuildable and not authoritative.

“The index may be cached. The model may not.”

### WB-069 — Plugin/schema compatibility
**Status:** Settled

Schema/configuration should declare compatibility/version information.

If Workbench is too old for the vault schema, preserve note readability but disable unsafe semantic edit/view actions with a clear message.

---

## J. Scope corrections and deferred mechanics

### WB-070 — Property inheritance discussion paused
**Status:** Out of scope for Workbench

The discussion reached a question about schema-defined property inheritance.

The user explicitly redirected the effort:

> “this is getting into model mechanics and i really only want a good interface to the model”

No Workbench implementation should assume a new property-inheritance policy from that unfinished discussion.

### WB-071 — No schema redesign through UI design
**Status:** Settled

When an interface requirement exposes a real schema gap, record it for separate methodology review. Do not silently solve it inside Workbench.

---

## K. Implementation-level decisions (decide during the build)

These are build-time choices, not product questions. Decide them with the working plugin in hand ([[#WB-089 — Decide implementation details during the build]]), not one at a time up front.

### WB-072 — Exact V1 standard View Profile set
**Status:** Open

Committed minimum: Structure, Behavior, Requirements. Likely additions: Interfaces, Verification, Impact. Choose by implementation effort and the first real test slice.

### WB-073 — Generated-view folder/path
**Status:** Open (direction settled in WB-036)

Dedicated, configurable, excluded from Git. The default path/name is chosen at implementation.

### WB-074 — Workbench launch affordance
**Status:** Open

Ribbon icon, command palette action, dedicated sidebar/tab entry, or a combination. Does not change the dashboard information architecture.

### WB-075 — Create-action list shown on home
**Status:** Open

How many buttons show before an overflow/"more" action; test against the current schema and screen size. Do not hard-code element names.

### WB-076 — View Options contents for V1
**Status:** Open (existence settled in WB-023)

Candidates: depth, node limit, contextual relationships on/off, relationship-family toggles, layout choice. Prefer a very small initial set.

### WB-077 — Review finding severity/presentation
**Status:** Open

Whether findings need error/warning/info, or category + explanation is enough initially. Do not add severity just because conventional tooling has it.

### WB-078 — Curated-view metadata format
**Status:** Open

V1 curated views are frozen snapshots; keep enough metadata for a later Compare/Update. No model semantics in Canvas-only metadata.

### WB-079 — Folder-navigation ruleset reconciliation
**Status:** Open — methodology, not implementation

Ruleset 1.22 section 9 still requires a Views and Bases note, a base and a canvas in every model-facing folder (kept as written in W-260). The Workbench direction uses generated views instead. Resolve in a separate methodology decision; Workbench work does not change the ruleset. Nothing in V1 depends on the outcome.

---

## L. Release-path proposals (2026-09-30)

Written after a review of this folder for the path to a first release. **All are Proposed or Open until approved.**

### WB-080 — Relationship service first; Canvas Model Edit is release-gated
**Status:** Proposed

Build the relationship service (validation, canonical owner-side writeback, batch preview, undo) first and expose it through a command/modal on notes. Canvas Model Edit (WB-039 to WB-043, WB-046, WB-047, WB-050) is a second surface over the same service.

Why: Canvas editing relies on Canvas internals Obsidian does not officially expose; the reference work (note [[05 - Reference Plugin Findings]]) depends on patching, and the most capable reference is GPL. Generated read-only Canvas is low risk; edit-in-Canvas is not.

If approved: Phase 0 probes Canvas edit feasibility; V1 ships with Canvas Model Edit only if the probe is low-risk, otherwise it ships in the next release. Behavior in WB-039 to WB-050 does not change, only timing. Those decisions keep their current status until this is approved.

### WB-081 — Performance gate in Phase 0
**Status:** Proposed

Phase 0 measures Workbench on the real translated vault before feature work continues. Starting targets (placeholders to revise after the first measurement):

- vault size assumed: up to about 60,000 notes;
- cold index build: under 60 s; incremental update after a note save: under 500 ms;
- Structure view with the default node cap: generated and opened in under 3 s;
- index memory: under 300 MB;
- Obsidian stays responsive while indexing (no blocking of the UI thread for more than a fraction of a second).

If a target cannot be met, the finding goes to the decision log before more is built on the index design.

### WB-082 — Node cap outranks depth
**Status:** Proposed (amends WB-027)

Traversal is bounded by depth **and** a node cap, and the cap wins. When the cap is reached, keep nodes nearest the start first, then by the profile's relationship order; report omitted counts per branch (WB-028). Path enumeration is capped so dense graphs cannot explode.

For multiple starting elements (WB-025): compute the bounded paths that connect the selected elements first (shared context), then expand around each element on request.

### WB-083 — Duplicate note names: id suffix (already settled in the workspace)
**Status:** Settled elsewhere; Workbench consequence proposed

Workspace decisions W-198 and W-199 give every note in a duplicate-name group an id suffix, so note names stay unique (WB-018 holds).

Workbench consequence (proposed): the element picker and Review modals show **type and id beside the name**, and link resolution uses `uid`/`id`, never the name alone (WB-064, WB-065).

### WB-084 — One creation spec shared with templates
**Status:** Proposed

The creation service reads the class templates in `99_System/05_Templates` and the rules in `99_System/02_AI/AI_INSTRUCTIONS.md` (property order, `uid`, `id`, author code from `.obsidian/author-code.txt`) instead of carrying its own definition. A note created by Workbench must have the same header as one created from the template by hand.

Acceptance test: create each common class both ways and compare the headers; they must match.

### WB-085 — Who writes inverse relationship fields
**Status:** Open (question for Spencer)

AI_INSTRUCTIONS say to author the forward (owner-side) relationship and treat generated inverse fields as derivative. Workbench writes only the owner-side field (WB-045, WB-046).

Open question: which mechanism produces the inverse fields in the vault today, and does the plugin-independence rule (WB-003) allow Workbench to depend on it? Proposal: Workbench never double-writes inverse fields. If a plugin generates them, the compatibility check (WB-069) records that dependency. Phase 0 verifies that the inverse appears after a Workbench write.

### WB-086 — Git and external change
**Status:** Proposed

- Workbench never runs Git or commits in V1. People and AI tooling commit; Workbench only edits files.
- Changes made outside Workbench (a pull, an AI push, hand edits) are picked up from vault file events and update the index incrementally. After a large change set, or on demand (**Rebuild index**), the index is rebuilt.
- Each semantic transaction stores a before-state (content hash) per affected note. Undo refuses, with an explanation, when a note changed since.
- Relationship lists are written in a stable, deterministic order so two people adding relationships to the same note merge with fewer conflicts. Check the ordering rule against the storage form in `relationships.yaml` before implementing.
- The generated-view folder stays excluded from Git (WB-036).

### WB-087 — Platform support
**Status:** Open (proposal: desktop only for V1)

Decide whether Obsidian mobile is supported. Proposal: desktop only for V1; set `isDesktopOnly` in the plugin manifest; revisit after the pilot.

### WB-088 — Distribution, versioning and build
**Status:** Proposed

- The plugin's source lives in its own repository, not in the vault. The vault holds only vault-side configuration: View Profiles and the schema/compatibility declaration (WB-069).
- Releases are GitHub Releases containing `main.js`, `manifest.json` and `styles.css`, with semantic versioning and `minAppVersion`.
- MDSE Bootstrap installs a pinned Workbench version with the other pinned plugins.
- Build with TypeScript and esbuild following the official Obsidian sample plugin; CI on GitHub Actions. No local build toolchain is assumed: use a cloud development environment (for example GitHub Codespaces) so the work does not depend on one computer.
- Because the final vault leaves out methodology material, this folder's design notes belong in the plugin repository once that exists; the vault keeps a short pointer.

### WB-089 — Decide implementation details during the build
**Status:** Proposed

Product questions that change what an engineer sees still go one at a time. Implementation-level items (WB-072 to WB-078) are decided with the working plugin in hand and recorded here when settled. The roadmap and architecture already hold enough direction to start the Phase 0 spike.

### WB-090 — Release gates
**Status:** Proposed

- **R0 — Go/No-go after Phase 0:** performance targets (WB-081) met or a plan recorded; inverse-field behavior verified (WB-085); Canvas edit feasibility decided (WB-080).
- **R1 — Pilot:** two or three engineers use the plugin on a real test slice (the first slice is `02 Product Context`, W-267) and run the acceptance scenarios in [[03 - Build Outline and Roadmap]].
- **R2 — Team release:** pilot findings resolved; compatibility check and Bootstrap install verified on a fresh vault.

---

## How to use this log

When a future proposal conflicts with a settled decision:

1. identify the conflicting decision number;
2. explain why new information justifies reopening it;
3. record the revised decision and date;
4. update affected build/interface documents;
5. preserve the old decision in history rather than erasing it.

---

## History

### 2026-09-30 — Initial consolidated Workbench definition
Created the `MDSE Workbench` workspace from the Workbench/dashboard design discussion: Workbench is an interface to the existing MDSE model; Create / Explore / Review home; compact modal creation; selection-first Explore with one-click views; Canvas as first graphical surface, not model authority; explicit temporary Model Edit; whole-vault Review with categorized queues. A scope correction was recorded: a drift into property inheritance was stopped and is model governance (WB-070), not Workbench (see WB-071).

### 2026-09-30 — Release-path review and consolidation
**Changed**
- Consolidated 12 notes into 5: dashboard, Canvas and Review notes merged into the Product Definition; Build Outline and Roadmap merged; Open Decisions, Continuation Handoff and Change Log folded into this log and the README.
- Decision IDs renamed `D-` to `WB-`; open items folded in (WB-063, WB-072 to WB-079).
- Added proposals WB-080 to WB-090 (release gating, performance, traversal bounds, creation parity, inverse writes, Git and external change, platform, distribution, process, release gates).

**Reason**
- Review of the folder for the path to a first release: untested assumptions (scale, Canvas internals), decisions restated in many notes, missing non-functional requirements, and ID collisions with other logs.

**Affected decisions**
- No approved decision was changed. WB-027 has an amendment proposed (WB-082); WB-039 to WB-050 are subject to timing proposal WB-080.

### Earlier wording kept
The pause point before this review was the Sequential Review question (WB-063). The one-question-at-a-time method is unchanged: ask one focused question, explain the impact, offer options, recommend the simplest scalable one, record the decision, move on.

### Former open-item IDs
`O-001` → WB-063 · `O-002` → WB-072 · `O-003` → WB-073 · `O-004` → WB-074 · `O-005` → WB-075 · `O-006` → WB-076 · `O-007` → WB-077 · `O-008` → WB-078 · `O-009` → WB-079.
