# Importer Issue Register

**Status:** Active correction backlog  
**Baseline date:** 2026-10-05  
**Current candidate:** `EA_to_MDSE_Native_Importer_v0.8.12.html`  
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
| IMP-001 | P0 | 9 | test required | Partial filesystem writes can leave a vault that looks legitimate | v0.8.7 implements W-371 persistent transaction state; browser fault-injection acceptance is still pending. | `IMPORT_IN_PROGRESS` is written before model output, caught failures attempt `IMPORT_FAILED`, the Run Manifest is late, and `IMPORT_COMPLETE` is the final authoritative write. Static ordering/syntax checks pass. | Fault-injection during note and evidence writes proves the state remains failed/in-progress, never authoritative PASS, and the dirty destination is refused on rerun. |
| IMP-002 | P0 | 5/10 | test required | Off-rule/provisional relationships are written into canonical YAML | v0.8.12 implements W-376: reviewed connector mappings are evidence-only and remaining endpoint-invalid/provisional graph edges are suppressed before rendering. | Static syntax/order checks pass; evidence retains reviewed connector GUID/type/endpoints and explicit suppression reason. | Real-QEAX run confirms the canonical graph contains no off-rule/provisional relationships and review evidence remains complete/resolvable. |
| IMP-003 | P0 | 10 | test required | One PASS label conflates mechanical completeness with semantic acceptance | v0.8.8 implements W-372 separate source, plan, write, semantic and acceptance states. | Generic Run Manifest PASS was removed; UI shows WRITE PASS separately and warns when semantic review is required. | Real-QEAX/browser run demonstrates statuses remain distinct through complete and failed writes. |
| IMP-004 | P0 | 1 | test required | SQLite WAL mode is only a warning | v0.8.9 implements W-373 and makes WAL mode a blocking preflight failure. | Static checks confirm `SQLITE_WAL_MODE` is severity `fail` and the old warning form is absent. | Browser test with WAL-mode fixture is blocked before planning; clean checkpointed QEAX proceeds. |
| IMP-005 | P0 | 0 | test required | Destination does not require initialized `vault_uid` | v0.8.10 implements W-374 and rejects missing/blank/`UNINITIALIZED` vault identity. | Static syntax/source checks pass. | Browser selection rejects an uninitialized base and accepts the same compatible base after governed initialization. |
| IMP-006 | P0 | 1/2 | test required | Source file lacks a strong recorded fingerprint | v0.8.11 implements W-375 streaming standard SHA-256 and persists it in preflight, transaction and manifest evidence. | Exact embedded hash implementation passes standard empty/`abc`/split-update vectors. | Real QEAX produces one digest copied identically into all three evidence locations and a changed byte produces a different digest. |
| IMP-007 | P1 | 2 | implementation required | Exact EA8647 source counts are compiled into the importer engine | Legitimate source-model evolution currently requires modifying executable code; engine behavior and source snapshot policy are coupled. | v0.8.6 constants contain all expected table/object/connector/diagram counts and `SOURCE_MODEL_ID="EA8647"`. | Introduce a versioned machine-readable source contract/profile loaded/validated by the generic importer engine. |
| IMP-008 | P1 | 2 | implementation required | Not every discovered/non-empty QEAX table is executable-gated by disposition | A future EA feature can start storing useful data in a previously empty/ignored table without necessarily becoming a hard review. | Source inventory includes tables such as tests/scenarios/risks/problems/tasks; executable preflight strongly count-gates only selected importer-used tables. | Every discovered table has a known disposition; newly non-empty governed/ignored tables fail or require explicit approval. |
| IMP-009 | P1 | 6 | implementation required | Local endpoint schema forces reusable Port definitions | W-377 decides that contextual endpoints may exist without reusable Port definitions, but only under new Local Model schema 0.3; schema 0.2 remains unchanged. | v0.8.3 Added Ports: 659 instance-Port rows, 617 distinct generated/resolved Port notes, 117 affected blocks, 367 unnamed ports. v0.8.12 still creates/suppresses endpoints to satisfy 0.2. | Add coordinated Local Model 0.3 + Workbench support, then update the importer so deterministic existing Port definitions are reused but unresolved contextual endpoints are preserved locally without manufactured Port notes. Targeted tests must prove topology survives and 0.2 compatibility is unchanged. |
| IMP-010 | P1 | 6 | implementation required | Folded Parts that resolve to non-Object definitions cannot be represented as Local Model parts | Contextual structure is retained only as warning/source evidence, limiting usable architecture reconstruction. | v0.8.3: 244 unique folded EA Parts affected — 142 resolve to Function, 61 Design, 25 Port, 16 Item Flow. | Decide which are source-model defects vs importer/model-schema cases; group and resolve deterministic cases without inventing semantics. |
| IMP-011 | P1 | 6 | decision required | Most BindingConnectors cannot be deterministically reconstructed | Lost contextual topology can make structure/interface views incomplete. | v0.8.3: 249 BindingConnector reviews; 47 temporary local `equals`, 202 unresolved contextual owner/endpoints. | Classify root causes; implement deterministic recoverable groups; keep genuinely ambiguous groups as evidence only. |
| IMP-012 | P1 | 4 | decision required | Folder-capacity rules conflict across current authorities and code | Navigation behavior cannot be considered deterministic/governed while authorities disagree. | `Translator Definition.md` 4.1 says do not split by element count alone; Ruleset 1.23 permits/limits to 75 generated files; v0.8.6 mechanically creates `folder_N`. v0.8.3 model contains 333 `folder_N` directories. | One authoritative folder-capacity/navigation rule is approved and all current docs/code/tests agree. |
| IMP-013 | P1 | 4 | test required | v0.8.6 naming/path behavior has not been proven on the real QEAX | v0.8.6 materially changed path behavior after the v0.8.3/v0.8.5 evidence. | v0.8.6 removes 212-char length-driven shortening, uses 400-char hard stop, shortest unique links and long-path review; only synthetic tests are recorded. | Decode/planning/full disposable real-QEAX evidence shows expected paths, zero illegal path writes and usable links. |
| IMP-014 | P1 | 8/10 | implementation required | Human review evidence is row-heavy and duplicates root causes | Thousands of rows make systemic issues look larger and make decisions harder. | 1,012 Local Model warning rows represent only 244 unique folded Parts. | Add stable finding/root-cause grouping with unique affected-source counts and representative examples while retaining exhaustive machine evidence. |
| IMP-015 | P1 | 8/10 | implementation required | No checked-in deterministic run-diff/headless acceptance gate yet | Manual review cannot prove equivalent imports or detect subtle drift. | Current Golden Model plan already identifies run diff, determinism and headless validation as release-enabling work. | Same QEAX + same base/importer produces no semantic diff; headless validator checks YAML, links, identity, inverses and Local Model and fails the run on structural errors. |
| IMP-016 | P1 | 7 | test required | Attachment decoder v0.8.6 is not yet proven end-to-end on real QEAX | v0.8.3 failed all attachments; v0.8.5 decode showed path failures; v0.8.6 changed both decoder acceptance and path behavior. | Benchmark target is 376 linked documents / 390 files / zero residual; v0.8.6 requires the benchmark but real decode-only run is still pending. | Real decode-only benchmark PASS, then full-run attachment reconciliation matches it. |
| IMP-017 | P1 | 3/5/6 | implementation required | Review output does not clearly separate importer-fixable systemic groups from true Stage-2 engineering decisions | Teams can waste time manually fixing issues that should be corrected once in the importer. | Current semantic, added-Port, nesting, equals and block-flow CSVs are exhaustive but not prioritized by remediation ownership. | Each finding group identifies owner: importer rule/code, source-data defect, or Stage-2/manual engineering review. |
| IMP-018 | P2 | all | deferred | Importer engine, SQLite reader, UI, mapping logic, validators and writer remain one large HTML/JS application | Continued rule growth raises regression risk and makes automated testing harder. | v0.8.6 is roughly 4,700 lines and contains reader, preflight, planner, identity, semantic graph, Local Model, attachments, evidence and filesystem writing. | Pure source-reader/planning/validation modules can run headlessly; browser UI becomes a thin orchestration layer. |

## Real-model evidence summary

Use the v0.8.3 whole-model import in `spencerskelly/261002083` as the current large-scale observation baseline until v0.8.6 is exercised on the same real source.

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
7. **IMP-009** — implement W-377 Local Model 0.3 definition-optional contextual endpoints.
8. **IMP-010** — folded non-Object Part groups.
9. **IMP-011** — BindingConnector reconstruction groups.
10. **IMP-017** — classify review ownership.

### Group C — stabilize source governance and navigation

11. **IMP-007** — externalize source profile.
12. **IMP-008** — enforce complete table dispositions.
13. **IMP-012** — resolve folder-capacity authority conflict.
14. **IMP-014** — aggregate evidence by root cause.

### Group D — prove the candidate

15. **IMP-016** — real attachment decode benchmark.
16. **IMP-013** — real-QEAX v0.8.6 path/link planning evidence.
17. Full disposable v0.8.6 import.
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
