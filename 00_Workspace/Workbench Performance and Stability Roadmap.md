# Workbench Performance and Stability Roadmap

**Status:** reconstructed working roadmap  
**Date reconstructed:** 2026-10-04  
**Authority:** replacement for the retired temporary performance/stability checklist. Steps 18–32 below are verified from implementation history; Steps 33 onward are reconstructed from the governing Startup Stability Plan and current Workbench architecture and are not claimed to be the lost checklist verbatim.

## Governing objective

Opening an MDSE vault must first produce a responsive, readable Obsidian workspace. Workbench capabilities may become ready afterward in explicit stages. Stability comes before feature latency.

The runtime should therefore:
- keep immediate Obsidian startup free of heavy Workbench work;
- make the reusable-note semantic graph usable before occurrence hydration;
- hydrate Local Model occurrence data only after core readiness or on demand;
- keep background work cooperative, activity-aware and preemptible;
- isolate core, occurrence, cache, schema and assurance failures;
- treat semantic cache as disposable acceleration, never authoritative model state;
- enable warm-start behavior only when it is proven safe and beneficial;
- reduce overlapping plugin/runtime work only after equivalent capability is proven;
- accept a release only from the exact CI-built candidate tested in a disposable integration vault.

## Execution contract for future chats

Use this section as the continuation protocol; do not reconstruct the plan from conversation memory.

1. **Authority and repositories.** This roadmap and `00_Workspace/Startup Stability Plan.md` in `spencerskelly/Test_Vault_` main define the numbered stability sequence. Runtime implementation belongs in `spencerskelly/MDSE_Workbench` main. Test_Vault_ records governance/status; it is not a duplicate runtime source tree.
2. **Resume point.** Find the first numbered step below that is not listed under **Verified completed steps** and has no later completion evidence in this file. That is the only active step.
3. **Read before changing code.** Read the active step, the immediately preceding completed steps it depends on, and the current Workbench implementation/tests for the affected seam. Treat newer source/tests on Workbench main as evidence that a reconstructed step may already be satisfied.
4. **Keep scope exact.** Implement or prove only the active numbered step. Do not silently pull later-step behavior forward. A prerequisite defect may be fixed only when it blocks the active step; document that exception.
5. **Prefer instrumentation before policy.** Measurement steps collect evidence without setting thresholds or changing runtime policy unless the numbered step explicitly says to do so. Thresholds, fallback behavior, diagnostics UI, and acceptance decisions belong to their own numbered steps.
6. **Proof required.** A step is complete only when the implementation or evidence exists in the authoritative repository, focused tests cover the new behavior, the full Workbench test suite/build are clean when code changed, and this roadmap records what changed and where the proof lives.
7. **Record enough for handoff.** Completion evidence must state the semantic intent, files changed, test/build result, and any intentionally deferred follow-on. A later chat should be able to continue without relying on hidden reasoning or prior chat text.
8. **One-step gate.** After completing and documenting one numbered step, stop. Report the result and wait for Spencer's explicit `y` before starting the next numbered step.
9. **No retroactive renumbering.** If a reconstructed step is already satisfied, mark that step complete with evidence; do not delete it or renumber later steps.
10. **Release boundary.** Performance/stability work on standalone Workbench main does not by itself change the Base Vault pin or constitute an MDSE release. Release promotion remains a separate controlled integration action.

## Verified completed steps

18. Collapse relationship evidence into one canonical internal representation.
19. Keep reverse relationship indexes canonical and incrementally maintained.
20. Separate semantic model state from derived visual state.
21. Add short-lived memoization for repeated local view requests.
22. Cache compiled view profiles instead of interpreting every request repeatedly.
23. Completed in prior history; retained as completed even though the retired checklist wording is unavailable.
24. Avoid rewriting unchanged semantic-cache shards.
25. Rate-limit cache persistence during rapid edit bursts.
26. Expose semantic-cache size in diagnostics.
27. Benchmark cold and warm core startup against identical repository states.
28. Ensure warm restore never retains stale link resolution after add, rename or delete.
29. Define the reconciliation-size threshold that forces a full rebuild.
30. Prevent semantic-cache clearing from racing an active cache writer.
31. Maintain reverse-path dependency indexes for targeted relationship re-resolution.
32. Use dependency candidates so path-set changes do not require whole-graph relationship re-resolution.
33. Measure targeted relationship re-resolution fan-out so we can see how many source notes each path-set change actually invalidates.
34. Define a candidate-count threshold above which targeted relationship re-resolution falls back to the cooperative whole-graph path.

### Step 33 completion evidence — 2026-10-04

Implemented on `spencerskelly/MDSE_Workbench` main.

- `src/core/relationship-dependencies.ts` now reports conservative candidate fan-out per changed path without changing reconciliation semantics.
- `src/obsidian/indexer.ts` records a bounded 20-sample in-memory history for each coalesced live path-set reconciliation: changed paths, per-path candidate fan-out, unique candidate count, count of source notes whose resolved evidence actually changed, and elapsed re-resolution time.
- `test/relationship-dependencies.test.ts` proves fan-out measurement remains consistent with the canonical candidate union and deduplicates repeated changed paths.
- GitHub Actions run `37219842542` passed `npm test`, the 60k semantic-cache scale smoke, the paired cold/warm startup benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Commits carrying the implementation/test are `e6ad7e6`, `e1116c6`, and `374f772` (followed by the normal CI-built artifact commit).
- Intentionally deferred: no candidate threshold/fallback policy was added (Step 34), and no user-facing diagnostics surface was added (Step 38).

### Step 34 completion evidence — 2026-10-04

Implemented on `spencerskelly/MDSE_Workbench` main.

- `src/core/relationship-dependencies.ts` defines `TARGETED_RELATIONSHIP_RERESOLUTION_MAX_CANDIDATES = 5_000` plus the pure policy helper `shouldUseFullRelationshipReresolution()`.
- Candidate sets of 5,000 or fewer continue through targeted relationship re-resolution; candidate sets above 5,000 fall back to the existing cooperative whole-graph resolver.
- `src/obsidian/indexer.ts` applies the same policy to both live path-set reconciliation and controlled warm-start add/delete reconciliation, so the threshold does not create two different runtime semantics.
- `test/relationship-dependencies.test.ts` proves the exact threshold boundary: below and at 5,000 remain targeted; 5,001 requires the full path.
- GitHub Actions run `37221600586` passed `npm test`, the 60k semantic-cache scale smoke, the paired cold/warm startup benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Implementation/test commits are `bc433577`, `4bf7d779`, `458e9f38`, and corrected test-import commit `839acda5`; CI produced built-artifact commit `1addb70c`.
- One intermediate CI run exposed a malformed test import introduced while editing; it was corrected before acceptance and the final full gate is green.
- The 5,000 threshold is intentionally a conservative safety policy, not a claimed performance optimum. Representative add/delete/rename benchmark tuning remains Step 37.
- Intentionally deferred: detailed link-form correctness proof remains Step 35, dependency-evidence fail-closed behavior remains Step 36, and user-facing reconciliation diagnostics remain Step 38.

### Step 35 completion evidence — 2026-10-04

Implemented on `spencerskelly/MDSE_Workbench` main.

- Reviewed the existing authored-link resolution and targeted dependency-candidate seam before changing behavior.
- Found one real correctness weakness: the derived dependency index normalized slashes and `.md`, but remained case-sensitive and depended on upstream callers to have already removed wikilink aliases/fragments.
- `src/core/relationship-dependencies.ts` now normalizes candidate keys conservatively by stripping alias/fragment syntax, normalizing Windows separators and leading slashes, removing `.md`, and comparing case-insensitively.
- This normalization affects only derived invalidation candidates; authoritative relationship resolution remains delegated to Obsidian metadata resolution.
- `test/relationship-dependencies.test.ts` now proves candidate coverage for ambiguous basenames, folder-qualified links, aliases, heading/block fragments, case variation, Windows separators, leading slashes, and `.md` normalization.
- Ambiguous basename handling deliberately over-includes candidates rather than risk missing a source note; the targeted pass remains semantically correct because authoritative re-resolution still decides the actual destination.
- GitHub Actions run `37221736297` passed `npm test`, the 60k semantic-cache scale smoke, the paired cold/warm startup benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Implementation/test commits are `44697378` and `6e9a3aa0`; CI produced built-artifact commit `9a8c9d52`.
- Intentionally deferred: fail-closed validation of incomplete/inconsistent derived dependency evidence remains Step 36.

### Step 36 completion evidence — 2026-10-04

Implemented on `spencerskelly/MDSE_Workbench` main.

- `ReversePathDependencyIndex.consistency()` now validates both internal reverse-map symmetry and completeness against expected authoritative source evidence.
- The completeness check compares each source note's resolved target paths and authored linkpaths against the derived dependency index, so a wholly missing source cannot appear "self-consistent" merely because no derived entries exist for it.
- `Indexer.relationshipDependencyConsistency()` requires every indexed note to retain authored relationship evidence and compares the derived accelerator against current `NoteRecord` evidence before path-set targeting is trusted.
- Live path-set reconciliation now fails closed: if dependency evidence is incomplete or inconsistent, targeted re-resolution is skipped and the cooperative rebuild path is scheduled.
- Warm incremental add/delete reconciliation now throws a scoped "full rebuild required" error on incomplete/inconsistent dependency evidence; the existing startup recovery path catches that condition and performs the proven cold build from authoritative Markdown.
- Focused tests prove complete evidence passes, missing expected source evidence fails, and deliberately corrupted reverse evidence is detected.
- GitHub Actions run `37221875787` passed `npm test`, the 60k semantic-cache scale smoke, the paired cold/warm startup benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Implementation/test commits are `2b4a7170`, `3e315960`, `42dce2a5`, and `99b85855`; CI produced built-artifact commit `9ece4567`.
- Intermediate CI runs occurred while the invariant was still being assembled; only the final test-bearing run above is acceptance evidence.
- Intentionally deferred: representative scale/performance tuning of add/delete/rename reconciliation remains Step 37.

### Step 37 completion evidence — 2026-10-04

Implemented and measured on `spencerskelly/MDSE_Workbench` main.

- Added `bench/relationship-reresolution-bench.ts` plus `npm run bench:relationships` to measure the warm path-set reconciliation seam after semantic state already exists.
- The benchmark uses a representative 60,000-note semantic graph and executes add, delete, and rename scenarios at candidate fan-outs of 10, 100, 1,000, 5,000, 10,000, and 20,000.
- Each scenario compares targeted candidate lookup + authored-link re-resolution against the exact same whole-graph resolver and fails if targeted and full results disagree semantically.
- The benchmark is now part of the CI build workflow as `60k relationship re-resolution benchmark`.
- Final CI run `37222063977` measured:
  - 5,000 candidates: targeted remained 4.82x to 15.31x faster than whole-graph.
  - 10,000 candidates: targeted remained 3.40x to 4.11x faster across add/delete/rename.
  - 20,000 candidates: margin narrowed materially to 1.41x to 2.24x in the final run.
- Based on the measured margin, `TARGETED_RELATIONSHIP_RERESOLUTION_MAX_CANDIDATES` was raised from the conservative 5,000 established in Step 34 to 10,000. This keeps the targeted path where the representative benchmark still shows a consistent >3x advantage while falling back before the lower-margin/noisier 20k region.
- Final CI run `37222063977` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and artifact commit.
- Step 37 commits are `0c814dc0`, `1e61193c`, `71ec5fe2`, and threshold-tuning commit `ccb639db`; CI produced built-artifact commit `07bb07f9`.
- This remains a synthetic semantic-graph benchmark rather than end-to-end Obsidian integration timing; integrated startup and live-edit measurements remain Steps 49–50 and 55–59.

### Step 38 completion evidence — 2026-10-04

Implemented on `spencerskelly/MDSE_Workbench` main.

- The existing bounded relationship re-resolution history now records the execution mode for each sample as `targeted` or `full` in addition to changed paths, per-path fan-out, unique candidate count, changed-source count, and elapsed time.
- Warm incremental add/delete reconciliation now records into the same history as live path-set reconciliation, so diagnostics reflect the last actual relationship reconciliation regardless of whether it came from startup reconciliation or an open-vault edit.
- The Workbench diagnostics report now exposes:
  - relationship reconciliation mode (`targeted` or `full`);
  - candidate count;
  - elapsed relationship re-resolution time;
  - count of source notes whose resolved relationship evidence actually changed.
- No parallel telemetry model was added; Step 38 reuses the Step 33 bounded in-memory evidence surface.
- GitHub Actions run `37222232640` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Implementation commits are `82f4ea1a` and `398c54af`; CI produced built-artifact commit `25259feb`.
- Intentionally deferred: reverse dependency index memory bounding and size reporting remain Step 39.

### Step 39 completion evidence — 2026-10-04

Implemented on `spencerskelly/MDSE_Workbench` main.

- The reverse relationship dependency accelerator now exposes an exact structural size summary: source count, resolved target-key count, authored-key count, resolved association count, authored-key association count, and total stored set memberships.
- The memory bound is deliberately structural rather than a lossy hard cap:
  - `set()` removes a source's previous entries before replacement, so the index cannot accumulate edit-history residue;
  - each current resolved source-target association is stored exactly twice, once source→target and once target→source;
  - each normalized authored-key association is stored exactly twice, once source→key and once key→source;
  - one authored link yields at most two normalized candidate keys (qualified path and basename).
- Therefore total stored memberships are exactly `2 × (resolved associations + authored-key associations)`, and growth remains proportional to current model relationship evidence rather than runtime history.
- No eviction or arbitrary entry cap was introduced because dropping dependency evidence would weaken targeted invalidation correctness.
- Workbench diagnostics now reports reverse relationship index sources, combined key count, stored memberships, and the split between resolved and authored-key associations.
- Focused tests prove replacement removes stale memory rather than accumulating it, and one authored link contributes at most two normalized dependency keys.
- GitHub Actions run `37222550717` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Implementation/test commits are `fac11490`, `db426f4d`, `58fd69e9`, and `4319f14f`; CI produced built-artifact commit `e089b8cb`.
- Intentionally deferred: schema-change invalidation of every relationship-derived cache/index surface remains Step 40.

### Step 40 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Traced relationship-schema dependencies across the live semantic graph, reverse relationship dependency accelerator, reconciliation history/readiness state, assurance/review consumers, and persisted semantic cache.
- `Indexer.setSchema()` now invalidates relationship-derived runtime state immediately instead of merely swapping the schema object:
  - replaces the existing `ModelIndex` with a fresh index bound to the new schema;
  - clears the reverse relationship dependency index;
  - clears relationship re-resolution history;
  - clears readiness stats so stale graph state cannot remain publishable during the schema-transition window;
  - clears cache-dirty path bookkeeping and bumps the semantic revision.
- The existing required full rebuild then repopulates the graph and reverse dependency index from authoritative Markdown under the new schema.
- The semantic-cache compatibility contract already included `relationshipsVersion`, `elementTypesVersion`, and a deterministic `schemaSignature` over parsed schema semantics. Step 40 adds explicit proof that relationship-rule changes invalidate every restore surface even when the human-readable schema version strings are deliberately left unchanged.
- Added tests proving relationship semantic changes reject core, Local Model, and full semantic cache restore before stale derived state can be installed.
- Added coverage proving the schema signature changes when relationship edge-interpretation fields change, including forward field, inverse field, relationship kind, from/to endpoints, same-class rule, provisional flag, and temporary flag.
- Because `setSchema()` bumps the semantic revision, revision-keyed assurance results become stale and must recompute against the rebuilt graph; Review/writer obtain the current schema/index through live accessors rather than retaining old relationship definitions.
- GitHub Actions run `37223259232` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Implementation/test commits are `b2dc7467` and `b5aa19be`; CI produced built-artifact commit `f61a29a3`.
- Intentionally deferred: proof that warm restore cannot publish core-ready before compatibility and source reconciliation complete remains Step 41.

**Current resume point:** Step 41. Do not begin it until Spencer explicitly answers `y` after the Step 40 completion report. A new chat should read this roadmap, verify the repository still matches this state, and then execute Step 41 only.

## Reconstructed remaining steps

41. Verify that warm restore cannot publish core-ready state until cache compatibility and source reconciliation have both completed successfully.

42. Add explicit recovery tests for corrupt, missing, partially written and incompatible semantic-cache generations during startup.

43. Ensure cache restore failure always falls back to a cooperative cold build without leaving partially restored semantic state visible.

44. Verify requested occurrence hydration preempts background occurrence hydration without duplicate body reads or stale publication.

45. Verify resumed foreground edits pause cache persistence, assurance and background occurrence work through one shared activity policy.

46. Add starvation bounds so deferred occurrence hydration, cache persistence and assurance eventually resume after sustained but intermittent foreground activity.

47. Expose core, occurrence, cache, schema and assurance readiness/failure independently in runtime health.

48. Add failure-injection tests proving one derived subsystem can fail without making ordinary Obsidian editing or unrelated Workbench capabilities unusable.

49. Measure end-to-end cold startup in the disposable integration vault, including real Obsidian metadata resolution and source parsing rather than only the pure core benchmark.

50. Measure end-to-end warm startup against the exact same vault/repository state and compare time-to-readable, time-to-core-ready and time-to-occurrence-ready.

51. Keep warm-cache preview disabled by default unless integrated measurements prove a real user-visible startup benefit without weaker correctness.

52. If warm startup earns promotion, define the exact acceptance threshold and fallback conditions required before making it the normal startup path.

53. Measure third-party plugin overlap one plugin at a time against startup responsiveness and MDSE capability.

54. Remove or demote an overlapping plugin only when Workbench replacement capability and startup benefit are both proven.

55. Install the exact CI-built candidate in the disposable integration vault and run the integrated startup-responsiveness acceptance test.

56. Run integrated occurrence-view acceptance: Structure, Interfaces, Where Used, Requirements and other occurrence-aware views must wait only for the capability they actually need.

57. Run integrated live-edit acceptance covering add, edit, rename, move and delete while background work is active.

58. Run integrated recovery acceptance covering bad cache, interrupted background work, plugin reload and Obsidian restart.

59. Run repeated cold/warm restart cycles and confirm no cumulative memory, stale-state or scheduling degradation.

60. Freeze the accepted performance/stability candidate, record hashes and runtime evidence, and update the handoff/current-state documentation.

## Mapping to Startup Stability Plan

- Pieces 1–3: substantially implemented and already exercised by earlier runtime work.
- Piece 4: substantially implemented; Steps 44–46 finish scheduling/preemption proof.
- Piece 5: partially implemented; Steps 47–48 finish explicit health/failure-isolation proof.
- Piece 6: active optimization area; Steps 33–43 and 49–52 complete warm-start safety and value proof.
- Piece 7: Steps 53–54.
- Piece 8: Steps 55–60.

## Execution rule

Proceed one numbered step at a time. After each completed step, stop and wait for explicit user approval before beginning the next step.

If future evidence shows that a reconstructed step is already fully satisfied, mark it complete with proof rather than reimplementing it. If a step exposes a prerequisite defect, fix the smallest prerequisite necessary and keep the numbered step scope intact.
