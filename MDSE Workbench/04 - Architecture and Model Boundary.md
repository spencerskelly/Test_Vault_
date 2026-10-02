# Architecture and Model Boundary

The sections at the end follow decisions WB-080 to WB-090 in [[02 - Workbench Decision Log]], approved 2026-09-30.

## Core rule

**Workbench is an interface to the MDSE model.**

It should not become a second model, a hidden schema, or an alternate persistence layer.

## Sources of authority

### Model semantics

Authoritative sources remain the current vault model governance, including:

- MDSE Modeling Ruleset;
- element type schema;
- relationship schema;
- templates;
- approved modeling decisions.

### Workbench product/interface

This folder defines how Workbench should expose and operate on those semantics.

If the interface definition and the current model schema conflict, the model schema remains authoritative until a separate governance decision changes it.

## Generic engine + vault configuration

Workbench should be reusable across MDSE vaults.

The plugin should read vault-defined configuration for:

- recognized element types;
- relationships and inverse/display behavior;
- validation rules;
- View Profiles;
- compatibility/version information;
- configured locations such as generated views.

Do not hard-code Ampure product semantics into the core plugin.

## Internal architecture

Recommended separation:

```text
Workbench UI
   ↓
Create / Explore / Review
   ↓
Model Services
   ├─ Index / identity
   ├─ Validation
   ├─ Relationship service
   ├─ Traversal / view service
   ├─ Model-health service
   └─ Transaction / undo service
   ↓
Obsidian vault Markdown + YAML
```

Canvas is one renderer/editor over the same services.

## Model index

A local index/cache is allowed for performance.

Requirements:

- derived from the vault;
- disposable;
- rebuildable;
- updated incrementally when safe;
- rebuilt when consistency is uncertain;
- not committed as authoritative model state.

> The index may be cached. The model may not.

## Identity

The vault already defines durable note identity.

Workbench should use durable identity internally where practical while preserving human-readable Markdown relationships.

Never rely on file path alone as permanent identity.

Ambiguous links must be treated as errors rather than guessed.

## Addressable Local Model

W-293/W-294 and W-298 add model content below the file-backed note level without changing the rule that the vault files are authoritative.

Workbench therefore indexes two addressable kinds:

W-303 fixes the local-reference token style used by local records: `part-*`, `ep-*`, `conn-*`, and `flow-*`. These tokens are durable and opaque; visible engineering names are display data rather than identity.

- **note element** — durable identity is the note `uid`; file path is current location metadata, not permanent identity;
- **local model record** — durable identity is the owning note UID plus its governed local address (part occurrence, endpoint occurrence, connection or connection-scoped flow).

The core index/traversal APIs should operate on an addressable model reference rather than assuming every node is a `TFile` path. This is also the correct seam for later cross-vault resolution.

Local Model records remain structured, human-readable Markdown in the owning note body. They are a governed region separate from ordinary narrative text. W-302 defines exactly one managed region per note, beginning `<!-- MDSE:LOCAL-MODEL START schema=0.1 -->` beneath `## Local Model` and ending `<!-- MDSE:LOCAL-MODEL END -->`. The Workbench popup presents the records in a separate **Local Model** section. The parser owns only content inside those markers. Missing/duplicate/nested/mismatched markers become findings and disable structured edits. The general text editor must never rewrite the governed region.

Definition links from a local record point to reusable file-backed MDSE elements. Context-specific wiring/flow remains on the local records rather than being flattened into duplicate note-level relationships.

## Writing relationships

Workbench should use the relationship vocabulary and storage rules defined by the current schema.

Important interface behavior:

- engineer sees the relationship in the natural visual direction;
- Workbench resolves the canonical owner-side storage direction;
- authoritative YAML is updated immediately after confirmation;
- Workbench writes the derived inverse with the forward field (WB-085, W-275).

Workbench does not invent a separate graph database as the model of record.

## Relationship provenance

The view engine may render:

- explicit relationships;
- derived inverse relationships;
- contextual/inherited relationships allowed by a View Profile;
- future calculated/rolled-up relationships;
- Canvas-only visual connections.

The UI must keep those categories distinguishable.

Only explicit model changes should be written as authoritative relationships.

## Creation

All creation surfaces call one common creation service.

V1 modal creation and future Canvas-inline/workflow creation therefore produce the same validated result.

Creation should follow current:

- element type definitions;
- required properties;
- templates;
- UID/ID rules;
- relationship validity;
- placement conventions.

## Transaction safety

Workbench semantic edits should be explicit transactions.

A transaction should know:

- intended change;
- affected notes;
- validation result;
- before state;
- after state.

This supports:

- safe failure;
- Undo/Redo;
- batch operations;
- future audit improvements.

## Generated vs curated views

Generated Canvas files are working artifacts and may be replaced.

Curated Canvas files are intentional user artifacts and must not be overwritten automatically.

This boundary should exist in code, not merely documentation.

## Cross-vault boundary

V1 is single-vault for Workbench traversal and editing.

Do not design identity/traversal APIs so narrowly that every target must always be a local file path.

Future cross-vault support should be possible through an external resolver without rewriting core view logic.

## Community plugin boundary

Community plugin code and behavior can inform implementation, but core Workbench correctness must not depend on those plugins being installed.

Permissively licensed projects may provide implementation patterns where appropriate and attribution/license requirements are followed.

GPL code must not be copied into a differently licensed Workbench without consciously accepting the licensing consequence.

## Schema changes

Workbench is not the ordinary schema editor.

If a new engineering need cannot be expressed using the current schema:

1. keep the engineering need visible;
2. use approved provisional behavior if available;
3. take the semantic question to model governance;
4. update Workbench only after the model decision is made.

## Compatibility

The vault/schema should expose enough version information for Workbench to determine whether semantic actions are safe.

If incompatible:

- keep Markdown readable;
- explain the mismatch clearly;
- disable unsafe creation/edit/view generation rather than guessing.

## Principle

The simplest reliable architecture is:

> Obsidian files are the model. Workbench makes them easier to use.

## Performance *(WB-081)*

The index is the performance-critical part. Design for the full translated vault (up to about 60,000 notes): build the index off the UI thread or in small chunks, update incrementally from file events, persist a rebuildable cache, and never render an unbounded graph (node cap outranks depth, WB-082). Measure on the real vault in Phase 0.

## External change and Git *(WB-086)*

- Workbench edits files; it does not run Git or commit.
- Changes from pulls, AI tools or hand edits arrive as file events; update the index incrementally, rebuild after a large change set or on demand.
- Each semantic transaction records a before-state hash per note; Undo refuses with an explanation if a note changed since.
- Write relationship lists in a stable order to reduce merge conflicts.

## Inverse relationship fields *(settled, WB-085, W-275 trial)*

Workbench writes the inverse with each forward field it writes, and writes inverses after hand edits made on the same machine. Changes from pulls or outside AI edits are reported as missing-inverse findings, not rewritten automatically, so machines do not race each other. The forward field is the authority; the inverse is regenerated from it. No dependency on Nodian.

## Creation parity *(WB-084)*

The creation service reads the vault's class templates and the `uid`/`id`/author-code rules rather than duplicating them, so a Workbench-created note equals a template-created one. Both the template and Workbench therefore change together when the rule changes.

## Platform, distribution and versioning *(WB-087, WB-088)*

Desktop only, with mobile-ready code: only Obsidian's own APIs (no Node or Electron), narrow-screen layouts, select-then-command interactions, a compact index (WB-087). Plugin source lives in its own repository; releases are GitHub Releases pinned by MDSE Bootstrap. The vault holds only vault-side configuration (View Profiles, schema/compatibility declaration).

