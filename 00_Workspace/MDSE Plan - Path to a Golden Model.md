# MDSE Plan: Path to a Golden Model

**Status: current plan (W-338), 2026-10-03.** This is the working plan from today's tools to a **golden** model: the vault the team uses as the single authoritative engineering model after EA is retired. Rules live in the authority files named in [[00 - Current State]]; this plan says what to do, in what order, and how to know a step is done. Items marked **proposal** are not decisions until logged as `W-n` or `WB-n`. Update this file in the same commit as any decision that changes a step.

## 1. What "golden" means (proposal, confirm as D1)

A model is golden when all of these hold:

1. It was produced by a **released matched set**: importer marked release-conformant in `mdse-release.yaml`, an issued clean 0.8.0 base, a WB-106 Workbench pinned in that base (`wb106Version` set), and MDSE Bootstrap passing the [[Base First-Open Test Sheet]] on macOS and on Windows.
2. The import run passed every check in [[Translator Definition]] section 10, with its evidence package kept (section 5 below).
3. Every task in [[Post-Import Tasks]] meets its "Done when" line, each change with a row in [[Review Changes Log]].
4. The model checks in section 7 report zero errors, and every remaining warning is either fixed or on an accepted list.
5. A sampled comparison against EA has been signed off (section 7, item 8).
6. It is tagged in git as a baseline, and the EA `.qeax` it came from is archived read-only with its checksum.

Until then every vault is a **candidate**. A candidate may be thrown away and regenerated at any time.

## 2. Where things stand

| Component | Version | State |
|---|---|---|
| Importer | v0.8.19 accepted candidate | Deterministic real-QEAX whole-model output completed with `IMPORT_COMPLETE`; W-384/W-385 Local Model 0.4 output passed bounded Workbench acceptance. Importer release conformity is still pending. |
| Base vault | 0.8.0 candidate, not issued | A Bootstrap-0.3.1 candidate base built successfully on 2026-10-03 and `check-release.py --base` completed with **0 fail / 4 expected pre-release warnings**. Initializer defects found during the dry run were fixed and shell syntax is release-gated (W-336). OS metadata is excluded from governed builds (W-338). |
| Workbench | **0.1.18 controlled WB-106 release** | WB-128 Local Model 0.4 read/validate/write/view compatibility passed real-vault Gates 1–4 and exact-artifact startup acceptance; Base pin/payload/lock aligned under W-386. |
| Bootstrap | 0.3.0 runtime / 0.3.1 candidate | 0.3.1 builds successfully on the development Mac and all 9 tests pass. Candidate payload/lock validation passes. First-open activation/persistence remains the promotion gate and is deferred to the next integrated candidate (W-337). |

### Run log

Add one row per real run. "Decision" is accept-for-review, restart (fix rules, rerun) or keep (section 6).

| Date | Tool | Kind | Result | Decision and next step |
|---|---|---|---|---|
| 2026-10-02 | v0.8.3 | whole model | 30,298 notes, 2,030 parts, 2,484 endpoints, 460 connections, 53 flows; preflight and plan PASS. All 376 attachments failed: EA stores linked documents as ZIP. | Restart. Decoder fixed in v0.8.4, hardened in v0.8.5 (W-323). |
| 2026-10-02 | v0.8.5 | decode-only | 376 decoded, 367 OK, 9 `PATH_ERROR` (attachment paths 221 to 262 characters over the old 212 limit); benchmark file not loaded. | Restart. W-324 removed length-driven rules (v0.8.6); decode-only now refuses to run without the benchmark. |
| 2026-10-03 | Workbench 0.1.17 + WB-114 editor expansion | implementation | 0.1.17 completed the original occurrence-aware read/navigation gate. WB-114 to WB-122 establish the structured-editor architecture and initial core services; no new base pin yet. | Continue editor surface/structural transactions, then release-align with importer v0.8.6 before creating the integration vault (W-337, W-339). |

### Current stopping point — 2026-10-05

Workbench WB-128/WB-106 release alignment is complete at 0.1.18. The deterministic v0.8.19 real-QEAX candidate has passed Workbench compatibility acceptance, but MDSE 0.8 is not yet G2: importer release conformity, clean-base issuance and Bootstrap first-open/OS acceptance remain. Do not add more standalone Workbench hardening unless new evidence exposes a regression; move to those remaining G2 gates.

**Importer release-conformity progress:** W-387 through W-392 close **all P0 IMP-001 through IMP-006**. Transaction integrity, canonical relationship suppression, write-vs-semantic status separation, WAL-source integrity, fresh-base initialization, and strong source fingerprinting all have automated acceptance evidence. IMP-006 artifact-reuse run `37420398404` proves the exact accepted QEAX SHA-256 is identical in preflight, transaction state and Run Manifest, while a one-bit virtual change produces a different digest; no new import was required. Normal importer/package CI on the same head passes (`37420404557`, `37420404553`). Continue the remaining release-blocking **P1** register in priority order; next is IMP-007. `tools.importer.release` remains unset until that bounded register is resolved or explicitly accepted.

## 3. Gates

| Gate | Passed when | Owner |
|---|---|---|
| G0 Run ready | Section 4 checklist done | Spencer |
| G1 Run accepted for review | Translator Definition checks 1 to 10 pass; attachment benchmark PASS; Workbench Local Model report read | Spencer, with Claude reading the evidence |
| G2 Keepable set | Importer release-conformant, WB-106 released and pinned, clean base issued, Bootstrap first-open passed on macOS and Windows, determinism shown (I2) | Spencer decides; tools prove |
| G3 Keep (freeze point) | A run made with the G2 set passes G1 and the rule-level post-import decisions are in the importer (section 6) | Spencer |
| G4 Golden | Section 7 checklist complete | Spencer, plus one engineer per discipline for the sample |
| G5 Team rollout | Section 8 done | Spencer |

## 4. Before the next run (G0)

1. **Revoke the GitHub tokens** pasted into earlier chats; issue fresh per-repo tokens when a chat needs one.
2. **Check Obsidian on the Mac.** The base requires Obsidian 1.13.0 or later (`obsidianMinVersion` in `.obsidian/plugin-lock.yaml`). Newer Obsidian builds can drop older macOS versions; confirm 1.13.0 or later installs and starts on this Mac before relying on it for first-open tests. If it does not, record it as a risk and decide whether the lock's minimum can be lower.
3. **Build a fresh base artifact:** `python3 "Base Vault/Tools/v0.8.0-r2/build-base.py" <empty folder>`, then `python3 "Base Vault/Testing/check-release.py" --base <that folder>`. It must report 0 fail. At this stage `vault_uid` is intentionally `UNINITIALIZED` and there is no `.git` repository (W-334).
4. **Prepare the candidate model repository:** copy/use that validated artifact, run `Initialize-Vault.sh` or `Initialize-Vault.ps1` once, initialize/connect Git for the candidate repository, and commit the clean initialized starting point. Ordinary engineers never perform this release-owner step.
5. **First-open on the Mac:** open the initialized candidate repository in Obsidian and run the macOS rows of `Bootstrap/Testing/Base First-Open Test Sheet.md`. Record date and result in the sheet.
6. **Decode-only check:** use the current v0.8.19 importer and its governed attachment benchmark, load the `.qeax`, preflight, build the plan, and run **Decode-only attachment check**. Expected: `docs 376/376 | files 390/390 | residual 0 | PASS`. If not PASS, stop and bring the CSV back.
7. **Whole-model run** into the initialized candidate repository.
8. **In the imported vault:** Workbench 0.1.18 **Rebuild index**, then **Check Local Model (write findings report)**, then the current steps at the end of `MDSE_Workbench/docs/Testing/06 - Test Sheet.md`. Note the Review screen counts.

## 5. Every run (G1): what to check and bring back

Bring back to the next chat (all in the imported vault's `99_System/11_Import`):
- `Run Manifest.md`, with the attachment benchmark line and the link counts (by name, by path);
- `Attachment Reconciliation.csv`;
- `Review - Long Paths.csv` (first rows and the count);
- counts from `Review - Altered Names and Paths.csv` and `Review - Duplicate Names.csv`;
- `Source Count Reconciliation.csv` and the terminal summary of `Ledger.csv`;
- `Diagram Reconciliation.csv` counts (every diagram deferred, none unreconciled);
- `Workbench Views/Local Model Findings.md` (counts, finding-code table, seconds);
- the Workbench Review screen counts (provisional, missing inverse, orphan inverse, off-rule, broken references);
- anything that looked wrong when you browsed.

Decide: **accept for review** (browse it, collect rule changes), **restart** (change rules, new fresh base, rerun) or, only after G2, **keep** (section 6). Record the decision in the run log above. Every rule change is a `W-n` decision and reaches the importer before the next run (W-36, W-37).

## 6. The freeze point (G3) and why order matters

The importer is a clean-import tool: it writes into a fresh base and is never run over a vault people have edited. So there are two kinds of fix:

- **Rule-level fixes** change the importer and take effect by re-importing. They are cheap and repeatable while no one has edited a candidate by hand.
- **Note-level fixes** are edits in the vault, one reviewed commit each. A fresh import would discard them.

Therefore: make every fix that a rule can make **before** keeping a run, then keep (freeze), then do the note-level work. After the freeze, a rule change can no longer be applied by re-importing; it becomes a scripted or manual change in the kept vault.

**Rule-level work to finish before the freeze** (each decided in groups, logged, put in the importer):
- [[Post-Import Tasks]] Task 5 items 1 and 2 (which tag lines become properties; the `Heading` value).
- Task 7 groups that a rule can settle (`modelCheck` groups by EA type, `hasClassifier` replacements by pattern, `hasChild` versus `includes` by pattern).
- Task 4's folding policy (which documents fold), if folding is to be done by the importer rather than by hand.
- Task 9's path rules, if the team path limit is known by then (D4). Otherwise Task 9 stays post-import as decided in W-324.
- Task 2's decision on third-party standards content. It must come before the freeze: removing content after the vault is pushed leaves it in git history, and a history rewrite after the team has cloned is disruptive.

**Note-level work after the freeze:** Tasks 1, 3, 6 and 8, the per-note parts of Tasks 4, 5 and 7, and Task 9 renames if not done by rule.

## 7. Golden checklist (G4)

1. Kept run met G1 with the G2 set; evidence package stored in `99_System/11_Import` and committed.
2. All [[Post-Import Tasks]] done, each with log rows.
3. **Links:** every link resolves (Workbench Review "broken references" 0; headless validator I3 0).
4. **Identity:** no duplicate `uid`, `id` or path; no identity-token collision (Workbench report `identity.collision` 0); Local Model Source Map committed.
5. **Relationships:** missing inverse 0; orphan inverse 0; off-rule 0 or each on an accepted list in the Decision Log; `tracesTo` 0 (W-288) or accepted.
6. **Local Model:** Workbench report errors 0; temporary `equals` 0 unless an approved unresolved-review policy says otherwise (Task 8).
7. **Paths:** every path within the team limit set in Task 9; Bootstrap path check (S2) passes on a Windows machine at the agreed vault location.
8. **Sample against EA:** for each class, a random sample (proposal: 20 notes per class, 50 for Requirement and Port) compared with EA for name, type, text, properties and relationships; one engineer per discipline (electrical, mechanical, software) signs off their part. Findings fixed or logged.
9. **Performance:** the vault opens and Workbench indexes on the slowest team machine within agreed limits (proposal: open under 60 s, index under 60 s, Check Local Model under 120 s).
10. **Baseline:** git tag (proposal `model-v1.0.0`), release note, `.qeax` archived read-only with SHA-256 recorded, `main` protected, CI checks on (X2).

## 8. Team rollout (G5)

1. Run the [[Base First-Open Test Sheet]] on a team Windows machine at the agreed vault location (D4).
2. Pilot (Workbench gate R1): two or three engineers work in the golden vault for an agreed period; collect findings.
3. Author registration for each engineer through Bootstrap (people notes in `99_System/04_People`).
4. Branch and review rules for model changes; who may merge.
5. EA retired: read-only, kept for reference; no new modeling in EA (EA is used for fixes only until then).
6. Repository clean-up (X3).

## 9. Improvements by component

Priority: **P1** needed for G2/G3; **P2** needed for G4/G5; **P3** after golden.

### Importer

| # | P | Item | Done when |
|---|---|---|---|
| I1 | P1 | **Run-to-run diff report:** compare a run with the previous one (notes added, removed, renamed, changed by field; Source Map changes). Turns "review it and record what changed" into a generated report. | Two runs produce `Review - Run Diff.csv` and a summary in the Run Manifest |
| I2 | P1 | **Determinism check:** two runs from the same `.qeax` into two fresh bases are identical except run timestamps. Proves identity cannot drift between candidate and keep. | I1 reports zero differences for a repeated run |
| I3 | P1 | **Headless validator** run after writing (shared with X1): links resolve, unique `uid`/`id`/path, YAML parses, inverses consistent, Local Model valid. | Validator result is in the Run Manifest; a failing run is marked FAIL |
| I4 | P1 | **Automated tests in the repo:** the decode, path-planning and link-target tests used for v0.8.5 and v0.8.6 checked in under the importer folder and run by CI. Longer term (P2): move the pure planning code out of the HTML into a tested module. | `node` test command passes in CI |
| I5 | P1 | **Release:** set `tools.importer.release` in `mdse-release.yaml` and freeze that file once G2 passes. | `check-release.py` reports a release-conformant importer |
| I6 | P1 | Rule-level post-import decisions put into the importer (section 6). | Each logged `W-n` is implemented before the keep run |
| I7 | P2 | Rerun-ownership tests (Source Map authority, preserved human edits) if reruns over a kept vault are ever needed. Not needed if the freeze rule is followed. | Decide first (D3) |
| I8 | P3 | Additive diagram pass (W-300, W-301): canvases by EA diagram type after the keep. | Decide whether diagrams are needed for golden (D2) |
| I9 | P3 | Move the importer to its own repository with tagged releases (keeps version folders out of the methodology workspace). | Part of X3 |

### Base vault

| # | P | Item | Done when |
|---|---|---|---|
| B1 | P1 | Fresh base per run, first-open test on the Mac each release. | Sheet rows recorded |
| B2 | P1 | Confirm Obsidian 1.13.0+ on the team's machines (section 4 item 2). | Recorded per machine |
| B3 | P2 | Issue the clean 0.8.0 base repository (`tools.cleanBase.repo`) from `build-base.py` once G2 passes; never hand-curated. | Repo exists, `check-release.py --base` passes on it |
| B4 | P2 | Decide the folder-stub rule: Ruleset 1.23 section 9 asks for `00 - Views and Bases`, `00 - Folder Contents` and `00 - Folder Map` in model-facing folders; the 24 existing stubs in `99_System` are empty, and Workbench generates views instead. (D7) | Rule kept, changed, or removed; stubs follow it |
| B5 | P2 | Performance on the slowest machine with the real vault (Dataview, Breadcrumbs, Nodian, Fileclass). | Numbers recorded against section 7 item 9 |
| B6 | P3 | Vault size budget and pruning against it. | Budget set |

### Workbench (next chat)

| # | P | Item | Done when |
|---|---|---|---|
| W1 | P1 | **Original occurrence-aware WB-106 baseline.** Structure, Interfaces, Where Used, Requirements, local Canvas nodes, read-only local details and Review integration. | **Implemented in standalone 0.1.17 candidate (WB-113).** Validate again on the next real import. |
| W2 | P1 | **Structured editor foundation (W-339/WB-114).** Pure transaction/history core, Local Model 0.2 patch/create planners, governed identity allocator, Obsidian storage adapter, one semantic undo/redo history. | **Foundation implemented through WB-122; editor surface not released yet.** |
| W3 | P1 | **Internal Structure (W-340/WB-123).** One occurrence-owning Object as a boundary; parts/endpoints/connections/flows inside; compact boundary interfaces; curated layout is presentation only and preserved on refresh. | Core layout is on standalone main; visually validate on representative assemblies and confirm refresh preserves manual placement. |
| W4 | P1 | **Occurrence/context editor.** Local data first; full reusable Definition under a dropdown; definition relationships nested; definition edits use a separate canonical-note mode. | Edit real part/endpoint/connection/flow records without raw Markdown and preserve ownership boundaries. |
| W5 | P1 | **Guided structural transactions.** Multi-object edits stage Review/Apply/Cancel, allow temporary invalidity, and block Apply on required integrity failures; lifecycle/impact review follows schema rules. | Restructure/reconnect a representative assembly with validation, cancel and semantic undo/redo. |
| W6 | P1 | **Release — COMPLETE (W-386):** Workbench 0.1.18 is merged, built, real-vault accepted, vendored, locked and set as `wb106Version`; the bounded Gate-5 workflow runs `check-release.py --workbench`. | Base pins the expanded WB-106 release. |
| W7 | P1 | Measure index, views, Local Model checks and editor operations on the real import (and on the slowest machine). **CI/real-import evidence is complete:** Gate 2 read-only scan 11.063 s / 236 MiB; Gate 3 representative views 5.111 s / 278 MiB; Gate 4 edit transactions 78 ms / 89 MiB. Physical slowest-machine validation remains B5/G4. | Numbers in the Workbench Decision Log. |
| W8 | P2 | **Headless CLI** over the pure core (`src/core`): the same checks without Obsidian, for I3 and CI (X1). | `node` command validates a vault folder. |
| W9 | P2 | Batch review (M3/M4) sized to the finding counts from the first kept run; region-aware body editing outside the governed region. | Exit criteria in Workbench roadmap. |
| W10 | P3 | W-314 persisted configuration/variation and broader Canvas gestures beyond the base editor. | Separate approved scope after the expanded WB-106 gate. |
| W11 | P1 | **Runtime architecture RTA-1/RTA-2 (W-343/W-344).** Explicit startup/ready state; persistent disposable semantic cache; vault/parser/schema binding; bounded crash-safe A/B slots; save-only persistence; inspection/recovery path; shared Local Model index. | **Source implemented through save-only runtime boundary.** Build/typecheck + real-vault acceptance still required before promotion. |
| W12 | P1 | **Warm restore and incremental reconciliation RTA-3.** Restore compatible semantic state, reconcile small stable-path content changes in bounded batches, and conservatively full-rebuild on path-set or large-burst changes. | **Opt-in preview source implemented; OFF by default.** Pass `RTA Startup and Semantic Cache Test Sheet` plus build gate before default enablement. |
| W13 | P2 | **Validation scheduling RTA-4.** Immediate dependency-scoped checks after edits; expensive global assurance jobs explicit/idle; Review exposes freshness. | Opening the vault never blocks on exhaustive validation. |
| W14 | P2 | **Runtime/view consolidation RTA-6/RTA-7.** Physical, Internal, Functional and other views query one semantic model service; remove duplicate parsing paths; run corruption/interrupt/slow-machine/OS gates and review third-party plugin dependencies. | One shared semantic interpretation drives views and recovery/performance gates pass. |

**Workbench continuation status — 2026-10-05.** The numbered stability roadmap remains closed at Step 60. Expanded WB-106 editor work is active under W4/W5. WB-128 Local Model 0.4 compatibility is implemented as Workbench 0.1.18 candidate on PR #5. CI run `37401786417` passes the full test, 60k semantic-cache, warm-start, relationship re-resolution, build, and artifact-hash gate. Local Model 0.1–0.3 remain readable but read-only for structured mutation; 0.4 writes `Parts`, `Interfaces`, and `Connections`, with `Connection.exposes` owning boundary exposure. The next gate is real-vault acceptance against the deterministic v0.8.19 import before WB-128 is merged, pinned, or promoted. WB-125 legacy-writer identity-symmetry work remains subsequent editor-safety backlog unless real-vault validation exposes a higher-priority regression.

**WB-128 real-vault acceptance — bounded 5-gate plan (2026-10-05).** Keep this validation off the interactive workstation and avoid whole-vault materialization in chat. The deterministic v0.8.19 run (Actions run `37399169045`) creates the 27,709-note candidate only in runner temporary storage; the retained `v0819-full-import-evidence` artifact contains import evidence, not the full generated vault. Acceptance therefore proceeds in the same GitHub Actions environment:
1. **Provenance/persistence check — COMPLETE.** Confirm importer 0.8.19, MDSE 0.8.0, relationships 1.36, element-types 1.18, Local Model 0.4, `IMPORT_COMPLETE`, and the deterministic source hash/counts without indexing the vault.
2. **Read-only Workbench real-vault scan — COMPLETE.** CI run `37405466855` regenerated the deterministic v0.8.19 candidate, reran the deterministic comparison, and executed the bounded Workbench 0.1.18 scanner with a 1 GiB Node memory ceiling and 10-minute hard timeout. Result: **PASS** in 11.063 s at 236 MiB RSS across 27,813 Markdown files. It parsed 803 Local Model regions, all schema 0.4, with 2,055 Parts, 4,387 Interfaces, 552 Connections, 72 flows, 1,051 definitionless Interfaces, and 23 `Connection.exposes` relationships. There were 0 parser errors, 0 blocking compatibility findings, 0 broken local block references out of 3,439 checked, 0 duplicate local IDs, and no legacy first-class Port notes/fields. One non-gating diagnostic counter (`unresolvedRelationshipLinks`) serialized as `null` because the scan harness treated a numeric result as an array length; the counter was corrected in Workbench commit `f51ed792f641077f3c68a426170d3b281f5590ca` and was not rerun through another full import because it did not affect any acceptance criterion. The legacy all-in-one acceptance workflow was found to hide failures behind `tee` and to rebuild/upload the full 28k-note vault on ordinary pushes; it is now manual-only with pipe failure propagation.
3. **Representative view checks — COMPLETE.** Gate 3 reused the retained deterministic v0.8.19 vault artifact instead of rerunning the importer and rendered only a deterministic minimum-size sample set. Actions run `37407337814` passed in 5.111 s at 278 MiB RSS across the indexed 27,813-file vault, with no Canvas files written. Structure: `Charger Context.md` rendered 6 visible Parts. Interfaces/Internal: `PCBA - PCE Adapter.md` rendered 12 Interfaces, 7 Connections, 15 local edges and 1 `Connection.exposes` edge; the Internal canvas data stayed bounded at 30 nodes / 8 edges. Conveyed flow: `Product.md` rendered 1 real flow. Definitionless Interface: `PCBA - Expansion.md` retained 1 contextual definitionless Interface. Where Used: the Charger definition correctly surfaced the selected Charger Context Part occurrence. Gate 3 had 0 failures. Workbench harness commit `b23a4bc94709e0473675e6e6d526f94f1f0cd146` also passes Workbench CI run `37407331582`.
4. **Representative edit checks on copies — COMPLETE.** Gate 4 reused the retained deterministic v0.8.19 artifact and copied only `PCBA - PCE Adapter.md` into a temporary fixture. Actions run `37407768954` passed the Workbench 0.1.18 structured-edit transaction path in 78 ms at 89 MiB RSS under a 512 MiB / 2-minute safety limit. The test created a disposable definitionless Interface and disposable Connection, verified structural Apply is rejected before Review, then exercised Review/Apply plus semantic Undo/Redo for create, patch, reconnect, Connection delete and Interface delete. A separately staged create was Cancelled and proved to change neither fixture content nor semantic history. Reconnect moved only the disposable Connection between two real imported Interfaces (`~J5 24VDC In` and `~J5 CAN`). The final fixture remained structured Local Model 0.4 with 0 error findings and six semantic-history entries. Most importantly, the real imported source note SHA-256 was `540c8e86374a44c88f1a2c0bfe863df04b536f57de7da9884a60690c65ece233` both before and after: the acceptance candidate was never mutated. Workbench harness commit `623a4d64d3d42c474397cba342472f49c778fcd1` passes full Workbench CI run `37407660514`.
5. **Acceptance decision — COMPLETE.** Gates 1–4 found no blocking Local Model 0.4 incompatibility. Workbench PR #5 merged at `e2364cabd97118c9e9cc359ad5404620309092cc`; the controlled 0.1.18 artifact is `b0c4e2c6bdfb96d36f51d8152b17be22592ef174`. Main build/scale gates pass, and exact-artifact startup run `37408519667` accepted 12,000 notes at 1.414 s readable and 30.010 s core/occurrence ready. W-386 pins 0.1.18 in the Base payload/lock and sets `wb106Version`. MDSE remains pre-release until the non-Workbench G2 gates complete.


### Bootstrap

| # | P | Item | Done when |
|---|---|---|---|
| S1 | P1 | Run the [[Base First-Open Test Sheet]] on macOS. | Rows recorded |
| S2 | P2 | **Proposal:** at first open on Windows, compare the vault folder's path length plus the longest path in the vault with the 260-character limit and warn before Git or Obsidian hit it. Ties to Task 9 and D4. | Decided; built if yes |
| S3 | P2 | Author registration tried by a second person. | A second author is registered and creates a note with the right `uid` |
| S4 | P2 | First-open test on Windows. | Rows recorded |

### Cross-cutting

| # | P | Item | Done when |
|---|---|---|---|
| X1 | P2 | **Shared core:** one schema loader, Local Model parser, link and identity rules used by Workbench, the headless validator and later the importer. Workbench's `src/core` is the starting point. | Importer validation (I3) runs on it |
| X2 | P2 | **CI** (GitHub Actions): `Test_Vault_` runs `check-release.py`, `update-plugin-lock.py --check` and the importer tests; `MDSE_Workbench` runs typecheck, tests and build (its `ci-workflows/` are prepared but not enabled). Needs your go (D6). | Both repos show checks on push |
| X3 | P2 | **Repository layout** before rollout (you planned to rebuild repos once the import is settled). Proposal: methodology authority (today `Test_Vault_`), `MDSE_Workbench`, importer repo (I9), and one model repository created from the issued base for the keep run; mark `20260930`, `261001` and the old base repo archived on GitHub. | Layout decided and done |
| X4 | P3 | Split the Workspace Decision Log by period (the file is several hundred KB); keep the current period in `10_Docs`, earlier periods in the archive. | Split done, links still resolve |

### After golden (direction, not commitment)

From the 2026-10-02 roadmap proposal (archived): team daily driver with pull requests and semantic diffs, baselines as tags, Canvas edit and variants (W-314); a headless platform (CLI, MCP server) so AI tools query and propose changes; generated outputs (traceability matrices, interface control documents, requirement specifications, FMEA tables, compliance coverage); a digital thread to Jira, Confluence, test results and BOM data; shared libraries across MHE, GSE, EVSE and PCE.

## 10. Decisions needed

| # | Question | Needed by |
|---|---|---|
| D1 | Confirm the golden definition (section 1) and checklist (section 7). | G2 |
| D2 | Are EA diagrams (as canvases, W-300/W-301) required for golden, or added after? | G4 |
| D3 | Confirm the freeze rule (section 6): no reruns over a kept vault, so rerun-ownership tooling (I7) is not built. | G3 |
| D4 | Team path limit and the standard vault location on Windows (Task 9, S2). | Task 9 |
| D5 | Third-party standards content in attachments (Task 2), including the git history question. | G3 |
| D6 | Turn on CI in both repositories (X2). | G2 |
| D7 | Folder-stub rule, Ruleset 1.23 section 9 (B4). | G4 |
| D8 | Who signs off the EA sample per discipline (section 7 item 8), and the pilot engineers (section 8). | G4 |

## 11. Risks

- **Old Mac:** Obsidian 1.13.0+ may not run on the Mac's macOS version (section 4 item 2).
- **Windows paths:** long paths fail on Windows without special settings; Task 9, D4 and S2 address it.
- **Review volume:** thousands of review lines (`hasChild` alone is about 19,600 links to judge in Task 7) need batch tools (W7) or rule-level decisions before the freeze.
- **Identity:** the Source Map and `uid` values cannot be repaired after the team links to them; I2 and the freeze rule protect them.
- **Performance** at 30,000+ notes on the team's hardware is unmeasured (B5, W5).
- **Credentials:** tokens pasted into chats must be revoked after use.

## 12. Keeping this plan true

Update the run log after every run. When an item is done, mark it in its table with the date and the decision or commit. A decision that changes a step is logged as `W-n` (or `WB-n`) and edits this file in the same commit. [[00 - Current State]] stays the registry; this file is the plan.
