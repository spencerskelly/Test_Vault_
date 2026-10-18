# Pass 03 — Plugin dependency and lock alignment (audit increment)
Date: 2026-10-17. **Status:** audit complete, release alignment **BLOCKED**. No versions/hashes modified.

## Authoritative artifact/pin matrix verified through GitHub file reads
| Plugin | Source package | Vendored manifest | plugin-lock.yaml | release YAML | Finding |
|---|---|---|---|---|---|
| mdse-bootstrap | 13_Bootstrap/Tools/v0.3.1 package version **0.3.1** | **0.3.1** | **0.3.1** | **0.3.0** active; 0.3.1 candidate source | **MISMATCH** in release manifest; first-open verification needed before promotion |
| mdse-workbench | 14_Workbench/package.json **0.1.18** | **0.1.18** | **0.1.18** | **0.1.18** | Versions align for **legacy shipped artifact**, not for latest v2 popup source; new build/lock/runtime acceptance needed |

## Locked runtime plugin dependencies
Current `.obsidian/plugin-lock.yaml` schema 2 lists 10 enabled community plugins with locked files and optional governed `data.json`. Required core plugins are `bases, canvas, properties, file-explorer, command-palette`; core `templates` is disabled. The lock requires Obsidian >=1.13.0, whereas vendored MDSE manifests themselves declare minAppVersion 1.5.0; the **stricter aggregate base requirement is 1.13.0**. Source code version declarations do not prove runtime SHA-256 equality; byte-by-byte hash verification and Obsidian first-open are still required. Preserve plugin IDs and locked settings.

Current locked community IDs: `mdse-bootstrap` 0.3.1, `mdse-workbench` 0.1.18, `templater-obsidian` 2.25.0, `fileclass` 0.2.15, `breadcrumbs` 4.21.11, `obsidian-git` 2.40.0, `advanced-canvas` 7.0.0, `nodian` 1.4.14, `quickadd` 2.23.0, `table-exporter` 0.3.0.

## Tests and release guard
`15_Testing/check_v2_import_kit.py` already checks version consistency for Bootstrap/Workbench, recorded hashes of their vendored runtime files, release dependencies and whether v2 importer/parser/editor are confirmed. Run `python 15_Testing/check_v2_import_kit.py . --json` on the full checkout. A real base build then requires `python '10_Base Vault/Tools/v0.8.0-r2/build-base.py' /path/to/empty/staging` followed by `python '10_Base Vault/Testing/check-release.py' --workbench 14_Workbench --base /path/to/empty/staging` (ensure output directory is a fresh staging base). The older checker still must be shown to function after path migration; no full checkout runtime validation was performed in this pass.

### Next safe action
- Keep v1 Workbench 0.1.18 pinned as the known legacy artifact. Build latest popup source separately as a **v2 candidate**, run `npm ci && npm test && npm run build`, inspect the output, then regenerate plugin lock from actual package hashes **after** Obsidian smoke testing.
- Promote Bootstrap 0.3.1 to active release manifest **only after** baseline compile, hash check, first-open activation/author registration pass. Do not simply edit the version number.
- Continue outstanding Pass 02 checkout-level base build and CI workflow path repair; they remain release-blocking regardless of this audit.
- Never modify the current source QEAX/BOM, active model vaults, or existing plugin-lock hashes just to produce a green status.

## Pass result
Audited: version/pin alignment and lock membership. Not tested: actual plugin hashes, full base construction, Obsidian first open, latest Workbench bundle, GitHub Actions. **Release NO-GO**. Next continuation requires user `y`.

## Pass 03 continuation — actual vendored binary hash evidence

On 2026-10-17 the six actual vendored files below were fetched from GitHub current main; SHA-256 was recomputed from their UTF-8 bytes and compared with the exact values in `.obsidian/plugin-lock.yaml`. **6/6 MATCH**:

| Plugin | main.js | manifest.json | styles.css |
|---|---|---|---|
| mdse-bootstrap 0.3.1 | PASS | PASS | PASS |
| mdse-workbench 0.1.18 | PASS | PASS | PASS |

Expected/actual hashes: Bootstrap main `16339af93abe34dc053ac2a8a60db7c081f7b07d584aa4b8d942fd9081eb0c62`, manifest `15586ffbfabee6a99d6b51777558ad2a36184eefa4b9ff782eb325350b61833a`, styles `dd7ba34452810f9d39ea03395fae66469decb386de83e6ab66d7a345e42ca645`. Workbench main `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`, manifest `6e2a74891743df424d80fe5cb551460ce4971852bf152909a2a5cecbbb218bd9`, styles `445abe199f3dbf00724dc3cffa13aed58fc087adc9396e79de18ebe6b274b008`.

**Interpretation:** the currently vendored binaries are internally consistent with the lock. The active release YAML still says Bootstrap 0.3.0, so alignment still fails; Workbench 0.1.18 binaries do not contain the recent uncompiled v2 popup. No third-party plugin data.json hash, Obsidian first-open test, nor npm source/build reproducibility test was performed. **Do not promote release yet.**

**Next user-gated pass:** run Bootstrap v0.3.1 TypeScript/tests/build and controlled first-open candidate smoke test, then address release manifest pin and regenerate lock only if artifact changes. Existing Pass 02 CI/build blockers remain independent.

## Pass 03 continuation — Bootstrap source-build readiness and first-open gate

Inspected `13_Bootstrap/Tools/v0.3.1/package.json`, `tsconfig.json`, `esbuild.config.mjs` and `13_Bootstrap/Testing/Base First-Open Test Sheet.md` in current main. Package version 0.3.1, build chain TypeScript `tsc --noEmit` + esbuild commonjs output `main.js` targeting ES2020 and treating `obsidian` as external; tests use `node --import tsx --test test/*.test.ts`. The package defines the necessary scripts, **but successful execution is not verified** because the complete source checkout/dependency installation is unavailable in this runtime.

An actionable test-sheet error was corrected: its row 15 instructed altering Dataview although Dataview is **not** in the locked ten-plugin list. In a *disposable vault* row 15 now tests drift of locked `mdse-bootstrap/styles.css`, requires backup and exact restoration. A warning at the top makes legacy v1 Port/Fileclass/Breadcrumbs checks distinct from SysML v2 note and menu acceptance. Commit `56978063f1d09934cf6c49b8dbdb2123ebfa8b46`.

### Next executable promotion gate (operator with checkout and Obsidian)
1. `cd 13_Bootstrap/Tools/v0.3.1 && npm ci && npm test && npm run build` — collect exit codes and output hash. Do not assume generated `main.js` identical to the already locked artifact until compared.
2. Confirm that `10_Base Vault/Runtime/Plugins/mdse-bootstrap/{main.js,manifest.json,styles.css}` still match lock; prior independent hash verification was 3/3 PASS.
3. Repair remaining Pass 02 CI and release path blockers, then generate an **empty disposable** controlled base, initialize its vault UID, and initialize its Git repository. Run the base release validator against this exact artifact.
4. Open in Obsidian at or above locked minimum; complete trust, safe activation, author registration, drift and restore scenarios on both macOS and Windows where practicable; capture actual results.
5. **Only after these gates** promote release YAML Bootstrap active version/source to 0.3.1 in the same controlled change as any necessary generated lock/payload updates. Avoid claiming native SysML v2 Workbench acceptance from v1 sheet.

**Status:** Pass 03 investigation progressed; hash lock 6/6 PASS (Bootstrap + legacy Workbench); source build and first-open acceptance **PENDING**. This is a clean handoff; no automatic version promotion.

## Pass 03 continuation — executable source-build gate (2026-10-17)

Verified on current GitHub main that Bootstrap 0.3.1 includes `package.json`, a lockfile, `src/main.ts`, `test/core.test.ts`, `tsconfig.json`, and `esbuild.config.mjs`. Local runner Node v22.16.0/npm 10.9.2 are present, but `git ls-remote` failed DNS resolution for github.com and no complete checkout or node_modules was available. **npm ci, npm test, npm run build were NOT executed.**

Added `15_Testing/check_bootstrap_candidate.py` (commit `a0413fe`) to perform the missing checks **from a complete checkout**: verify source input existence, SHA256 of locked Bootstrap runtime files, execute `npm ci`, `npm test`, `npm run build` in Bootstrap 0.3.1, hash the resulting `main.js`, compare to the locked bundle and report mismatch without changing release files. Run:
```sh
python3 -m pip install pyyaml
python3 15_Testing/check_bootstrap_candidate.py . --output /private/bootstrap-031-build.json
```
The checker fails closed on input, hash or test errors. Even if these pass, `BUILD_AND_TEST_PASS` is **not** an Obsidian first-open pass and does not authorize automatic promotion of the Bootstrap release declaration.

**Next:** Run the checker from a checkout with npm dependency access/cache, then verify first-open and update active pin only after runtime sign-off. Pass 02 workflow/base build remains pending. No model data or live vault changes.

## Continuation — Base Vault builder dependency/readiness inspection

On 2026-10-17 inspected the current `10_Base Vault/Tools/v0.8.0-r2/build-base.py` and `10_Base Vault/Definition/mdse-release.yaml`. Builder reads governed manifest via relative filesystem location, copies positive-include runtime files/trees, copies only locked plugin files, emits `.vault.yaml` with UNINITIALIZED UID, rejects nonempty target folders, and enforces forbidden-path exclusions. Source import remains external and must operate on fresh vault copies.

A concrete fix was committed: the builder's printed validation command incorrectly referenced old `Base Vault/Testing/check-release.py`; it now names `10_Base Vault/Testing/check-release.py` (commit `8300715`). This is a command correctness fix, not release promotion.

**Outstanding:** end-to-end builder run, full include-file existence audit, parser/native v2 compatibility, and first-open Bootstrap QA require a complete checkout. No generated base ZIP, npm build, or Obsidian acceptance was produced during this pass. Current release YAML remains Bootstrap 0.3.0 while lock/vendor use 0.3.1. Pass 02 CI workflow remains open. Continue in next user-approved bounded pass.

## Pass 03 continuation — critical Base Vault builder fix (2026-10-17)

Attempted to retrieve complete Test_Vault_ Git checkout from local runtime; `git ls-remote https://github.com/spencerskelly/Test_Vault_.git HEAD` failed with DNS resolution error. Therefore **no end-to-end base build can be claimed**.

Read the active `10_Base Vault/Tools/v0.8.0-r2/build-base.py` and identified a definitive failure: `MANIFEST=os.path.join(ROOT,"Base Vault","Definition","mdse-release.yaml")` still named an absent pre-consolidation folder, although the release YAML had been moved. Commit `2f84fb680df60fbe143d7e5c860596803dcaae32` fixes the path to `10_Base Vault/Definition/mdse-release.yaml`, updates usage documentation, and adds **fail-early input preflight before writing output** for required files/trees, plugin-lock schema and referenced locked runtime payloads.

This is a real source correction but **not execution evidence**. The new builder needs syntax/build tests on checkout; further latent path assumptions may remain. It preserves the old release version, all plugin hashes, and the non-overwrite destination policy. Critically, missing dependencies now produce visible BLOCKER messages instead of leaving an incomplete destination staging vault. Existing CI workflow migration and Bootstrap source build/Obsidian first-open remain open.

**Next gated increment:** run checkout-level Python syntax check, `python3 10_Base Vault/Tools/v0.8.0-r2/build-base.py /tmp/clean-mdse-base`, and `python3 10_Base Vault/Testing/check-release.py --base /tmp/clean-mdse-base`. Capture exact error codes and iterate only on verified blockers. Do not accept an incomplete output as a release artifact.
