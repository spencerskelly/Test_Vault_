# Continuation Handoff

## Purpose

This note is the fastest way for a future engineer or AI to resume Workbench design without replaying the original conversation.

## Current objective

Build a practical Obsidian interface to the existing MDSE model.

Do **not** restart with metamodel design.

The Workbench should let engineers:

- create model content;
- explore it through useful views;
- edit relationships safely;
- review model-health findings;
- work graphically without making Canvas the model authority.

## Read before continuing

1. [[README_MDSE Workbench]]
2. [[01 - Workbench Product Definition]]
3. [[02 - Dashboard Interface Definition]]
4. [[03 - Workbench Decision Log]]
5. [[04 - V1 Build Outline]]

Use the specialized Canvas and Review notes when working in those areas.

## Current UI direction

### Home

```text
CREATE
EXPLORE
REVIEW
```

### Create

Compact modal in V1.

After creation, open the new note.

Preserve a path to richer Workbench workflow screens later.

### Explore

Select one or more elements first.

V1 picker:

- unique-name search;
- optional type filter;
- multi-select.

Clicking a normal view button generates immediately.

**View Options...** supports advanced overrides.

### Review

Home shows categorized whole-vault finding counts.

Click category → dedicated Review screen.

Click finding → focused resolution modal.

## Current Canvas direction

- generated Canvas is a disposable working view;
- curated Canvas is an intentional frozen snapshot in V1;
- View Mode is default;
- Model Edit is explicit and temporary;
- relationships can be created from selected nodes;
- future drag-to-connect should reuse the same relationship service;
- semantic removal requires confirmation;
- removing a Canvas node never removes the model element;
- contextual/inherited edges are visually distinct and read-only;
- semantic edits support in-session Undo/Redo.

## Current V1 priority

Build working behavior before completeness.

Recommended implementation order:

1. Workbench skeleton + index;
2. element picker + Structure view;
3. creation modal;
4. Model Edit relationship workflow;
5. Behavior/Requirements views;
6. Review;
7. hardening.

## Exact discussion pause point

The last unanswered interface question was:

> Should the focused Review screen support working through findings sequentially?

Options were effectively:

- manual selection only;
- Previous/Next with automatic advance after resolution;
- full batch resolution.

The recommendation was **Previous/Next without bulk editing**.

This decision has not yet been approved.

Continue from this question if resuming the one-question-at-a-time design process.

## Important scope correction

Immediately before dashboard design, the discussion had drifted into schema mechanics, ending at a question about property inheritance.

The user stopped that direction and stated that the goal is a **good interface to the model**.

Do not resume property inheritance as though it were an unfinished Workbench requirement.

If it matters later, treat it as a separate model-governance question.

## One-question-at-a-time method

When continuing product design:

1. ask one focused question;
2. explain the impact;
3. offer clear options;
4. recommend the simplest scalable option;
5. record the user's decision;
6. move to the next question.

Do not reopen settled decisions without new information.

## Known reconciliation item

Current MDSE Ruleset 1.21 still requires a Canvas in every model-facing folder.

The newer Workbench direction replaces much of that need with generated Canvas views, and the user had separately moved toward README + Base only for top-level folders.

Do not silently alter the ruleset from Workbench work. Reconcile that folder-navigation rule in a dedicated methodology update.

## Implementation rule

Whenever the UI needs a model fact, read it from the current governed schema/configuration rather than embedding a duplicate assumption in the plugin.

## Definition of a good next step

A good next step either:

- resolves an open interface decision; or
- implements/tests one V1 user journey.

A poor next step is adding model complexity that does not improve the engineer's interface.
