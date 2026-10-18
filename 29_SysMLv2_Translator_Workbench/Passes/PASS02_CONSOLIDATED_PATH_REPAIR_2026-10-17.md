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
