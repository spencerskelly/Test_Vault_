# Branch cleanup — checkpoint BR-09: Workbench monorepo rehearsal divergence and validation parity

Date: 2026-10-12
Status: PASS — net branch effect classified and critical validator parity verified; individual commit-level audit remains open
Candidate: `consolidation/step22-single-repo-cutover-2026-10-11`
Diverged branch: `integration/workbench-monorepo-rehearsal-2026-10-09`

## Live branch comparison
GitHub compare base=Step22, head=Workbench monorepo rehearsal returned `diverged`, `ahead_by=1` (rehearsal-only), `behind_by=1806` (Step22-only). Net tree difference:
- Added on rehearsal branch: `.github/workflows/workbench-monorepo-rehearsal.yml`, 94 changed lines, blob `253722a1273e9d0f30255e25299c7ec56c18684b`.

File was fetched and inspected. It is a branch-scoped read-only CI experiment, pinned to old standalone `spencerskelly/MDSE_Workbench` source SHA `59fc6219b1d0586900aa7d38685e7087a9d47fec`, that rehearsed subtree import under `55_Workbench` and ran npm typecheck/test/build. It never pushes, opens a PR or modifies main.

Disposition: **HISTORICAL REHEARSAL — do not reactivate on the consolidated branch**. Retain historical provenance until PR, remote refs and contributor-local work signoff.

## BR-08 validator parity resolved

Fetched exact file `66_Testing/check_importer_workbench_localmodel.py` from Step22 and compared blob SHA with the previously fetched diverged importer branch file. Both have Git blob SHA:

`95c29b377ad8c7a0596e1c164db2e6bb66168b52`.

Therefore this fail-closed Local Model reader/writer compatibility validator is **already exactly present** on Step22. BR-08's open action to port/recover the file is closed by content parity (though real runtime tests on final promoted tree remain required).

Also fetched Step22 `66_Testing/check_release_alignment.py` (blob `ca0a9278254a2aaf997a858206cb5d10b1bd01e2`). Its documented role is read-only preflight of monorepo migration roots, plugin/release pins and dependencies. Fetching it establishes presence, not execution success or proof of full equivalence to historical workflows.

## Overall integration status
- Nine of 12 integration branches have ancestor tips included in Step22.
- Three diverged: BOM A14 reconciliation (2 branch-exclusive commits, historical external Workbench merge rehearsal net added), importer reconciliation (6 branch-exclusive commits, two net files of which Local Model validator is byte-identical to Step22), and Workbench monorepo rehearsal (1 branch-exclusive commit, historical external subtree CI).
- All three branch-tip net changes are now characterized. **Do not claim every individual exclusive commit has been separately inspected**.
- No need to bulk-merge any of the three branches. Before branch deletion, verify individual commit ancestry/diffs as needed, PR disposition and contributor-local work preservation.

## Handoff
STEP: BR-09
STATUS: PASS — Workbench rehearsal net effect and validator byte parity
SOURCE: GitHub compare; file fetches on rehearsal and Step22 heads
OUTPUT: this checkpoint on PR #41
CHECK: diverged ahead=1 behind=1806; one net added workflow; identical validator SHA `95c29b...`
NEXT: BR-10 — inspect remaining 9 non-main/non-consolidation/non-integration branches, in bounded groups. Follow with PR cleanup and branch promotion gate.
BLOCKERS: permissions/approvals, branch-exclusive commit enumeration, unpushed local work, QEAX data security, document-control and GUI acceptance.
