# Golden Import — Source Reconciliation and Vault Controls (Phase 1)
Date: 2026-10-17
Status: Implementable audit baseline; semantic mapping and golden-import acceptance remain OPEN.
Authority: SYSML_V2_RELATIONSHIP_COVERAGE_GAP_REVIEW.md, SYSML_V2_ANALYSIS_TRADE_STUDIES_APPROVED.md and preceding approved decisions.
Model evidence boundary: the local October 15 QEAX is fixture input, **not** committed into this methods/tools repository.

## First source evidence check
Source: EA_2026_10_15_endgame_mini.qeax (SQLite read only)
SHA-256: `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822`
t_object 11,447; t_connector 14,688; t_package 1,389; t_diagram 2,208.
Distinct (type, stereotype) families: 60 elements, 26 connectors.
Integrity: 0 missing connector endpoint IDs; 0 missing object GUID; 0 missing connector GUID; 0 duplicate populated object GUID values; 0 duplicate populated connector GUID values. These are structural checks **only**, not semantic or SysML conformity certification.
The earlier reference baseline of 35,969 source elements must **not** be used as a hardcoded assertion for this reduced fixture.

## Phase 1 contract: audited disposition, never silent drop
For every object and connector, produce one row in a versioned, machine-readable source ledger with fields:
source_system, fixture_hash, source_table, source_pk, ea_guid, ea_type, ea_stereotype, source_package_id, rule_id, rule_version, disposition, target_semantic_kind, target_stable_id, target_file, evidence, diagnostic_code, confidence, operator_action.
Disposition enumeration: `native`, `alias_merged`, `evidence_only`, `deferred_review`, `excluded_by_policy`, `error`. Every source row gets exactly one disposition. `excluded_by_policy` still requires a traceable reason. Multiple authored target features can be registered as child projections without multiplying source disposition rows.
Do not use raw EA package nesting as a determinant of MDSE vault placement. Keep package provenance and separately resolve target ownership from modeled semantics and approved vault rules.
EA GUID identifies source evidence; canonical MDSE ID identifies semantic definition or usage. Preserve definition/usage distinction and permit many usages of one definition.

## Approved semantic guardrails
- Do not make unsupported custom SysML v2 relationships. When no native equivalent is justified, retain non-native evidence outside canonical SysML source and flag for review.
- Shared physical part: one reusable Definition, parent-owned typed PartUsages for each occurrence; cardinality on usage/relationship, and separate BOM quantity + unit where applicable.
- `Copy` can become a native alias with consolidated note contents and relationships **only** when identity equivalence is independently established; collisions go to review.
- Native redefinition/subsetting and variation are supported but automatic EA/BOM inference remains deferred.
- Explicit compatible Flow, Message, Interface, Port, Binding, state/activity nesting, allocation and use-case semantics must retain distinctions.
- Avoid deriving satisfaction or verification from generic Realization. Analysis results and execution evidence remain separate from analysis definitions.
- Source `trace`, `refine`, `Realisation`, `Association`, and unusual stereotypes must be bucketed with explicit evidence/rules; never fall through a generic map.

## Vault write contract
1. Preflight: read-only source fingerprint + schema check; fixed/pinned ruleset version and SysML v2.0 library manifest; no write on mismatch.
2. Transform to intermediate typed semantic graph; validate source ledger coverage and no unresolved target-ID collision.
3. Stage a complete manifest of planned file additions/changes/deletions under a disposable staging directory, not directly into approved vault files.
4. Keep canonical semantic files separate from local view/layout metadata and generated reports. Persist provenance and conflict signals, not imported fixture rows, in this repository.
5. Merge policy by field ownership: EA owns source semantics, BOM owns versioned BOM evidence, MDSE owns canonical IDs/placement/derived projections, users own local annotations. Do not silently overwrite manually edited semantic content.
6. For reimport, reconcile by (source system, source GUID, semantic role) to stable target ID; compare three-way against last-generated baseline. Detect source changed, user changed, and concurrent change independently.
7. Remove or relocate only with explicit tombstone/redirect plan; maintain backlinks and where-used indexing. Stale entries and unresolved references fail gate.
8. Execute validation and preview diff; only then atomic publish to intended vault branch through review. Failed validation leaves approved vault untouched.
9. Workbench structural, canvas, analysis and other views must read/write the same canonical semantic graph. A view edge is not a new relationship unless a valid native operation is committed.
10. Record import run manifest: fixture hash, timestamps, tool/rule/library versions, disposition totals, validation results, decision exceptions, generated file hashes, changeset and rollback reference.

## Gates for initial golden fixture
G0 SOURCE — all four table counts and fixture checksum recorded; 100% objects+connectors ledgered; endpoint/GUID issues explained.
G1 COVERAGE — every encountered type/stereotype pair has one registry entry or explicit review disposition; no implicit catch-all.
G2 SEMANTICS — stable definition/usage identity; lawful ownership/ports/flows/relationships; no inferred non-native edges.
G3 NATIVE — generated textual notation parses and type checks against pinned official SysML v2.0 grammar/libraries; violations block.
G4 VAULT — no broken canonical links; complete inverse where-used; no duplicate part definitions; limits for folder/canvas checked as presentation constraints only.
G5 IDEMPOTENCE — second identical import produces zero semantic file changes; BOM-before-EA and EA-before-BOM converge where supported.
G6 EDIT SAFETY — user annotations retained, divergent semantic modifications detected, rename/move redirects resolved, no accidental deletion.
G7 ROUND TRIP — Workbench edit -> canonical persisted syntax/Markdown -> reopen -> same typed graph; provenance and review trace preserved.
G8 RELEASE — published artifact diff approved; source fixture/reports stay out of methods repository; rollback tested.

## Next bounded implementation steps
1. Commit a reusable local-only audit script and anonymized/aggregate fixture statistics; keep model data out of Test_Vault_.
2. Expand audit to all EA object/connector families, endpoint-type pairs, source direction, aggregation flags, tagged evidence and source-evidence coverage.
3. Create machine-readable normative construct and relation registry with distinct `approved`, `implemented`, `parser_verified`, `fixture_covered` fields.
4. Add deterministic source family disposition matrix and evidence-only exception handling.
5. Build an executable golden-import dry run with full file manifest and no write to approved vault.
6. Add parser conformance, idempotence, three-way merge and reverse-lookup regression gates.

## Explicit open items
- Native KerML/SysML v2.0 exhaustive inventory and exact grammar checks.
- Rules for all 60 encountered element and 26 connector family combinations; exact endpoint shape analysis is still pending.
- Ambiguous EA Realisation, trace/refine, association and erroneous proxy/full port classification.
- BOM revision identity and quantity/units reconciliation from representative source records.
- Shared central relationship/operation eligibility registry and Workbench editing implementation.
- Native library pin and positive/negative conformance fixtures.
