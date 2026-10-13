# Branch Cleanup — Checkpoint BR-72: Workbench Local Model Regression Coverage and Runtime Lock

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Candidate source: consolidation/step22-single-repo-cutover-2026-10-11 @ 58ab10870f11757cf1bf367ecd5868be9b60933d
Status: SOURCE COVERAGE REVIEW ONLY; no suite execution or binary attestation.

## Source files read with exact Git blobs

- `55_Workbench/test/localmodel.test.ts`: `c411610890d23c5fc13ddea4d25ed663f7b8a047` (33 `test(` declarations)
- `55_Workbench/test/localmodel-edit.test.ts`: `77ac97b27261a9f9f4974bbbeb09147f9f06db9b` (68 `test(` declarations)
- `.obsidian/plugin-lock.yaml`: `c430670577318457972a154012d08c6d28e6d11b`
- Prior BR-71: `55_Workbench/src/core/localmodel.ts` `f7fd4d43bafb57f8b4b706689f4cf8d03bc1971c` and `src/core/localmodel-edit.ts` `72a1e48acc72b8d516642544d4cf3b29f740cca8`.
- Prior BR-71: `55_Workbench/manifest.json` version 0.1.18, `package.json` version 0.1.18.

## Source-level regression coverage

**Reader/validator file — 33 tests:** includes explicit test names for governed 0.5 schema fixture agreement, 0.4 syntax and owner-specific Connection.exposes rules, 0.4/0.5 Object/interface definition semantics, canonical 0.5 reciprocal same-owner Interface `equals`, unilateral `equals.asymmetric` error, cross-owner `equals.cross-context`, self/duplicate/malformed `equals`, and preserving 0.4 temporary review semantics. Also has unsupported-future-schema behavior test.

**Mutation planner file — 68 tests:** includes structured editing rejection on old 0.1, endpoint deletion dependency reporting for `equals`, adding a new equality target without discarding previously persisted links and updating its reciprocal endpoint, removing an equality target while retaining other relationships, blocking missing local endpoint, 0.5 definition validation, and invalid self/duplicate/cross-owner/malformed equality proposals.

Together 101 test declarations are present in these two files. This is not equivalent to 101 current passing tests or complete repository suite coverage.

## Exact lock evidence

Controlled `.obsidian/plugin-lock.yaml` entry:
- plugin id `mdse-workbench`
- version `0.1.18`
- source claims standalone `spencerskelly/MDSE_Workbench` artifact `b0c4e2c6bdfb96d36f51d8152b17be22592ef174` with historic verified build run `37408465530` and startup run `37408519667`.
- Locked runtime main.js SHA-256: `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`.
- locked manifest.json SHA-256: `6e2a74891743df424d80fe5cb551460ce4971852bf152909a2a5cecbbb218bd9`.
- The `manifest.json` and `package.json` in 55_Workbench both name 0.1.18. **Matching version strings and lock metadata do NOT prove the checked-in main.js binary's bytes or provenance match current TypeScript source.** Hash against exact runtime files and compile in a separately controlled disposable checkout.

## Remaining release/authority gaps

1. Actually run Workbench test suite and build/typecheck on exact reviewed candidate SHA.
2. Compute SHA-256 of generated/retained plugin binaries and compare against runtime lock and Base payload without silently overwriting lock.
3. Run read-only real imported Local Model 0.5 scan and safe disposable edit/reparse/undo/redo, including old 0.4 nonreinterpretation.
4. Validate importer 249 BindingConnector dispositions: 23 resolved exposes, 209 canonical equality, 17 cross-owner review-only on authorized private snapshot.
5. Resolve read-authority mismatch: Workbench parser lists 0.6 as readable but governed 0.5 YAML lists readable versions through 0.5. Source tests and runtime support cannot override governed release decision.
6. Obtain owner approval before updating IMP-011 to closed or claiming released Workbench 0.1.19 / MDSE 0.8.0.

## Current interpretation

IMP-011 is **partially implementation-complete with significant relevant test coverage present**, but still OPEN for integrated verification and formal release. Previous issue-register wording 'implementation required' is likely too coarse; correct it only through a reviewed engineering/governance change.

NEXT BR-73: Validate actual Workbench built-bundle provenance or release lock alignment using available read-only source, distinguishing what can be established remotely from what requires a local reproducible build.

No source change, build execution, GUI operation, PR approval, merge, branch deletion, archive, QEAX content retrieval or release.
