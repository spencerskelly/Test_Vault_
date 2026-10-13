# Branch Cleanup — Checkpoint BR-73: Byte-Level Workbench Bundle / Lock Verification

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Exact candidate commit: 58ab10870f11757cf1bf367ecd5868be9b60933d
Result: ALL THREE WORKBENCH BUNDLE FILES MATCH CONTROLLED PLUGIN-LOCK SHA-256.

## Evidence method

Fetched exact GitHub file contents at the frozen Step22 commit and computed SHA-256 over their UTF-8 bytes using an in-tool JavaScript SHA-256 routine; verified routine against known `abc` vector (`ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`). Compared hashes to **mdse-workbench-specific** lock subsection, not similarly named keys under other plugins.

| Runtime file | Git blob | Computed SHA-256 | Lock SHA-256 | Result |
|---|---|---|---|---|
| `55_Workbench/main.js` | `f8a0b6cfa454437e68edaff7d5adf21965606a3c` | `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7` | same | MATCH |
| `55_Workbench/manifest.json` | `a5852e592eafa027f52c2d052497293aec51a107` | `6e2a74891743df424d80fe5cb551460ce4971852bf152909a2a5cecbbb218bd9` | same | MATCH |
| `55_Workbench/styles.css` | `ad4045967523303d67d8330282fade2fc3a8943a` | `445abe199f3dbf00724dc3cffa13aed58fc087adc9396e79de18ebe6b274b008` | same | MATCH |

Lock blob: `c430670577318457972a154012d08c6d28e6d11b`.
Lock entry identifies Workbench version `0.1.18`, source `spencerskelly/MDSE_Workbench` artifact `b0c4e2c6bdfb96d36f51d8152b17be22592ef174`, historical verified build run `37408465530` and startup run `37408519667`.

## What is established

The committed three-file `55_Workbench` runtime payload at the exact Step22 commit is byte-identical to the controlled Workbench lock references. This is stronger than matching version strings or Git blob counts. It is a source-level remote hash verification, not execution of the installed plugin.

## What is NOT established

- Whether current TypeScript source reproduces these same bundle bytes using pinned dependency/toolchain conditions.
- Whether the generated lean Base copies *these* exact bytes without accidental overwrite or stale payload.
- Whether the running Obsidian plugin at a test workstation loads this same bundle.
- Whether the locked Workbench 0.1.18 build handles new importer 0.8.19 Local Model 0.5 output correctly end to end.
- Actual Windows/Mac Obsidian tests, full release checks, QEAX owner decisions or formal signoff.

## Next action

BR-74: Inspect the runtime Base builder's Workbench artifact source/copy and plugin lock enforcement path; distinguish artifact source path from authoritative 55_Workbench source. Then a separate, approved clean reproducible build and real/imported fixture acceptance can close runtime-origin and integration gates.

No GitHub code or PR state changed beyond adding this audit checkpoint. No PR merge, close, release, branch deletion or archive.
