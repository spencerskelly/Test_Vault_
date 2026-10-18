# Pass 02 — Consolidated path repair: partial implementation and handoff

Date: 2026-10-17. **Status: PARTIAL — two files updated; CI not updated or tested.**

## Changes on main
1. `10_Base Vault/Definition/mdse-release.yaml`: migrated historical unnumbered path prefixes to numbered checkout paths, including active base-builder, runtime-plugin copy/config/lock paths, importer candidate/profile paths and document registry locators. Kept all versions and source profile contents unchanged. Commit `b8ef11d6b45ffd503e18a16582734e3c9a3048b8`.
2. `10_Base Vault/Testing/check-release.py`: migrated legacy path prefixes used by the active release checker to the numbered layout. Commit `c253efe37fae8b97732fb54cf704dd4755693550`.
3. Both files were fetched after writing: no obvious double-numbering path prefixes. This is *not* successful execution of the base builder/release checker.

## Known blockers
- The attempted `.github/workflows/importer-candidate.yml` edit was rejected before writing. It remains unchanged and references legacy directories/commands.
- No local complete source checkout was available for full `build-base.py`, `check-release.py` or plugin hash tests. Some mapped files and document registry paths may still be invalid and require existence-by-path inspection.
- The original release still identifies Bootstrap 0.3.0 while its vendored manifest/lock use 0.3.1; do not promote in Pass 02.
- The native v2 importer/parser/editor remains a separate unreleased candidate and this change must not be described as passing import readiness.

## Pass 02 completion criteria remaining
- Review existence of every active `runtimeBase.includeFiles`, `includeTrees` and `mappedFiles.source` relative to the consolidated checkout.
- Inspect `10_Base Vault/Testing/check-release.py` for assumptions beyond simple path strings and run it.
- Repair importer candidate CI path triggers and commands using approved workflow tooling, if possible; verify a live run on current main.
- Build disposable base and execute current release validator; classify remaining failures without altering plugin pins.
- Record validation output and commit a Pass 02 completion addendum before beginning Pass 03.

Do not overwrite existing vaults or commit source model rows; this was infrastructure-only work.

## Pass 02 continuation after user `y` — 2026-10-17

Confirmed the previous GitHub path commits remain present. The active release manifest now identifies numbered paths for builder, importer candidate/profile, vendored plugin payload, plugin config and lock generators, and source mappings. Discovered one additional base construction discrepancy: `runtimeBase.includeTrees` still copied an absent old source `Definitions`; updated this to the consolidated `16_Definitions`. Updated forbidden `Cross-Vault/History` to `66_Cross-Vault/History`. Commit `77b621745b6e95b3b373e1ae54a09f4237db3a2d`. This alters the generated vault's definitions folder name, so importer placement and Obsidian navigation must be checked during the base-build acceptance test.

The current `.github/workflows/importer-candidate.yml` was fetched and **confirmed unchanged**; it still watches `Importer/**`, `Base Vault/**`, `00_Workspace/**` and invokes legacy paths. Previous attempt to write the protected workflow was blocked. No GitHub CI run or local base-build execution is claimed; this step used targeted GitHub file inspection. The base builder likely still fails on any other missing directory or manifest path until complete-checkout validation.

**Exit status: Pass 02 PARTIAL / infrastructure paths improved; CI + full checkout execution remain blockers.** Do not promote release labels or proceed as though runtime integration is verified. The next bounded pass should be a checkout-level base-build rehearsal plus CI path repair (where repository permissions allow), before formal Pass 03 plugin pin/hash reconciliation.
