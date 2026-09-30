# Review Experience

## Purpose

Review turns model-health findings into actionable engineering work.

The goal is not to build another issue tracker. It is to make the existing model easier to keep coherent.

## Dashboard presentation

The Workbench home screen shows concise finding categories and counts.

Example:

```text
REVIEW

New Relationships        7
Model Errors              3
Incomplete Elements      12
Broken References         2
Ambiguous References      1
```

Exact categories should come from the model-health engine and current schema rather than being hard-coded to this example.

## Scope

Review represents the **whole-vault model state** by default.

The engineer can narrow the queue using filters.

Possible filters:

- finding category;
- element type;
- relationship type;
- folder;
- product/system context;
- status where relevant.

Saved personal filters may be added later.

## Dedicated Review screen

Clicking a category opens a dedicated Workbench screen.

Suggested flow:

```text
Workbench
  → Review
  → choose category
  → search/filter list
  → select finding
  → focused resolution modal
```

The home dashboard remains uncluttered.

## Focused finding modal

The modal should explain the issue in context and present only relevant actions.

For a provisional relationship:

```text
New Relationship

Source:
Temperature Sensor

Current relationship:
newRelationship

Target:
Thermal Requirement

Valid replacements:
○ <schema-valid relationship>
○ <schema-valid relationship>

[Open Source] [Open Target]

[Cancel] [Replace Relationship]
```

## newRelationship behavior

`newRelationship` is intentionally available when an engineer knows two elements are related but does not know the approved semantic relationship.

### Resolve

Replace it with an **existing valid relationship**.

### No valid relationship

Leave it unresolved.

The Review modal must not become a schema-authoring interface.

### Explanation

No explanation is required to create `newRelationship`.

## Other finding types

### Broken reference

Show the source element, affected property, unresolved target, and safe repair actions.

### Ambiguous reference

Show candidate targets and require explicit engineer selection.

Never guess.

### Incomplete element

Show the element, missing/flagged information, and an action to open/edit it.

### Invalid or legacy relationship

Show the current relationship, why it is rejected by the current schema, safe valid replacements if available, and the source note.

### Stale generated view

Prefer a lightweight view-state notification rather than a governance finding unless future use shows that central review adds value.

## Sequential review

**Open decision at the time this package was created.**

The next unanswered interface question was whether a user should be able to move through the filtered queue with:

```text
← Previous     4 of 17     Next →
```

and automatically advance after resolving an item.

The recommendation at the pause point was to support this because it improves cleanup sessions without introducing broad batch-edit behavior.

## Batch review

Do not make broad batch resolution a V1 requirement.

If batch review is added later, require explicit preview and semantic validation.

## Dismiss/ignore behavior

No generic permanent “dismiss model error” behavior has been approved.

A finding that reflects current model state should normally remain until the model or governing rule changes.

Future finding types may justify explicit waivers, but those should be designed deliberately.

## Success criteria

Review succeeds when:

1. an engineer can see that unresolved work exists;
2. they can narrow the queue to the current engineering context;
3. each finding explains enough context to act;
4. straightforward corrections happen without manual YAML editing;
5. unresolved methodology gaps remain visible instead of being guessed away.
