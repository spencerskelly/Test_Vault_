# Open Decisions

## Purpose

This note keeps unresolved Workbench questions separate from settled decisions so future design work does not accidentally treat recommendations as approvals.

## O-001 — Sequential Review navigation

**Question**

When a user opens an individual Review finding, should Workbench support moving directly through the current filtered queue?

### Option A — Manual selection

Resolve/close a finding, return to the list, choose another.

### Option B — Previous / Next

Show navigation such as:

```text
← Previous     4 of 17     Next →
```

After successful resolution, optionally advance to the next unresolved finding.

### Option C — Batch resolution

Allow multi-select and bulk semantic correction.

### Current recommendation

**B — Previous / Next**, without broad batch editing in V1.

### Why it matters

This changes how usable Review feels during cleanup sessions but does not require a new model concept.

---

## O-002 — Exact V1 standard View Profile set

The minimum committed set is:

- Structure
- Behavior
- Requirements

Likely useful additions include:

- Interfaces
- Verification
- Impact

The final V1 set should be chosen based on implementation effort and the first real test model.

---

## O-003 — Exact generated-view folder/path

Direction is settled:

- generated views use a dedicated location;
- location is configurable;
- generated views are excluded from Git.

The exact default path/name still needs to be chosen during implementation.

---

## O-004 — Exact Workbench launch affordance

The dashboard is the primary intentional entry point.

Implementation still needs to choose the Obsidian-native launch affordance, for example:

- ribbon icon;
- command palette action;
- dedicated sidebar/tab entry;
- combination of these.

This is an implementation/UI detail, not a change to the dashboard information architecture.

---

## O-005 — Exact create-action list shown on home

The dashboard is task-oriented and Create uses schema-driven modals.

The exact number of buttons visible before an overflow/more action should be tested against the current schema and screen size.

Do not hard-code obsolete element names.

---

## O-006 — View Options contents for V1

The existence of **View Options...** is settled.

The smallest useful V1 option set still needs to be chosen.

Candidates:

- depth;
- node limit;
- include/exclude contextual relationships;
- relationship-family toggles;
- layout choice.

Prefer a very small initial set.

---

## O-007 — Review finding severity/presentation

Review categories are settled.

A future implementation decision remains on whether findings need explicit severities such as error/warning/info, or whether category + explanation is sufficient initially.

Do not add severity just because conventional tooling uses it.

---

## O-008 — Curated-view metadata format

V1 curated views are frozen snapshots.

The implementation should preserve enough metadata to support future Compare/Update behavior.

The exact metadata representation should be decided during technical design, while avoiding model semantics in Canvas-only metadata.

---

## O-009 — Folder navigation ruleset reconciliation

Current Ruleset 1.21 requires a Canvas in every model-facing folder.

The newer Workbench direction and recent vault decisions move toward generated views and reduced folder scaffolding.

This requires a separate methodology decision.

It should not be resolved inside Workbench implementation.

## Explicitly not an open Workbench decision

The paused question about schema property inheritance is **not** on this list.

It belongs to model/schema governance if revisited.
