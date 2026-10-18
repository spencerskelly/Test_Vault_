# Pass 6 — Fail-closed local Phase 8 publication

Date: 2026-10-17. The CLI now calls `reconcile_atomic`, which rejects an existing destination, writes detailed local-only CSV and aggregate summary in a newly created staging directory, and renames the completed directory into place only after reconciliation returns. On failure it removes the staging directory. A fresh target directory is mandatory; previous local ledgers cannot be silently overwritten.

Changes: `14_Workbench/registry/runtime/normalize_qeax_phase8.py` commit `1dfe0fa`; synthetic existing-destination and failure-cleanup tests `15_Testing/test_phase8_atomic_publication.py` commit `293a676`; GitHub Actions workflow includes them in commit `0c6ab90`.

## CI acceptance

No successful CI run has been observed or verified. Connected status APIs reported no statuses and only PR-triggered workflow lookups were exposed; no conclusion is inferred. The local container cannot clone GitHub by HTTPS DNS, so no exact checkout tests were run here. The new tests are **committed but their outcome is not yet verified**.

## Further boundaries

This change improves the CLI entrypoint only; direct calls to `reconcile()` still write to their provided working directory and must not be treated as atomic public output. Directory rename on one filesystem supports all-or-nothing visibility, but this does not establish power-loss durability. No native parser tests or imported model records. Native certified = 0; emission disabled.

Next: verify current workflow execution with run URL and logs, then harden the library API and pin the registry/source digest before production acceptance.
