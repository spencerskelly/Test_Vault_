# V1 Build Outline

## Goal

Deliver the smallest Workbench release that makes the MDSE vault substantially easier for an engineer to use every day.

V1 should prove the interface and semantic-editing pattern before investing in advanced automation.

## V1 capability set

### Dashboard

- dedicated MDSE Workbench view;
- task-oriented **Create / Explore / Review** sections;
- common create actions;
- element selection for Explore;
- standard view launch buttons;
- Review finding counts.

### Create

- compact schema-driven modal;
- valid initial note creation;
- duplicate-name protection;
- folder/default placement support;
- automatic open of created note.

### Explore

- fast unique-name search;
- optional type filter;
- multi-select;
- Structure, Behavior, and Requirements views at minimum;
- one-click governed defaults;
- adjacent View Options path.

### View engine

- read current model index;
- bounded semantic traversal;
- one or multiple starting elements;
- shared/connecting context for multi-start;
- all valid paths within bounds;
- omitted-branch indicators;
- deterministic standard layout;
- stale-view indication;
- generated-view refresh;
- generated view reuse by starting set + profile.

### Canvas

- generated native Obsidian Canvas;
- View Mode by default;
- explicit temporary Model Edit mode;
- selected nodes → Create Relationship;
- one-to-many / many-to-one batch relationship creation;
- valid/invalid preview before batch commit;
- immediate model write after confirmation;
- relationship removal confirmation;
- Canvas node removal does not remove the model element;
- in-session semantic Undo/Redo;
- Save as Curated View.

### Review

- categorized whole-vault findings;
- dedicated Review screen;
- filters/search;
- focused finding modal;
- open source/target;
- straightforward resolution actions;
- `newRelationship` replacement with an existing valid relationship.

### Model/index foundation

- schema/config loader;
- element registry/index;
- relationship registry;
- validation service;
- traversal service;
- local disposable cache;
- plugin/schema compatibility check.

## Suggested internal modules

Workbench should feel like one plugin but use clear internal services.

### Model Core

- vault scan/index;
- identity resolution;
- schema/config loading;
- relationship registry;
- validation;
- model-health findings;
- incremental cache update and rebuild.

### Create

- dashboard create actions;
- schema-driven forms;
- naming/duplicate checks;
- placement selection;
- note creation;
- future richer workflows.

### Explore

- element picker;
- View Profile selection;
- traversal;
- path finding;
- context expansion;
- View Options.

### Canvas

- Canvas generation;
- deterministic layout;
- provenance styling;
- View Mode / Model Edit;
- relationship edit actions;
- batch edit preview;
- semantic Undo/Redo;
- generated/curated behavior.

### Analyze / Review

- model-health categories;
- finding list;
- filtering;
- focused finding modal;
- resolution actions.

## Service-oriented design

Even if V1 uses simple gestures, internal services should not encode those gestures.

Conceptually:

```text
createElement(...)
createRelationships(sourceIds[], targetIds[], relationshipType)
removeRelationship(...)
buildView(startIds[], viewProfile, options)
findModelHealthFindings(filters)
resolveFinding(...)
```

Exact APIs can change; the separation is what matters.

## Suggested phases

### Phase 0 — Skeleton

- plugin registration;
- Workbench view;
- config loading;
- compatibility check;
- model index;
- diagnostics.

**Exit:** Workbench opens and lists recognized model elements.

### Phase 1 — Explore first

- element picker;
- Structure profile;
- native Canvas generation;
- deterministic layout;
- refresh;
- stale detection.

**Exit:** engineer can select an element and create a useful Structure view in one click.

### Phase 2 — Creation

- modal framework;
- common element creation;
- duplicate-name check;
- folder selection;
- open new note after create.

**Exit:** common elements can be created without manually writing YAML.

### Phase 3 — Model Edit

- explicit Model Edit mode;
- relationship picker;
- endpoint validation;
- canonical writeback;
- relationship removal prompt;
- Undo/Redo.

**Exit:** engineer can safely correct relationships from a generated Canvas.

### Phase 4 — More views

- Behavior;
- Requirements;
- other approved profiles;
- multi-start behavior;
- omitted-branch indicators;
- Expand/Collapse.

**Exit:** several common engineering questions work through the same traversal engine.

### Phase 5 — Review

- finding categories/counts;
- dedicated Review screen;
- filters;
- focused modal;
- `newRelationship` resolution.

**Exit:** unresolved/model-health items can be worked without manual queries.

### Phase 6 — Hardening

- large-vault performance;
- cache rebuild behavior;
- schema-version compatibility;
- failed-edit recovery;
- test fixtures;
- documentation.

## V1 acceptance scenarios

### Create a Function

Open Workbench → Create Function → complete modal → Create → new Function note opens and follows current schema/template.

### View structure

Open Workbench → search/select PCBA → Structure → generated Canvas opens with profile-defined context and explicit omission indicators if bounded.

### Add a relationship

Generated view → Enable Model Editing → select nodes → Create Relationship → choose valid relationship → confirm → authoritative model updates immediately.

### Resolve `newRelationship`

Workbench Review → New Relationships → open finding → choose existing valid replacement → confirm → unresolved finding clears.

### Preserve an important view

Generate quick view → adjust/annotate → Save as Curated View before refresh → curated Canvas becomes a normal intentional vault artifact.

## Explicit V1 deferrals

Do not delay V1 for:

- native drag-to-connect;
- full Canvas property editing;
- semantic Canvas groups;
- live redraw;
- non-destructive curated-view sync;
- cross-vault traversal;
- query/filter starting sets;
- advanced naming enforcement;
- bulk governance actions;
- schema authoring inside Workbench.

## Testing priorities

1. Never corrupt authoritative notes.
2. Never create a relationship the current schema rejects.
3. Never silently infer semantics.
4. Generated views are reproducible.
5. Undo reverses a Workbench semantic transaction.
6. Refresh cannot destroy a curated view.
7. Index/cache can be rebuilt from the vault.
8. Plugin failure leaves Markdown/YAML usable.
