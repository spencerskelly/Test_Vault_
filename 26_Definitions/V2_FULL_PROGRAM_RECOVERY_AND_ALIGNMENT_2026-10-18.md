# V2 Full-Program Recovery and Architecture Alignment — 2026-10-18

Status: working integration index and questions for approval; not a release, semantic decision change, or certification of complete recovery.

## Objective and boundary
Deliver an independent SysML v2-first MDSE product suite, including Base Vault, Bootstrap/updater, EA translator, BOM translator, Workbench, validation, CI/release, GitHub workflow, and long-lived documentation. Preserve approved work from V1 as **values and tested concepts**, not executable V1 dependencies or user-facing V1 references. Separate formal native syntax from MDSE extensions and evidence. Keep raw QEAX/BOM and row-level model data local.

## Recovered authorities (consult before new work)
1. `26_Definitions/APPROVED_V2_TRANSLATION_BASELINE_AND_TEST_HANDOFF_2026-10-18.md` — consolidated v2 semantic authority, note format, ownership, test path.
2. `24_Workbench/docs/GOLDEN_IMPORT_*_2026-10-17.md` — element/relationship mapping approvals, all 2,267 aggregation dispositions, usage names, distinct repeated usages and exceptions.
3. `24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md` — 26 relationship families / 14,688 connector review coverage.
4. `29_SysMLv2_Translator_Workbench/Passes/` and `25_Testing/phase9_*` — preflight, canonical graph, ledger, direction, normalization and review gates.
5. `24_Workbench/registry/` — candidate registries, decision register, schema pins, runtime eligibility.
6. `24_Workbench/docs/SYSML_V2_BUILD_READINESS_STABILITY_UX_GATE_2026-10-17.md` — cross-subsystem contracts and release gates.
7. `24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md` — source ledger, staged writes, no silent drops and reimport requirements.
8. `29_SysMLv2_Translator_Workbench/FIRST_RUN_FAST_TRACK_DEPENDENCY_RULES_DOC_AUDIT_2026-10-17.md` — release chain, offline HTML, parser and disposable vault fast track.
9. `24_Workbench/docs/BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md` — BOM quantities, identity, variants, alternates and EA/BOM matching.
10. `26_Definitions/SysML Source Ownership and Note Storage.md` — provenance for text ownership; its illustrative mid-note format is superseded by bottom `## SysML v2` section.
11. `20_Base Vault/`, `21_Importer/`, `23_Bootstrap/`, `24_Workbench/`, `25_Testing/`, `26_Definitions/`, `29_SysMLv2_Translator_Workbench/` — intended active product/workspace layout.
12. `100_Archive/V1/` — historical implementation reference only. `55_Workspace/`, `66_Cross-Vault/`, `88_Reference/`, `99_System/` retain cross-cutting decisions and future program context.

## Product surface inventory and recovery state

| Product/workstream | Reusable existing evidence | Not yet demonstrated end-to-end |
|---|---|---|
| Base Vault | independent test base builder; approved note envelope; Obsidian/plugin settings history | fully locked, distributable, repeatably updated v2 base and fresh-client acceptance |
| Bootstrap and team updates | prior plugin lock, configuration and release governance | versioned v2 upgrade/migration flow, rollback, compatibility and rollout UX |
| EA source adapter | read-only QEAX preflight, Phase 8 full ledger reconciliation, evidence tools, conversion approvals | canonical-to-native text generation and validated note output for real scoped import |
| BOM adapter | A01–A14 prior work and October 17 integration analysis | approved quantity/UOM schema, source effectivity and real assembly acceptance |
| Shared semantic core | typed graph, 60 element families, 26 relationship families, approval register | single executable mapping contract aligned to all later approved rules |
| Native SysML | parser smoke tests and pinned fixture workflows previously reported | parser-tested generated model scope, ownership/name/namespace correctness and full relation conformance |
| Workbench | read-only v2 prototype and prior note-first interaction decisions | shipping Obsidian plugin, synchronized structural/visual/text editing and guarded transactions |
| Git/GitHub governance | V1 review/PR workflow, v2 source boundary and CI | v2 change publishing, release policy, user permission and conflict workflow |
| Cross-vault | resolver history and deferred capability requirements | v2-link contract, stability and lifecycle across repositories |
| Tests and deployment | synthetic regression, ledger checks, CI wiring, historic pilot parser run | independently verified current CI, real-import acceptance, platform coverage and packaged release |
| Documentation | numerous approved records and history preserved in repo | one indexed, status-labelled authority map and generated implementation traceability register |

## Architectural decisions already approved — do not reask
- Native SysML v2 is formal semantic authority; no custom native relations.
- One reusable definition note, usages in owner notes; preserve distinct occurrences.
- Final governed `## SysML v2` region is text authority; free Markdown and metadata are preserved.
- YAML holds stable IDs, provenance and explicit review flags; not an independent semantic graph.
- EA folder/package alone does not imply SysML containment.
- Proxy/full/binding port distinctions remain separate.
- All source rows receive exclusive auditable dispositions; unknown semantics remain visible.
- EA and BOM source records initially retain separate identity and never automatically merge by same-looking names.
- No raw fixture/real model rows in public repository; staged offline imports with preview and rollback.
- Native parser acceptance and human GUI checks are separate gates.

## Strategic gaps requiring resolution
G1. **Scope and release boundary**: what constitutes first shippable v2—view-only validated EA import or editable team platform; optional BOM and cross-vault at first release?
G2. **Canonical edit authority**: how edits in Markdown text, Workbench and external SysML tooling reconcile, including parse failure and concurrent changes.
G3. **Configuration upgrade authority**: centrally pinned managed plugin settings vs per-user customizations, migration opt-out, non-destructive revert.
G4. **EA/BOM semantic identity**: operator merge approval, occurrence equivalence, provenance and surviving UID.
G5. **MDSE extension schema**: namespace `flagLink`, variantOf, units/effectivity, results and source-specific metadata; separate proposed from approved.
G6. **Importer acceptance policy**: allowed deferred/flagged counts for first viewing vs golden acceptance; no conflation with native certification.
G7. **Workbench interaction scope**: minimum v2 release gestures, text editing, structure/diagram edits, save/undo, validation and notes merge.
G8. **Git publishing model**: main vs PR branches, single approver or two, local offline editing behavior and config updates across mixed Windows/macOS.
G9. **Support and release matrix**: tested Obsidian, Python/browser, Node, macOS Big Sur and Windows; offline packaging and update cadence.
G10. **System-of-systems modeling coverage**: exact Workbench views for units, ports, interfaces, behavior, state, causation, verification, requirements, analysis/trade studies and configurations.
G11. **Coverage evidence**: complete crosswalk of approved rule → registry → executable → tests → parser → Workbench, including source-row proof; no claim of exhaustiveness before audit.
G12. **Historic assets transfer**: reproducibly inventory and classify valuable V1 archives, old release assets, conversation decisions, branches and external repos; copying approved values only.

## Implementation strategy after alignment
Phase 0: recover/index authorities and assets; freeze decision statuses and provenance.
Phase 1: executable traceability/CI baseline; check source graph and parser pins.
Phase 2: canonical core, namespaces, source adapters and approved semantic operations.
Phase 3: scoped real EA importer → deterministic native serializer → note writer → fresh base → parser validation.
Phase 4: BOM independent adapter, extension schema and cross-source review matching.
Phase 5: Workbench reader/editor/diagrams, provenance, review actions, transactions.
Phase 6: Bootstrap, reproducible base/plugins/config management and team updater.
Phase 7: deterministic reimport, Git/PR publishing, rollback, cross-vault and release hardening.
Each phase has synthetic, real-source-local, parser, UI and release acceptance as applicable. Do not rerun mapping debates unless a genuine new gap appears.

## Questions for user (architecture-level only)
Q1. First milestone: validated view-only golden EA import, or full multi-user editable v2 platform? Can BOM be a separately gated second milestone?
Q2. Is the bottom SysML source block unequivocally the sole model authority on write, with Workbench and visual views always performing parsed AST transactions against it?
Q3. Must team plugin/config updates be centrally enforced, centrally recommended with opt-out, or hybrid by setting class?
Q4. At first release should cross-vault resolution be required or intentionally follow after a single-vault golden import?
Q5. What is the minimum acceptable release device matrix: Windows plus macOS Big Sur, and does first release require installation-free offline importer for both?
Q6. For approvals and merge actions: keep main as approved, all AI/user changes through PR by default, with one or two approvers?

## Maintenance contract
This document is an index, not a copy of every prior artifact. Canonical decisions stay in their owning files, indexed with stable references; implementation completion requires a separately generated crosswalk and tests. Mark each claim as approved, implemented, tested synthetic, tested actual data, parser accepted, GUI accepted or released. Never upgrade a status by implication.
