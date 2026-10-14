# Step 81 — Historical PR supersession and retained-control matrix (2026-10-14)

Status: **source-level evaluation; no approval or PR changes**. Historic PR #7, #8, #9 still open.

| Original PR/control | Consolidated evidence | Coverage decision | Required closeout |
|---|---|---|---|
| **#7** ephemeral Git subtree import; pinned Workbench source and history parents | Step62 compares 57 original and 59 consolidated tracked `src/` paths and exact blob IDs; historical Step58 rebuilds original; P04 builds/tests candidate | **PARTIAL**: no fresh complete subtree parent-ancestry/every-original-tracked-file proof | Preserve PR #7 run 37970033542 and archived exact rehearsal workflow; independently verify source ancestry via Git parents and complete tree comparison before closure |
| **#7** original Workbench npm install/typecheck/test/build | P04 builds and tests candidate; Step58 independently builds old source | **COVERED for build**, not for historical migration ancestry | Retain two separate build identities |
| **#8** staged full Workbench history under `55_Workbench/` | Frozen Step22 includes Workbench subtree; source blob comparison, historical rebuild pass | **PARTIAL**: complete staged Git ancestry/whole-tree object proof not repeated | Verify original parent commits reachable and archive PR #8 run 37970531725 + cutover evidence |
| **#8** root-integrated Workbench CI | P04 and MDSE read-only integration gates pass | **COVERED for candidate CI**, subject to review | Keep source-only CI and release/GUI separation |
| **#9** ephemeral no-conflict importer merge pinned at original SHAs | `66_Testing/check_importer_workbench_localmodel.py` identical in Step22 and PR43; no current CI-equivalent no-commit importer merge proven | **NOT COVERED** for merge choreography | Preserve archived source; replace with source-only isolated merge test if needed before next importer merge |
| **#9** fail-closed importer manifest, schema and Workbench parser/writer compatibility | Exact checker present but not established as executed by active passing workflow | **NOT VERIFIED as a gate** | Add checker to reviewed consolidated CI after checking schema path availability; test both pass and fail modes |
| **#9** importer headless, source-profile, Base/release diagnostic and Workbench regression | P04 covers Workbench, MDSE integration status alone does not establish exact importer tests | **PARTIAL** | Map exact importer commands to active CI or preserve as explicitly deferred acceptance before PR closure |

## Preserve-before-close criteria

- Historic evidence refs: PR #7, #8, #9 and linked CI run URLs, frozen branch tip SHAs from Step80.
- Archived historical workflows (three exact SHA matching non-executable copies from Step77).
- Original Workbench full subtree ancestry and exact imported tree proof separate from later `src/` feature changes.
- Explicit approval to retire a PR; avoid closing by inference from green CI or matching source blobs.
- Real-QEAX, macOS/Windows Obsidian UI, and new candidate artifact-release gates remain outstanding.

## Next Step 82

Inspect the currently passing **MDSE consolidated integration** workflow for exact importer checker coverage (locate workflow by run/job metadata), then decide whether to add a blocking, source-only compatibility job. Do not re-enable historical merge rehearsals.
