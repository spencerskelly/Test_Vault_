# Runtime Plugin Dependency Audit

**Status:** architecture working document for MDSE v0.8 pre-release.
**Purpose:** reduce startup/runtime surface over time without removing useful engineering capability prematurely.

## Governing rule

A plugin belongs in the controlled default stack only when it provides a capability that is still required for the standard MDSE experience and is not already provided more reliably by Obsidian core, Bootstrap, or Workbench.

This is **not** a removal list. The current controlled stack remains unchanged until a replacement path is proven in a disposable integration vault and the release process explicitly changes the baseline.

The stability goal is:

> Fewer independent runtime engines, fewer duplicate vault scans, and one semantic interpretation of the model.

## Evaluation criteria

Each plugin is reviewed against the same questions:

1. **Engineering value** — what user-visible MDSE capability would disappear if it were absent?
2. **Semantic role** — does it interpret MDSE meaning, or is it only presentation/convenience?
3. **Startup/runtime cost** — does it index/scan the vault, register broad file listeners, or perform other heavy startup work?
4. **Overlap** — is Workbench or Obsidian core already providing the same capability?
5. **Failure impact** — can the plugin fail without preventing engineers from reading/editing Markdown?
6. **Configuration burden** — does MDSE need to govern and verify plugin-specific settings?
7. **Replacement gate** — what must be proven before it could leave the default stack?

## Current stack

| Plugin | Current MDSE role | Architecture tier | Direction |
|---|---|---|---|
| `mdse-bootstrap` | Controlled release integrity, vault/author setup, runtime health of the controlled environment | **Core MDSE** | Keep small; no model indexing |
| `mdse-workbench` | Shared semantic model service, governed editing, navigation, views, Review | **Core MDSE** | Primary model runtime |
| `obsidian-git` | Current human-facing Git sync workflow | **Operational dependency** | Keep until the managed sync-agent path is proven |
| `templater-obsidian` | Current governed templates and Bootstrap author/Person creation path | **Operational dependency** | Keep until Workbench/Bootstrap can provide equivalent governed creation without it |
| `advanced-canvas` | Enhanced Canvas interaction/presentation for curated engineering views | **Presentation dependency** | Retain while it provides unique Canvas UX; never semantic authority |
| `nodian` | Existing typed-note/model navigation capability from the earlier MDSE architecture | **Under overlap review** | Measure remaining unique value now that Workbench owns the semantic index |
| `breadcrumbs` | Existing relationship navigation/bidirectional browsing | **Under overlap review** | Measure remaining unique value against Workbench Where Used/details/navigation |
| `fileclass` | Existing typed-property/class editing support | **Under overlap review** | Measure remaining unique value against the structured Workbench editor |
| `quickadd` | Convenience creation/actions | **Under overlap review** | Candidate to retire only after Workbench creation flows cover actual use |
| `table-exporter` | Convenience export | **Optional/convenience candidate** | Determine whether it belongs in the controlled default or a user-optional layer |

## Retired from controlled runtime

- **Dataview 0.5.68 — retired by W-370.** Dependency inventory found no Dataview queries in the current controlled vault, so no engineering workflow depended on it. Native Bases provide folder/property tables and Workbench provides schema-aware Explore/Details/Review/navigation for the modeled workflows in use. The Step 53 one-plugin-at-a-time integration benchmark measured Dataview at **+34.246 s** to Workbench core/occurrence readiness versus the bracketed Workbench-only baseline while preserving identical model counts. Because both the replacement/dependency gate and startup-benefit gate were satisfied, Dataview was removed from the controlled lock, enabled list and runtime payload. Reintroducing it would require a new demonstrated requirement and dependency-budget review.

## Runtime tiers

### Tier A — Core MDSE runtime

The default engineering model cannot provide the intended controlled MDSE experience without these:

- `mdse-bootstrap`
- `mdse-workbench`

These two components must remain architecturally narrow:

- Bootstrap protects the environment.
- Workbench owns model semantics.
- Neither should duplicate the other's work.

### Tier B — Current operational dependencies

These are still needed by the current workflow, but MDSE should not assume they are permanent architectural foundations:

- `obsidian-git`
- `templater-obsidian`

Their replacement gates are explicit and must be proven before removal.

### Tier C — Presentation / engineer-experience dependencies

These may remain valuable even if they are not semantic authority:

- `advanced-canvas`
- potentially selected navigation/property UX plugins after measurement

A presentation plugin may fail or be disabled without corrupting the model.

### Tier D — Optional convenience

Convenience features should not force every engineer's vault to carry permanent startup/indexing cost unless their value justifies it.

## Required evidence before changing the baseline

For every candidate removal or demotion:

1. identify every MDSE file/template/process that currently depends on it;
2. identify the replacement workflow;
3. test the replacement in `261002083` or another disposable integration vault;
4. compare startup/runtime behavior with and without the plugin;
5. verify macOS and Windows behavior where relevant;
6. update the Base Vault, plugin lock, enabled-plugin documentation and troubleshooting;
7. only then change the controlled stack.

Do **not** remove several overlapping plugins at once. Change one dependency at a time so regressions have a clear cause.

## Recommended measurement pass

Once the current Workbench/Bootstrap staged-start candidate is stable, capture:

- Obsidian startup time with the complete controlled stack;
- per-plugin startup timing from Obsidian's plugin debug/startup information where available;
- whether each plugin performs a whole-vault index/scan;
- memory after idle;
- functionality actually exercised by the current Base Vault.

The first likely candidates for investigation are plugins whose original MDSE purpose now overlaps directly with Workbench navigation, typed editing, or note creation. **No removal is approved by this document.**

## Long-term target

The preferred steady-state architecture is a small controlled core:

- Obsidian core;
- Bootstrap;
- Workbench;
- the minimum operational sync mechanism;
- only presentation/convenience plugins that still provide measurable engineering value.

Reducing the stack is an architectural optimization, not a goal by itself. A plugin stays when its unique user value exceeds its maintenance/startup cost.
