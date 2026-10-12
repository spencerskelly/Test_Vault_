# Test_Vault_ Single-Authority Consolidation — Execution and Handoff

**Date:** 2026-10-12
**Status:** PROPOSED (branch; not governing until reviewed/merged)
**Repository:** `spencerskelly/Test_Vault_`
**Scope:** Consolidate MDSE methodology, importer, runtime, queries, validators and release workflow into this repository. Eliminate mandatory use of `MDSE_Workbench` or any other repository to modify, validate, build, recover or continue this work.

## Work protocol

- One numbered task per user `y`, no more than five minutes of bounded effort. If a task is larger, repeat its ID with a numbered batch.
- Read this file and the last checkpoint before acting. Write results into this repository on a feature branch and use PR review for governance changes.
- Record each pass: ID; status PASS/BLOCKED/PARTIAL; source commit; changed paths; verification; next step; blockers.
- Never rely on uncommitted chat/container content. Do not equate a written plan with completed implementation.
- No unreviewed semantic schema changes, no direct main mutation, no deleting historical code before replacement tests pass.
- Independent tools may exist as optional exports, but no required source, definition, validation or generated artifact may live outside Test_Vault_.
- Existing `MDSE_Workbench` behavior is reference evidence only; functionality necessary for user workflows must be reimplemented or vendored with auditable licensing and in-repo tests. Do not promise Workbench feature parity unnecessarily.

## Ordered tasks (each <=5 minutes)

### Phase 1: Authority (01–06)
- [x] **01 — Inventory current authority boundary.** Read current-state registry, tool definitions, Ruleset, decision log and BOM plan. Document verified contradictions and external requirements below.
- [ ] **02 — Draft authority decision.** Formally propose Test_Vault_ as the only authoritative work repository and define approved exception rules; avoid changing schemas yet.
- [ ] **03 — Consolidate checkpoint entry point.** Link this plan from the Current State registry and add an exact resume procedure.
- [ ] **04 — Search broken/external authority references.** Search scoped documentation and scripts for MDSE_Workbench, cross-repo pins and external paths; record path-level remediation matrix (one bounded batch).
- [ ] **05 — Specify minimal replacement features.** Define essential Where Used, query, authoring, validation and release functionality; separate optional GUI features.
- [ ] **06 — Verify continuity.** Simulate a fresh-chat recovery using only committed Test_Vault_ files and list missing inputs.

### Phase 2: Self-contained operations (07–13)
- [ ] **07 — Inventory importer.** List active importer entrypoints, mapping schemas and external dependencies with versions.
- [ ] **08 — Inventory schema/template generation.** Find generators, checked-in artifacts, source/derived ownership and version compatibility.
- [ ] **09 — Inventory validators/build.** Check release checker, test entrypoints and reproducible install procedure.
- [ ] **10 — Audit Workbench dependencies.** Find compile/runtime imports, release pins and expected integration checks (bounded search).
- [ ] **11 — Implement first replacement query fixture.** Headless Local Model Where Used over parent-owned parts; no child inverse.
- [ ] **12 — Replace one mandatory external dependency.** Make one workflow local; record old/new invocation and tests (repeat).
- [ ] **13 — Standalone smoke test.** Validate a small fixture with only Test_Vault_ instructions/code; report real missing dependencies.

### Phase 3: Stable baseline (14–19)
- [ ] **14 — Reconcile decisions.** Find latest W decision and any pending semantic conflicts, including folder taxonomy and importer changes.
- [ ] **15 — Record version lock.** Freeze intended schemas/Local Model release versions in a reproducible manifest.
- [ ] **16 — Verify identities/links.** Test UID/ID, definition links, occurrence IDs and optional relationships on a small fixture.
- [ ] **17 — Run importer regression slice.** Classify a small EA fixture and compare evidence to expected outputs.
- [ ] **18 — Verify controlled vault build.** Build and validate one small self-contained candidate.
- [ ] **19 — Freeze baseline checkpoint.** Exact commit, checksums, test report, known limitations, next-priority list.

### Phase 4: Improvements (20–25)
- [ ] **20 — Importer correction backlog.** Reconcile known placement/linking corrections against live mapping authority; prioritize.
- [ ] **21 — Class/placement fix.** Correct one EA→MDSE mapping or folder issue with test (repeat).
- [ ] **22 — Relationship/interface fix.** Implement one verified correction including exposes/internal Connection behavior (repeat).
- [ ] **23 — Local Model/BOM semantics.** Govern quantities, UOM, multiplicity, single parent-owned occurrences and derived Where Used (bounded changes).
- [ ] **24 — BOM/variant integration.** Adapt BOM plan to this repository; variantOf is not subtypeOf; verify on fixture.
- [ ] **25 — Acceptance/release.** Run standalone validation, report open gates and issue release candidate only if evidence passes.

## Existing BOM plan preservation

The attached `BOM_MDSE_Vault_Implementation_Plan.md` dated 2026-10-08 specifies A–H work units, source ledgers, stable part IDs, variantOf, quantity/UOM, active graph/retirement and ZIP acceptance gates. It is **input evidence, not replaced by this consolidation plan**. Before task 23, bring its full authoritative copy into Test_Vault_ with verified source hashes and revise its Workbench-only tasks (A-14 to A-17; F-01 to F-10; H-06) into in-repository alternatives. The earlier plan says S1 `AllBOMsProduction.xlsx` and S2 `Ampure_all_BoMs.xlsx`; confirm S1 availability before normalizing BOMs.

## Step 01 — Evidence and outcome (PASS: audit only)

Live inspected on 2026-10-12 using GitHub's main branch; most recent returned commit: `19f565859e4b9fb7ae63004f1b6f0a7de1b9144e` (2026-10-05; no claim this is an exhaustive branch audit).

- `00_Workspace/00 - Current State.md`: verified 2026-10-05; release target 0.8.0 pre-release. Schemas relationships 1.35, element-types 1.17, Local Model 0.2; Workbench 0.1.16 pinned; Workbench 0.1.17 development reportedly through WB-126. This file points Workbench implementation and definition outside the repository.
- `00_Workspace/MDSE Tool Definitions and Boundaries.md`: explicitly states all tools except Workbench are in Test_Vault_; places Workbench source/tests/build and product definitions in `spencerskelly/MDSE_Workbench`. This violates the new single-authority target.
- `00_Workspace/Workspace Decision Log.md`: starts with W-01; states Test_Vault_ is methodology/translator workspace rather than a delivered engineering vault; W-07 permits direct main changes historically. New policy must distinguish historical records from future governance and avoid rewriting history.
- `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`: authoritative model meaning; distinctions between classification, generalization, physical folder placement, note/local occurrence and relationship semantics must survive consolidation.
- BOM plan (2026-10-08, supplied project attachment): calls for Workbench-dependent A-14/A-15/A-16, F-series and H-06; must be re-scoped rather than abandoned. Plan is not yet proven committed to Test_Vault_.
- **Important:** This audit verifies document-level authority conflicts, **not yet** an exhaustive source-code dependency scan, standalone runtime, or current PR/branch state. Those are separate tasks.

### Disposition
PASS: current authoritative boundaries captured without modifying existing semantics or claiming tool independence already exists.

### Handoff
`STEP: 01 | STATUS: PASS | SOURCE: main 19f565859e4b9fb7ae63004f1b6f0a7de1b9144e (reported latest) | OUTPUT: this file on consolidation branch | CHECK: source files read; conflicting authority links identified | NEXT: 02 | OPEN: full dependency inventory, approval/merge of proposed authority, BOM source S1 availability`

## Rule for restarting chats

“Open `00_Workspace/Test Vault Single Authority - Execution Plan.md` in `spencerskelly/Test_Vault_`. Use its latest checked completion and branch/PR state. Complete only the first incomplete task in <=5 minutes, commit/checkpoint evidence, then ask me to reply y. Do not use MDSE_Workbench or any other repository as an authority.”
