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

### Step 41 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Added an explicit core-ready publication gate; restored or built `stats` are now treated as provisional internal state rather than a readiness signal.
- Warm startup cannot report ready merely because `installRestoredCore()` has installed compatible cached state.
- Before publishing core-ready, startup now awaits `indexer.whenSourceSettled()`, which covers:
  - active whole-index build/rebuild work;
  - queued rebuilds;
  - coalesced live source updates;
  - active live apply work;
  - pending/active relationship re-resolution.
- After the source-settled barrier, startup verifies publishable index statistics still exist, then opens the explicit publication gate.
- `isReady()` now requires the publication gate, loaded schema, writer availability, statistics, no active build, and no pending source reconciliation.
- Added pure `canPublishCoreReady()` readiness policy plus tests proving:
  - every prerequisite is required;
  - restored statistics alone never make warm startup ready while reconciliation/publication is incomplete.
- Cache compatibility remains checked before `installRestoredCore()`; therefore the final ready state is now ordered as: compatibility validation → provisional restore → required reconciliation/recheck → source-settled barrier → explicit publication.
- This also closes the cold/recovery case where a build could return while another rebuild had already been queued by startup churn; ready publication now waits for that queued source work to settle.
- GitHub Actions run `37223756621` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Implementation/test commits are `acf7919d`, `4358064f`, `684cf69a`, and `f95bcdb5`; CI produced built-artifact commit `71abc470`.
- Intentionally deferred: explicit corrupt/missing/partial/incompatible semantic-cache generation recovery tests remain Step 42.

### Step 42 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Added a small storage-neutral `probeCoreCacheStartup()` test seam that exercises the exact startup boundary of: read a core generation → enforce cache/schema compatibility → either produce restored state or a scoped restore-unavailable reason.
- The probe deliberately does **not** choose the cold-build fallback; that runtime fallback/publication behavior remains Step 43.
- Added explicit startup recovery tests for:
  - no semantic-cache manifest present;
  - corrupt newest committed generation with an older complete generation available;
  - partially written/torn newest generation with an older complete generation available;
  - every committed generation unreadable;
  - a complete but schema-incompatible generation.
- Corrupt/partial newest generations fall back deterministically to the older committed A/B slot before compatibility restoration is attempted.
- Missing/all-unreadable cache conditions report restore unavailable without producing any restored semantic state.
- A structurally complete but schema-incompatible generation is rejected by the semantic compatibility contract rather than being restored.
- Existing storage tests continue to prove manifest-last publication, generation-token matching, bounded read concurrency, and semantic atomicity across every observable write boundary.
- GitHub Actions run `37223981257` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and artifact handling.
- Step 42 commits are `cae60778` and `786ff30e`. No new built-artifact commit was required because this step changed only pure core/test sources and did not alter the bundled plugin output.
- Intentionally deferred: proving that restore failure always transitions to a cooperative cold build with no partially restored state visible remains Step 43.

### Step 43 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Warm restore failure/recovery now follows an explicit ordered path: freeze provisional live work → drain already-active source tasks → discard provisional semantic state → re-enable live tracking → run the authoritative cooperative cold build.
- Added `Indexer.discardProvisionalSemanticState()` to remove every provisional warm surface before recovery:
  - semantic `ModelIndex`;
  - reverse relationship dependency index;
  - relationship re-resolution history;
  - Local Model derived state and hydration bookkeeping;
  - fingerprints;
  - dirty/live/path-change sets;
  - cache-dirty bookkeeping;
  - readiness statistics.
- Recovery also clears provisional rebuild/live/relationship timers, stops new live work while discard is in progress, waits for active live-apply/relationship-resolution tasks to settle, and invalidates pending Local Model publications through hydration/local revision guards.
- Added pure `recoverWithColdBuild()` ordering used by runtime startup. It awaits provisional-state discard before allowing the cold build callback to start.
- Cold recovery re-enables live tracking only immediately before the cold build, so edits during the authoritative rebuild continue to enter the normal cold-build reconciliation path rather than mutating discarded warm state.
- The cold build remains the existing cooperative `Indexer.build()`/`doBuild()` path with UI-yielding `CooperativeBudget` checkpoints.
- Step 41's explicit publication gate remains closed throughout restore failure, discard, and cold rebuild; partially restored state therefore cannot become core-ready.
- Focused tests prove:
  - discard completes before the cold build starts;
  - the cold build never starts if discard itself fails;
  - a cold-build failure occurs only after provisional state has already been discarded.
- GitHub Actions run `37224209387` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Step 43 commits are `41edf8c4`, `60d4ca0f`, `307482a7`, `c28472f5`, `28d0ae80`, `3e10cd53`, and `327253ec`; CI produced built-artifact commit `17287a58`.
- Intentionally deferred: requested occurrence hydration preemption/duplicate-read/stale-publication proof remains Step 44.

### Step 44 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Requested/foreground occurrence hydration and background occurrence hydration now share one keyed in-flight owner body-read registry rather than issuing independent `cachedRead()` calls for the same owner.
- The shared flight is keyed by owner path and returns the body text plus read timing; background and requested consumers reuse the same physical read while retaining their own publication/revision semantics.
- Background occurrence hydration now explicitly pauses at its next cooperative owner boundary whenever requested occurrence work is active. Existing background-idle and live-update gates remain in force.
- Requested owner hydration takes semantic ownership by advancing the owner's local revision before awaiting the shared body read.
- If a requested hydration overtakes an older background read for the same owner, the background publication fails the owner-revision guard while the requested publication succeeds.
- Source/hydration epoch changes still invalidate both requested and background stale publication after source semantics change.
- Added pure `shouldPauseBackgroundOccurrence()` and `canPublishOccurrence()` guards so priority/publication behavior is testable without Obsidian runtime coupling.
- Focused tests prove:
  - active requested occurrence work pauses background hydration;
  - background and requested hydration for one owner share exactly one in-flight body read;
  - a newer requested owner revision prevents an older background result from publishing;
  - a source epoch change prevents stale publication from either lane.
- Existing `SingleFlightByKey` still guarantees concurrent callers for one owner share one promise; Step 44 extends its use to both background and requested occurrence body reads.
- GitHub Actions run `37224403052` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Step 44 commits are `4fe00529`, `91fc1900`, `c7f34bf4`, and `d992e82d`; CI produced built-artifact commit `ab8a4502`.
- Intentionally deferred: unified foreground-activity pausing of cache persistence, assurance, and background occurrence work remains Step 45.

### Step 45 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Foreground activity is now one shared runtime signal for all optional/background Workbench subsystems: background occurrence hydration, semantic-cache persistence, and automatic/stale-retry assurance.
- All three paths use the same `lastChange` foreground-activity timestamp through `canRunBackgroundWork()`, plus the same explicit runtime-work priority ordering from `canStartRuntimeWork()`.
- `backgroundWorkAllowed()` now accepts `assurance` in addition to background hydration and cache writes.
- Added a shared `waitForBackgroundWork()` loop so automatic assurance can wait on the same policy rather than using a separate assurance-specific quiet heuristic.
- Assurance behavior is intentionally split by intent:
  - automatic assurance waits for shared background permission before scanning;
  - a deliberately forced/manual assurance request may start immediately as foreground work;
  - if that forced scan races a foreground edit and becomes stale, its retry must yield to the shared background policy before rescanning.
- Cache persistence already used the shared foreground gate when its timer fired. Step 45 adds a second shared-policy recheck after Local Model settling and immediately before the expensive serialize/write boundary, so an edit that resumes during the wait defers persistence instead of continuing from an invalidated quiet period.
- Background occurrence hydration continues to consult the same shared gate both before starting and, through the Indexer's background-idle callback, between cooperative owner boundaries.
- Runtime work priority remains explicit: indexing > requested hydration > background hydration > assurance > cache write. Therefore lower-priority optional work cannot begin while higher-priority work is active.
- Focused assurance tests prove:
  - automatic assurance does not scan until shared background permission is granted;
  - forced assurance can run immediately;
  - a stale forced scan's retry yields to shared background permission before rescanning.
- Existing background-policy tests continue to prove the common foreground quiet window and runtime-work priority ordering.
- GitHub Actions run `37224995767` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Step 45 commits are `f136f0a0`, `aa284891`, `992bf04c`, and `c26fbdb5`; CI produced built-artifact commit `9274b8c0`.
- Intentionally deferred: starvation bounds ensuring deferred occurrence hydration, cache persistence, and assurance eventually resume under sustained intermittent foreground activity remain Step 46.

### Step 46 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Added a shared bounded starvation rule for optional/background Workbench lanes: background occurrence hydration, semantic-cache persistence, and automatic/stale-retry assurance.
- New `BACKGROUND_MAX_DEFERRAL_MS` is 30,000 ms.
- Each background lane tracks when it first became pending. Re-scheduling caused by intermittent edits does not reset that age.
- Before the starvation bound expires, the normal foreground quiet window remains authoritative:
  - background hydration / assurance use the shared 3 s quiet window;
  - cache persistence retains its longer 8 s quiet requirement.
- Once a lane has been pending for 30 s, only the quiet-time requirement may be bypassed. The following remain hard blockers and are never overridden by starvation relief:
  - plugin unload;
  - core not ready;
  - active indexing;
  - queued rebuild;
  - pending live semantic updates;
  - higher-priority active runtime work.
- Runtime work priority remains unchanged: indexing > requested hydration > background hydration > assurance > cache write.
- Pending age is cleared when the corresponding work has actually completed/no longer remains pending, so a prior starvation event does not permanently weaken future quiet-window behavior.
- Background occurrence hydration keeps its pending age across repeated scheduling attempts until occurrence work is settled.
- Cache persistence keeps its pending age across edit-triggered reschedules until the matching semantic revision is committed.
- Automatic assurance begins its pending-age window when it requests background permission; forced/manual assurance remains foreground-capable, while any stale retry uses the bounded background policy.
- Focused tests prove:
  - intermittent edits below the quiet threshold continue to defer work before the 30 s bound;
  - the quiet-window rule is relieved once the bound is reached;
  - starvation relief never overrides unload, not-ready, indexing, rebuild, or live-update blockers;
  - without a pending-age bound, the original quiet-window semantics remain unchanged.
- GitHub Actions run `37225163961` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Step 46 commits are `6f86db87`, `eda9ea97`, and `48bc05de`; CI produced built-artifact commit `1edf2f67`.
- Intentionally deferred: independently exposing core, occurrence, cache, schema, and assurance readiness/failure in runtime health remains Step 47.

### Step 47 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Runtime health now exposes five independent capability states: `core`, `occurrence`, `cache`, `schema`, and `assurance`.
- Each capability reports an explicit `ready`, `pending`, or `failed` state plus a scoped detail string.
- Schema load failure is no longer folded into `coreError`; it has its own `lastSchemaError` and appears as `schema=failed` while core remains `pending · blocked by schema`.
- Core health independently reports startup/indexing/live-reconciliation availability and core-specific startup failure.
- Occurrence health independently reports settled, queued, hydrating, Local Model read failures, or background occurrence failure.
- Cache health independently reports current, pending/coalesced/not-current, or cache write failure.
- Schema health independently reports not loaded, compatible, compatible-with-warnings, or schema load failure.
- Assurance health independently reports not run/stale/computing, current findings/no findings, or assurance validator failure.
- The runtime-health modal now renders one row per capability using these explicit states; it remains observation-only and does not trigger indexing, cache I/O, hydration, or assurance.
- Top-level Workbench status is derived from capability states but does not erase them:
  - any failed subsystem produces attention;
  - core-not-ready remains starting/syncing;
  - occurrence/live work can produce syncing while core remains usable;
  - engineering findings remain a review state rather than runtime failure.
- Focused tests prove:
  - schema failure is distinct from core failure;
  - occurrence failure is distinct from core availability;
  - cache pending/failure is independently visible;
  - assurance pending/ready/failure are independent states;
  - schema warnings remain readiness-compatible;
  - deferred occurrence data does not imply core unavailability.
- GitHub Actions run `37225620835` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Step 47 commits are `f44af72a`, `965f4e2e`, and `ca609f18`; CI produced built-artifact commit `6ffbdb00`.
- Intentionally deferred: failure-injection proof that one derived subsystem can fail without ordinary Obsidian editing or unrelated Workbench capabilities failing remains Step 48.

### Step 48 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Added an explicit pure edit-availability policy: ordinary Workbench model editing depends only on authoritative core readiness and schema compatibility.
- Derived subsystem state is intentionally excluded from the edit gate. Occurrence, semantic-cache and assurance failures therefore cannot disable ordinary Workbench model editing while core/schema remain valid.
- The existing UI edit gate now delegates to this pure policy, making the isolation contract directly testable.
- Added failure-injection coverage for three derived subsystems:
  - injected occurrence failure;
  - injected semantic-cache failure;
  - injected assurance failure.
- Each injected failure proves all of the following:
  - only the targeted capability enters `failed`;
  - core remains `ready`;
  - unrelated derived capability states remain usable/ready;
  - schema remains ready;
  - the edit gate remains open.
- Added fail-closed tests proving editing is blocked only when authoritative prerequisites fail:
  - core is not ready;
  - schema is unavailable;
  - schema relationship version is too old for safe editing.
- This preserves the intended failure-isolation boundary: derived accelerators/diagnostics may degrade independently without taking down ordinary Obsidian editing or unrelated Workbench capabilities.
- The first Step 48 CI attempt (`37225750204`) passed all 210 tests and all three 60k benchmark gates but failed the TypeScript build because `editingBlocked` was still used by an existing diagnostic path after its import was removed during edit-gate refactoring.
- Restored that existing schema diagnostic import without changing the Step 48 isolation design.
- Final GitHub Actions run `37225802020` passed `npm test`, the 60k semantic-cache scale smoke, paired cold/warm startup benchmark, 60k relationship re-resolution benchmark, `npm run build`, artifact hashing/sync, and built-artifact commit.
- Step 48 commits are `e0c9447b`, `5cf6a3f2`, `1605ac61`, and corrective build commit `ec7d6173`; CI produced built-artifact commit `6bf7338b`.
- Intentionally deferred: measuring end-to-end cold startup in a disposable integration vault with real Obsidian metadata resolution/source parsing remains Step 49.

**Current resume point:** Step 49. Do not begin it until Spencer explicitly answers `y` after the Step 48 completion report. A new chat should read this roadmap, verify the repository still matches this state, and then execute Step 49 only.

## Reconstructed remaining steps

43. Ensure cache restore failure always falls back to a cooperative cold build without leaving partially restored semantic state visible.

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
