# STEP-02D — Approved Phase 8 Private Gate and Reduced-QEAX Outlier Review

Date: 2026-10-18. Status: **gated runner implemented; synthetic CI passed; independent real-source aggregate/integrity audit completed. Exact gated runner on real QEAX not yet independently executed in this environment.** Not a SysML parser/golden-import approval.

[Master MOC](../MOC_MDSE_V2.md) · [STEP-02C](STEP_02C_PHASE8_PHASE9_APPROVED_POLICY_INTEGRATION_2026-10-18.md) · [Approved policy](../24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json) · [EA diagram exclusion](STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md).

## STEP-02D.1 — Current gated executable (done and synthetic-tested)

[Current v2 approved Phase 8 runner](../25_Testing/run_gated_v2_approved_phase8.py) connects the existing [diagram-free QEAX source preflight](../21_Importer/qeax_v2_preflight.py), [approved exact family resolver](../21_Importer/v2_approved_family_resolver.py), and the **original** [Phase 8 ledger normalizer](../24_Workbench/registry/runtime/normalize_qeax_phase8.py), rather than duplicating an importer or editing legacy candidate definitions.

The supported CLI requires a locally selected private QEAX SHA-256:
```bash
# Calculate the source fingerprint locally; never commit the private source/ledger.
shasum -a 256 "/path/to/EA_2026_10_15_endgame_mini.qeax"
python3 25_Testing/run_gated_v2_approved_phase8.py \
  --qeax "/path/to/EA_2026_10_15_endgame_mini.qeax" \
  --source-sha256 "<calculated locally>" \
  --out "/path/outside/Test_Vault_/approved_phase8_private"
```

Before publishing the output directory, the runner requires: the approved pinned three-table profile; exact approved registry with no diagram support; selected source hash equality; same source+registry hash after processing; 24 original-evidence columns in fixed order; exactly one ledger row per source connector in PK order; matching GUIDs/raw endpoints/family/direction/role/cardinalities/aggregation flags; only explicit evidence/review statuses; and aggregate counts identical to the ledger. The full ledger, source input attestation and gate record remain **outside** the repository. Any failure removes the staging directory and never writes the destination. Never overwrite an existing run. `native_certified=0`.

The superseded [historical runner](../25_Testing/run_gated_phase8.py) still references old source profiler dependencies and a 13-column ledger. It is retained for historical tests, **not** an approved golden-import entrypoint. Do not wire it to current V2 CI or importer releases.

## STEP-02D.2 — Reproducible synthetic CI (passed)

[Current gated runner regression](../25_Testing/test_run_gated_v2_approved_phase8.py) exercises profile mismatch, source-fingerprint mismatch, whole-row ledger attestation, aggregation role/cardinality preservation, unknown connector family, staged tampering/rollback, private destination guard, stale output guard, and diagram independence. [GitHub Actions run 39167341807](https://github.com/spencerskelly/Test_Vault_/actions/runs/39167341807) passed after the test was wired into the existing V2 migration workflow.

## STEP-02D.3 — Independent real reduced-source aggregate and integrity audit

The supplied reduced `EA_2026_10_15_endgame_mini.qeax` was read locally via SQLite **read-only**. Queries accessed `t_object`, `t_connector`, `t_package` only, not EA diagrams. The source file, raw rows, source GUIDs and any row-level ledger were **not** committed.

| Metric | Source count |
|---|---:|
| Element rows | **11,447** |
| Connector rows | **14,688** |
| Organizational packages | **1,389** |
| Unknown element families | **0** |
| Unknown connector families | **0** |
| Duplicate connector primary keys | **0** |
| Missing source connector GUIDs | **0** |
| Duplicated source connector GUIDs | **0** |
| Connectors referring to missing elements | **0** |
| SQLite integrity | **ok** |
| EA diagram tables read | **0** |

The 26-connector family set is fully identified. Distinct semantic review concentrations (overlapping categories, **not an additive backlog**):

| Evidence category | Source records | Interpretation |
|---|---:|---|
| Shared aggregation | 597 | Approved mapping group; requires real owner/type evidence; do not auto-reject shared |
| Composite aggregation | 1,670 | Approved mapping group; requires owner/type evidence |
| Non-explicit source direction | 433 | **395 Association**, **27 NoteLink**, **9 Connector**, **1 allocation**, **1 trace dependency** |
| Connectors touching non-native element types | 946 | Source MDSE-note/reference/link evidence; not synonymous with data loss or unknown mapping |
| Reference-only connector families | 413 | 220 NoteLink and 193 Sequence; Sequence is non-diagram reference only until authorized diagram phase |
| Connectors touching conditional usage kinds | 49 | Requires typed context/source evidence review |

The only *non-explicit-direction rows outside known Association/NoteLink/Connector source groups* are **two**: one `Abstraction:allocate` and one `Dependency:trace`, both with reversed EA direction. These are focused direction-evidence outliers, not newly undefined semantic families.

The 946 connectors with non-native endpoints concentrate in Dependency:trace (303), Abstraction:allocate (255), NoteLink (220), ControlFlow (69), and smaller families. These need approved MDSE descriptive/flagLink or alternate legal native endpoint review, not automatic deletion.

**Evidence limitation:** the real-source aggregate/integrity check was performed with an independent local SQLite auditor, **not the newly committed current gated runner**. We cannot yet claim that its full real-source 24-column output has passed the gate. The synthetic CI evidence does not substitute for that full-run acceptance.

## STEP-02D.4 — Next acceptance: real full runner and outlier evidence classification

1. Run the current gated CLI against the supplied QEAX in a checkout with the new repo scripts, using its local source SHA and private output directory. Verify exactly **14,688 source connector rows**, no altered evidence, and atomic private output. Publish **aggregate diagnostics only** to the repo.
2. Reuse approved group-level rules to classify the 597 shared vs 1,670 composite aggregations and the 946 non-native endpoint relationships into compatible native-use, MDSE-link/flagLink and genuine exceptional review buckets; do not reopen source-family mappings.
3. Extend Phase 9 endpoint/direction trust only where semantics require it. Association and NoteLink should not each count as unknown-direction semantic failures merely because EA recorded an unordered relationship.
4. Review the two reversed direction exceptions explicitly. Verify original connector orientation and intended legal SysML semantics.
5. Ensure the same full-source gate accepts no diagram-dependent evidence and never authorizes native emission on its own.

**Next titled work:** `STEP-02E — Real-Source Phase 8 Acceptance and Semantic Outlier Prioritization`. A later native parser and Obsidian golden-import gate remains separately required.
