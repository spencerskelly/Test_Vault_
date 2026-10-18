# STEP-02A — EA Diagram Deferral and Golden Import Scope

Date: 2026-10-18. Status: **USER APPROVED**. This decision supersedes EA-diagram tasks in prior plans until completion of the entire toolset, its testing, and acceptance of the golden import.

[Master MOC](../MOC_MDSE_V2.md) · [STEP-02 plan](V2_NEXT_STEP_TITLES_2026-10-18.md) · [Latest approved model handling](STEP_00_APPROVED_MODEL_HANDLING_CLARIFICATIONS_2026-10-18.md)

## Scope lock

**All EA diagram import, extraction, interpretation, translation, preview, Canvas seeding, diagram-provenance processing, and EA-diagram-specific validation are deferred.** This includes the Sparx QEAX diagram tables `t_diagram`, `t_diagramobjects`, `t_diagramlinks`; EA diagram metadata/position/layout; diagram-driven actors, messages, sequence ordering and fragment interpretation; diagram-specific tool UI, test acceptance and output packaging.

**Still in scope:** original EA **elements, connectors, packages for folder structure, tags and other non-diagram source evidence**, including `Sequence` or `Message` semantic elements/connectors *if explicitly present in non-diagram source tables*. Translate only semantics supported by that evidence; never infer behavior, ordering, membership, ports or requirements from EA diagram placement.

**Still in scope:** native SysML v2 text, definitions/usages, non-diagram behavior and requirement semantics, a read-only Obsidian Workbench, **native model-derived structural/visual views**, and standard Obsidian note browsing. An EA diagram import is a different capability from displaying an already parsed native model. Native model-derived Workbench views must not require or consume EA diagram rows. Legacy `.canvas` documentation is left as historical reference, not activated by the importer.

## Enforced stage boundary

Do not enable EA diagram work during mapping closure, canonical graph and source adapter integration, native serialization, test-base packaging, read-only Workbench, golden import tests, or subsequent tool completion and validation. **Revisit only after both (1) the golden import is explicitly accepted and (2) all planned tools and their relevant tests are complete, followed by separate user approval of a diagram phase.** Mere CI success or a prototype is not authorization.

The active first-release QEAX profile must verify non-diagram tables only. Input files may contain diagrams as untouched source material, but tools must neither query them nor report their rows, compare counts, stage diagram assets, emit Canvas based on EA diagrams, or require diagram-profile drift checks. Existing diagram-bearing source profiles and legacy scripts are historical; they are not permitted in the v2 critical execution path.

## Cross-tool impact and repair

| Tool/area | Required scope |
|---|---|
| `21_Importer` | No `t_diagram*` queries or assumptions; Source profile checks element/connector/package counts only; no EA diagram reading or output |
| `24_Workbench/registry/runtime` | Eligibility derives from direct typed elements/connectors, never source diagram positions; no EA diagram adapters |
| `20_Base Vault` / `23_Bootstrap` | Do not package EA diagram artifacts, diagram-import plugins or EA-diagram dependencies |
| `24_Workbench` | May show native SysML-generated views; do not import, inspect or replay EA diagrams |
| `25_Testing` and CI | Golden tests neither expect nor query diagram rows; synthetic negative checks ensure diagram tables can be absent |
| BOM / future reimport | No inferred EA diagram relationships; update stable semantic identities using source elements/connectors |
| historical workflows | Keep earlier EA diagram and Canvas implementation plans discoverable in MOC, marked `DEFERRED_EA_DIAGRAM`; never infer they are current release requirements |

## Explicit sequence adjustment

The [workflow note and Canvas contract](../24_Workbench/docs/SYSML_V2_WORKFLOW_LOCAL_CANVAS_SEQUENCE_DECISION.md) remains an approved **future EA-diagram source adapter and view-creation design**, not a current EA diagram deliverable. Within the golden import, a Sequence element/connector may be dispositioned only from explicit non-diagram evidence; unresolved semantics stay flagged. Do not count visually represented message order as model evidence or promise diagram fidelity before the deferred phase. Future first EA diagram import should demonstrate native Message/Succession syntax, workflow ownership and preserved view meaning after the toolchain is accepted.

## Acceptance and reopening trigger

- Strict preflight succeeds on a synthetic QEAX with **no diagram tables** and fails for actual element/connector/package drift.
- Static regression detects any added active EA diagram-table read or active diagram-profile dependency.
- All translated semantics and source-row disposition counts are based only on permitted source tables; no native relation depends on an EA diagram ID.
- Tool packages and the golden import contain no extracted EA diagram assets.
- Future diagram work requires its own separate titled plan, source scope, native-versus-view-only decisions, tests and explicit approval.

This scope lock does **not** delete, rewrite or shrink the original QEAX. The user retains source data externally; after golden acceptance the diagram phase can read it under a new authorized plan.


## Existing legacy profile gate identified

The older `25_Testing/gate_v2_qeax_reconciliation.py` / `run_gated_phase8.py` pathway still refers to historical `profile_qeax_local`, `check_qeax_source_profile` and `reconcile_qeax_dispositions` implementations that are not active V2 dependencies in this checkout. Historical profile tests refer to diagram totals. **This pathway is not approved for the current golden import.** Before reconnecting it, replace its source profiler with the diagram-free V2 preflight/schema contract and prove it never touches diagram tables. No reason to reconstruct diagram support to repair the Phase 8 pipeline.

Older V1 branch-specific or historical GitHub workflows and `99_System` diagram schemas remain retained as historical assets, not runtime dependencies for V2. Their existence does not override the current no-diagram scope gate.
