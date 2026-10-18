# Pass 5 — Pinned translator preflight entry

Committed `v2-translator-preflight.mjs` at `980a1bd14ec5ba6511bf2e0ec83f176d6440888c`; it requires one explicit checkout root, invokes the pinned registry integrity and coverage loader and exits nonzero when validation fails. Success reports PREVIEW_ONLY and nativeEmission false. No model data is loaded, and no SysML v2 text is emitted.

Fixed `pinned-v2-eligibility.test.mjs` at `7f8ec9b2310fd1cb761a90f068415f21fdaa9b2b` to derive the test directory using `fileURLToPath(import.meta.url)` instead of `import.meta.dirname`, improving compatibility with older Node ESM runtimes.

The actual SysML v2 emitter/translator is not yet implemented as a release-grade entrypoint. Therefore the new CLI is a prepared integration boundary, **not** proof that every importer path is gated. No exact full-checkout JS/Python tests or actual-registry runtime checks were executed here. Native emission remains disabled; release NO-GO.

When a complete checkout is available, run `node --test 14_Workbench/registry/runtime/pinned-v2-eligibility.test.mjs`, `node 14_Workbench/registry/runtime/v2-translator-preflight.mjs .`, and `python3 -m unittest discover -s 15_Testing -p 'test_sysml_v2*.py'`. Follow with deliberate registry drift injection and verify nonzero exit. Never bypass preflight for the future emitter.
