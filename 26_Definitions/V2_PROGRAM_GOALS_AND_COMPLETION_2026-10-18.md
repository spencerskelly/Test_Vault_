# MDSE v2 — Program Goals, Work Breakdown and Readiness

Status: planning baseline (2026-10-18). **Percentages are conservative planning estimates, not measured test pass rates or release acceptance.** Reassess after executable and CI verification. Related home: [V2 Program Navigation](V2_PROGRAM_HOME.md).

## Status method
Each goal is scored by five evidence gates: (A) approved scope/rules (20%), (B) executable integration (30%), (C) automated/synthetic tests (20%), (D) actual fixture and parser/GUI verification (20%), (E) versioned release/documentation (10%). Partial gate scores are judgmental and not validation claims. For later features, design work scores but postponed runtime does not. No goal is complete until acceptance criteria are met.

| Goal | Objective | Planned completion | First release? | Main remaining deliverable |
|---|---|---:|---|---|
| G01 | Product governance, decisions and recovery | 55% | Yes | Exhaustive decision→code→test authority crosswalk |
| G02 | Native SysML v2 definition/relationship catalog | 45% | Yes | Complete versioned normative definitions and approved-rule resolver |
| G03 | Common canonical graph, UID and provenance | 35% | Yes | Integrated authoritative source/usage identity contract |
| G04 | EA/QEAX translator and semantic reconciliation | 40% | Yes | Scoped real-source native generation and ledger replay |
| G05 | Native parser, serialization and note writer | 25% | Yes | Parser-validated output in bottom SysML v2 note section |
| G06 | Base Vault and local first-run packaging | 30% | Yes | Reproducible plugin-locked disposable vault acceptance |
| G07 | Read-only v2 Workbench | 25% | Yes | Browser/Obsidian model inspection, where-used and source diagnostics |
| G08 | Validation, CI and golden-import acceptance | 35% | Yes | Verified current CI, parser output, model/UI acceptance |
| G09 | Transactional editing, reimport and merge | 15% | Later | AST edit/save/undo/conflict and reimport transaction |
| G10 | BOM importer and EA/BOM reconciliation | 25% | Later | Approved units/effectivity schema and validated assembly import |
| G11 | Bootstrap/team updates and Git publication | 20% | Later | Hybrid managed configuration, migration and rollback |
| G12 | Cross-vault, distribution and support lifecycle | 15% | Later | Resolver contract then tested releases on mixed platforms |

**Indicative average:** 30% across 12 goals (unweighted; not a release percentage). The first-release subset G01–G08 averages approximately 36%. None is certified complete.

## Goal tasks and acceptance evidence

### G01 — Governance, decisions and recovery (55%)
- Link all approvals from October 12–18 and older project work; record supersession and provenance without reopening approved semantics.
- Link the 60 element families and 26 connector families to approved rule, runtime selector, test, parser, UI and status.
- Separate approved, proposed, implemented, synthetic-tested, real-source-tested, parser-accepted, GUI-accepted and released statuses.
- **Done when:** every active rule has a unique canonical home; links and ownership tests pass; no contradictory active definitions.

### G02 — SysML v2 relationship and definition catalog (45%)
- Reuse October 17 central relationship reference, shared eligibility operations and dedicated approved mappings.
- Complete individually traceable definitions for Binding, ports/conjugation, requirement constructs, constraints, calculations, attributes/quantities and other already-approved concepts.
- Record semantics, legal endpoint and owner context, source orientation, native construct, examples, validation, visualization, reference help, provenance.
- **Done when:** all approved mappings have a discoverable definition and machine-readable rule; official parser fixtures and help-panel parity are checked.

### G03 — Canonical semantics, identity, and provenance (35%)
- Reuse typed graph and Phase 8/9 source trust checks; preserve definition vs usage; never infer ownership from folder hierarchy.
- Define UID/usage IDs, namespace ownership, EA and BOM independent identities, stable symbol and where-used indexes.
- Build provenance and extension/flagLink storage separate from native text and three-way merge evidence.
- **Done when:** deterministic graph, identity collision/round-trip tests and traceable multi-source lineage pass.

### G04 — EA importer and ledger (40%)
- Reuse QEAX preflight, 60+26 mapping approvals, Phase 8 all-row reconciliation and Phase 9 orientation tests.
- Implement approved-family precedence, exact source patterns, cases needing review, separate connector instances and missing multiplicity.
- Generate private ledger with one disposition for each source row and no silent drops.
- **Done when:** selected real QEAX slice consistently produces validated model candidates and reconciled diagnostics; full reduced model auditable.

### G05 — Native text, parser and note writer (25%)
- Produce valid SysML v2 definitions and usages under correct owner/namespace, preserve source evidence and flags in governed YAML.
- Write one definition note, context-owned usages and final `## SysML v2` fenced block; preserve free Markdown.
- Independently parser-validate generated native text with pinned library/parser and negative fixtures.
- **Done when:** generated source parses, notes round-trip, and a no-op rerun yields no semantic diff.

### G06 — Base Vault and packaging (30%)
- Keep independent v2 base builder and approved vault folders, Obsidian plugin versions, configuration lock, fixtures and user preferences.
- Rehearse offline fresh base, first open, no accidental production writes, Windows and macOS Big Sur acceptance.
- **Done when:** repeatable archive can be installed into a fresh disposable vault with validated content and settings.

### G07 — Read-only Workbench (25%)
- Use existing v2 prototype and approved note-first, structural/visual, definition/usage and help panel contracts.
- Implement inspector for model/ports/relationships, source provenance, deferrals, where-used, typed view and navigation.
- Show consistent projections from native text; do not expose accidental write pathways.
- **Done when:** a real generated model can be inspected in target runtime with passing UI scenarios.

### G08 — Testing, CI and acceptance (35%)
- Run existing synthetic suites, full source ledger checks, parser attestation and isolated base QA at pinned commit.
- Repair outdated CI invocation/path/pin failures; establish reports with separate source, semantic, parser, GUI and release verdicts.
- **Done when:** CI and local real-source acceptance have witnessed, reproducible passing evidence and no hidden skips.

### G09 — Editing/reimport (15%; later)
- AST-aware transactional Workbench edits of the authoritative SysML text, staged preview, parser validation, undo and Git diff.
- Incremental import with three-way conflict handling; Merge Notes review; atomic save, redirects and rollback.
- **Done when:** source-vault-UI concurrent edits round-trip safely with deterministic conflict outcomes.

### G10 — BOM integration (25%; later)
- Recover A01–A14 decisions and October 17 cross-source plan without adopting unapproved proposals.
- One numbered-part definition; parent-owned usages, multiplicity distinct from exact quantity and units, revision/effectivity, alternates.
- Independent source identities with human-approved EA/BOM equivalence.
- **Done when:** real assembly import passes effective-BOM, where-used and parser/round-trip tests.

### G11 — Bootstrap/team operations (20%; later)
- Govern core plugin/schema versions centrally; preserve personal preferences by field-ownership class.
- Implement update diff, version gate, schema migration, rollback, PR approval and user-friendly release mechanism.
- **Done when:** mixed-user upgrade and rollback tests work without overwriting personal configuration.

### G12 — Cross-vault and distribution lifecycle (15%; later)
- Define stable link/resolver contracts now, ship cross-vault support after single-vault golden acceptance.
- Establish platform matrix, offline policies, support and lifecycle of tool modules and documentation.
- **Done when:** interoperability, upgrade and deployment acceptance complete.

## Priority order
1. Finish canonical decisions/index/links and automatically validate existing files (G01/G02).
2. Verify current executable entrypoints and CI, pin parser/source/registry baseline (G03/G08).
3. Wire a small approved EA slice into native serializer, note writer, disposable vault and read-only Workbench (G04–G07).
4. Scale coverage, support/rollback; then proceed with later-phase features (G09–G12).

## Source of truth and update rule
Approved semantic decisions live in their specific documents, not in this rollup. This file owns high-level goals and estimates. `v2_mapping_family_recovery.v0.1.json` owns the family recovery list; `v2_executable_candidate_crosswalk.v0.1.json` identifies provisional selector coverage only. Update the status table **after** attaching actual acceptance evidence. A passing synthetic test may not automatically increment a parser/GUI/release gate.
