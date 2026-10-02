# MDSE v0.8 Toolchain Review — 2026-10-02

## Scope

Cross-repository review of the tools and artifacts that lead to the first keepable EA → MDSE v0.8 model.

Reviewed:
- `spencerskelly/Test_Vault_` main;
- `spencerskelly/MDSE_Workbench` main;
- `spencerskelly/Test_Vault_-base-vault-2026-09-30-rel133-v051` main;
- `spencerskelly/20260930` main;
- `spencerskelly/261001` main.

Also checked the active plugin lock/specification in the authority vault.

## Authority map

| Area | Authority | Current status |
|---|---|---|
| MDSE semantics | Test_Vault_ Ruleset 1.23 + Workspace Decision Log | current |
| Relationships | relationships.yaml 1.35 | current |
| Element/property schema | element-types.yaml 1.17 | current |
| Local Model format | local-model.yaml 0.2 | current writer contract; 0.1 readable |
| Native importer behavior | Translator Definition + 2026-10-02 reconciliation | current; v0.8 code not yet built |
| Workbench product direction | Test_Vault_/MDSE Workbench folder | current |
| Workbench implementation | spencerskelly/MDSE_Workbench | 0.1.15 source alignment; WB-106 not built |
| Clean v0.8 base | must be generated from current authority | not yet built |
| 20260930 / 261001 | assessment/reference only | fenced |
| old rel133/v051 base repo | reference only | fenced |

## Conflicts found and disposition

### Identity

**Found:** Ruleset 1.22 said Local Model IDs were only context/scope unique while the 2026-10-02 design requires collision-resistant identity across every independently referenceable point.

**Resolved:** W-315 / Ruleset 1.23 / Local Model 0.2 establish one globally unique 30-character token namespace. Notes store the token in `uid`; local records wrap the token with `part-`, `ep-`, `conn-`, or `flow-`.

### EA author fallback and timestamps

**Found:** `uid.md` and `authors.yaml` still described `sparxeaauthor` as the missing-author behavior.

**Resolved for EA8647:** W-316 defines the current import override: missing/unusable author uses `skellyspencer`; source time is used exactly as stored with no timezone conversion; missing milliseconds are `000`; no source time begins at `20260911000000001`. The generic/historical authors.yaml fallback remains documented as non-EA8647 behavior.

### Local Model version

**Found:** the deployed schema and multiple current docs still said 0.1 while W-314 required the usage/abstract advance.

**Resolved:** Local Model 0.2 is canonical writer contract; readers must support 0.1 + 0.2. Element schema is 1.17 with sparse optional `abstract`.

### Duplicate relationship count

**Found:** Workbench 0.1.14 source displayed repeated note-level relationship targets as engineering quantity (`×N`).

**Resolved in source:** Workbench 0.1.15 labels repeated targets explicitly as duplicate evidence. True engineering quantity is Local Model `multiplicity`. Relevant unit-test expectations were updated.

### Ordinary body editing

**Found:** Workbench could replace the whole post-frontmatter body, risking governed Local Model destruction.

**Resolved as immediate safety behavior:** Workbench 0.1.15 refuses ordinary body editing when a governed Local Model START marker is present. WB-106 still must implement region-aware reading/indexing and later safe editing.

### Duplicate filenames and paths

**Found:** older guidance used ID-based duplicate filename suffixes and left the hard path limit open.

**Resolved:** W-318 uses `~2` duplicate markers, `~a` alteration markers, the same rules for folders, semantic folder shortening first, and a hard 212-character generated repository-relative limit.

### Rerun ownership

**Found:** prior material did not fully define what is refreshed, preserved, removed, or flagged on rerun.

**Resolved:** W-317 defines Source Map identity authority and EA-owned vs MDSE-owned fields/relationships. Missing source entities are preserved/flagged, not automatically deleted.

### Attachments / diagrams / legacy evidence

**Found:** v0.7 did not import attachments; diagram scope and four legacy empty CSVs were still hanging over the acceptance path.

**Resolved semantically:** failed approved attachment import is non-blocking but reconciled; source diagram reconciliation is mandatory even though artifact creation is deferred; four empty legacy CSVs are retired.

## Native importer code review

Current executable prototype in the authority repo is still `EA_to_MDSE_Native_Importer_v0.7.html`.

It is **implementation evidence only** and is not release-conformant. Specific active mismatches confirmed in source:

1. hard-coded `LOCAL_BODY_SCHEMA="0.1"`;
2. local IDs are GUID-tail tokens rather than the governed 30-character identity allocation;
3. separate `loc-...` anchors exist instead of block ID = local ID;
4. no canonical Local Model 0.2 managed-region writer;
5. no `usage`/abstract-aware schema contract;
6. source provenance remains mixed into prototype local rendering rather than the final Source Map contract;
7. no `mdse_release: 0.8.0` pairing enforcement;
8. no final 212-character path planner/naming convention;
9. no final W-308/W-309 generalized folder normalization;
10. no approved attachment writer/reconciliation;
11. no final diagram-defer reconciliation gate;
12. no authoritative Local Model Source Map;
13. evidence set remains assessment-oriented rather than the final v0.8 set;
14. BindingConnector handling does not yet implement the final deterministic-context/evidence rule.

**Instruction:** do not patch generated v0.7 output. Build `EA_to_MDSE_Native_Importer_v0.8.0.html` from the accepted v0.5.2 safety lineage plus useful v0.7 occurrence/QEAX code, governed by the current schemas/docs.

## Workbench code review

### Correct and retained
- Markdown/YAML remain model authority;
- disposable index;
- schema-driven relationship vocabulary;
- endpoint validation;
- forward/inverse transaction behavior;
- generated Canvas is a view;
- review/findings architecture;
- existing view engine remains reusable.

### Immediate 0.1.15 corrections applied
- repeated links no longer presented as quantity;
- body editing blocked on governed Local Model notes;
- element schema test fixture advanced to 1.17;
- generic `optionalProperties` are read from element-types and ordered after `tags` / before relationship fields, so `abstract` is not reordered incorrectly during ordinary frontmatter edits;
- standalone WB-106 implementation contract added.

### Still required for WB-106
1. load Local Model schema as third schema;
2. ModelRef identity instead of path-only semantics;
3. parse Local Model 0.1 + 0.2;
4. preserve `#^local-id` frontmatter/link fragments;
5. local-record index and health findings;
6. Local Model popup/surface;
7. occurrence-aware Structure / Interfaces / Where Used / Requirements;
8. add Local Model 0.1/0.2 fixtures and parser tests;
9. only after that, parse/validate `abstract` and `usage`, derive candidates, and add read-only variation/session configuration.

## Base-vault review

The repository `Test_Vault_-base-vault-2026-09-30-rel133-v051` is obsolete as a release base and now carries a reference-only warning.

Do not mutate it into v0.8.

A new clean base must be produced from the current authority and must contain/declare:
- `mdse_release: "0.8.0"`;
- relationships 1.35;
- element-types 1.17;
- local-model 0.2;
- current templates/Definitions/AI instructions;
- v0.8.0 importer;
- the approved plugin/configuration baseline.

## Assessment repos

`20260930` and `261001` now carry explicit reference-only warnings. Their generated content and old importer/schema files remain historical evidence and should not be upgraded in place.

## Bootstrap / plugin packaging finding

> [!NOTE]
> Later on 2026-10-02 this finding was resolved by W-322 (controlled plugin release, MDSE Bootstrap 0.3.0). See [[00 - Current State]].

The authority vault pins `mdse-bootstrap: "0.2.0"` in `.obsidian/plugin-lock.yaml`, and `MDSE Bootstrap - Author Registration Spec.md` defines expected author-registration behavior.

However:
- no mdse-bootstrap source exists in the authority repo;
- no accessible standalone mdse-bootstrap repository was found through the connected GitHub installation;
- the old cross-vault resolver is archived and is not part of the current single-vault v0.8 design.

This is a **base-packaging dependency**, not a model-semantic conflict.

The current authority plugin lock also does not yet pin an MDSE Workbench release. If WB-106 is a keepability gate, the final base packaging must pin the WB-106-capable Workbench release rather than 0.1.15.

Before issuing the clean v0.8 base, either:
1. verify a retrievable/pinned mdse-bootstrap 0.2.0 release/package that conforms to the spec; or
2. explicitly remove/defer it from the required base-plugin set.

Do not make the native importer or WB-106 depend on unavailable Bootstrap implementation code.

## Validation status

Source-level consistency checks were performed through the connected GitHub repositories.

The standalone Workbench test expectations were updated for the 0.1.15 safety changes. An executable `npm test` / `npm run build` could not be run in this session because the container environment could not resolve GitHub/npm. The repository does not commit `main.js`; release artifacts are expected from the build/release process.

Therefore:
- documentation/schema reconciliation: complete;
- Workbench source-level safety alignment: complete;
- Workbench executable build verification: still required;
- v0.8 importer implementation: still required;
- clean v0.8 base generation: still required;
- WB-106 implementation: still required.

## Final implementation sequence

1. Build `EA_to_MDSE_Native_Importer_v0.8.0.html` against relationships 1.35 / element-types 1.17 / Local Model 0.2.
2. Implement global identity allocation + Source Map first.
3. Implement canonical Local Model 0.2 writer, native block IDs/links and BindingConnector review behavior.
4. Implement final naming/folder planner and 212-character preflight.
5. Implement attachment reconciliation, diagram deferral reconciliation and final evidence package.
6. Produce a brand-new clean v0.8 base.
7. Run static/synthetic importer checks and the representative real-EA acceptance sample.
8. Implement and executable-test Workbench WB-106.
9. Resolve/verify Bootstrap packaging for the clean base.
10. Only when importer/base and WB-106 gates pass, run a whole-model import eligible to keep.

## Current conclusion

The **decisions and instructions are now reconciled**. Remaining risk is implementation work, not unresolved semantics.

Do not restart design from old importer/base/assessment artifacts. Continue from the 2026-10-02 reconciliation, Ruleset 1.23, W-315 through W-319 and the WB-106 implementation contract.


## W-321 resolution — 2026-10-02

The follow-up consistency review found remaining drift inside files registered as current. W-321 resolves it by eliminating manually duplicated runtime-base contracts.

Resolved:
- Translator Definition active text now matches element-types 1.17, Local Model 0.2, EA8647 identity, W-318 naming and Source Map rerun authority.
- relationships.yaml no longer points local exposure at Local Model 0.1.
- `mdse-release.yaml` owns one positive runtime-base include list.
- `build-base.py` produces the lean runtime artifact from that list.
- `check-release.py --base` verifies the artifact against the authority workspace.
- vault initialization preserves `mdse_release`.
- unavailable MDSE Bootstrap is removed from the v0.8 runtime baseline rather than left as an unresolvable dependency.
- Current State and the release manifest are explicitly workspace-only and are not duplicated into engineering vaults.
- Workbench keeps only portable schema fixtures required for independent tests: current schema copies plus a frozen Local Model 0.1 compatibility fixture.

Remaining work is implementation: importer v0.8.0, WB-106, then pinning the WB-106-capable Workbench and issuing the clean base.
