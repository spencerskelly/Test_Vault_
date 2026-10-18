# Pass 5 — Pinned eligibility preview integration

Added `14_Workbench/registry/runtime/pinned-v2-eligibility.mjs` (commit `a67a6b9`). It loads three version-pinned JSON registry files, independently checks their SHA-256 digests, validates exact 26-family coverage and 11-decision coverage, and forbids native emission when checks fail. It calls the existing Phase 4 eligibility engine for candidate previews only. An unknown source relationship family is rejected. Every returned preview is marked nonmutating and non-emitting, regardless of candidate eligibility.

Added `14_Workbench/registry/runtime/pinned-v2-eligibility.test.mjs` (commit `9c92328`) with three synthetic Node tests: normal pin loading, unknown family denial, and modified registry hash refusal. Run: `node --test 14_Workbench/registry/runtime/pinned-v2-eligibility.test.mjs`.

**Not yet verified:** the exact tests have not executed in a full repository checkout, and existing consumers have not been switched to use this wrapper. This is an opt-in gate, not universal enforcement. The registry describes provisional candidate semantics; no SysML v2 parser or serializer is invoked, and no native content is written. Still release NO-GO.

Next pass: run exact JS/Python pin tests from checkout, remove reliance on `import.meta.dirname` if the chosen supported Node version requires it, integrate this check into the translator entrypoint, and add explicit no-bypass behavior on pin drift.
