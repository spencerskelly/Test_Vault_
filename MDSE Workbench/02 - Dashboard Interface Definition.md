# Dashboard Interface Definition

## Purpose

The dashboard is the primary intentional entry point for MDSE Workbench actions in V1.

Normal Obsidian notes and menus should remain clean. Engineers know that when they want to actively work with the model, they open Workbench.

## V1 dashboard organization

The dashboard is organized by **engineering activity**.

```text
MDSE WORKBENCH

CREATE
[ Object ] [ Requirement ] [ Function ] [ Design ]
[ Port ] [ Verification ] [ Plan ] [ Issue ] ...

EXPLORE
[ Search for one or more elements... ]
Type: [ All ▼ ]

Selected:
• Main Control PCBA
• Power Module

[ Structure ] [ Behavior ] [ Requirements ]
[ Interfaces ] [ Verification ] [ Impact ]

                        [ View Options... ]

REVIEW
New Relationships      7
Model Errors            3
Incomplete Elements    12
Broken References       2
```

Exact labels and supported create actions should follow the current vault schema rather than be hard-coded from this mockup.

## Create area

### V1 behavior

Creation uses a **compact modal form**.

The form:

- is schema-driven;
- asks only for information needed for a valid initial element plus useful basic fields;
- validates before creation;
- uses normal vault placement rules;
- creates the note through the same underlying creation service that future workflows will use.

After creation, the new note opens automatically.

### Future path

Complex activities may later graduate to a dedicated Workbench workflow screen without changing the underlying creation service.

Examples that may eventually justify a richer workflow:

- planning verification campaigns;
- creating a connected set of elements;
- configuring a complex engineering context.

A future user preference may also allow rapid-entry mode that stays in Workbench after creation.

## Explore area

### Selection-first workflow

V1 starts by selecting what the engineer wants to inspect.

The element picker supports:

- fast unique-name search;
- optional type filter;
- multi-select.

V1 intentionally does **not** begin as a general query builder.

### Future picker improvements

Possible later additions:

- recent elements;
- favorites;
- richer property filters;
- saved searches;
- starting from a view button and selecting afterward.

### View launch

The normal interaction is one click:

```text
select elements → click Structure → Canvas opens
```

The main button uses the standard governed View Profile.

An adjacent **View Options...** path allows overrides before generation.

Possible options include:

- depth;
- node limit;
- relationship categories;
- contextual/inherited content;
- expansion behavior.

The default path should not require these choices.

## Review area

The dashboard shows categorized whole-vault findings, such as:

- New Relationships;
- Model Errors;
- Incomplete Elements;
- Broken References;
- Ambiguous References;
- other schema/model-health findings.

The dashboard should show concise counts rather than a long list of individual findings.

Clicking a category opens the dedicated Review screen.

## Dashboard personalization

The shared dashboard structure is common to the vault.

Future users may locally:

- favorite actions;
- hide low-use actions;
- reorder actions.

Personal dashboard changes affect presentation only. They never change schema semantics, permissions, or shared model state.

Personal Workbench settings should be local by default, with a future path to export/import or sync.

## Dashboard implementation direction

V1 should be a dedicated custom Obsidian Workbench view, not a Markdown dashboard.

A lightweight Markdown landing/help note may be added later for onboarding and documentation, but it should not be the primary interactive interface.

## V1 interaction priority

The dashboard should optimize for:

1. obviousness;
2. low click count;
3. safe model changes;
4. fast transition into normal Obsidian notes or Canvas;
5. minimal configuration before useful output.
