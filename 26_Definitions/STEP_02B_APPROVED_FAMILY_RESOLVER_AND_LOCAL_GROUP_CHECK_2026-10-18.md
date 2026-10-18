# STEP-02B — Approved Family Resolver, Whole-Source Group Match and Outliers

Status: group lookup implemented and synthetically tested; native row semantics/parser and Workbench acceptance **not** established. Snapshot: October 18, 2026.

[Master MOC](../MOC_MDSE_V2.md) · [Diagram deferral](STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md) · [Original 60-element approvals](../24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md) · [Original 26-connector approvals](../24_Workbench/docs/GOLDEN_IMPORT_RELATIONSHIP_26_FAMILY_DECISION_AUDIT_2026-10-17.md)

## Work created without changing prior approvals

- [Versioned exact 60+26 mapping registry](../24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json): every known EA element/connector source family has one explicit approved group disposition, conditional native candidate or non-native outcome. `automatic_native_emission=false`, `ea_diagrams_enabled=false`; nothing silently inherits a broad wildcard.
- [Read-only group resolver](../21_Importer/v2_approved_family_resolver.py): exact type/stereotype identity, fail-closed unknown outlier, separate native candidate vs descriptive note/attachment/folder/Boundary grouping. Does not emit syntax or mutate source.
- [Read-only full-QEAX aggregate review adapter](../21_Importer/review_approved_qeax_mapping.py): `t_object`, `t_connector`, `t_package` only. Returns counts by approved family and dispositions, no row IDs/notes/source data, zero EA-diagram processing.
- [Exact-group synthetic test](../25_Testing/test_v2_approved_family_resolver.py) and [QEAX adapter synthetic test](../25_Testing/test_v2_approved_qeax_mapping.py). Both wired to main CI.

## Independent real-source family-key check

Local-only query of `EA_2026_10_15_endgame_mini.qeax` (read-only) grouped `t_object.Object_Type/Stereotype` and `t_connector.Connector_Type/Stereotype`; no EA diagram tables or source-row payloads were read.

| Scope | Actual rows | Matched exact approved family | Unmatched source-family rows |
|---|---:|---:|---:|
| Elements | 11,447 | 11,447 (100%) | 0 |
| Connectors | 14,688 | 14,688 (100%) | 0 |

This check used an independent comparison of the **same 60 and 26 exact family names**, not an official parser or a full generated model. It is aggregate-only and does not publish proprietary row data or the source QEAX. The new adapter's synthetic CI and real-source grouping check are distinct evidence. Full direct live-source adapter acceptance is still required.

## Group readiness / unresolved row-level exceptions

**Family selection is complete for the reduced QEAX.** This does **not** establish that every row has compatible endpoints, source direction, owner, classifier, valid native syntax, uniqueness, or complete provenance.

Resolve later as bounded outlier classes, reusing [the 12 approved exception decisions](V2_APPROVED_EXCEPTION_HANDLING_AUDIT_2026-10-18.md):
- Class:Physical Context composite/external distinction and unknown context.
- Object classifier specialization vs simple definition typing; alias/copy coalescence.
- Port, Action and Part untyped usages stay importable and flagged.
- Shared/composite aggregation typed owned usages, with genuine owner/direction evidence; duplicate connectors remain distinct.
- Binding/connection/inclusion/extension/verification eligibility by native endpoint roles.
- Non-native InformationItem and ProxyConnector, Boundary combined note, attachment links, organizational folders.
- Sequence family remains **reference-only from explicit non-diagram rows**. All EA diagram interpretation is deferred until toolchain and golden import acceptance.
- Unknown families in future source revisions become explicit outlier counters, never generic wildcard/native coercion.

## Next atomic integration

**STEP-02C — Integrate Approved Resolution into Phase 8/9 Row Normalization.** Existing `normalize_qeax_phase8.py` and `reconcile_qeax.py` contain older hard-coded candidate kind assumptions (including InformationItem→ItemDefinition and composite-only aggregation) and must not be promoted to native emission unchanged. Wire the new approved resolver into the source-row normalization at a versioned interface, keep all source rows independently dispositioned, and validate explicit outlier categories. Use accepted elements/connectors only; no EA diagram dependencies. Preserve existing private source ledgers and atomic staging; avoid a parallel duplicate translator.
