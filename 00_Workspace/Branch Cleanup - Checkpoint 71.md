# Branch Cleanup — Checkpoint BR-71: Workbench Local Model 0.5 Reader and Mutation Planner

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Candidate source: consolidation/step22-single-repo-cutover-2026-10-11
Status: SOURCE INSPECTION ONLY; no build, test or real GUI run.

## Inspected exact source files

- `55_Workbench/manifest.json`, blob `a5852e592eafa027f52c2d052497293aec51a107`: plugin version 0.1.18.
- `55_Workbench/package.json`, blob `2d4607eaf1ceaf0d2a822b3f75c957795de603a5`: version 0.1.18; build/typecheck/test scripts and real-vault read/edit scan scripts listed.
- `55_Workbench/src/core/localmodel.ts`, blob `f7fd4d43bafb57f8b4b706689f4cf8d03bc1971c`: reader and validation.
- `55_Workbench/src/core/localmodel-edit.ts`, blob `72a1e48acc72b8d516642544d4cf3b29f740cca8`: structured text mutation planner.
- Governed schema `99_System/03_Schemas/local-model.yaml`, blob `361dee8269f9fbdfd16bcee33a1b808015f7ba5a`.

## Observations

1. `READABLE_VERSIONS = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6"]` in parser; `WRITABLE_VERSION = "0.5"`.
2. Parser contains schema-specific handling of Local Model 0.5, `equals` references and a comment describing symmetric same-owner 0.5 BindingConnector equality versus older schema review semantics.
3. Mutation planner checks `region.schemaVersion !== WRITABLE_VERSION` and throws with a read-only warning. This is a critical implementation protection for 0.4 records not silently promoted.
4. Mutation planner explicitly identifies canonical 0.5 BindingConnector edits changing both Interface records in a single planned operation. It rejects nonlocal, missing block identity and duplicate equals targets, with peer update logic.
5. `manifest.json` and `package.json` retain Workbench 0.1.18, not 0.1.19. Workbench 0.5 logic is present in those sources despite importer UI's statement that 0.1.19 compatibility is pending.
6. **Authority inconsistency:** governed `local-model.yaml` readable versions only 0.1–0.5, but parser includes 0.6. Cannot infer whether 0.6 is experimental, accidentally carried forward, or intentionally forward-compatible without a separate W decision, actual validators and tests.

## Updated IMP-011 interpretation

- Local Model 0.5 format rules: PRESENT in governed schema.
- Importer 0.8.19 code for same-owner canonical equals and explicit Connection.exposes: PRESENT (BR-70).
- Workbench 0.1.18 parser and symmetric equals mutation plan: PRESENT in source.
- Exact generated Workbench artifact compiled from inspected source: NOT VERIFIED.
- Workbench regression tests for older 0.4 read-only semantics, 0.5 canonical equals, source-preserving save/reopen: NOT VERIFIED IN THIS STEP.
- Real source import/reconciliation matching 23 exposes, 209 canonical equals, 17 review-only: NOT RERUN / UNVERIFIED.
- Physical Mac/Windows Obsidian GUI acceptance and formal release approval: OPEN.

## Release qualification / next bounded work

1. Review the Workbench Local Model 0.5 test suite and actual build artifact/version pin; distinguish existing tests from untested behaviors.
2. Find owner decision governing optional 0.6 reader support or remove unsupported compatibility claim only through approved source PR—not by editing this audit.
3. Check importer 0.8.19 version expectation for Workbench 0.1.19 against the source and runtime lock; resolve factual drift after tests.
4. Run a separate approved 0.5 import-to-Workbench roundtrip and deterministic source disposition audit, then update IMP-011 status as appropriate.

BR-71 completed substantive source inspection. No manifest, source, plugin binaries, CI, PR statuses, release or branches modified.

NEXT BR-72: Inspect Workbench Local Model 0.5 test cases and version lock checks, with exact paths and evidence; do not assume source code alone proves runtime behavior.
