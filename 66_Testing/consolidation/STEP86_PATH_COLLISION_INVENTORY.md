# Step 86 — Four-ref path collision inventory (2026-10-14)

Status: **read-only audited sample and exact high-impact path matrix; not exhaustive whole-tree comparison**. GitHub compare against main returns only the first 300 changed files for Step22 and PR43; therefore this pass **cannot certify no other collisions**.

## Compare metadata
- main → Step22: ahead 1809, behind 1; first 300 files: 290 added, 10 modified.
- main → PR42: ahead 8, behind 1; **all 4 changed files** enumerated (all added).
- main → PR43: ahead 1896, behind 1; first 300 files: 290 added, 10 modified.
- Important: all three branches are behind current main by one commit; refresh/merge-base review before any integration attempt.

## Four-ref exact blob classification

| Path | main | Step22 | PR42 | PR43 | Decision |
|---|---|---|---|---|---|
| `.github/workflows/p03-legacy-compat-tests.yml` | absent | absent | `a415194b` | `4b7f853a` | **Same-path content collision**: curate tested triggers and source scope |
| `.github/workflows/p04-workbench-readonly.yml` | absent | absent | `dcd76567` | `104b3ab1` | **Same-path content collision**: PR43 contains governed/candidate separation; merge by review |
| `66_Testing/consolidation/p04_full_workbench_tree.py` | absent | absent | `0ea4153a` | `0ea4153a` | Identical addition; one copy only |
| `66_Testing/consolidation/test_p03_legacy_compat.py` | absent | absent | `90b8a6d7` | `90b8a6d7` | Identical addition; one copy only |
| `Base Vault/Definition/mdse-release.yaml` | `a1692487` | `6d06db25` | `a1692487` | `6d06db25` | Governed 0.2 → 0.5 authority migration, not blind overwrite |
| `99_System/03_Schemas/local-model.yaml` | `04b8592d` | `361dee82` | `04b8592d` | `361dee82` | Governed Local Model 0.2 → 0.5 |
| `.obsidian/plugin-lock.yaml` | `2039b5dd` | `c4306705` | `2039b5dd` | `c4306705` | Governed plugin lock change requires matching release contract |

Abbreviated blob prefixes uniquely describe observed identities in this matrix; Step85 lists full schema/manifest SHA evidence.

## Integration classes

1. **Identical additions**: two PR42 test scripts also exist byte-identically on PR43. Avoid duplicate paths, keep provenance.
2. **Same-path divergent additions**: P03 and P04 workflow YAML exists on PR42 and PR43 with different blob IDs. Do not apply both via blind tree merge, and do not assume automatic conflict detection will protect semantics.
3. **Governed contract replacements**: release manifest, 0.5 canonical Local Model and plugin lock match Step22/PR43, not current main/PR42. Advance atomically with Workbench source and importer checker.
4. **Additional changes**: Step22/PR43 have >300 changed files and GitHub compare truncation. A comprehensive Git-tree path/hash inventory is required before authorizing integration.

## Next Step87

Run complete Git tree inventory of all four refs (e.g. read-only checkout with `git ls-tree -r -z`) and classify every path as main-only, Step22-only, PR42-only, PR43-only, identical across suppliers or conflicting. Produce machine-readable and bounded human summary. No model archive content checkout required for Git object metadata.

No merge, main edit, PR change, tag, release promotion, historical artifact rewrite or branch deletion occurred in Step86.
