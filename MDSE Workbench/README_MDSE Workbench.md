# MDSE Workbench

## Purpose

This folder is the living product-definition workspace for the **MDSE Workbench**: a practical Obsidian interface that helps engineers create, explore, review, and graphically work with the existing MDSE model without requiring them to become modeling specialists.

The Workbench is an **interface to the model**, not a replacement metamodel and not a second source of model semantics.

## Current direction

The Workbench is intended to become the primary everyday MDSE user interface in Obsidian.

V1 centers on three activities:

1. **Create** — quickly create valid MDSE elements using compact modal forms.
2. **Explore** — select one or more model elements and generate useful engineering Canvas views.
3. **Review** — surface model-health findings and work through them in a focused review workflow.

The normal engineer should be able to use the vault without understanding schema files, plugin internals, Git mechanics, or formal SysML tooling.

## Start here

1. [[01 - Workbench Product Definition]]
2. [[02 - Dashboard Interface Definition]]
3. [[03 - Workbench Decision Log]]
4. [[04 - V1 Build Outline]]
5. [[05 - Canvas and View Experience]]
6. [[06 - Review Experience]]
7. [[07 - Architecture and Model Boundary]]
8. [[08 - Roadmap and Revision Strategy]]
9. [[09 - Continuation Handoff]]
10. [[10 - Open Decisions]]
11. [[11 - Reference Plugin Findings]]
12. [[12 - Change Log]]

## Authority

This folder is authoritative for the **Workbench product/interface direction** once decisions are approved through the normal Git review process.

It is **not authoritative for MDSE model semantics**. Current element definitions, relationships, templates, and modeling rules remain governed by the vault's existing ruleset and schema files under `99_System`.

If this folder conflicts with the MDSE schema, the schema remains authoritative until a separate model-governance decision changes it.

## Design boundary

Workbench should:

- read the model;
- use the current vault-defined schema;
- create and edit model content through the approved semantics;
- validate user actions;
- provide useful graphical and tabular views;
- make model-health issues visible;
- keep engineers close to normal Obsidian workflows.

Workbench should not:

- invent new model semantics;
- silently infer relationships;
- redefine element-type mechanics;
- turn folder placement into model meaning;
- require users to understand implementation details to perform normal engineering work.

## Working-before-perfection principle

V1 should solve the common engineering workflow with the least interface complexity that can scale. More advanced behavior should be added only after real use shows value.

Where a future capability is already valuable, V1 should preserve an architectural path to it without requiring the full feature immediately.

## Known ruleset reconciliation item

MDSE Modeling Ruleset 1.21 currently says every model-facing folder contains a Views and Bases note, Folder Contents base, and Folder Map canvas.

The newer Workbench direction intentionally moves away from requiring a prebuilt Canvas in every folder and uses generated views instead.

This folder therefore contains a README and local Base only. The navigation rule should be reconciled separately in the modeling ruleset; this Workbench package does not silently change model governance.

## Status

Initial consolidated definition created 2026-09-30 from the Workbench/dashboard design discussion.
