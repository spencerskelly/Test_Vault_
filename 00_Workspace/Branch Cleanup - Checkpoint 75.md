# Branch Cleanup — Checkpoint BR-75: Vendored Workbench Runtime Exact Blob Match

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Exact candidate commit: 58ab10870f11757cf1bf367ecd5868be9b60933d
Status: COMMITTED VENDORED PAYLOAD VERIFIED; GENERATED BASE NOT EXECUTED.

## Direct GitHub evidence

At the exact frozen Step22 SHA, fetched three committed files under `Base Vault/Runtime/Plugins/mdse-workbench/` and matched each native Git blob SHA to its independently fetched `55_Workbench/` counterpart in BR-73:

| File | Vendored Git blob | Corresponding 55_Workbench Git blob | Result |
|---|---|---|---|
| main.js | f8a0b6cfa454437e68edaff7d5adf21965606a3c | f8a0b6cfa454437e68edaff7d5adf21965606a3c | IDENTICAL |
| manifest.json | a5852e592eafa027f52c2d052497293aec51a107 | a5852e592eafa027f52c2d052497293aec51a107 | IDENTICAL |
| styles.css | ad4045967523303d67d8330282fade2fc3a8943a | ad4045967523303d67d8330282fade2fc3a8943a | IDENTICAL |

Lock file `.obsidian/plugin-lock.yaml` blob `c430670577318457972a154012d08c6d28e6d11b` retains mdse-workbench v0.1.18 and expected per-file SHA-256:
- main.js: `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`
- manifest.json: `6e2a74891743df424d80fe5cb551460ce4971852bf152909a2a5cecbbb218bd9`
- styles.css: `445abe199f3dbf00724dc3cffa13aed58fc087adc9396e79de18ebe6b274b008`

BR-73 independently computed these SHA-256 values for the same Git blobs under 55_Workbench and matched lock. Therefore Git-object identity carries this verified byte equality to the vendored payload. This step did not separately recompute vendored SHA-256, and it need not: identical Git blob means identical file content.

## Evidence boundary

- The **three committed Workbench runtime artifacts** and **their corresponding vendored plugin files** are identical at the frozen Step22 SHA and agree with the Workbench section of the release lock.
- `build-base.py` copies vendored payload files and `check-release.py --base` validates generated copies (BR-74); neither script was executed in BR-75.
- A clean generated Base still needs its exact file inventory, payload hash identity, initialization state and runtime plugin checks recorded after execution.
- TypeScript source-to-bundle reproducibility, imported Local Model 0.5 Workbench integration, real Mac/Windows GUI acceptance, QEAX/security and formal release decisions remain unresolved.

## Next bounded action

BR-76: Create a controlled, disposable Base-generation execution recipe with expected source commit, clean output directory, explicit check-release flags, artifact digest report and cleanup rules; if an actual complete checked-out workspace becomes available, run it and preserve only confidentiality-safe results. Do not treat a script inspection as an executed PASS.

No runtime updates, source changes, PR review/merge/close, release, archival, branch deletion or QEAX access.
