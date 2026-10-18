# V1 → V2 deep repository analysis and engineering platform architecture

Date: 2026-10-18
Status: verified source excerpts + manifest-path recovery; implementation gaps are hypotheses until independent test. This is **not** a native parser or v2 release attestation.

[Master MOC](../MOC_MDSE_V2.md) · [V1 archive MOC](../100_Archive/MOC_V1_ARCHIVE.md) · [Machine-readable reuse ledger](v1_to_v2_reuse_ledger.v0.1.json) · [Approved v2 release architecture](V2_RELEASE_ARCHITECTURE_DECISIONS_2026-10-18.md) · [Program goals](V2_PROGRAM_GOALS_AND_COMPLETION_2026-10-18.md)

## Executive technical finding

The last month's work is **not primarily missing definitions**. Significant v1 functionality and test methodology exists, and the October 17 v2 source-family policies have been approved. The central risks are (i) distributed authority, (ii) incomplete native text-to-Workbench integration, (iii) v2 provisional runtime logic that differs from newer approved policies, (iv) absent independent acceptance at full scale and (v) rollout/configuration governance. Building another parser, connector classifier or UI shell before closing these seams risks recreating work.

The repository migration manifest records 1,165 archived v1 files and 268 v2-relocated paths; these are **path counts only**, not a count of available features or complete current repository inventory. The 28-record reusable capability ledger references actual archived files and known v2 destinations, but every v2 behavior remains unverified until tested.

## Three independently grounded implementation conflicts

### DEF-01: Shared aggregations are rejected by current v2 eligibility
**Approved:** [October 17 shared/composite usage policy](../24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_SHARED_COMPOSITE_USAGE_APPROVED_2026-10-17.md) allows source EA shared flag `1` and composite flag `2` to become a valid owned native usage **if** typed parent/child semantic ownership has independent evidence. Not every shared aggregation is a valid containment.

**Implemented:** [eligibility-engine.mjs](../24_Workbench/registry/runtime/eligibility-engine.mjs) rejects rule `AGG-OWNED` unless `aggregationKind === 'composite'`. Its `AGGREGATION_UNPROVEN` diagnostic therefore blocks valid shared cases regardless of separately validated ownership.

**Remedy:** use a policy-versioned normalization predicate for evidence-backed owned usage, retain original shared/composite flag, and assert both positive and negative tests. Never remove the requirement for valid owner, endpoints or multiplicity.

### DEF-02: Approved unresolved untyped usages receive unconditional errors
**Approved:** [October 17 60-family reconciliation](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md) permits untyped `ActionUsage`, `PartUsage`, `PortUsage` with separate `UNRESOLVED_*_TYPE` diagnostics.

**Implemented:** [canonical-model.mjs](../24_Workbench/registry/runtime/canonical-model.mjs) emits `UNTYPED_USAGE` for any usage without `definitionId`. That is a valid reason for a diagnostic but not for silently replacing the approved rule with a universal invalidity decision.

**Remedy:** distinguish permitted unresolved usage (review diagnostic) from disallowed missing typing or ownership; add conditional fixtures per native kind and ensure serialization is parser legal.

### DEF-03: Candidate registry predates detailed approval
[Provisional element candidate rules](../24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json) differ from October 17 specific approvals (e.g., `InformationItem` candidate `ItemDefinition` vs approved descriptive MDSE-only note). The [element/relationship executable crosswalk](v2_executable_candidate_crosswalk.v0.1.json) reports only 2 exact element selectors, 26 wildcard and 32 uncovered families; all 26 relationship keys are present but candidate/deferred. Never promote this preliminary registry by updating its wording or silently mapping unmatched families generically.

**Remedy:** author a new, approved-version resolver based on [60 approved element families](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md) and [26 approved connector families](../24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md), with typed exceptions and regression tests. Keep prior pinned files for audit history.

### DEF-04: Canonical definition-kind list omits approved native kinds
[October 17 element-family mapping](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md) includes `UseCaseDefinition` and `OccurrenceDefinition` for approved source families. [canonical-model.mjs](../24_Workbench/registry/runtime/canonical-model.mjs) exports a `DEFINITION_KINDS` array without either. It also uses the set for identity/eligibility checks. This is **an identifiable registry coverage risk, not proof every use case/event is rejected**. Add positive/negative definition/usage tests and reconcile the closed-world type lists with approved native constructs before allowing full-source output.

## What was already engineered and must be leveraged

### A — EA importer maturity and large-model scale
[V1 real-source acceptance](../100_Archive/V1/11_Importer/Testing/v0.8.19/FULL_IMPORT_EXECUTION_STATUS.md) reports 35,969 source elements, 21,822 connectors, 27,709 engineering notes, 28,273 output files per deterministic rerun, 71,938 relationship values, and zero detected lost planner rows. It explicitly labels semantic review as pending. This is evidence of the historic importer's source handling and deterministic staging, **not native SysML v2 acceptance**. A real O(N²) path-planner defect was corrected and guarded with [scalability regression](../100_Archive/V1/11_Importer/Testing/v0.8.19/path_planning_scalability_regression_test.js).

The same report records 397 source documents, 376 approved linked documents, 390 attachment files written, 249 BindingConnector review cases and source-conveyed-flow review outcomes. These are important coverage **dimensions** for v2; reduced QEAX snapshot counts and mapping families alone miss them. First-release attachment scope needs acceptance criteria, not a hidden drop.

Reuse: source fingerprint, completeness ledger, path planning, stable names, transactional staging, deterministic rerun comparison, attachment provenance, release states and negative review fixtures. Retire: v1's custom YAML relationship model as native semantic authority.

### B — Workbench beyond a browser preview
The archived [Obsidian indexer](../100_Archive/V1/14_Workbench/src/obsidian/indexer.ts) implements chunking, change-burst suppression, deferred semantic cache, occurrence hydration and source-state reconciliation. [Reverse path dependency index](../100_Archive/V1/14_Workbench/src/core/relationship-dependencies.ts) supports targeted invalidation with a 10k-candidate fallback to full re-resolution; its comments reference representative 60k-note performance studies. [Transaction manager](../100_Archive/V1/14_Workbench/src/core/transaction.ts) has pure semantic transaction validation and undo/redo orchestration. [ModelRef identity contract](../100_Archive/V1/14_Workbench/WB106_IMPLEMENTATION_CONTRACT.md) distinguishes stable note and local occurrence identities. The archive also contains ~48 `src/core` modules and 50 test-area entries in the migration manifest.

The current [v2 Workbench HTML](../24_Workbench/v2-workbench.html) is a read-only local preview, **not an Obsidian integration with all those behaviors**. Reuse v1's indexer, responsive background work, stale-edit safety, navigation semantics and tests as specifications/algorithms. Rebuild parsing around authoritative v2 text and namespaced usage identities; **no runtime import of v1 code**.

### C — Team stability and release controls
[V1 plugin stack](../100_Archive/V1/10_Base%20Vault/Definition/Enabled%20Plugin%20Stack.md), [base release checker](../100_Archive/V1/10_Base%20Vault/Testing/check-release.py), and [Bootstrap core](../100_Archive/V1/13_Bootstrap/Tools/v0.3.1/src/core.ts) already specify plugin version/hash pinning, activation-only repair and per-user setting exclusions. Bootstrap explicitly does not silently download/replace plugin files or governed settings. [Author registration](../100_Archive/V1/13_Bootstrap/Definition/Author%20Registration%20Spec.md) includes persistent local author code and collision checks.

The current [standalone v2 test-base builder](../20_Base%20Vault/build_v2_test_base.py) deliberately outputs `native_import_ready:false` and `plugin_ready:false`; copying eight reference files is not a deployable Obsidian base. Reuse release-gate invariants while implementing the user-approved **hybrid** managed configuration contract: enforce core compatibility, preserve approved personal settings and support dry-run migration/rollback.

### D — BOM and authoring lifecycle
[Archived BOM plan](../100_Archive/V1/14_Workbench/docs/bom/a01-a14/BOM_MDSE_Vault_Implementation_Plan.md) and [reader](../100_Archive/V1/15_Testing/bom_xlsx_reader.py) provide detailed spreadsheet/source handling and partial implementation tests. The [October 17 V2 BOM crosswalk](../24_Workbench/docs/BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md) is the approved/proposed-status discriminator. Different EA/BOM source keys do **not** automatically identify the same part or usage; native multiplicity differs from quantity/UOM, and alternates should not inflate consumed quantities.

[Workbench definition migration service](../100_Archive/V1/14_Workbench/src/core/definition-note-migrate-service.ts) includes transactional multi-note work and precise YAML revisions. Its transaction semantics are reusable, but its YAML-centric model edit is **not** authoritative for V2 formal SysML. Later phase must edit parsed SysML text atomically and update derived indexes.

## Architecture to build: one model authority, multiple projections

```text
EA QEAX   BOM XLSX   authored SysML text    other evidence
    \        |                |                    /
       immutable source observations / source ledgers
                         |
      approved source-specific adapters + semantic eligibility
                         |
       typed semantic IR with stable definition/usage IDs
                         |
                native SysML v2 emitter
                         |
              independent parser + library
                         |
        governed SysML section in Markdown notes
                         |
      derived index / where-used / symbol/provenance registry
         /          |           |           \
    structure      canvas      tables      requirements/
       view         view        views       behavior/analysis
                         |
         preview + transactional AST edits (later)
                         |
            Git review, packaging, CI + rollback
```

The IR is **transient/derived**, not a second independent semantic database. SysML v2 text is formal authority; governed YAML owns identity and source/extension evidence only. All Workbench representations derive from the same text and metadata. Obsidian must stay responsive at large vault scale by cooperative indexing and targeted invalidation. Native legal structures and every model source row must be separated from review-only `flagLink` evidence.

For system-of-systems engineering, preserve logical, electrical/mechanical/software structure, interfaces and ports, requirements/satisfaction/verification, states/activities/actions/flows, allocation, causal and temporal semantics, attributes/units/constraints/calculations, analysis and trade studies, variants/configurations, test/results and issues. A single graph view must not flatten these distinct semantic kinds.

## Product and release gates

**Release A (approved first milestone):** source-qualified EA import into a fresh disposable Base; one auditable disposition per row; native parser-accepted subset; correct note source layout; read-only Obsidian Workbench and source/provenance/where-used navigation; reproducible offline package with locked compatible plugins; separate mechanical/semantic/parser/GUI acceptance.

**Release B (post first milestone):** parser-backed transactional visual/text editing, stable UID redirects, source reimport and conflict resolution, semantic undo and approved review/PR workflow.

**Release C (post first milestone):** BOM adapter, exact quantities and effectivity, cross-source evidence matching and controlled merge review, hybrid config/Bootstrap updates, multi-vault resolution and distributed lifecycle.

These are scope groupings, not newly approved deadlines. User-approved roadmap remains [v2 release decisions](V2_RELEASE_ARCHITECTURE_DECISIONS_2026-10-18.md), with cross-vault interfaces designed early and operational support after single-vault acceptance.

## Ranked execution handoff (avoid recreating engineering)

| Order | Build work | Reused evidence | Acceptance |
|---|---|---|---|
| 1 | Fix P0 rule-vs-runtime divergence with separate resolver and failing/positive fixtures | approved October 17 docs, Phase 3/8/9 code | All 60+26 family dispositions agree with policy; no silent fallback |
| 2 | Inspect and run canonical graph/Phase 8/9 at exact git SHA | source/ledger tools and historical invariants | bounded and full ledger replay; direction trust, zero missing rows |
| 3 | Build narrow owned-definition/usage serializer + note writer | v1 staged writer safeguards; v2 canonical graph/parser harness | native parser accepts generated scope; no-op rerun stable |
| 4 | First Obsidian read-only Workbench with performance-aware index | v1 indexer/cache patterns; v2 preview/UX contract | stable identity, navigation, where-used and deferrals in actual vault |
| 5 | Release/reproducibility packaging and real acceptance | v1 plugin lock/checker/Bootstrap; v2 base builder | offline first open; files/settings/versions locked; GUI evidence |
| 6 | Full reduced-QEAX acceptance, attachments and semantics | V1 deterministic real-scale tests; v2 14,688 ledger | source row and attachment coverage; no hidden lost records |
| 7 | Later phase: atomic edits and incremental reimport | v1 transaction manager and migration service | round-trip, three-way merge and rollback |
| 8 | Later phase: BOM, updater, cross-vault | A01–A14, plugin stack/Bootstrap, resolver history | real BOM/upgrade/multi-vault acceptance separately |

## Definition of complete and next controls

A feature is **documented** only when an owner note and trace links exist; **implemented** when an active V2 runtime path exists; **synthetically tested** when invoked by a passing regression; **real-source validated** when run against current local QEAX/BOM fixture; **native accepted** after actual generated syntax/parser conformance; **GUI accepted** after actual Obsidian verification; and **released** after pinned package/rollback evidence. These levels never imply each other.

Next: inspect exact Python/JS call graph and baseline CI, implement contract-level failing tests for DEF-01/02/03, fix discrepancies using approved policy and schema migration, then connect existing graph/serializer/note writer without writing a second importer.
