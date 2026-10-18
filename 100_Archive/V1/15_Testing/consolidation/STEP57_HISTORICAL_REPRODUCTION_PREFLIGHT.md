# Step 57 — Historical reproduction preflight (2026-10-14)

**Status: preflight completed; historical binary reproduction NOT executed. Release hold remains.**

## Evidence at original Workbench commit
Original reference: `b0c4e2c6bdfb96d36f51d8152b17be22592ef174`. GitHub API returned **no pull-request-triggered Actions runs** for this commit; this does not establish the absence of all historical runs.

The following Git blob IDs were compared directly with PR #43 `integration/p03-legacy-compat-tests-20261013`:

| Original path -> consolidated path | Original blob | Current blob | Match |
| --- | --- | --- | --- |
| `main.js` -> `55_Workbench/main.js` | `f8a0b6cfa454437e68edaff7d5adf21965606a3c` | same | yes |
| `artifact-sha256.txt` -> `55_Workbench/artifact-sha256.txt` | `adb97fff4887e425e5060e3ee8525544bcaa761c` | same | yes |
| `package-lock.json` -> `55_Workbench/package-lock.json` | `ed6db5399ef290ba77b7e36389619a49aa48b791` | same | yes |
| `esbuild.config.mjs` -> `55_Workbench/esbuild.config.mjs` | `98c041f56369a620c931ee9c884442116c9eebbb` | same | yes |
| `package.json` -> `55_Workbench/package.json` | `b70548164ea577939de38f5ddfcf0cf6d96f8bdd` | `2d4607eaf1ceaf0d2a822b3f75c957795de603a5` | **no** |

**Package.json delta:** the consolidated copy adds script `accept:real-vault:05` with command `tsx scripts/real-vault-05-acceptance.ts`. Other parsed package fields, including the `build` script and declared dependencies, match. This difference was not surfaced in the earlier rename-centric compare summary; do not claim all files are identical.

## Controlled bundle provenance

The historical committed bundle itself and its hash manifest are byte-identical to the consolidated tracked artifacts. The difference arises **when CI rebuilds** `main.js`; it is not evidence of a changed committed artifact.

- Governed SHA-256: `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`
- Two current CI builds: `d2c4d90142718f3363196f0c5e7663cc9d87fc22655b62bfbc2887a69d2dec13`
- First difference offset: 13733.
- `npm ci` consumes the same original lockfile, while CI selects Node `20` (not an exact historical patch). Exact original Node/npm/esbuild runtime information has not been retrieved.

## Safe reproduction procedure (not yet run)

1. In a **disposable** directory, checkout the original commit tree into a detached worktree, excluding any model archives; no historical branch movement.
2. Capture `node --version`, `npm --version`, `npm ls esbuild typescript --depth=0`, operating system and lockfile SHA before build.
3. Run `npm ci`, then `npm run build` on that historical Workbench root and SHA-256 the generated `main.js`.
4. Repeat with controlled Node 20 patch versions if toolchain evidence warrants it; never change `artifact-sha256.txt`, `main.js` on the governed branch, or other releases.
5. Compare candidate hashes to `1690d32a...` and current `d2c4d901...`; preserve failed results as evidence. If none match, explicitly retain the unresolved provenance hold.

### Next checkpoint

Run a detached, isolated historical source build and capture exact versions/hashes as evidence. A CI workflow or runner must be provisioned for that experiment; this pass was API-only and did not execute historical Node builds.

No binaries, source, model data, branches, workflows or governance manifests modified.
