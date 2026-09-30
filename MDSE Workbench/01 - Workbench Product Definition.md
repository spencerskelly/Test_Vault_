# Workbench Product Definition

## Problem

The MDSE model can become highly connected and valuable while still being difficult for a normal engineer to use directly.

The engineering interface should make the model feel like a useful working environment rather than a database or formal modeling tool.

The primary problem is therefore not to create more model mechanics. It is to provide a simple interface that lets an engineer answer questions and make valid changes without needing to understand the implementation behind the model.

## Product statement

**MDSE Workbench is an Obsidian-native engineering workspace for creating, exploring, reviewing, and graphically editing an existing MDSE model.**

It provides a guided interface over the model while leaving Markdown notes, YAML, explicit relationships, and vault governance as the durable engineering record.

## Primary users

### Everyday engineer

Needs to:

- create engineering elements quickly;
- find an element by name;
- see useful connected context;
- create or correct relationships;
- identify things that need attention;
- move between graphical views and detailed notes.

Should not need to:

- know YAML syntax;
- know schema implementation;
- know Nodian internals;
- manually build routine Canvas views;
- understand Git for ordinary modeling actions.

### Model maintainer

Needs the same interface plus:

- visibility into unresolved or invalid content;
- model-health review;
- predictable schema-driven behavior;
- a controlled path for future Workbench capabilities.

Schema governance itself remains outside the ordinary Workbench interface.

## Product principles

### 1. Interface first

The model already exists. Workbench should expose it well rather than redesign it.

### 2. Task-oriented

The primary dashboard is organized around **Create**, **Explore**, and **Review**, not around the metamodel taxonomy.

### 3. Fast normal path

Common tasks should require very few actions.

Examples:

- Create element → compact modal → create → note opens.
- Explore → select element(s) → click view → Canvas opens.
- Review → click category → select finding → focused resolution modal.

### 4. Explicit semantics

Workbench may suggest, filter, and validate, but it must not silently invent engineering meaning.

### 5. Graphical views are interfaces, not authority

Canvas should visualize and help edit the underlying notes and relationships. The Canvas itself is not the authoritative model.

### 6. Useful defaults, optional depth

Normal use should work with governed defaults. Advanced controls should exist without blocking the quick path.

### 7. Reversible growth

V1 should be intentionally simple while keeping a clear path to:

- richer creation workflows;
- native graphical relationship gestures;
- direct property editing;
- richer filters and searches;
- non-destructive curated-view synchronization;
- cross-vault views.

## Primary user journeys

### Create

```text
Workbench
  → Create
  → choose element type/action
  → compact modal
  → Create
  → new note opens
```

### Explore

```text
Workbench
  → Explore
  → search/select one or more elements
  → optional type filter
  → click Structure / Behavior / Requirements / ...
  → generated Canvas opens
```

The main view button uses governed defaults. **View Options...** allows an engineer to alter the view before generation.

### Review

```text
Workbench
  → Review
  → see whole-vault finding counts
  → choose category
  → dedicated Review screen
  → filter/search
  → choose finding
  → focused resolution modal
```

## What V1 is not

V1 is not:

- a replacement for Obsidian;
- a SysML implementation;
- a full schema editor;
- a project-management system;
- a full issue tracker;
- a query language;
- a cross-vault graph engine;
- a live always-redrawing visualization system.

## Success criteria

V1 succeeds when an engineer can:

1. open Workbench and understand the main actions without training;
2. create a valid common MDSE element through a compact modal;
3. find a model element quickly by unique name;
4. generate a useful engineering view in one click;
5. enter Model Edit intentionally and change a relationship safely;
6. see unresolved/model-health items without running manual queries;
7. resolve straightforward review findings without editing YAML by hand;
8. leave the underlying vault readable and useful even if Workbench is unavailable.

## Relationship to other MDSE tools

The intended tool split is:

- **MDSE Workbench** — everyday engineer interface.
- **MDSE Bootstrap** — setup/configuration verification.
- **MDSE Translator** — EA/native import and migration.
- **Cross-Vault Resolver** — cross-vault infrastructure.

Workbench should be internally modular, but it should feel like one primary plugin to the engineer.
