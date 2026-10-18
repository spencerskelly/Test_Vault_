# V2 implementation traceability audit — first controlled inventory

Date: 2026-10-18. Status: repository-path evidence inventory, not functional acceptance.
Governing release decisions: `26_Definitions/V2_RELEASE_ARCHITECTURE_DECISIONS_2026-10-18.md`.
Canonical semantic authority: `26_Definitions/APPROVED_V2_TRANSLATION_BASELINE_AND_TEST_HANDOFF_2026-10-18.md`.

## Reading the matrix
A source path means material is present in main and discoverable, **not** that its function is complete. The work does not repeat the approved October 17 conversion decisions. The next stage must verify actual invocation, tests, and artifact results at a pinned commit.

| ID | Approved/established contract | Recovered executable and tests | Current evidence level | Gap or integration work |
|---|---|---|---|---|
| V2-01 | Source QEAX read-only; 11,447 objects, 14,688 connectors; one disposition per source row | `21_Importer/` QEAX preflight and source slice readers; `25_Testing/run_gated_phase8.py`, `verify_phase8_rows_against_qeax.py`, `replay_phase8_local_normalization.py` | Earlier 14,688-row replay reported; new readers have synthetic CI coverage | Re-run pinned full ledger check independently; unify output contract instead of creating a second ledger |
| V2-02 | All 26 relationship families and 60 element families have review policy | `24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json`, `sysml_v2_semantic_decisions.v0.1.json`; `24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md` | Approved policy and candidate registry; native emission disabled | Reconcile later approved per-family decisions into a versioned executable policy adapter without editing pinned candidate bytes |
| V2-03 | Shared/composite aggregation create eligible typed owner usages; repeated relationships remain distinct | `24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_RECONCILIATION_2026-10-17.md`, aggregate usage/naming/repetition decision files; newer `21_Importer/v2_validate_connector_evidence.py` | 2,267 candidate dispositions already classified; syntax-only diagnostics additionally available | Connect existing disposition rules to semantic graph/writer; 56 flagged exceptions remain non-native. Do **not** repeat category review |
| V2-04 | Trusted source direction for generalization; no connector orientation guessing | `25_Testing/phase9_source_direction_bridge.py`, `phase9_generalization_family_matrix.py`, `phase9_local_specialization_evidence_gate.py`, `24_Workbench/registry/runtime/phase9-generalization-evidence-bridge.mjs` | Source-bound review gate implemented; native certification expressly absent | Integrate trusted evidence with canonical graph and native serializer |
| V2-05 | Native SysML text owns model semantics; final note section authoritative | `26_Definitions/SysML Source Ownership and Note Storage.md` (historical proposal with superseded layout); `24_Workbench/docs/SYSML_V2_BUILD_READINESS_STABILITY_UX_GATE_2026-10-17.md` | Architecture approved | Implement deterministic owner/namespace-aware AST writer with bottom `## SysML v2` fenced text and transactional validation |
| V2-06 | Official parser, standard libraries, and validated generated SysML | `25_Testing/sysml2_parser_runner.py`, `sysml2_parser_attestation.py`, `25_Testing/Fixtures/Golden Charger v2/` and parser pin, `29_SysMLv2_Translator_Workbench/Passes/PASS07_FIRST_PASSING_NATIVE_PARSER_GATE_2026-10-17.md` | Prior official parser fixtures passed; generated real model not accepted | Pin and rerun official parser, then parse actual emitted scope (not only hand-authored fixture) |
| V2-07 | Fresh offline disposable Base, no approved vault overwrite | `20_Base Vault/build_v2_test_base.py`; `25_Testing/test_v2_test_base_builder.py` | Builder and synthetic tests present | Verify first-open plugin configuration, release lock and actual generated note import |
| V2-08 | Read-only first-release Workbench with native definition/usage navigation and diagnostics | `24_Workbench/v2-workbench.html`; `24_Workbench/V2 Workbench MVP.md` | Exploratory read-only prototype, not released Obsidian plugin | Verify actual UI fixture and source mapping; scope first milestone without edit transactions |
| V2-09 | Later graphical edits always transact against authoritative SysML source | `24_Workbench/docs/SYSML_V2_BUILD_READINESS_STABILITY_UX_GATE_2026-10-17.md` and historical Workbench contracts | Approved later-phase requirement | Build parser-backed edit, preview/undo/conflict and rollback only after first read-only release |
| V2-10 | Later BOM reader: one definition per numbered part, parent-owned usages, exact quantities/UOM | `24_Workbench/docs/BOM_TO_SYSMLV2_MDSE_ELEMENT_RELATIONSHIP_INTEGRATION_REVIEW_2026-10-17.md`; retained `100_Archive/V1/14_Workbench/docs/bom/a01-a14/` | Mixed approved and proposed schema decisions; prior fixture work | Preserve design in core; approve quantity/variant schema migration before writer; independently test actual assembly |
| V2-11 | Hybrid managed team plugin/schema updates with protected personal settings | `23_Bootstrap/README.md`; `100_Archive/V1/13_Bootstrap/` and versioned plugin assets | Prior implementation available as historical reference; no v2 update delivery verified | Define settings ownership classes, release lock, compatible migrations, opt-out rules, rollback, mixed OS tests |
| V2-12 | Cross-vault architecture now, functional support later | `66_Cross-Vault/README.md` and archived resolver implementation history | Deferred product delivery, retained architecture | Define UID cross-vault resolver contract now, do not gate first release |
| V2-13 | Git approval, traceable releases, no raw public source data | `24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md`; `.github/workflows/v2-migration-executable-repair.yml` | Main CI wiring exists; current passing status not independently attested | Validate current workflow runs, release gating, staged dry-run outputs, PR publication and rollback |
| V2-14 | Independent V2 runtime; archived V1 is reference only | `100_Archive/V1/`; `26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json`; v2 archive/runtime CI checks | Repository separation implemented and merged | Continue guarding imports and generated outputs against runtime archive dependence |

## Recovery and completeness gate

The first-release **critical path** is V2-01, 02, 03/04 for selected relationships, 05, 06, 07, 08, 13, and 14. V2-09–12 must retain design contracts and interfaces, but may ship later under approved phased release.

Important uncovered verification:
1. Enumerate every approved October 17 mapping (not only high-volume aggregation) and link its implementation and tests.
2. Inspect Python/JS runtime imports and entrypoints rather than trusting file names.
3. Read actual CI run conclusions at exact SHA and record any failures.
4. Build a machine-readable source-of-truth traceability manifest, with tests that fail when a required rule lacks an owner or when an implementation is unreferenced.
5. Audit retained historical tools, conversations, and other repositories for valuable unported behavior. This matrix includes known high-value authorities but **is not proof of complete historical recovery**.
6. Run a tightly scoped actual source native-generation test through canonical graph, parser, Markdown writer, and read-only Workbench; keep model data and private ledgers local.

Do not treat proposals as approvals, file presence as execution, parser fixture passing as generated model acceptance, or synthetically tested utilities as a released tool.
