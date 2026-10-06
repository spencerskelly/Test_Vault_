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
| IMP-003 | P0 | 10 | test required | One PASS label conflates mechanical completeness with semantic acceptance | v0.8.8 implements W-372 separate source, plan, write, semantic and acceptance states. | Generic Run Manifest PASS was removed; UI shows WRITE PASS separately and warns when semantic review is required. | Real-QEAX/browser run demonstrates statuses remain distinct through complete and failed writes. |
| IMP-004 | P0 | 1 | test required | SQLite WAL mode is only a warning | v0.8.9 implements W-373 and makes WAL mode a blocking preflight failure. | Static checks confirm `SQLITE_WAL_MODE` is severity `fail` and the old warning form is absent. | Browser test with WAL-mode fixture is blocked before planning; clean checkpointed QEAX proceeds. |
| IMP-005 | P0 | 0 | test required | Fresh generated base is reported incompatible until initialized outside the importer | A distributed base must ship with `vault_uid: UNINITIALIZED`, but v0.8.16 rejected that valid fresh-base state at selection time. | v0.8.16/W-381 accepts and fully validates an uninitialized fresh base for selection, keeps model generation blocked, performs explicit in-tool initialization from vault name + governed 13-character author code, then re-runs strict initialized-base validation before enabling writes. | Browser test proves fresh-base selection succeeds, generation is blocked before initialization, a unique 30-character UID is created, `mdse_release`/schema/plugin identity is preserved, and only then can import proceed. |
| IMP-006 | P0 | 1/2 | test required | Source file lacks a strong recorded fingerprint | v0.8.11 implements W-375 streaming standard SHA-256 and persists it in preflight, transaction and manifest evidence. | Exact embedded hash implementation passes standard empty/`abc`/split-update vectors. | Real QEAX produces one digest copied identically into all three evidence locations and a changed byte produces a different digest. |
| IMP-007 | P1 | 2 | implementation required | Exact EA8647 source counts are compiled into the importer engine | Legitimate source-model evolution currently requires modifying executable code; engine behavior and source snapshot policy are coupled. | The current v0.8.13 lineage retains the compiled EA8647 source-count contract and `SOURCE_MODEL_ID="EA8647"`. | Introduce a versioned machine-readable source contract/profile loaded/validated by the generic importer engine. |
| IMP-008 | P1 | 2 | implementation required | Not every discovered/non-empty QEAX table is executable-gated by disposition | A future EA feature can start storing useful data in a previously empty/ignored table without necessarily becoming a hard review. | Source inventory includes tables such as tests/scenarios/risks/problems/tasks; executable preflight strongly count-gates only selected importer-used tables. | Every discovered table has a known disposition; newly non-empty governed/ignored tables fail or require explicit approval. |
| IMP-009 | P1 | 6 | test required | Local endpoint schema forces reusable Port definitions | W-377/W-378 define and implement Local Model 0.3 definition-optional contextual endpoints while freezing schema 0.2 semantics. v0.8.13 no longer synthesizes reusable Port notes when deterministic definition evidence is absent. | Historical v0.8.3 Added Ports: 659 instance-Port rows, 617 distinct generated/resolved Port notes, 117 affected blocks, 367 unnamed ports. v0.8.17 static/source/syntax checks pass; W-380 now preserves the exact EA source Object_ID and W-377 connector review reason, and `imp009_output_acceptance.py` is checked in; Workbench PR #4 CI passes schema-0.3 compatibility. | `Importer/Testing/v0.8.14/IMP-009 Real-QEAX Acceptance Runbook.md` passes end-to-end: fresh whole-model real-QEAX output passes the checked-in validator, topology/connector evidence is exercised and traceable, no synthetic Port notes are emitted, and Workbench 0.1.17 reads/edits/reloads the schema-0.3 result. |
| IMP-010 | P1 | 6 | implementation required | Folded Parts that resolve to non-Object definitions cannot be represented as Local Model parts | Contextual structure is retained only as warning/source evidence, limiting usable architecture reconstruction. | v0.8.3: 244 unique folded EA Parts affected — 142 resolve to Function, 61 Design, 25 Port, 16 Item Flow. | Decide which are source-model defects vs importer/model-schema cases; group and resolve deterministic cases without inventing semantics. |
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
7. **IMP-009** — fresh real-QEAX validation of v0.8.16 + checked-in output validator + Workbench Local Model 0.3.
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
