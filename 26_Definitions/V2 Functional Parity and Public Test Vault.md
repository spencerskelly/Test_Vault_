# V2 functional parity and public test vault contract

Status: implementation plan; v1 preserved intact. Initial review 2026-10-16.

## Goal

Deliver an installable, **synthetic-only**, public Obsidian vault in which the v2 Workbench and Canvas are alternate views over the same SysML v2 textual authority. Avoid requiring complete vault recreation for ordinary edits. Do not copy or publish imported EA model data, proprietary product names, BOMs, drawings, customers, revision histories, or source exports.

## v1 functionality is the baseline, not the v2 serialization

Carry forward (and inspect the actual v1 implementation before declaring parity):
1. Bootstrap/first-open setup, schema/release compatibility, plugin deployment, health and repair.
2. Workbench: element creation, rename/move/delete with backlink integrity; browsing, filtering and searching; property and relationship editing; Local Model occurrence/context awareness; internal structure; schema-driven UI.
3. Views: note, hierarchy/text explorer, Canvas visualization, relationship navigation, where-used, orphan/health and review queues.
4. Importer: EA acquisition and shared normalized source evidence, mapping, deterministic identity, stage previews, duplicate handling, conflicts/review, issue reporting, transaction safety and resume.
5. Test/release: fixture coverage, regressions, migration tests, repeatable packaging, rollback and changelog.
6. Export: controlled SysML source, Markdown vault, linked model tables, Excel (BOM / interfaces / requirements / where-used / mapping), and eventually product-definition document packages.

For each function, record: v1 entry point, v2 equivalent, shared vs replaced logic, minimum acceptance, and gap. A baseline claim requires comparing actual code/tests, not this checklist alone.

## Authority and changes

- Authoritative model: OMG SysML v2 textual source for formal structural/behavioral elements and relationships. Markdown note metadata retains identity, human descriptions, evidence and workflow.
- Derived: Obsidian links, Canvas JSON, indexes, query materializations, Excel exports, HTML previews. Derived state is rebuildable, not a competing source of truth.
- Stable identity: MDSE UID + optional EA GUID provenance; **rename/path changes must not change identity**.
- Change tracking: inspect changed file/content hashes, track directly affected model owners/dependents, compute a deterministic change plan.
- Transaction: stage proposed edits and projections, validate syntactic/schema consistency and references, report conflicts; then apply only changed output files, retaining unrelated notes and local human-authored content.
- Deletion: explicit tombstone/review for imported deletions; never silently erase manually edited notes or unmodeled attachments.
- Reconciliation: unchanged inputs produce zero edits; repeated incremental runs are idempotent; full rebuild is optional recovery/verification, not a normal edit path.
- Review and Git: main is approved; updates staged for diff/PR approval; never automatically overwrite another contributor's work.
- Model ownership: parent/context owns part usages and connections; reusable definitions retain own notes; cross-note views are projections.
- Maintain an undo manifest including pre-change hashes and original bytes/versions for changed files.

## Public test-fixture boundaries

Synthetic fixtures must cover every defined element and relationship kind, **including** invalid edge cases:
- Structure: package, definition, typed usage, assembly, part, item, multiplicity, specialization, redefinition, reference, variant candidate, configuration and effectivity.
- Interfaces: port definition/usage, connection, interface definition/usage, flow, binding, nested context, proxy/exposed port.
- Behavior: action/function, activity, state, transition, sequence, event, control and item flows.
- Intent: requirements, constraints, verification cases, verification results, allocations, satisfy/verify/trace/refine and coverage.
- Organization/evidence: actors, stakeholders, use cases, concerns, issues/risks, documents, decisions, rationale, tests, changes, provenance.
- Import nuances: duplicate names, name/alias collisions, illegal filename characters, missing targets, unresolved stereotypes, cross-package references, ordering, moved nodes, renamed elements, deleted sources, cycles, duplicates and legacy mapping exceptions.
- BOM: parent-owned usages, quantities and UOM, multiplicity, revisions, alternates (BOM-ALT-001), approved equivalents, lifecycle, effectivity, nested where-used without adding parent data to part notes.
- Non-happy paths: damaged source, partial update, stale hashes, conflicts, interrupted update, new user fields, unrelated attachment preservation.

These are **coverage targets**, not a claim that all are implemented or have direct SysML syntax equivalents. Approved MDSE semantic differences require explicit mapping decisions.

## Safe fictitious demonstrator

Use an imaginary modular research instrument, e.g., `Sample Instrument`, with invented components `Control Unit`, `Sensor Unit`, `Power Unit`, `Operator Panel`, and generic interfaces. No names, ratings, product topology, bill of material, firmware details or relationships from real company models. Use fabricated IDs, costs and revisions solely as test values, clearly marked synthetic.

## First usable deliverable / repo handoff

Create `20_Base Vault/Public Sample Vault/` with Obsidian-ready directory tree, v2 definitions/relationship coverage registry, a model note set and SysML files, read-only Workbench navigation, Canvas view, a manifest and install/readme. Add a small incremental-update demonstrator with dry-run/diff/apply semantics before declaring the vault ready for collaborative testing.

**Repo request gate**: ask the user to create a separate public test repository only when a versioned vault ZIP or reproducible folder is installed locally and passes first-open, navigation, non-destructive incremental-update and secret/IP scans. Until then, keep all sample work in this methodology repository. Repo should contain synthetic content only.

## Next milestones

1. Capture actual v1 function/integration inventory and trace each capability to a v2 backlog item.
2. Generate synthetic public vault skeleton and content, including comprehensive coverage matrix with supported/proposed/unmapped statuses.
3. Obsidian native view (or an explicitly documented interim embedded HTML pane) for sample-note context, text explorer and linked Canvas.
4. Transactional incremental patching of model files and derived views; test rename/move/add/delete, idempotence, conflicts, rollbacks.
5. Preview and export model tables; later implement Excel and controlled product-definition deliverables.
6. Import actual user CSV **only in a private/local environment**, and never commit source data or extracted model fragments to public GitHub.

## Safety / licensing

A public repo is accessible to anyone; a fictional fixture is the default. An automated sensitive-content scan is a useful backstop but not a guarantee. Do not make public any private dependencies, access tokens, proprietary schematics, customer references or user-supplied EA exports. Use local-only paths for real models.
