# Step 60 — Historical binary reproduced (2026-10-14)

## Verified GitHub Actions evidence

Run: https://github.com/spencerskelly/Test_Vault_/actions/runs/38604566786
Job ID: 115992019801
Workflow: Step58 isolated historical Workbench reproduction
Outcome: SUCCESS, diagnostic result **Historical binary reproduced: YES**.

- Original commit: `b0c4e2c6bdfb96d36f51d8152b17be22592ef174`
- Node: `v20.20.2`
- npm: `10.8.2`
- esbuild: `0.24.2`
- TypeScript: `5.9.3`
- Original package-lock SHA-256: `abdd780bd9fd725adef366096ed4070144e41297e00b73e3d672ad4116d73c92`
- Governed original `main.js` SHA-256: `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`
- Rebuilt original source `main.js` SHA-256: `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`

The current consolidated P04 validation is **still failing** (run `38604566857`); earlier P04 run produced bundle `d2c4d90142718f3363196f0c5e7663cc9d87fc22655b62bfbc2887a69d2dec13`. The latest P03 and MDSE integration runs succeeded.

## Interpretation and control

Historical binary provenance is **verified** for the exact original commit and reproducible current Ubuntu/Node 20 environment. This does NOT prove all consolidated source files are unchanged or that the current candidate is release-equivalent.

The historical-vs-current package.json differs by an additional acceptance-test script, while original package lock, esbuild configuration, committed bundle and hash manifest are byte-identical. Diffing *all* source blobs and instrumenting the two builds is now the most valuable next operation; avoid assuming a toolchain cause.

**Release hold remains in effect** for consolidated Workbench until controlled source/build equivalence or separately approved release governance. Do not overwrite `main.js` or `artifact-sha256.txt`, merge, delete branches, or publish plugins.

## Next: Step 61

Compare exact Git blob IDs for every historical `src/` and consolidated `55_Workbench/src/` path, including new/removed files. Locate the first changed source contributing to the binary delta; then test the minimum source/config hypothesis on a disposable copy. Preserve the historical artifact.
