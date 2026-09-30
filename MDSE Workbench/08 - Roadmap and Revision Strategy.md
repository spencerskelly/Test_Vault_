# Roadmap and Revision Strategy

## Purpose

This roadmap protects two goals at once:

1. get a useful Workbench into engineers' hands quickly;
2. avoid decisions that make later improvements unnecessarily expensive.

The roadmap is capability-based, not a promise of release dates.

## V1 — Useful interface

Primary objective: make the existing model easy to create, explore, and review.

### Include

- dedicated Workbench dashboard;
- Create / Explore / Review organization;
- compact creation modals;
- simple element picker;
- one-click standard views;
- View Options;
- Structure, Behavior, Requirements views at minimum;
- generated Canvas;
- bounded traversal and omission indicators;
- stale detection and refresh;
- Save as Curated View;
- explicit Model Edit mode;
- relationship create/remove workflows;
- batch one-to-many/many-to-one validation preview;
- semantic Undo/Redo;
- categorized Review screen;
- focused finding modal;
- `newRelationship` resolution to an existing relationship;
- local disposable model index;
- compatibility checking.

## V1.x — Improve high-use workflows

Add only after V1 usage shows clear value.

Candidates:

- recent elements;
- favorites;
- richer picker filters;
- saved personal filters;
- more View Profiles;
- improved layouts;
- sequential Review navigation;
- faster repeated creation;
- better relationship source tracing;
- improved model-health explanations.

## V2 — Rich graphical modeling

Potential capabilities:

- native drag-to-connect;
- inline Canvas element creation;
- direct Canvas property editing;
- more sophisticated expansion/collapse;
- richer batch editing;
- semantic group binding;
- improved guided relationship creation.

All should reuse the V1 model services.

## Later — Curated-view synchronization

Potential capabilities:

- Compare Curated View with Model;
- Update from Model;
- preserve manual placement;
- preserve annotations;
- show added/removed model context before applying updates.

Do not retrofit this by making curated views disposable.

## Later — Advanced discovery

Potential capabilities:

- query/filter starting sets;
- saved shared searches;
- analytical/rolled-up relationships;
- evidence-chain exploration;
- variant comparison;
- richer impact analysis.

## Later — Cross-vault Workbench

V1 is intentionally single-vault.

Future direction may include:

- resolving external UIDs;
- including external context in views;
- following cross-vault relationships;
- clear read/write authority display;
- editing only where the user has valid access.

Core identity/traversal APIs should keep this path open.

## Revision discipline

### Preserve decisions

Do not rewrite history to make current decisions look inevitable.

When a decision changes:

1. keep the prior decision in the Decision Log;
2. mark it superseded;
3. add the replacement decision and date;
4. explain what changed;
5. update affected build/interface notes.

### Separate interface and model governance

If a Workbench discussion starts redefining the model, stop and move that question to the appropriate model-governance work.

The Workbench can expose model mechanics, but it should not accidentally decide them.

### Favor evidence from use

Prefer:

1. simple V1 behavior;
2. observe engineer friction;
3. identify repeated/high-value needs;
4. add capability where it materially improves engineering work.

Avoid speculative feature depth solely because the plugin could support it.

## Backward-compatibility principle

Where practical, future interface improvements should be new views or gestures over stable model services rather than incompatible rewrites.

Examples:

- modal creation → richer workflow, same creation service;
- select + command relationship → drag-to-connect, same relationship service;
- one-click profile → advanced View Options, same view engine;
- frozen curated view → later non-destructive sync using preserved metadata.

## Definition of successful evolution

Workbench is succeeding if it becomes more capable while the everyday workflow remains understandable to an engineer who does not care how the model is implemented.
