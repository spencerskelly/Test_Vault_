# Proposed superseding W decision — unified Workbench source authority

**Status:** PROPOSAL ONLY — no W identifier assigned, not approved, not a new release authority.  
**Candidate prepared:** 2026-10-10.  
**Source:** Step 08 real-tree audit at `256330788ba03a17596112ecd5f9a9b406359cfa`; draft cutover branch `consolidation/step09-authority-ci-rehearsal-2026-10-10`.

## Proposal for review

`spencerskelly/Test_Vault_` becomes the sole continuing MDSE tool-development repository, with Workbench implementation and product definitions at `55_Workbench/`. The standalone `spencerskelly/MDSE_Workbench` repository remains publicly accessible and unarchived until a **separately approved, read-only archival** after source, security, CI, release and Obsidian acceptance.

This decision would supersede the **source repository owner/location** clauses of W-328 and W-329, and harmonize documentation whose earlier source authority derives from those decisions. It does **not** retrospectively rewrite the original W entries, diminish Workbench ownership of its product behavior, or transfer shared semantic authority out of `99_System/`.

## Out of scope and explicitly retained

- Release status stays `pre-release`, target release `0.8.0`, Workbench pinned `0.1.18`, schema versions relationships `1.36`, elementTypes `1.18`, localModel `0.5`; no 0.6 writer activation.
- Base Vault controls the actual runtime plugin payload and lock; `.obsidian/plugin-lock.yaml` and its active generator remain byte-identical. The old Workbench source label identifies the original **pinned artifact provenance**, and is **not** an instruction to fetch the standalone branch during daily development.
- The 8 historic root CI workflows, original release artifacts, the complete 19-branch Workbench lineage and other prior GitHub handoffs remain reference evidence; do not rebaseline frozen acceptance to new code and claim it is the same acceptance.
- Open security hold: the `EA_2026_09_06_endgame.qeax.zip` file is exposed on public staging history but has **not** been owner-classified or cleared for public distribution. No data-copy/merge/history-rewrite is approved.
- Actual contributor local clones, stash/unpushed work and Windows PowerShell audit signoffs remain outstanding.
- A-15 BOM writer candidates are not yet active Workbench source and `variantOf` is not an approved live schema relation.

## Proposed ratification checklist

1. Approve exact text and assign next valid W decision ID *in the normal governance process*. Do not fabricate an ID or override historical W-328/W-329.
2. Resolve QEAX owner/security classification and exposure handling, contributor clone checks, release/version/lock validation and true Obsidian GUI first-open/edit/restart acceptance.
3. Confirm root workflows build and typecheck all `55_Workbench/` source with read-only permissions; compare generated artifact/checksums to approved controlled runtime.
4. Apply the reviewed cutover patch through its normal PR approval path, with no direct public `main` push. Record current repo head SHAs, CI run IDs and the exact PR commit.
5. Only after controlled promotion consider marking `MDSE_Workbench` archived read-only; retain its full Git history and existing refs.

**Do not copy this proposed text into `00_Workspace/Workspace Decision Log.md` as an approved decision until the governance review actually occurs.**
