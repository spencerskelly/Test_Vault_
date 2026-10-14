# Step 56 — Historical Workbench artifact provenance (2026-10-14)

Status: **historical source ancestry assessed; cause unproven; release hold remains**.

## Commits and comparison
- Original Workbench origin: `b0c4e2c6bdfb96d36f51d8152b17be22592ef174`
- PR #43 at prior gate: `b89f9664004f1b676e9b8f6499a194435bfbcf1b`.
- GitHub compare reports ahead=1718, behind=0. Relevant path comparisons show *renamed with zero changes* from root Workbench files to `55_Workbench/`: `main.js`, `package.json`, `package-lock.json`, `esbuild.config.mjs` and listed `src/core/*` modules. This is evidence of matching paths reported, NOT proof that every source file in the full tree is identical (compare may limit returned files).
- Current `55_Workbench/artifact-sha256.txt` governs `main.js` digest `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`; manifest and CSS have separate hashes.
- CI two clean builds agree on `d2c4d90142718f3363196f0c5e7663cc9d87fc22655b62bfbc2887a69d2dec13`. Earliest bundle byte mismatch: 13733. Validation run 38601601253 step `Require reproduced artifacts to match governed Workbench baseline` fails.

## Build environment facts
- Current `package.json`: Workbench `0.1.18`, `npm run build` = `tsc --noEmit && node esbuild.config.mjs production`; esbuild dependency declaration `^0.24.0`.
- Current package lock is v3 and records esbuild `0.24.2` platform package. `npm ci` installs lock-managed dependencies.
- `esbuild.config.mjs` bundles `src/main.ts`, CommonJS target es2020, external Obsidian/Electron/code-mirror/etc., tree shaking on, production sourcemap disabled.
- Current validation workflow uses `actions/setup-node@v4` with `node-version: '20'`; exact historical Node patch/build environment was not established by this comparison.
- **Hypothesis only:** Node version, esbuild build environment, platform, or historical artifact generation provenance may account for difference. The current evidence does not assign causality.

## Required next experiment (read-only)
1. Obtain exact earlier GitHub Actions run build logs/manifest for historical `b0c4e2c6` commit where possible; record Node/npm/esbuild/TypeScript versions with timestamps and provenance.
2. Confirm every relevant Workbench source path and blob ID against the historical root (not just the compare API's returned subset).
3. Build a *temporary, isolated* historical checkout with recorded Node patch and `npm ci`. Compare `main.js` hashes and byte-offset; do not commit resulting artifacts.
4. If unchanged source + exact old environment reproduces governed hash, pin CI environment and rerun; otherwise classify binary provenance gap and seek approval for a controlled release decision.
5. Leave release-equivalence check failing until match or separately approved governance resolution. Never update `artifact-sha256.txt` merely to make CI pass.

No source, model, QEAX, historical branch, controlled binary, hash manifest, or workflow changes were made by this step.
