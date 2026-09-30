# Canvas and View Experience

## Purpose

Canvas is the first graphical renderer and graphical editing surface for MDSE Workbench.

The model remains in Markdown/YAML. Canvas is an interface over that model.

## View families

### Core everyday views

- Structure
- Behavior
- Requirements
- Interfaces
- Verification
- Impact / Change Impact

### Additional future profiles

- Where Used
- Type / Reuse
- Functional Allocation
- Function Context
- Requirement Trace
- Test Context
- State Context
- Scenario
- Failure / Risk Context
- Variant Comparison
- Design Rationale
- Evidence Chain
- Model Health

V1 does not need every profile. Prove the engine with a small number of high-value profiles first.

## View Profile concept

A View Profile defines how the same model should be explored for a particular engineering question.

A profile may define:

- allowed relationship types;
- traversal direction;
- default depth;
- stop conditions;
- node limits;
- whether contextual/inherited content is shown;
- layout rules;
- expansion rules;
- edge display rules.

The model is not duplicated for each view.

## Relationship provenance in views

Rendered connections should preserve how they were obtained.

Useful classes:

- **explicit** — directly stored model relationship;
- **derived inverse** — reverse presentation of an authoritative stored relationship;
- **contextual/inherited** — shown because the active profile permits context propagation;
- **calculated/rolled-up** — possible future analytical connection;
- **Canvas-only** — visual annotation with no model semantics.

Contextual/inherited edges must be visually distinct and read-only.

## Generated views

Generated views are for fast engineering exploration.

They are:

- generated from current model state;
- disposable;
- refreshable;
- deterministic enough to reproduce;
- stored in a configured generated-view location;
- excluded from Git.

### Refresh

V1 may rebuild a generated Canvas completely.

Manual Canvas-only layout and annotations can be lost.

If manual work matters, the user should choose **Save as Curated View** before refresh.

### Staleness

Workbench should indicate when relevant model changes make a generated view out of date.

The user can then refresh intentionally.

No continuous redraw is required.

## Curated views

V1 curated views are frozen intentional snapshots.

Workbench does not automatically overwrite them.

Future revisions may add:

- Compare with Model;
- Update from Model;
- non-destructive refresh;
- improved source trace.

Preserve enough generated-view metadata to keep that future path open.

## Starting elements

V1 supports one or multiple selected elements.

For multiple selected elements:

1. show shared/connecting context first;
2. avoid exploding each entire neighborhood immediately;
3. allow local expansion around each selected element.

## Traversal and bounds

The View Profile supplies a sensible default depth.

The engineer may request deeper traversal.

Within the current bound, Workbench should show all valid semantic paths relevant to the profile.

If the graph is too large:

- render a useful bounded result;
- show omitted-branch indicators such as “+12 additional requirements”;
- allow expansion.

Never imply that omitted content does not exist.

## Layout

Standard profiles should use predictable engineering-oriented layouts.

Examples:

### Structure

Prefer parent/supertype above and child/part below where practical.

### Behavior

Favor performer → behavior → flow/context reading.

### Requirements

Favor scope/basis → requirement → satisfaction/verification trace.

These are view conventions only; they do not change model semantics.

## View Mode

Generated views open in View Mode.

Typical actions:

- inspect;
- navigate;
- expand/collapse;
- open notes;
- follow relationship source.

View Mode is the safe default.

## Model Edit mode

The engineer explicitly enables **Model Editing** on the current Canvas.

Edit mode is temporary for that Canvas session.

Closing/reopening the Canvas or restarting Obsidian returns to View Mode.

## Relationship creation

### V1 gesture

1. select source/target model nodes;
2. choose **Create Relationship**;
3. Workbench shows schema-valid choices;
4. engineer selects one;
5. confirmation writes the authoritative relationship immediately.

### Display vs storage direction

The Canvas should label a relationship in the natural visual reading direction.

The write service translates that into the canonical owner-side relationship required by the model.

### Future drag gesture

Native drag-to-connect can later call the same relationship service.

The semantic service must therefore remain independent of the gesture.

## Batch relationship creation

The desired long-term interaction supports:

- many selected nodes → one target;
- one source → many selected targets.

V1 can expose the behavior through selection + command rather than drag.

Before commit:

- show valid pairs;
- show invalid pairs;
- require confirmation;
- do not silently skip invalid pairs.

Avoid automatic many-to-many/all-to-all creation.

## Relationship removal

Deleting a semantic edge prompts:

1. **Remove from this view only**
2. **Remove relationship from model**
3. **Cancel**

If the displayed edge is inverse/contextual/inherited, Workbench must trace to the authoritative stored source rather than pretending the rendered edge is directly stored.

## Node removal

Removing a node from Canvas removes only the Canvas node.

It does not delete, retire, or otherwise remove the model element.

## Element creation from Canvas

Long-term goal: allow natural model creation while working graphically.

V1 path:

- Canvas action opens the standard Workbench creation modal;
- common creation service creates the note;
- new node is placed on the Canvas.

Future inline creation should reuse the same service.

## Ordinary property editing

V1: open the note.

Future: expose safe property editing directly from Canvas.

## Groups

V1 Canvas groups are visual only.

A future explicitly bound semantic group may propose a schema-defined relationship when a compatible element is dropped into it.

Any semantic change still requires engineer confirmation.

## Undo and recovery

Workbench provides in-session semantic Undo/Redo.

A batch edit is one semantic transaction.

Git provides durable history; normal mistakes should not require a Git operation to undo.

## Principle

Canvas should help engineers think spatially without making graphical layout a hidden source of model truth.
