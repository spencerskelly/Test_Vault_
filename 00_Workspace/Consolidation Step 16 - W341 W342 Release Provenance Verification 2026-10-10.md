# Consolidation Step 16 — W-341 user-guide parity and W-342 Workbench release provenance

**Status:** staging candidate verification, no release, no owner authorization, and **NO changes to any runtime pins/lock/source guide/W decision**.  
**Review parent:** Step 15 `8d527fee6733cf586ef23318770729c7512b59a0`; proposed branch `consolidation/step16-w341-w342-release-provenance-2026-10-10`.

## W-341 — guide correspondence: verified same source bytes at baseline

Two copies retrieved from the exact Step 15 consolidated staging tree have the **same Git blob**, `2a82d21f89a2e80e4df227760f85f1215cd76ec5`:

| Source purpose | Path | Git blob |
| --- | --- | --- |
| Workbench development guide | `55_Workbench/docs/User Guide/MDSE Workbench User Guide.md` | `2a82d21f89a2e80e4df227760f85f1215cd76ec5` |
| Base Vault release-managed copy | `Base Vault/Definition/MDSE Workbench User Guide.md` | `2a82d21f89a2e80e4df227760f85f1215cd76ec5` |

The release manifest's `tools.workbench.userGuide` selects that Base copy. Its `runtimeBase.mappedFiles` maps this file to `99_System/01_Admin/MDSE Workbench User Guide.md` in a generated base. This is confirmed **configuration and source-copy correspondence**. It does **not** prove an actual generated vault contained the right guide, nor real Obsidian acceptance.

`Base Vault/Testing/check-release.py --workbench 55_Workbench` includes the original W-341 comparison with normalized newlines/trailing whitespace; Step 16 additionally tests byte equality and fails if a single byte changes. The guide itself remains unchanged.

## W-342 — separate development candidate from pinned runtime

**Current checked manifest:**

| Source | Value |
| --- | --- |
| `mdseRelease` / status | `0.8.0` / `pre-release` |
| Workbench release `version` | `0.1.18` |
| Workbench `candidateVersion` | `null` (no independent unapproved candidate) |
| Workbench `wb106Version` | `0.1.18` |
| Workbench `package.json` and `manifest.json` | `0.1.18` / `0.1.18` |
| `.obsidian/plugin-lock.yaml` `mdse-workbench.version` | `0.1.18` |
| Local Model schema pin | `0.5` (no `0.6` writer) |

The original historical **W-342** describes an earlier, intentional Workbench `0.1.17` candidate while the base was pinned to `0.1.16`. That is a dated accepted design pattern, **not the current pin state**. The existing release checker allows a pre-release Workbench candidate only when explicitly declared and package/manifest agree, and rejects a mismatch on an issued release. Step 16 covers both positive baseline and tampered negative cases.

The generated plugin-lock source string still cites the original standalone Workbench artifact (Git provenance); **do not rewrite** it as an active authority URL or regenerate artifacts during this verification. Locked source SHA: `c430670577318457972a154012d08c6d28e6d11b`. The original W Decision Log Git blob is `49ab9bc513b27ce7e1c2beed6e039aad5c0bebbb`.

## Verification actions

1. Run `python3 -m unittest discover -s 66_Testing/consolidation -p 'test_step16_release_provenance.py' -v`. The tests cover exact guide-copy bytes, manifest mapping, controlled runtime version agreement, pre-release candidate compatibility, issued-release negative cases, native checker coverage and unchanged original W records.
2. Run the **existing** `python3 'Base Vault/Testing/check-release.py' --workbench '55_Workbench'` in a read-only sparse checkout. The native script returns code `1` on any FAIL, but may report justified pre-release WARN; do not conflate warnings with issued-release acceptance.
3. Retain Step 15 governance tests and signoff blocks. CI checks are restricted to a disposable runner; the public QEAX ZIP is excluded from its checkout and no file/model contents or full audit report are uploaded as GitHub Actions artifacts.
4. Record actual native release-checker exit/result before calling the candidate verified. Do not claim generated Base Vault/Obsidian GUI verification from source-file checks.

## Further required gates

- W-341 **generated engineering Base Vault** guide-copy check, plus real first-open/read/edit/restart in Obsidian on Mac and Windows; source guide parity alone is not this acceptance.
- W-342 artifact hash comparison, Bootstrap release candidate vs pinned source and full importer/Workbench/Bootstrap integration on the exact future promotion commit.
- Proposed W source-authority decision still unassigned and unapproved; Step 15 governance register has 12 `NOT_APPROVED` gates.
- QEAX public-history source-data owner/security classification and contributor workstation unpushed/stash/worktree signoffs.
- No protected public-main merge or standalone read-only archive until those independent gates are explicitly satisfied.

**Next bounded step:** verify a disposable generated Base Vault has exactly the mapped Workbench guide and pinned plugin payload, then prepare a real Obsidian GUI acceptance protocol without declaring it completed.
