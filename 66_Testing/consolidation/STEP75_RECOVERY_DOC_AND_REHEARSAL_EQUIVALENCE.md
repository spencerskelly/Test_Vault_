# Step 75 — Recovery documents and historical rehearsal control equivalence (2026-10-14)

## Recovery handoffs: all exact blobs preserved

Read-only GitHub file fetches at both `recovery/repository-consolidation-2026-10-09` and `consolidation/step22-single-repo-cutover-2026-10-11` confirmed **15 of 15** same-path recovery handoff markdown documents have identical Git blob SHA, covering Steps 04B and 05–18; **zero missing; zero mismatches**. Thus the earlier compare status `added` describes comparison history, not actual missing endpoint files. No duplicate copying needed.

| Step | Git blob |
|---|---|
| 04B | 7c3dc3a51495d5e9edbb2bd60f58f5de106ae2eb |
| 05 | 774d3959507a8684533f2717f16d244c5a4efcab |
| 06 | cf7d17034f2ed32b29e59bd5bd67bfeaa84cc626 |
| 07 | 531531f475c106efb5e1617edf8626bbf83f0847 |
| 08 | 2db622f6bfb6f5cb81fb627674d7553dc20fb68c |
| 09 | 268071d83c800577924bbe92056a9fb6d330904d |
| 10 | c18cc684ff41d4460fdee18d55361900988f24c4 |
| 11 | 854872ddf504e7252ca70d0d90bd0a52f78d68e3 |
| 12 | ed276a95778ca3f70da469870d98567b3eff0d21 |
| 13 | 63a401913fcfc10758f7a04550d993ac8decb0ee |
| 14 | 51cd4cdf6cb7f443ae4751f1d4ab233bb2a325ed |
| 15 | 85f6e0d0db3d90eb8744f90b71ff6641611224db |
| 16 | a73dc7707cbe03d1e554db16ea00f7bad661a09e |
| 17 | 566a380eb3bac153be31787f611e5764daa8eaaf |
| 18 | 81a4978e0ddbc01d5ac36a27a4dada499f05a632 |

## Historical CI control map (source-level, not full functional parity)

| Control | Original rehearsal | Consolidated current evidence | Disposition |
|---|---|---|---|
| Workbench npm install/typecheck/test/build | BOM and Workbench rehearsal | PR43 P04 workflow passing | Replaced for candidate source |
| Historical Workbench artifact reproduction | Older Workbench rehearsal used pinned Workbench source; not equivalent to current candidate hash | Step58 historical reproduction + P04 distinct candidate build and integrity | Stronger current separation; keep historical source metadata |
| Workbench original subtree tree/path migration | Workbench rehearsal checks pinned external SHA and original-tree migration | Step62 blob tree compares original and consolidated source; does NOT independently demonstrate complete original subtree import | Partially replaced; retain archival workflow |
| BOM A14 integration merge conflict rehearsal | BOM rehearsal fetch/ancestry/merge checks pinned source SHAs | Current P04/MDSE gates test consolidated state, NOT same BOM branch merge choreography | NOT equivalent; preserve historical workflow without reactivation |
| BOM quantity/unitOfMeasure semantic test | Historical BOM rehearsal invokes typecheck/build/tests | Step66–69 include 0.6 quantity and cache tests | Candidate semantic read coverage increased; BOM merge gate not superseded |
| Importer schema and source compatibility | Historical importer rehearsal invokes a checker | Checker identical at Step22 and PR43, but active CI execution not independently confirmed | Preserve until executed via approved workflow |

## Branch disposition

- Recovery: document contents for all 15 confirmed preserved; branch exclusive ancestry still exists and may require durable-history preservation before ref deletion.
- BOM and Workbench rehearsal: historical workflows not on Step22, are frozen to old SHAs and must be archived/inactivated with provenance rather than blindly merged. **Both branches remain HOLD.**
- No false claim of full CI-equivalence, merge readiness or branch retirement.

## Step 76

Check exact tip SHAs and identify durable historic preservation strategy for the three inactive rehearsal workflows and recovery-only ancestry. Prepare a proposed non-executable archive manifest and reviewer decision gate. Do not delete/merge without approval.
