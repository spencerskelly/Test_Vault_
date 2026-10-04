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

## Reconstructed remaining steps

33. Measure targeted relationship re-resolution fan-out so we can see how many source notes each path-set change actually invalidates.

34. Define a candidate-count threshold above which targeted relationship re-resolution falls back to the cooperative whole-graph path.

35. Prove targeted re-resolution remains correct for ambiguous basenames, folder-qualified links, aliases, fragments and case/path normalization.

36. Add a fail-closed invariant that prevents targeted re-resolution when its derived dependency evidence is incomplete or inconsistent.

37. Benchmark add, delete and rename warm reconciliation with targeted relationship re-resolution at representative vault scale.

38. Expose targeted-versus-full relationship reconciliation mode, candidate count and elapsed time in diagnostics.

39. Bound the memory cost of reverse relationship dependency indexes and report their size in explicit diagnostics.

40. Verify that a schema change invalidates every derived index/cache surface that depends on relationship definitions.

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
