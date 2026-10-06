# Importer Issue Register

**Status:** Active correction backlog  
**Baseline date:** 2026-10-05  
**Current candidate:** `EA_to_MDSE_Native_Importer_v0.8.19.html`  
**Operating model:** [[Importer Operating Contract]]

This register turns observed importer/model problems into bounded engineering work. It is intentionally focused on issues that affect model integrity, traceability, deterministic behavior, release confidence or everyday usability.

## Priority

- **P0 — integrity / false-confidence risk:** can corrupt, misrepresent or falsely certify the imported vault.
- **P1 — release blocker / major usability risk:** must be resolved or explicitly accepted before a keepable/golden import.
- **P2 — maintainability / efficiency:** important after correctness gates are closed.

Status values:
- `open`
- `decision required`
- `implementation required`
- `test required`
- `deferred`
- `closed`

## Ranked register

| ID | Pri | Phase | Status | Issue | Why it matters | Current evidence | Exit condition |
|---|---|---|---|---|---|---|---|
| IMP-001 | P0 | 9 | closed | Partial filesystem writes can leave a vault that looks legitimate | v0.8.19 centralizes transaction state in `runImportTransaction`; no partial write can become authoritative. | Production-path fault injection in `transaction_failure_regression_test.js` passes inside the aggregate release gate (run `37414098512`): an injected body write failure persists `IMPORT_FAILED / WRITE_FAIL`; an injected failure while persisting `IMPORT_FAILED` leaves the prior `IMPORT_IN_PROGRESS / WRITE_IN_PROGRESS` marker authoritative; both dirty states are rejected by `assertFreshImportDestination`. Acceptance also exposed and fixed a strict-JSON defect in `Import State.json`. The changed production path then passed full real-QEAX import, deterministic comparison and Workbench scan in bridge run `37414094667`. | **Closed.** Failure/in-progress states cannot masquerade as PASS and a destination with any import-state file is refused for rerun. |
| IMP-002 | P0 | 5/10 | closed | Off-rule/provisional relationships are written into canonical YAML | v0.8.19 retains W-376 and now has both fast and real-output release gates for the canonical relationship boundary. | Real-QEAX bridge run `37415340902` passed an independent written-output audit: 1,010 reviewed connector plans = 1,010 exact review-evidence rows, with **0 reviewed-plan canonical writer calls**; 237 endpoint/provisional findings = 237 exact suppression-evidence rows, with **0 suppressed relationship values in written YAML** and **0 `tracesTo`/`tracesFrom` values**. Deterministic rerun and Workbench read-only scan passed on the same run. `canonical_relationship_boundary_regression_test.js` is also in the aggregate fast release gate; importer CI run `37415891266` passes. | **Closed.** Review-only/off-rule source semantics remain explicit evidence and cannot silently enter canonical YAML. |
| IMP-003 | P0 | 10 | closed | One PASS label conflates mechanical completeness with semantic acceptance | v0.8.19 retains W-372 separate source, plan, write, semantic and acceptance states and now gates that separation in both fast CI and the real-QEAX bridge. | Fast production-path transaction regression preserves `SEMANTIC_REVIEW_REQUIRED / ACCEPTANCE_PENDING` across `WRITE_PASS`, `WRITE_FAIL`, and `WRITE_IN_PROGRESS`; importer CI run `37416807483` passes. Real-QEAX bridge run `37416802624` proves the same distinction on EA8647: successful transaction = `IMPORT_COMPLETE / WRITE_PASS / SEMANTIC_REVIEW_REQUIRED / ACCEPTANCE_PENDING`; injected failed transaction reusing that exact real plan = `IMPORT_FAILED / WRITE_FAIL / SEMANTIC_REVIEW_REQUIRED / ACCEPTANCE_PENDING`. Determinism and Workbench scan also pass. | **Closed.** Mechanical completion/failure can no longer be interpreted as semantic/model acceptance from governed importer status evidence. |
| IMP-004 | P0 | 1 | closed | SQLite WAL mode is only a warning | v0.8.19 retains W-373: SQLite header WAL mode is a blocking preflight failure. | Real-QEAX bridge run `37417967397` reuses the accepted EA8647 source and presents a virtual copy with only SQLite header bytes 18/19 changed to WAL mode. Clean source: `PASS`, `walMode:false`, whole-model plan `PASS`. WAL-header source: preflight `FAIL`, `walMode:true`, sole hard-fail code `SQLITE_WAL_MODE`, `planCreated:false`, and source SHA-256 remains null because hard preflight failure stops fingerprinting/planning. Fast importer CI and package checks on the same head also pass (`37417971551`, `37417971522`). | **Closed.** WAL-mode source snapshots cannot reach planning/import; a clean checkpointed source proceeds normally. |
| IMP-005 | P0 | 0 | closed | Fresh generated base is reported incompatible until initialized outside the importer | W-381/v0.8.19 accepts `vault_uid: UNINITIALIZED` under the loose selection validator, while strict write validation rejects it until explicit importer initialization completes. | Importer CI run `37419754379` builds a real governed 0.8.0 Base, proves loose selection **PASS**, strict pre-initialization write **BLOCKED**, creates governed UID `20261006054124829testuser-----` (30 chars), then proves strict post-initialization validation **PASS**. The full non-`.vault.yaml` Base snapshot (160 files) is byte-for-byte unchanged; relationships/element-types/Local Model schemas, plugin lock and enabled-plugin identity are preserved. Static UI coverage still proves the fresh-base state enables initialization and blocks generation until initialization. | **Closed.** A distributed fresh Base remains safely uninitialized, is selectable by the importer, and becomes writable only after in-tool identity initialization succeeds. |
| IMP-006 | P0 | 1/2 | closed | Source file lacks a strong recorded fingerprint | v0.8.19 retains W-375 streaming standard SHA-256 and now gates the current implementation plus immutable real-source evidence. | Fast current-version regression passes standard empty/`abc`/split-update vectors. Dedicated artifact-reuse run `37420398404` hashes the exact accepted 186,036,224-byte QEAX with the production v0.8.19 implementation and gets `16c055ec1a5af57b0f4f9059d6292c5ddd3ed052124c7ef54d9af288971ae02c`; that digest matches preflight, `Import State.json`, and `Run Manifest.md` exactly. Flipping one virtual bit at byte offset 93,018,112 yields `00ae9590b2a970830545d80a281f8e238274c9f8c1310b9a7f0000b8d764635c`, proving sensitivity. Normal importer CI and package checks on the same head pass (`37420404557`, `37420404553`). | **Closed.** Exact source identity is strongly fingerprinted, consistently persisted, and independently sensitive to source-byte changes. |
| IMP-007 | P1 | 2 | closed | Exact EA8647 source counts are compiled into the importer engine | v0.8.19 externalizes source-shape policy into the versioned `mdse-ea-source-profile/1` authority `Importer/Definition/Source Profiles/EA8647-2026-09-06-v1.json`; the self-contained importer embeds a canonical copy but the executable engine only loads/validates generic profile data. | `mdse-release.yaml` declares the source profile and sync tool. `source_profile_regression_test.js` proves the external/embedded profiles match, legacy compiled count objects/source ID are absent, and malformed schema/count/missing-table/empty-section profiles are rejected by the production loader. Bridge run `37422210977` passes profile sync, aggregate release gate, real EA8647 whole-model import, deterministic rerun and Workbench scan; Run Manifest records `Source profile: EA8647-2026-09-06-v1 (mdse-ea-source-profile/1)`. Normal importer/package CI on the same head also passes (`37422215257`, `37422215224`). | **Closed.** Legitimate source evolution changes/version-controls governed profile data and regenerates the embedded copy; source-count logic no longer requires an engine-code change. |
| IMP-008 | P1 | 2 | closed | Not every discovered/non-empty QEAX table is executable-gated by disposition | A future EA feature can start storing useful data in a previously empty/ignored table without necessarily becoming a hard review. | W-394 governs all 100 tables in the active source profile: 12 `imported` exact-count tables (including `t_operationparams: 0`), 34 `ignored_nonempty_approved`, and 54 `ignored_must_be_empty`. Real-QEAX bridge run `37425094714` passed profile sync, the aggregate release gate including `table_disposition_regression_test.js`, and preflight against the accepted 186,036,224-byte EA8647 source with exactly 100 discovered tables and **0 fail / 0 warn**. The same run completed two full imports (`IMPORT_COMPLETE / WRITE_PASS`), deterministic comparison, and the Workbench read-only real-vault scan. Current importer CI on head `6c69f64a4185d852e2cf6a74af0b6d86af84941d` also passed in run `37425291335`. | **Closed.** Every discovered table has an executable disposition before planning; unknown/missing tables, imported-count drift, and newly non-empty `ignored_must_be_empty` tables fail closed. |
| IMP-009 | P1 | 6 | closed | Contextual EA Ports without deterministic reusable definitions must remain usable without synthetic Port notes | Current v0.8.19 / Local Model 0.4 represents every EA Port as a contextual Interface occurrence; a reusable Object/interface definition is optional and only written when deterministic source evidence exists. | **Closed on real-QEAX bridge `37492673084`.** Gate 1 returned `HEADLESS PASS (25 checks, 0 warnings)` across all 1,051 definitionless Interfaces: no first-class Port notes, exact Source Map/Ledger traceability, 306 definitionless Interfaces referenced through persisted local links, 256 participating in Connections, and all 8 applicable connector-review rows traceable to exact source Object_IDs. Workbench 0.1.18 Gate 2 passed with 0 parser/block-reference/compatibility failures. Gate 3 passed across 27,813 Markdown files and 1,050 no-op record checks with `noOpDrift: 0`, 0 duplicate local IDs, 0 parser errors, 23 `Connection.exposes` references, and representative Structure/Interfaces/flow/Where Used views. Gate 4 passed disposable reviewed create/edit/reconnect/delete plus Undo/Redo; the real imported source note hash was unchanged and the final fixture had 0 Local Model errors. W-395 removed the four mixed-EOL byte drifts found by the preceding run by canonicalizing generated Markdown to LF. Exact-artifact Obsidian startup run `37409833814` remains green. | **Closed.** Definitionless contextual Interfaces are deterministic, traceable, connected and editable through the controlled Local Model 0.4 / Workbench 0.1.18 contract without manufacturing reusable Port/Interface notes. |
| IMP-010 | P1 | 6 | closed | Folded EA Parts that resolve to non-Object semantic definitions must not be invented as structural Local Model Parts | W-396 resolves the 203 Activity/State carrier Parts as note-level Behavior/Condition ownership (`hasChild` / `hasDesign`) with zero Local Model Part occurrences. W-397 resolves the remaining 16 Port-owned signal carrier Parts as strict contextual copies of reusable FlowProperty `Item Flow` definitions: each folds to the FlowProperty UID, reusable `Object/interface` definitions own their FlowProperties through `hasChild` / `childOf`, and direction plus typed Signal/Class remain explicit EA source evidence. No retired Port-note `hasFlow` vocabulary or new Local Model record type is introduced. | **Closed by real-QEAX bridge run `37502083911` on head `2492b64f3e6caf9acf7745c8936b6a43040e964f`.** Two full imports wrote 27,709 notes, **2,055** Local Model Parts, 4,387 Interfaces, 552 Connections and 72 flows; deterministic comparison passed. Gate 1b revalidated all 203 Behavior/Condition carriers. Gate 1c passed with exactly 16 contextual FlowProperty copies (14 `3.3V`/`ps3V3Analog`, 2 `can`/`psCan`), 760 FlowProperty definitions, 752 interface-owned definitions checked, zero Local Model Part occurrences for the 16 copy GUIDs, zero exact-copy Local Model warnings, and zero duplicate folded-Part review GUIDs. Workbench Gates 2–4 passed on the same generated vault. | Closed. Reopen only if a future source Part resolves to a non-Object definition without a deterministic semantic rule, or if a regression reintroduces structural Local Model Parts / duplicate findings for handled carrier rows. |
| IMP-011 | P1 | 6 | decision required | Most BindingConnectors cannot be deterministically reconstructed | Lost contextual topology can make structure/interface views incomplete. | v0.8.3: 249 BindingConnector reviews; 47 temporary local `equals`, 202 unresolved contextual owner/endpoints. | Classify root causes; implement deterministic recoverable groups; keep genuinely ambiguous groups as evidence only. |
| IMP-012 | P1 | 4 | decision required | Folder-capacity rules conflict across current authorities and code | Navigation behavior cannot be considered deterministic/governed while authorities disagree. | `Translator Definition.md` 4.1 says do not split by element count alone; Ruleset 1.23 permits/limits to 75 generated files; v0.8.6 mechanically creates `folder_N`. v0.8.3 model contains 333 `folder_N` directories. | One authoritative folder-capacity/navigation rule is approved and all current docs/code/tests agree. |
| IMP-013 | P1 | 4 | test required | Current naming/path behavior has not been proven on the real QEAX | The v0.8.6 path changes are inherited by v0.8.16, but the last whole-model evidence predates them. | The current lineage removes 212-char length-driven shortening, uses a 400-char hard stop, shortest unique links and long-path review; only synthetic tests are recorded. | Decode/planning/full disposable real-QEAX evidence on v0.8.16 shows expected paths, zero illegal path writes and usable links. |
| IMP-014 | P1 | 8/10 | implementation required | Human review evidence is row-heavy and duplicates root causes | Thousands of rows make systemic issues look larger and make decisions harder. | 1,012 Local Model warning rows represent only 244 unique folded Parts. | Add stable finding/root-cause grouping with unique affected-source counts and representative examples while retaining exhaustive machine evidence. |
| IMP-015 | P1 | 8/10 | implementation required | No checked-in deterministic run-diff/headless acceptance gate yet | Manual review cannot prove equivalent imports or detect subtle drift. | Current Golden Model plan already identifies run diff, determinism and headless validation as release-enabling work. | Same QEAX + same base/importer produces no semantic diff; headless validator checks YAML, links, identity, inverses and Local Model and fails the run on structural errors. |
| IMP-016 | P1 | 7 | test required | Current attachment decoder is not yet proven end-to-end on real QEAX | v0.8.3 failed all attachments; v0.8.5 decode showed path failures; the decoder/path corrections introduced in v0.8.6 are inherited by v0.8.16. | Benchmark target is 376 linked documents / 390 files / zero residual; the real decode-only run is still pending. | Real v0.8.16 decode-only benchmark PASS, then full-run attachment reconciliation matches it. |
| IMP-017 | P1 | 3/5/6 | implementation required | Review output does not clearly separate importer-fixable systemic groups from true Stage-2 engineering decisions | Teams can waste time manually fixing issues that should be corrected once in the importer. | Current semantic, added-Port, nesting, equals and block-flow CSVs are exhaustive but not prioritized by remediation ownership. | Each finding group identifies owner: importer rule/code, source-data defect, or Stage-2/manual engineering review. |
| IMP-018 | P2 | all | deferred | Importer engine, SQLite reader, UI, mapping logic, validators and writer remain one large HTML/JS application | Continued rule growth raises regression risk and makes automated testing harder. | v0.8.6 is roughly 4,700 lines and contains reader, preflight, planner, identity, semantic graph, Local Model, attachments, evidence and filesystem writing. | Pure source-reader/planning/validation modules can run headlessly; browser UI becomes a thin orchestration layer. |

## Real-model evidence summary

Use the v0.8.3 whole-model import in `spencerskelly/261002083` as the current large-scale observation baseline until v0.8.16 is exercised on the same real source.

| Evidence | Observed |
|---|---:|
| Notes written | 30,298 |
| Relationship values | 92,758 |
| Local parts | 2,030 |
| Local endpoints | 2,484 |
| Local connections | 460 |
| Local flows | 53 |
| Relationship endpoint findings | 587 |
| Provisional `tracesTo` | 384 |
| Local Model warning rows | 1,012 |
| Unique folded Parts represented by those Local Model warnings | 244 |
| BindingConnector review rows | 249 |
| BindingConnectors reconstructed as temporary local `equals` | 47 |
| BindingConnectors unresolved | 202 |
| Added-Port source rows | 659 |
| Distinct added/resolved Port notes | 617 |
| Affected reusable blocks | 117 |
| Unnamed instance Ports in Added-Port review | 367 |
| Duplicate-name review rows | 519 |
| Mechanical `folder_N` directories visible in the reference tree | 333 |
| Source diagrams reconciled/deferred | 2,924 |

These numbers are diagnostic evidence, not acceptance thresholds.

## Recommended execution sequence

### Group A — eliminate false-confidence/failure-state risk

1. **IMP-001** — import transaction/completion state.
2. **IMP-003** — multi-level run status.
3. **IMP-004** — source WAL policy.
4. **IMP-005** — initialized destination requirement.
5. **IMP-006** — source fingerprint.

These are small relative to semantic mapping work and make later full-model runs safer and more trustworthy.

### Group B — stop uncertain data from becoming accepted semantics

6. **IMP-002** — canonical-vs-review relationship policy.
7. **IMP-009** — current v0.8.19 real-QEAX validation + checked-in Local Model 0.4 output validator + accepted Workbench 0.1.18 real-vault/edit gates.
8. **IMP-010** — folded non-Object Part groups.
9. **IMP-011** — BindingConnector reconstruction groups.
10. **IMP-017** — classify review ownership.

### Group C — stabilize source governance and navigation

11. **IMP-007** — externalize source profile.
12. **IMP-008** — enforce complete table dispositions.
13. **IMP-012** — resolve folder-capacity authority conflict.
14. **IMP-014** — aggregate evidence by root cause.

### Group D — prove the candidate

15. **IMP-016** — real attachment decode benchmark on v0.8.16.
16. **IMP-013** — real-QEAX v0.8.16 path/link planning evidence.
17. Full disposable v0.8.16 import.
18. **IMP-015** — run diff, deterministic repeat and headless validation.

### Group E — maintainability

19. **IMP-018** only after the correctness/release gates above are stable, unless implementation changes first make the monolithic file a measured blocker.

## Working rule

Do not fix a generated reference vault to make an importer defect disappear. Correct the rule/implementation, rerun at the smallest useful scope, and use the next disposable whole-model import to prove the result.

For each issue completed:
1. resolve the governing rule/decision;
2. update the owning authority;
3. implement;
4. add focused regression evidence;
5. update this register;
6. only then advance to the next systemic group.
