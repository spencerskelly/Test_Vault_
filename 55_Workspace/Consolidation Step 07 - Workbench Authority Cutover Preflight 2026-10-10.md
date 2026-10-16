# Consolidation Step 07 — Repository authority cutover preflight and negative test candidate

**Date:** 2026-10-10  
**Status:** isolated candidate prepared; **NOT activated or merged into `main`**.  
**Parent:** `090266d642e39584c2ebd9fc87e7d74d9b07cefb`, `consolidation/step06-local-clone-hardening-2026-10-10`.  
**Output:** 66_Testing/consolidation/audit_workbench_authority.cjs, 66_Testing/consolidation/test_workbench_authority.cjs, 66_Testing/consolidation/STEP07_CONTROLLED_CUTOVER_PREVIEW.md.

## Completed

1. Added a self-contained, read-only Node checker using `git grep -I -l -z -F` on the local tracked working tree. It reports path classes instead of file/model contents.
2. **33/33 isolated tests PASS**, executed using Node's built-in test runner with disposable Git repositories; `node --check` passed for both candidate JS files.
3. Candidate distinguishes `blocking` (active current ownership documents, release manifest, root workflows, executables), `historical` (explicit archived paths and named older consolidation handoffs), `detector` (three explicit self-reference sources), and `needs_review` (unclassified documents). Strict readiness requires zero blocking **and** zero review-needed matches.
4. Negative tests prove root workflow reference fails; unknown model guidance fails closed; archived references alone are informational; exact Git-tracked references are found; untracked files are outside scope.
5. Both committed JS blob hashes were independently matched against the source files tested in the isolated runtime. Reported Git blob SHA: checker `9d21fc35c9cdd008669f9ca4ab38cd73b18f2915`, tests `143b0aa3564fcd0710383dcd7aa515376e8e350e`.
6. Prepared a source-specific seven-part cutover preview, **not** an actual change to the release manifest, CI workflows, existing preflight or Workbench.

## Evidence and limitations

- Local isolated `node --test test_workbench_authority.cjs`: **33 passed / 0 failed**. Real `Test_Vault_` full-checkout scan and root CI **not run**; the current pre-cutover source intentionally has active old repository references, so strict readiness must be expected to fail.
- The script uses the user's installed Node + Git but does not fetch, reset, push, modify the model, or download QEAX data. With `--output`, it writes only its requested JSON report.
- This checker is **candidate-only**. The existing `66_Testing/check_release_alignment.py` remains the active release diagnostic.
- The `detector` class explicitly excludes only the old preflight and this candidate scanner/test from strict blocking; that is a narrow self-referential exception, not a blanket bypass. An unexpected current document is instead flagged for review.
- No real workstation audit results or approval to publicly distribute the 73.2 MB QEAX archive exist in this checkpoint.
- A-15.1–A-15.4 BOM writer work remains isolated, not promoted/committed as production features. No Local Model 0.6 writer or `variantOf` schema was approved.

## Hard stop conditions

**Do not archive standalone `MDSE_Workbench` or promote `Test_Vault_` to public `main`** until: QEAX owner/security classification and any needed public-history response; workstation clone/branch sign-offs; reviewed authority/CI cutover; full integrated build/tests; controlled runtime version/pin/lock acceptance; and real Obsidian GUI acceptance.

## Next bounded step

Step 08 should run the candidate reference audit against an actual checked-out integrated staging tree in a controlled CI environment (without including restricted QEAX bytes in test artifacts), then draft a line-level authority/CI cutover PR with explicit approval and rollback plan. Keep existing release and standalone repository untouched until the blocking gates are resolved.
