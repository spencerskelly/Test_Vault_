# Branch Cleanup — Checkpoint BR-74: Base Builder Workbench Payload Chain

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Exact candidate commit: 58ab10870f11757cf1bf367ecd5868be9b60933d
Result: STATIC COPY-CHAIN AND RELEASE-CHECK ENFORCEMENT VERIFIED; EXECUTION PENDING.

## Source inspection

- `Base Vault/Tools/v0.8.0-r2/build-base.py` blob `67af4b69ea76a22b97db8851bd54ddc560b15784`.
- `Base Vault/Tools/v0.8.0-r2/build-plugin-config.py` blob `ae9db005992a0c03f638a0d68e38d9619044c795`.
- `Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py` blob `74f18af673263d87d123d31056251ddbab265d4b`.
- `Base Vault/Testing/check-release.py` blob `aae6d70357fbeea2c56aac7c3307604750dfdefe`.
- `.obsidian/plugin-lock.yaml` blob `c430670577318457972a154012d08c6d28e6d11b`.

## Verified source behavior

**Builder:** Reads runtimePlugins.lock from manifest, requires schema 2, enumerates locked plugin IDs and copies only main.js, manifest.json, styles.css and data.json from `Base Vault/Runtime/Plugins/<pluginId>/` into generated `.obsidian/plugins/<pluginId>/`. It refuses absent payload directories. It does **not** take runtime JS directly from `55_Workbench/main.js`; nor does this copy loop hash each file.

**Lock generator:** `update-plugin-lock.py --check` compares generated lock/config state to vendored runtime plugin files and hashes payload contents. The Workbench provenance entry is a declared source text, not evidence of reproducible rebuilding.

**Release checker without --base:** Runs the plugin-config and lock generator `--check` steps. For every plugin listed in lock, hashes files located in `Base Vault/Runtime/Plugins/<id>/` and fails any SHA-256 mismatch against per-file lock. Also checks pinned Workbench and Bootstrap versions against manifest and required WB-106 version.

**Release checker with --base:** Constructs exact expected generated-file inventory, disallows ungoverned extras, and hashes each generated `.obsidian/plugins/<id>/...` file against its authoritative vendored `Base Vault/Runtime/Plugins/<id>/...` counterpart. It compares non-plugin governed runtime files against workspace authority and checks Workbench/Bootstrap lock visibility in Base.

## What follows

- BR-73 established `55_Workbench/{main.js,manifest.json,styles.css}` directly match Workbench-specific lock hashes on frozen Step22.
- BR-74 establishes the *code path* that will validate vendored payload against lock and generated Base against vendored payload.
- Neither checkpoint actually executed `check-release.py --workbench 55_Workbench --base <freshBase>` on the frozen candidate, hashed the vendored payload independently, nor attested reproducible TypeScript->main.js build.
- Copy loop does not hash inputs by itself; never accept 'build success' alone as complete release approval. Execute checker with --base and verify 0 FAIL, record warnings explicitly, followed by independent GUI/operator release gates.

## Bounded next gate

BR-75: Byte-verify actual vendored Workbench runtime payload against locked reference on the exact frozen Step22 commit, then determine if a clean generated Base run can be executed in a disposable environment; do not alter lock or source.

No builder, runtime, source or repository state changed other than this audit checkpoint. No release, QEAX access, merge, PR close, branch delete, archive or destructive operation.
