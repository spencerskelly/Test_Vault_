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
