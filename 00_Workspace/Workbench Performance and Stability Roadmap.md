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

## High-priority semantic compatibility To-Do

These items are release-blocking compatibility work and do **not** renumber or interrupt the performance/stability sequence below.

- **WB-128 · HIGH · Local Model 0.4 + W-384/W-385 compatibility.** Update Workbench to read Local Model 0.4 while preserving frozen 0.1/0.2/0.3 semantics; write 0.4 using `Parts`, `Interfaces`, and `Connections`; treat reusable interface definitions as `Object / interface` instead of Port notes; update type filters/editors/views for `Behavior` subtypes (`function`, `activity`, `action`, `step`) and `Condition` subtypes (`state`, `state machine`, `mode`, `design`); remove creation/validation assumptions that require first-class Port/Function/State/Design/Step notes; and support connection-level `exposes` links to boundary Interface occurrences so Internal/Interfaces views show how an internal connection is exposed at the owning context boundary. Required proof: parser compatibility fixtures for 0.1–0.4, structured editor round-trip, view rendering, schema-driven relationship filtering, and regression tests proving legacy 0.3 headings are read without silent rewrite.

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

### Step 49 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Added/used a disposable real-Obsidian integration harness rather than relying on the synthetic core benchmark.
- Integration environment:
  - Obsidian desktop 1.13.7 on the GitHub Actions Linux runner under Xvfb;
  - 12,000 generated Markdown notes (~19 MB) plus the real MDSE schema files;
  - current Workbench build installed into a disposable vault;
  - semantic cache removed before the measured launch;
  - Workbench startup instrumented only when the disposable integration sentinel is present.
- The measured cold run records:
  - process launch timestamp;
  - Workbench plugin-load timestamp;
  - real Obsidian metadata-resolution timestamp from `metadataCache.resolved`;
  - Workbench core-ready timestamp;
  - parsed Markdown file count, model-element count, authored-link count, index mode and Workbench core work time.
- The validator fails closed unless:
  - the run label matches the cold-integration scenario;
  - index mode is `full`;
  - a real metadata-resolution timestamp exists;
  - core-ready occurs after metadata resolution;
  - at least the requested generated Markdown count was parsed.
- A harness race discovered in earlier integration attempts was corrected: the cold-run controller could see the renderer before community-plugin activation had fully settled and treated that transient state as terminal. The controller now retries until both Restricted Mode state and `mdse-workbench` activation are confirmed.
- Final real-Obsidian integration run: `37228021691` (run 7), conclusion `success`.
- Final measured evidence:
  - requested/generated notes: **12,000**;
  - Markdown files parsed: **12,000**;
  - model elements: **1,587**;
  - authored links: **2,655**;
  - index mode: **full**;
  - launch → Workbench plugin load: **7,315 ms**;
  - launch → Obsidian metadata resolved: **8,737 ms**;
  - launch → Workbench core ready: **10,013 ms**;
  - plugin load → core ready: **2,698 ms**;
  - Workbench core indexing/parsing work: **70 ms**.
- Metadata-resolution evidence source was the Workbench listener on the real Obsidian `metadataCache.resolved` event, not a synthetic timer.
- The integration artifact `obsidian-cold-start-evidence` was uploaded as artifact ID `11313275718` and contains the validated result JSON plus Obsidian/controller logs.
- The Step 49 harness-trigger/fix commits are `63ee7877` and `88edc4f5`. The normal Build Workbench artifact workflow for `88edc4f5` also passed as run `37228021709` (run 378).
- Interpretation: on this controlled 12k-note Linux integration run, most elapsed cold-start time precedes Workbench core indexing itself; the measured Workbench core parsing/indexing slice was 70 ms, while launch-to-metadata-resolution was 8.737 s and launch-to-core-ready was 10.013 s.
- Intentionally deferred: measuring warm startup against the exact same vault/repository state and comparing time-to-readable, time-to-core-ready and time-to-occurrence-ready remains Step 50.

### Step 50 completion evidence — 2026-10-04

Implemented and verified on `spencerskelly/MDSE_Workbench` main.

- Extended the real-Obsidian disposable-vault harness so cold and warm startup are measured sequentially against the exact same generated model state.
- Added independent launch milestones for:
  - Obsidian renderer/vault readable;
  - Obsidian metadata resolved;
  - complete per-file metadata-cache coverage;
  - Workbench core ready;
  - Workbench occurrence ready;
  - semantic cache committed.
- The controller records the first point at which the correct disposable vault renderer is available as the user-visible/readable milestone.
- The cold instance remains alive until occurrence data is ready and a complete semantic cache generation has been committed; only then is the warm launch started.
- Warm preview is enabled only for the measured second launch. The Markdown/YAML model files are not regenerated or edited between launches.
- A deterministic hash of all Markdown/YAML model sources is taken before the cold launch and checked after the warm launch; final validation proved the source model was identical.
- Step 50 uncovered and corrected an important cold-start completeness defect: Obsidian's global `metadataCache.resolved` event could occur before every Markdown file had an available per-file metadata cache entry. Because Workbench derives frontmatter/type/link semantics from those entries, the earlier Step 49 core-ready sample could be semantically incomplete even though all file fingerprints had been visited.
- Workbench startup now waits, after the global resolved/quiet gate, until every current Markdown file has a non-null Obsidian metadata-cache entry before the authoritative cold build/restore proceeds. Obsidian remains readable during this wait; only Workbench core readiness is withheld.
- This correction supersedes the earlier Step 49 cold timing as the authoritative cold baseline. Step 49 still proved the real-Obsidian harness and file-parsing path, but its 1,587-element sample was incomplete relative to the fully resolved 12,000-element graph discovered in Step 50.
- Final real-Obsidian comparison run: `37228561757` (run 11), conclusion `success`.
- Environment:
  - Obsidian 1.13.7 under Xvfb on the GitHub Actions Linux runner;
  - 12,000 generated Markdown notes;
  - identical repository/model source state for cold and warm measurements;
  - warm run used semantic-cache mode `restored`.
- Final cold measurement:
  - launch → readable: **5,536 ms**;
  - launch → metadata resolved: **10,129 ms**;
  - launch → complete metadata coverage: **10,152 ms**;
  - launch → core ready: **11,353 ms**;
  - launch → occurrence ready: **11,353 ms**;
  - launch → cache committed: **19,749 ms**;
  - Workbench core work: **171 ms**;
  - files: **12,000**;
  - elements: **12,000**;
  - authored/resolved graph links: **21,491**;
  - mode: **full**.
- Final warm measurement against the same model state:
  - launch → readable: **2,281 ms**;
  - launch → metadata resolved: **8,522 ms**;
  - launch → complete metadata coverage: **8,609 ms**;
  - launch → core ready: **9,866 ms**;
  - launch → occurrence ready: **9,866 ms**;
  - Workbench core work: **0 ms** reported for restored state;
  - files: **12,000**;
  - elements: **12,000**;
  - links: **21,491**;
  - mode: **restored**.
- Warm-minus-cold deltas:
  - readable: **-3,255 ms** (warm renderer became readable earlier);
  - core ready: **-1,487 ms**;
  - occurrence ready: **-1,487 ms**.
- The semantic counts match exactly between cold and warm, and the Markdown/YAML source hash was identical.
- Interpretation is deliberately deferred to Step 51: Step 50 establishes the measured fact that warm restore was about 1.49 s faster to core/occurrence readiness in this controlled 12k-note run, while the larger 3.26 s readable difference is an Obsidian/process-launch variation and cannot be attributed solely to Workbench cache restore.
- Integration evidence artifact `obsidian-cold-start-evidence` was uploaded as artifact ID `11313037402` and contains cold result, warm result, comparison JSON, and controller/Obsidian logs.
- Step 50 implementation commits are `904f8a61`, `141ebf93`, `312977d9`, `5b031d6d`, and correctness-barrier commit `13476498`; normal Build Workbench workflow run `37228561784` passed, producing built-artifact commit `31c1093a`.
- Intentionally deferred: deciding whether this measured benefit is sufficient to keep/promote warm-cache preview remains Step 51.

### Step 51 completion evidence — 2026-10-04

Decision: **keep warm-cache preview disabled by default.**

Evidence reviewed:
- Step 50 proved warm restore can be correct against the same 12,000-note model state:
  - identical Markdown/YAML source hash;
  - identical 12,000 files / 12,000 elements / 21,491 links;
  - warm mode was `restored`;
  - Steps 40–48 already proved schema/cache invalidation, source reconciliation, fail-closed restore, recovery, publication gating, background-work isolation and subsystem failure isolation.
- The measured warm improvement was real but limited:
  - core ready improved from **11.353 s** to **9.866 s**: **1.487 s faster**;
  - occurrence ready improved by the same **1.487 s**;
  - this is about a **13.1%** reduction in launch-to-Workbench-readiness for the controlled 12k-note run.
- The apparent **3.255 s** improvement in Obsidian/vault readable time is not accepted as a Workbench warm-cache benefit because that milestone precedes Workbench restore and is subject to normal process/runner launch variation.
- Warm restore does not eliminate the dominant startup prerequisite: Workbench still waits for Obsidian metadata resolution and complete per-file metadata coverage before publishing authoritative core state.
- Only one controlled real-Obsidian cold/warm pair has been accepted so far. That is enough to prove feasibility and correctness, but not enough evidence to change the controlled default for every vault/user machine.
- No regression requires removal of the preview. The opt-in setting remains available for further controlled measurements and later acceptance work.
- Production default remains exactly as implemented: `warmCachePreview: false`.
- No runtime/code change was required for Step 51, so no new Build Workbench CI run was necessary; the current implementation evidence remains Step 50's successful build run `37228561784` and built artifact commit `31c1093a`.
- Step 52 is conditional on warm startup **earning promotion**. Because Step 51 does not promote warm restore to the normal startup path, Step 52 is **not activated** and no retrospective acceptance threshold is being invented after seeing one favorable measurement.
- A future decision to reconsider promotion should first gather broader/repeated evidence; if that later earns promotion, Step 52's threshold/fallback-definition work becomes applicable before changing the normal startup path.

### Step 53 completion evidence — 2026-10-04

Measured third-party plugin overlap one plugin at a time on the real-Obsidian disposable integration harness.

Scope:
- Only plugins with material architectural overlap were included:
  - Nodian 1.4.14;
  - Breadcrumbs 4.21.11;
  - Dataview 0.5.68;
  - Fileclass 0.2.15;
  - Advanced Canvas 7.0.0.
- Utility/workflow plugins such as Git, Templater, QuickAdd and Table Exporter were intentionally excluded because they do not materially duplicate Workbench semantic indexing, relationship handling, schema validation or model visualization.
- Test environment remained the Step 49/50 real-Obsidian setup:
  - Obsidian 1.13.7 under Xvfb;
  - 12,000 generated Markdown notes;
  - warm-cache preview disabled;
  - authoritative full Workbench rebuild;
  - complete per-file metadata coverage required before core-ready.

Measurement method:
- A sacrificial warmup absorbed first-run runner/filesystem effects.
- The startup reference was the mean of a warmed Workbench-only baseline at the beginning and another Workbench-only baseline at the end.
- Each candidate plugin was then enabled **alone with Workbench** in its own disposable copy.
- Each case had to prove:
  - candidate plugin enabled;
  - Workbench enabled and core-ready;
  - required Workbench commands registered;
  - mode remained `full`;
  - all 12,000 Markdown files were represented;
  - files/elements/links matched the Workbench-only model;
  - governed Markdown/YAML source hash did not change.

Bracketed Workbench-only reference:
- readable: **5,175 ms**;
- core ready: **9,913 ms**;
- occurrence ready: **9,913 ms**.
- Baseline-start core ready: 10,014 ms.
- Baseline-end core ready: 9,812 ms.

Candidate results versus the bracketed baseline:
- **Nodian 1.4.14**
  - readable: 5,083 ms;
  - core/occurrence ready: 9,092 ms;
  - delta: **-821 ms**;
  - interpretation: no measurable startup penalty; negative delta is treated as run variation, not evidence that Nodian accelerates Workbench.
- **Breadcrumbs 4.21.11**
  - readable: 5,021 ms;
  - core/occurrence ready: 9,846 ms;
  - delta: **-67 ms**;
  - interpretation: effectively neutral within measurement noise.
- **Dataview 0.5.68**
  - readable: 4,901 ms;
  - core/occurrence ready: 44,159 ms;
  - delta: **+34,246 ms**;
  - interpretation: clear and material startup-contention outlier in this 12k-note test.
- **Fileclass 0.2.15**
  - readable: 5,199 ms;
  - core/occurrence ready: 11,073 ms;
  - delta: **+1,160 ms**;
  - interpretation: measurable but modest startup cost.
- **Advanced Canvas 7.0.0**
  - readable: 5,045 ms;
  - core/occurrence ready: 10,138 ms;
  - delta: **+225 ms**;
  - interpretation: small enough to treat as near-neutral in this single integration run.

MDSE capability preservation:
- Every candidate case retained:
  - **12,000 files**;
  - **12,000 elements**;
  - **21,491 links**;
  - all required Workbench commands;
  - Workbench core readiness.
- No candidate modified the governed Markdown/YAML model during default startup.

Authoritative integration evidence:
- GitHub Actions workflow: `Obsidian plugin overlap integration`.
- Successful run: `37230191195` (run 5).
- Evidence artifact: `plugin-overlap-evidence`, artifact ID `11314055099`.
- Primary comparison commit: `9d9a008a`.
- Supporting Step 53 harness commits: `92f4a546`, `2b40639f`, `2390dc2d`, `caf19372`, `9d45ea1b`, `b8de791e`, `356f0aba`, and `b4c04591`.
- Later Step 53 harness-only commits `80166a16` and `ea305824` do not alter Workbench runtime semantics; normal Build Workbench workflows for them passed.

Step 53 conclusion:
- Dataview is the only plugin showing a clearly material startup-responsiveness penalty in this controlled overlap test.
- Fileclass shows a smaller measurable penalty.
- Nodian, Breadcrumbs and Advanced Canvas did not show a meaningful startup penalty in this run.
- **No plugin is removed or demoted by Step 53.** Step 54 must separately prove that Workbench actually replaces the overlapping capability and that removing/demoting the plugin produces a startup benefit before changing the baseline.

### Step 54 completion evidence — 2026-10-04

Verified the one-plugin removal/demotion gate against the current controlled MDSE runtime.

Decision:
- **Dataview 0.5.68 is retired from the controlled MDSE runtime.**
- No additional plugin is removed or demoted in Step 54.

Why Dataview satisfies both required gates:

1. **Replacement/dependency gate passed**
   - Current controlled vault search found no Dataview query blocks (```dataview`).
   - W-370 records that no current engineering workflow depends on Dataview-specific query execution.
   - Native Obsidian Bases cover the tabular/property views currently present.
   - Workbench provides the schema-aware semantic index plus Explore, Details, Review and relationship/navigation workflows used by MDSE.
   - Therefore removing Dataview does not remove a required current engineering capability.

2. **Startup-benefit gate passed**
   - Step 53 isolated Dataview 0.5.68 against the bracketed Workbench-only 12,000-note baseline.
   - Dataview preserved the same **12,000 files / 12,000 elements / 21,491 links** and all required Workbench commands.
   - It nevertheless delayed Workbench core/occurrence readiness by **34.246 s**.
   - This is a clear, material startup penalty rather than measurement noise.

Controlled-stack verification:
- `.obsidian/community-plugins.json` no longer contains `dataview`.
- `.obsidian/plugin-lock.yaml` contains no Dataview entry.
- `Base Vault/Runtime/Plugins/` contains no Dataview payload.
- `Base Vault/Definition/Enabled Plugin Stack.md` records Dataview retirement under W-370.
- `00_Workspace/Runtime Plugin Dependency Audit.md` records Dataview under retired controlled runtime.
- The governed one-plugin change is W-370 in `00_Workspace/Workspace Decision Log.md`.

Plugins intentionally retained:
- **Fileclass 0.2.15** remains transitional. Step 53 measured a smaller +1.160 s cost, but the current Base Vault still uses generated Fileclass definitions in `99_System/06_Fileclasses/` for typed-property input/validation. Workbench replacement of that complete editing workflow is not yet proven.
- **Breadcrumbs 4.21.11** remains under overlap review; no meaningful startup penalty was measured, and its unique navigation value has not been proven unnecessary.
- **Nodian 1.4.14** remains under overlap review; no meaningful startup penalty was measured.
- **Advanced Canvas 7.0.0** remains a presentation dependency; it showed only +225 ms in the Step 53 run and still provides unique Canvas UX.
- No multi-plugin cleanup was performed; the architecture rule remains one dependency change at a time.

Step 54 conclusion:
- Dataview is the only overlapping plugin for which both replacement and startup-benefit gates are currently proven.
- The controlled runtime already reflects that retirement.
- No runtime code change was needed in this step, so no new Workbench CI run was required.

### Step 55 completion evidence — 2026-10-04

Installed and accepted the exact CI-built Workbench candidate in a real disposable Obsidian integration vault.

Candidate identity:
- Workbench manifest version: **0.1.17**.
- The integration job did **not** run `npm run build` before installation.
- It installed the checked-in CI-built bundle directly:
  - `main.js`;
  - `manifest.json`;
  - `styles.css`.
- Before installation, `sha256sum -c artifact-sha256.txt` passed.
- Accepted candidate hashes:
  - `main.js`: `bc553fef67b5aa2cc7623b2811c05e7af8952296dd3b3ba55e663e3de5fc64aa`;
  - `manifest.json`: `a898ec3acce99650f18ded11235a236881ce8a8de86bfc857c70c5c4508d0e5d`;
  - `styles.css`: `445abe199f3dbf00724dc3cffa13aed58fc087adc9396e79de18ebe6b274b008`.
- The latest normal Build Workbench workflow for the Step 55 harness commit also passed: run `37232100200` (run 395), confirming the repository/build gate remained green.

Acceptance environment:
- Obsidian 1.13.7 under Xvfb on GitHub Actions.
- 12,000 generated Markdown notes.
- Warm-cache preview disabled; authoritative cold `full` build.
- Same real metadata-resolution/per-file-coverage barriers proven in Steps 49–50.
- Step 53/54 already handled third-party plugin overlap separately; Step 55 intentionally validates the exact Workbench candidate itself before the deeper integrated capability tests in Steps 56–59.

Acceptance criteria:
- exact artifact hashes must match CI-recorded hashes;
- Obsidian/vault must become readable before Workbench core-ready;
- complete per-file metadata coverage must precede Workbench core publication;
- all 12,000 Markdown files and generated model elements must be present;
- occurrence readiness must complete no earlier than core readiness;
- required Workbench commands must be registered;
- launch-to-core-ready must remain below the existing **60 s** full-size acceptance target.

Final acceptance result:
- GitHub Actions workflow: `Exact candidate startup acceptance`.
- Successful run: **`37232100208`** (run 1), conclusion `success`.
- Evidence artifact: `exact-candidate-startup-evidence`, artifact ID **`11313868263`**.
- Harness commit: `338eb289`.
- **Accepted: yes.**

Measured startup:
- launch → readable: **4,453 ms**;
- launch → complete metadata coverage: **31,218 ms**;
- launch → Workbench core ready: **32,416 ms**;
- launch → occurrence ready: **32,416 ms**;
- Workbench core indexing work: **175 ms**;
- files: **12,000**;
- elements: **12,000**;
- links: **21,491**;
- mode: **full**;
- required Workbench commands: **ready**.

Interpretation:
- The runner showed substantially slower Obsidian metadata completion than the Step 50 run, but the vault became readable at 4.453 s and remained usable while metadata continued loading.
- Workbench correctly withheld authoritative core publication until complete metadata coverage and then became ready ~1.2 s later.
- Core readiness at 32.416 s remained comfortably inside the existing 60 s acceptance bound.
- The Workbench-owned core work remained only 175 ms; most elapsed time was Obsidian metadata startup, reinforcing the staged-start architecture rather than motivating earlier Workbench work.

Step 55 conclusion:
- The exact CI-built Workbench candidate passes integrated startup-responsiveness acceptance.
- This step does not yet accept occurrence-view behavior, live editing, recovery or repeated restart behavior; those remain Steps 56–59.

### Step 56 completion evidence — 2026-10-04

Ran integrated real-Obsidian capability-staging acceptance for occurrence-aware versus core-only Workbench views.

Acceptance design:
- Used the exact accepted Workbench bundle from Step 55; artifact hashes were reverified before launch.
- Disposable Obsidian 1.13.7 vault contained:
  - the standard 12,000 generated MDSE notes;
  - six explicit acceptance fixture notes;
  - one governed Local Model on `Acceptance/Fixture Object.md` with:
    - a part occurrence `part-20261004210000002acceptfixture`;
    - an endpoint occurrence `ep-20261004210000003acceptfixture`;
  - a Requirement with block-targeted `appliesTo` to that local part occurrence.
- The real Workbench view commands were executed through Obsidian:
  - core-only controls: Functional and Design;
  - occurrence-aware: Internal, Structure, Interfaces, Where Used, Requirements.
- During each probe, the relevant Indexer occurrence-hydration gates were deliberately held closed.
- Acceptance required:
  - core-only views to complete while occurrence capability remained blocked;
  - occurrence-aware views not to publish a canvas before their required occurrence gate was released;
  - owner-targeted profiles to use `hydrateLocalOwners()`;
  - vault-wide occurrence profiles to use `whenLocalSettled()`;
  - the final canvas to contain the expected local occurrence marker.

Existing declaration contract also remained green:
- Internal: occurrence-aware;
- Structure: occurrence-aware;
- Interfaces: occurrence-aware;
- Where Used: occurrence-aware;
- Requirements: occurrence-aware;
- Functional, Design, Verification, Scenario, Behavior, Failure/Risk and Evidence: core-only.

Final integrated results:
- **Functional**
  - class: core-only;
  - completed while occurrence hydration was blocked: yes;
  - occurrence-hydration calls: none.
- **Design**
  - class: core-only;
  - completed while occurrence hydration was blocked: yes;
  - occurrence-hydration calls: none.
- **Internal**
  - class: occurrence-aware;
  - gate: targeted owner hydration;
  - owners requested: `Acceptance/Fixture Object.md`;
  - published before occurrence release: no;
  - local occurrence marker present after release: yes.
- **Structure**
  - class: occurrence-aware;
  - gate: targeted owner hydration;
  - owners requested: `Acceptance/Fixture Child.md`, `Acceptance/Fixture Object.md`;
  - published before occurrence release: no;
  - local part occurrence marker present after release: yes.
- **Interfaces**
  - class: occurrence-aware;
  - gate: vault-wide occurrence settlement;
  - published before occurrence release: no;
  - local endpoint occurrence marker present after release: yes.
- **Where Used**
  - class: occurrence-aware;
  - gate: vault-wide occurrence settlement;
  - published before occurrence release: no;
  - local part occurrence marker present after release: yes.
- **Requirements**
  - class: occurrence-aware;
  - gate: targeted owner hydration;
  - owners requested: `Acceptance/Fixture Object.md`;
  - published before occurrence release: no;
  - block-targeted local `appliesTo` occurrence marker present after release: yes.

Semantic/runtime result:
- mode: `full`;
- files: **12,006**;
- elements: **12,006**;
- occurrence work fully settled after the acceptance sequence.

Authoritative evidence:
- Workflow: `Integrated occurrence-view acceptance`.
- Successful run: **`37232510452`** (run 1).
- Evidence artifact: `view-capability-evidence`, artifact ID **`11314622355`**.
- Probe commit: `93935d39`.
- Workflow commit: `72871c1b`.
- Normal Build Workbench workflow for the final Step 56 commit also passed: **`37232510529`** (run 397).

Step 56 conclusion:
- Workbench view capability staging is behaving as intended in real Obsidian.
- Core-only views do not wait for occurrence hydration.
- Occurrence-aware views wait for only the capability they declare:
  - targeted owner hydration where the needed owners are knowable from the core graph;
  - full occurrence settlement only for Interfaces and Where Used, whose semantics require vault-wide occurrence completeness.
- No view published occurrence-derived output before the required capability was ready.

### Step 57 completion evidence — 2026-10-04

Ran integrated real-Obsidian live-edit acceptance while genuine Workbench background occurrence work was active.

Acceptance design:
- Used the exact accepted Workbench candidate from Step 55; artifact hashes were reverified before launch.
- Disposable Obsidian 1.13.7 vault contained:
  - 12,000 generated MDSE notes;
  - 500 Local Model background-owner fixtures;
  - a live-edit anchor Object with an initially unresolved `hasPart: [[Live Target]]`;
  - a reusable Function target.
- Background occurrence hydration was deliberately slowed for the 500 background fixtures so every foreground file operation could be proven to begin while background work was active.
- Before each operation the probe required:
  - `localHydrationActive > 0`;
  - 500 background candidates still pending.
- The acceptance sequence then performed real Obsidian vault operations:
  1. add;
  2. edit;
  3. rename;
  4. move;
  5. delete.
- Every potentially blocking vault/source/occurrence barrier had a bounded timeout and progress breadcrumb, so a deadlock would fail by named stage instead of hanging the workflow.

Per-operation proof:
- **Add**
  - background active: 500;
  - background pending: 500;
  - new `Acceptance/Live Target.md` indexed;
  - previously unresolved `Live Anchor hasPart Live Target` relationship resolved;
  - target Local Model region hydrated with 1 record.
- **Edit**
  - background active: 500;
  - background pending: 500;
  - added `performs: [[Live Function]]` relationship resolved in the live semantic graph;
  - edited Local Model region remained valid with 1 record.
- **Rename**
  - background active: 500;
  - background pending: 500;
  - old path removed from the model;
  - new renamed path indexed;
  - renamed note's `performs` relationship converged correctly;
  - Local Model ownership migrated to the renamed path with 1 record and no stale old-path region.
- **Move**
  - background active: 500;
  - background pending: 500;
  - old pre-move path removed;
  - folder-qualified moved path indexed;
  - moved note's `performs` relationship remained correct;
  - Local Model ownership migrated to the moved path with 1 record.
- **Delete**
  - background active: 500;
  - background pending: 500;
  - deleted path removed from the model;
  - relationship to the deleted path disappeared;
  - Local Model region removed completely (0 records).

Final convergence proof:
- source reconciliation pending: **false**;
- live update pending: **0**;
- occurrence hydration pending: **0**;
- Local Model read errors: **0**.
- Interrupted/requeued occurrence work completed successfully after the edit sequence.

Harness note:
- An earlier meaningful attempt showed `fileManager.renameFile()` itself exceeded a 10 s bound in the 12.5k-note vault because that API includes broader Obsidian link-maintenance behavior.
- Step 57 was narrowed to the actual Workbench requirement by using the real low-level `app.vault.rename()` event for rename/move, while separately asserting Workbench path, relationship and Local Model convergence.
- No Workbench runtime code change was required to pass Step 57; the changes were integration-harness-only.

Authoritative evidence:
- Workflow: `Integrated live-edit acceptance`.
- Successful run: **`37234448220`** (run 7).
- Evidence artifact: `live-edit-evidence`, artifact ID **`11314204465`**.
- Final Step 57 probe commit: `8fa81f09`.
- Normal Build Workbench workflow for the final Step 57 commit also passed: **`37234448217`** (run 406).

Step 57 conclusion:
- Add, edit, rename, move and delete all converge correctly while background occurrence work is active.
- Foreground source edits successfully preempt/cancel and requeue background occurrence work without leaving stale semantic state, stale paths, stale Local Model regions or stranded background queues.

### Step 58 completion evidence — 2026-10-04

Ran integrated real-Obsidian recovery acceptance covering bad cache, interrupted background work, plugin reload and full Obsidian restart.

Acceptance design:
- Used the exact accepted Workbench candidate; artifact hashes were reverified before launch.
- Disposable recovery vault contained:
  - 12,000 generated MDSE notes;
  - 300 Local Model background-owner fixtures;
  - one reusable background target Object;
  - warm-cache preview explicitly enabled for the recovery test.
- Recovery phases were isolated across separate Obsidian/XDG profiles and explicit process shutdowns so one renderer/process could not satisfy a later phase accidentally.

1. **Seed a valid semantic cache**
   - A normal real-Obsidian launch was allowed to reach core readiness and commit a valid Workbench semantic-cache generation.

2. **Inject bad cache**
   - Both cache manifests were deliberately corrupted before the next launch:
     - `manifest-a.json`;
     - `manifest-b.json`.
   - Warm preview remained enabled, forcing the startup restore path to attempt the damaged cache rather than bypass it.

3. **Bad-cache fallback acceptance**
   - Workbench rejected the cache:
     - restore record: `not used: No semantic cache manifest is available.`
   - Startup recovered through the authoritative cooperative cold path.
   - Resulting startup mode: **`full`**.
   - No partially restored semantic state was accepted as core-ready.

4. **Interrupted background work + plugin reload**
   - The 300 Local Model fixtures were slowed so genuine occurrence hydration was active.
   - At plugin reload:
     - active background occurrence owners: **300**.
   - Workbench was disabled/unloaded through persisted Obsidian plugin controls, then enabled again in the same renderer.
   - After reload:
     - plugin enabled: **yes**;
     - mode: **`full`**;
     - files: **12,301**;
     - elements: **12,301**;
     - source reconciliation pending: **false**;
     - occurrence hydration pending: **0**;
     - Local Model read errors: **0**.
   - Background work interrupted by unload did not leave stale or stranded derived state after reload.

5. **Full Obsidian restart**
   - The recovery renderer/process was explicitly terminated.
   - A fresh Obsidian process/profile reopened the same vault.
   - Post-recovery restart reached authoritative Workbench core-ready state:
     - launch → core ready: **43,257 ms**;
     - files: **12,301**;
     - elements: **12,301**;
     - links: **21,491**;
     - mode: **`full`**.
   - Source coverage after restart matched the recovery vault rather than reverting to any pre-recovery snapshot.

Authoritative evidence:
- Workflow: `Integrated recovery acceptance`.
- Successful run: **`37235759018`** (run 4), conclusion `success`.
- Evidence artifact: `recovery-evidence`, artifact ID **`11315602310`**.
- Step 58 implementation/harness commits:
  - `1fded7a0` — integrated recovery probe;
  - `f1e743ad` — recovery workflow;
  - `c1344437` — isolated Obsidian profiles across launches;
  - `e9d16e58` — explicit process shutdown between recovery phases;
  - `4c9eaa91` — persisted Obsidian plugin-control reload path.
- Normal Build Workbench workflow for the final Step 58 commit passed: **`37235759063`** (run 411).

Step 58 conclusion:
- Bad semantic cache fails closed and falls back to an authoritative full build.
- Plugin unload/reload safely interrupts active background occurrence work and returns to a fully settled source/occurrence state.
- A subsequent full Obsidian restart recovers the same current vault model without stale semantic state or stranded background work.
- No new runtime defect was required to be fixed in the accepted candidate; Step 58 changes were recovery-integration harness/control refinements.

### Step 59 completion evidence — 2026-10-04

Ran repeated real-Obsidian cold/warm restart-cycle acceptance against the accepted Workbench candidate and added explicit regression gates for cumulative degradation.

Acceptance design:
- Obsidian 1.13.7 under Xvfb.
- 12,000 generated semantic notes plus 300 Local Model background-owner fixtures and one reusable target, for **12,301** total modeled files/elements.
- Warm-cache preview enabled.
- Three cold launches alternated with three warm launches.
- Cold launches deleted semantic cache before startup and were required to use authoritative `full` mode.
- Warm launches restored the same known-good seeded semantic cache and were required to prove a real compatible restore.
- Each launch waited for source reconciliation and occurrence work to settle before measurement.
- The probe forced GC where available, then captured semantic counts, scheduler queues, reverse dependency size, renderer node/document/listener counts, JS heap usage, and launch-to-core-ready time.

Final explicit acceptance gates:
- semantic file/element/link counts must remain identical across all six launches;
- source reconciliation must be complete;
- live-update, occurrence-pending, occurrence-queued and occurrence-active counts must all be zero;
- Local Model read errors must remain zero;
- reverse relationship dependency-index size must remain identical across cycles;
- renderer `Nodes`, `Documents`, and `JSEventListeners` must remain identical across cycles;
- first-to-last same-mode JS heap growth must remain ≤10%;
- first-to-last same-mode core-readiness degradation must remain ≤20%.

Final accepted run:
- Workflow: `Repeated restart acceptance`.
- Successful run: **`37239424333`** (run 12).
- Evidence artifact: `restart-cycle-evidence`, artifact ID **`11315944954`**.
- Acceptance-hardening commit: **`476fbcad`** (`Enforce restart degradation acceptance limits`).
- Normal Build Workbench workflow also passed for the same commit: **`37239424369`** (run 425).

Semantic/scheduler results across every cycle:
- files: **12,301**;
- elements: **12,301**;
- links: **21,491**;
- source reconciliation pending: **false**;
- live updates pending: **0**;
- occurrence pending/queued/active: **0 / 0 / 0**;
- Local Model read errors: **0**;
- relationship re-resolution history after settled restart: **0**;
- reverse dependency index remained exactly:
  - sources: **12,000**;
  - resolved target keys: **12,000**;
  - authored keys: **12,000**;
  - resolved associations: **42,266**;
  - authored associations: **42,266**;
  - stored memberships: **169,064**;
- renderer metrics remained exactly:
  - Nodes: **39,871**;
  - Documents: **2**;
  - JS event listeners: **1,332**.

Cold-cycle trend:
- JS heap used: **77,284,260 → 77,348,128 → 77,299,176 bytes**;
- first-to-last heap ratio: **1.00019** (~+0.02%);
- core ready: **42,903 → 42,124 → 43,529 ms**;
- first-to-last core-ready ratio: **1.01459** (~+1.46%);
- all three launches used `full` mode.

Warm-cycle trend:
- JS heap used: **78,792,288 → 78,888,180 → 77,977,276 bytes**;
- first-to-last heap ratio: **0.98966** (~-1.03%);
- core ready: **42,297 → 43,255 → 43,563 ms**;
- first-to-last core-ready ratio: **1.02993** (~+2.99%);
- all three launches used `restored` mode with `restored; cache matched current file fingerprints`.

Interpretation:
- There is no cumulative semantic-state drift across repeated restarts.
- There is no accumulation of pending or active scheduler work.
- Reverse dependency-index and renderer structural counts remain stable.
- JS heap shows no cumulative growth trend in either cold or warm sequences.
- Core-readiness timing shows normal run-to-run variance but no cumulative degradation approaching the acceptance limit.
- Warm restore remains semantically equivalent to cold reconstruction across repeated cycles.

Step 59 conclusion:
- Repeated cold/warm restarts do not produce cumulative memory growth, stale semantic state, reverse-index drift, renderer/listener accumulation, stranded background work or material scheduling/startup degradation.
- The accepted performance/stability candidate is ready for Step 60 release-candidate freeze and handoff documentation.

**Current resume point:** the numbered performance/stability roadmap is complete at Step 60. Do not invent a Step 61; return to the separate MDSE v0.8 integration/release plan for subsequent work.

### Step 60 completion evidence — 2026-10-04

Frozen the accepted Workbench performance/stability candidate and recorded the exact handoff evidence.

Accepted candidate:
- repository: `spencerskelly/MDSE_Workbench`;
- branch: `main`;
- frozen source commit: **`476fbcad08ecd03f8c2c49cd3126393beb6ab412`**;
- Workbench manifest version: **0.1.17**;
- no runtime source change was introduced by Step 60.

Exact checked-in plugin artifact hashes:
- `main.js`: **`bc553fef67b5aa2cc7623b2811c05e7af8952296dd3b3ba55e663e3de5fc64aa`**;
- `manifest.json`: **`a898ec3acce99650f18ded11235a236881ce8a8de86bfc857c70c5c4508d0e5d`**;
- `styles.css`: **`445abe199f3dbf00724dc3cffa13aed58fc087adc9396e79de18ebe6b274b008`**;
- hash authority: `MDSE_Workbench/artifact-sha256.txt` at the frozen commit.

Integrated acceptance evidence retained for the frozen candidate:
- Step 55 exact-candidate integrated startup acceptance completed before later acceptance work.
- Step 56 occurrence-view staging acceptance: workflow `Integrated occurrence-view acceptance`, run **37232510452**.
- Step 57 live-edit/background-work acceptance: workflow `Integrated live-edit acceptance`, run **37234448220**.
- Step 58 recovery acceptance: workflow `Integrated recovery acceptance`, run **37235759018**.
- Step 59 repeated restart acceptance: workflow `Repeated restart acceptance`, run **37239424333**.
- Normal `Build Workbench artifact` workflow for the frozen commit passed as run **37239424369**.

Frozen runtime conclusions:
- immediate/startup work is staged rather than monopolizing Obsidian startup;
- core semantic readiness is separated from deferred occurrence hydration;
- occurrence-aware views wait only for the capability they require;
- live edits converge while background occurrence work is active;
- corrupted semantic cache fails closed to authoritative cold reconstruction;
- plugin reload and full process restart recover without stale or stranded derived state;
- three cold plus three warm restart cycles showed no cumulative semantic drift, scheduler buildup, reverse-index growth, renderer/listener accumulation, JS-heap growth trend or material core-readiness degradation.

Governance/handoff updates:
- `00_Workspace/00 - Current State.md` now identifies the frozen standalone Workbench stability candidate and points to this roadmap for acceptance evidence.
- `00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md` now tells later chats not to reopen Steps 18–60 unless the frozen candidate changes or new evidence invalidates acceptance.
- Performance/stability work is complete at this boundary. Promotion into the controlled Base Vault remains a separate release/integration action and is not implied by this freeze.

Step 60 conclusion:
- The performance/stability sequence **Steps 18–60 is complete**.
- The accepted standalone candidate is frozen at `476fbcad08ecd03f8c2c49cd3126393beb6ab412`.
- Any later runtime change creates a new candidate and requires rerunning the acceptance scope affected by that change.

**Current resume point:** the numbered performance/stability roadmap is complete. Do not invent Step 61. Continue with the separate MDSE v0.8 integration/release plan when Spencer explicitly chooses to proceed.

## Integration follow-up — acceptance harness packaging (high priority, outside Steps 18–60)

This is **not Step 61** and does not reopen the completed runtime performance/stability roadmap.

During IMP-009 integration on 2026-10-06, real-QEAX bridge run `37487843505` proved the importer-side IMP-009 validator and Workbench read-only real-vault scan, then failed before semantic model evaluation because Workbench 0.1.18's `scripts/real-vault-acceptance.ts` uses top-level `await` while the package is executed in a CommonJS context. The direct `npm run accept:real-vault` path therefore fails during TSX/esbuild transformation rather than because of a vault/runtime defect.

High-priority Workbench follow-up:
- make `accept:real-vault` directly runnable from the repository's declared package/module configuration (preferred: wrap executable code in an async `main()` like the existing edit harness, or otherwise make the script explicitly ESM);
- add CI that executes the packaged command itself so module-format drift cannot silently break acceptance tooling;
- keep this change isolated from `main.js` runtime behavior unless runtime changes are actually necessary;
- rerun the affected real-vault acceptance command after the harness fix.

Until that follow-up is landed in Workbench, the importer bridge uses the **same accepted Workbench 0.1.18 source** from artifact commit `b0c4e2c6bdfb96d36f51d8152b17be22592ef174`, bundles the acceptance harness as ESM, and runs that bundle. This preserves the semantic gate without treating a test-runner packaging defect as an importer failure.

### 2026-10-06 follow-up — preserve unrelated bytes during Local Model edits

IMP-009 bridge run `37490701170` exposed a second integration-level hardening opportunity after the acceptance harness itself was made runnable. Workbench 0.1.18 passed Local Model parsing/topology checks but reported four no-op formatting drifts. All four were traced to three importer-generated notes whose EA narrative contained CRLF while generated structure used LF. The importer side is corrected by W-395 so generated Markdown is canonical LF.

Defense-in-depth Workbench follow-up, **high priority but not a new numbered stability step**:
- structured Local Model patching should preserve text outside the replaced governed record byte-for-byte, even if a legacy/user-authored note has mixed line endings;
- `editableLocalRegion()` currently selects one EOL for the entire reconstructed file from `text.includes("\\r\\n")`, which can normalize unrelated text;
- prefer a minimal splice or record-local EOL strategy that changes only the intended Local Model record;
- add a focused mixed-EOL no-op and real edit regression before the next Workbench release that changes writer behavior.

This does not invalidate the accepted 0.1.18 runtime for canonical importer output, but it closes a useful robustness gap for noncanonical/legacy notes.

## Reconstructed remaining steps

43. Ensure cache restore failure always falls back to a cooperative cold build without leaving partially restored semantic state visible.

48. Add failure-injection tests proving one derived subsystem can fail without making ordinary Obsidian editing or unrelated Workbench capabilities unusable.



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
