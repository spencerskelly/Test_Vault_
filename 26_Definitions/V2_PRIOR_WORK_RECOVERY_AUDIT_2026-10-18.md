# V2 recovery audit — 2026-10-18

Status: repository authority review; no ontology decisions changed.

## Stop duplicate development

The October 17 golden-import work already reviewed **all 2,267** EA aggregations, not just a sample. Refer to:
- `24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_RECONCILIATION_2026-10-17.md`
- `24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_ENDPOINT_CATEGORY_AUDIT_2026-10-17.md`
- `24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_SHARED_COMPOSITE_USAGE_APPROVED_2026-10-17.md`
- `24_Workbench/docs/GOLDEN_IMPORT_AGGREGATION_USAGE_NAMING_APPROVED_2026-10-17.md`
- `24_Workbench/docs/GOLDEN_IMPORT_REPEATED_AGGREGATION_DISTINCT_USAGES_APPROVED_2026-10-17.md`

The October 18 connector readers and validators are supplemental source-evidence diagnostics; they are **not** the translation authority. Do not rerun an aggregation policy discovery pass or ask for renewed approval.

## Frozen aggregation contract

Both shared (1) and composite (2) EA aggregation can produce a context-owned native usage when endpoint semantics are valid. Do not equate all aggregation with physical PartUsage. Preserve distinct connectors, roles, original flags and provenance. Missing multiplicity remains unspecified. One note per reusable definition, not per usage. Reused definitions may have multiple context-owned usages, with stable collision-safe naming.

Existing 2,267 candidate dispositions: PartUsage 1,959; ActionUsage 148; StateUsage 76; UseCaseUsage 10; ItemUsage 6; MDSE-only Change hierarchy 12; flagged unresolved 56. These are candidate dispositions, not parser accepted native statements. The 56 remain separately reviewable and must never be silently discarded.

## Other recovered authorities

- `24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md` already assigns direction/review disposition to all 26 connector families (14,688 source connectors).
- `24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json` and `sysml_v2_semantic_decisions.v0.1.json` are candidate/runtime gate registries. Their conservative defer state does **not** negate subsequently approved specific mapping policies.
- `29_SysMLv2_Translator_Workbench/Passes/` and `25_Testing/phase9_* ` hold Phase 8/9 direction and source-ledger reconciliation code. Reuse before implementing a second normalizer.
- `26_Definitions/APPROVED_V2_TRANSLATION_BASELINE_AND_TEST_HANDOFF_2026-10-18.md` is the consolidated approved semantic and implementation authority.

## Implementation gap vs already done

Already done: source graph/ledger reconciliation (14,688 replay), 26-family policy coverage, aggregated assignment and naming decisions, official parser fixture baseline, Phase 9 review-only direction checks, V2 archive separation, local read-only QEAX diagnostics.

Still requires independent verification: exact CI status on main and actual invocation of existing scripts; coverage of all approved policies in executable gate registries; graph-to-native serializer and bottom-of-note writer integration; source-row validation of flagged categories; deterministic identity/name replay; real sample parser and Workbench inspection.

## Required next build sequence

1. Inventory executable entrypoints in `20_Base Vault`, `21_Importer`, `24_Workbench`, `25_Testing`, `29_SysMLv2_Translator_Workbench` and their CI coverage.
2. Produce a crosswalk: approved decision document → registry rule → executable path → synthetic fixture → source-row reconciliation → parser acceptance → Workbench behavior; mark missing links rather than inventing new conversion policies.
3. Reuse the existing canonical graph/Phase 8–9 trust checks and approved mapping decisions for a narrowly scoped native emitter integration.
4. Keep actual source connector IDs, model names and ledgers local. Publish aggregate outcomes only.
5. Do not modify frozen V1 archives or reauthorize native relationships without parser-backed validation.

This file is a navigation/recovery checkpoint. It is not a new semantic standard, and does not independently certify implementation completeness.
