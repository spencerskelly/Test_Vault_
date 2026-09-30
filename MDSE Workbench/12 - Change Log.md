# Workbench Change Log

## Purpose

Keep a human-readable history of changes to the Workbench product definition.

Do not erase prior direction when decisions change.

## 2026-09-30 — Initial consolidated Workbench definition

### Added

Created the top-level `MDSE Workbench` workspace with:

- product definition;
- dashboard interface definition;
- consolidated decision log;
- V1 build outline;
- Canvas/view behavior;
- Review behavior;
- architecture/model boundary;
- roadmap and revision strategy;
- continuation handoff;
- open decisions;
- reference plugin findings;
- local folder Base.

### Key direction captured

- Workbench is an interface to the existing MDSE model.
- Primary home is task-oriented: Create / Explore / Review.
- V1 creation uses compact modal forms.
- V1 Explore uses selection-first element search and one-click standard views.
- Canvas is the first graphical view/edit surface, not the model authority.
- Model editing is explicit and temporary.
- Review is whole-vault by default and uses categorized queues plus focused resolution.
- V1 prioritizes useful working behavior over feature completeness.
- Architecture preserves paths to richer creation, drag-to-connect, property editing, curated-view sync, advanced discovery, and cross-vault operation.

### Scope correction recorded

The prior discussion had begun moving into schema mechanics, specifically property inheritance.

That line of discussion was explicitly paused so Workbench work could return to interface design.

### Known reconciliation item

MDSE Modeling Ruleset 1.21 still contains the older requirement for a Canvas in every model-facing folder.

The Workbench direction relies increasingly on generated views and recent vault direction reduced mandatory folder scaffolding.

This remains a separate methodology reconciliation item.

### Next open decision

Sequential Review navigation: manual selection vs Previous/Next vs batch behavior.

Current recommendation: Previous/Next, no broad batch editing in V1.

---

## Future entry format

### YYYY-MM-DD — Short title

**Changed**
- ...

**Reason**
- ...

**Affected decisions**
- D-...

**Migration/implementation impact**
- ...
