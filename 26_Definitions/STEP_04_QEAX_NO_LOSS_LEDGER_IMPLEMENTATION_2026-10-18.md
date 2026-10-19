# STEP-04 — QEAX importer and no-loss ledger: first executable gate

Date: 2026-10-18. Status: **initial synthetic gate committed; real QEAX not run against this gate**.

## Authority and scope
- Follows [approved handling clarifications](STEP_00_APPROVED_MODEL_HANDLING_CLARIFICATIONS_2026-10-18.md) and [source/vault controls](../24_Workbench/docs/GOLDEN_IMPORT_SOURCE_AND_VAULT_CONTROLS_PHASE1.md).
- EA diagrams are completely excluded from this tool, report and acceptance scope.
- Source QEAX, source identities, per-row ledger and generated sensitive content remain local only. Commit code, synthetic fixtures and aggregate reports.

## New executable
- `24_Workbench/registry/runtime/v2_step04_ledger_gate.py`: checks exactly one audited row per source table/pk, recognized dispositions, populated mandatory evidence, a single input fixture fingerprint, native/alias target identity and reasons for deferred/evidence-only/error/policy-excluded rows. Optional exact source object/connector counts.
- `25_Testing/test_v2_step04_ledger_gate.py`: synthetic happy path, duplicate, missing native target, missing evidence-only explanation, expected-count mismatch and mixed snapshot.

Example local commands (paths must remain private):

```sh
python3 -m unittest discover -s 25_Testing -p 'test_v2_step04_ledger_gate.py' -v
python3 24_Workbench/registry/runtime/v2_step04_ledger_gate.py \
  --ledger /private/step04/source_disposition.jsonl \
  --objects 11447 --connectors 14688
```

A successful ledger check establishes **source accounting only**. It does not establish correct native semantics, generated markdown, parser conformance or golden import.

## Required integration sequence
1. Consume existing Phase 2 family classifications and Phase 8 connector normalization; preserve raw identity, direction and evidence without inventing missing semantics.
2. Produce one private disposition row per `t_object` and `t_connector` row; distinct child projections may reference a disposition, but cannot multiply source rows.
3. Cover alias-merged source text plus individual inbound/outbound connectors with deterministic target references. Boundary sources map to grouped evidence and links. Packages map to folders without spurious package semantic notes.
4. Carry isolated open target/usage issues as `flagLink`/`flagNote` with a body explanation and an independently identifiable originating source row.
5. Produce an output crosswalk from source GUID+role to stable canonical ID, planned Markdown target, model construct, rules and any review flags. Missing required ownership remains an error or explicit review, not fabricated ownership.
6. Verify combined input/output counts, source→target references, orphan attachments and missing link targets before staging. Keep generated files under a disposable directory and preview the diff.
7. Repeat the same input and rules: require no changes to canonical semantic output. Changed source requires fingerprint comparison and a controlled merge/conflict preview.
8. Only after local proof connect STEP-05 native text generation and pinned SysML v2 parser checks. Workbench release is a separate later gate.

## Acceptance and known gaps
- Initial reduced QEAX baseline is 11,447 objects and 14,688 connectors = 26,135 source ledger entries. Full QEAX counts must be discovered at runtime, not hard-coded.
- A row counted as native is not proof that the target file or SysML expression exists: a separate generated-target existence/integrity gate is necessary.
- Existing historical Phase 8 `deferred_review` counts are provisional normalization statuses, not final flag counts.
- No result is claimed for running the new gate against the uploaded QEAX or golden-import output.
- Next atomic step: execute synthetic test, wire the typed Phase 2/8 source output to this ledger, and compare results against actual generated output. Report aggregate errors by family and concentrate only on blockers.
