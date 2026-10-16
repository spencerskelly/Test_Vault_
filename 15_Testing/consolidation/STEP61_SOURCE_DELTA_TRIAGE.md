# Step 61 — Source tree delta triage (2026-10-14)

Status: **partial source comparison; no claim of full-tree equivalence.** No binary or model changes.

## Method and limitations

Compared original Workbench commit `b0c4e2c6bdfb96d36f51d8152b17be22592ef174` to PR #43 validation branch using GitHub compare. The API returned **300 files** (its result cap). The returned changes **do not constitute the complete source inventory**; later paths may be omitted. No full-tree Git tree enumeration was available in this pass.

Of the returned 300 files, 59 were under `55_Workbench/src/`. Most were classified as unchanged renames; two newly added source modules were visible:
- `55_Workbench/src/core/variantof.ts`, Git blob `60ae2e4e581a73ffc8116a816bdcbe31731b48de`
- `55_Workbench/src/core/variantof-format.ts`, Git blob `2c4dd163cb19f5a4be69a1e2b0865cc0c0d946a0`

Their headers describe read-only optional `variantOf` review/format checks. This is a source delta candidate, **not proof that it causes the artifact mismatch**. `main.ts` on candidate branch has blob `a85eee3be657830a253b3bd746ef0e75fec9b05b`; its original blob must still be compared.

Previously verified identical original/current blobs: `main.js`, `artifact-sha256.txt`, `package-lock.json`, `esbuild.config.mjs`. `package.json` differs by the `accept:real-vault:05` script.

## CI evidence

- Historical source from original commit rebuilt to governed SHA-256 `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7` in run 38604566786.
- Consolidated candidate fresh bundle hash previously observed `d2c4d90142718f3363196f0c5e7663cc9d87fc22655b62bfbc2887a69d2dec13`.
- These facts prove candidate build non-equivalence, not whether one or many source changes are involved.

## Step 62 action

Execute a **complete blob-ID inventory** in read-only GitHub Actions or isolated checkout:
`git ls-tree -r HEAD:src` at original commit and `git ls-tree -r HEAD:55_Workbench/src` at candidate commit (or equivalent Git `ls-tree -r` calls with path prefixes). Normalize prefixes; compare relative path and blob SHA for every source file, classify added/modified/deleted/identical, and record counts plus a bounded list of changes. Do not checkout historical model/QEAX archives or upload source files. Specifically inspect original versus consolidated `src/main.ts` and dependencies imported by the two new variantOf modules.

Then run a controlled disposable build with only isolated candidate delta reverted, confirming hash outcomes; do not modify tracked governed files or assume optional `variantOf` semantics can be dropped.
