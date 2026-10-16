# GitHub Consolidation — Step 9: Persisted Importer History on WB-129

**Recorded:** 2026-10-09
**Status:** **PASS — non-squashed importer branch history integrated on isolated remote staging branch after compatibility and component tests.**
**Release:** NOT APPROVED. No `main` branch changed, no repository retired, no importer PR closed.
**Previous:** [[GitHub Consolidation Step 08 Importer WB129 Acceptance 2026-10-09]]

## Frozen source and destination

- Destination repository: `spencerskelly/Test_Vault_`.
- Branch: `integration/importer-persisted-2026-10-09`.
- Starting integration baseline: `caafef60781b91712687e86bfdf1ddaebf3b78f0`, which holds Step 8's read-only source/schema compatibility and full real-QEAX test scripts.
- Staging CI workflow commit: `5c9898611aa00d521dce2e757acddddaafd5550d`.
- Original importer candidate: `importer/baseline-contract-2026-10-05` at **`0494354ec40378e119b17c61fdf6e828844035e4`** ([existing importer PR #5](https://github.com/spencerskelly/Test_Vault_/pull/5)).
- Original WB-129 Workbench source: `MDSE_Workbench/recovery/wb129-test-alignment-2026-10-08` at `8097f383c41617f879eac8e4ca19fab1d0cb7657`; ancestry carried by `55_Workbench/`.
- **Persisted merge commit:** [`dcfe3e45bd45f0a3619c18ae5841a357f526347b`](https://github.com/spencerskelly/Test_Vault_/commit/dcfe3e45bd45f0a3619c18ae5841a357f526347b).
- Git API independently confirms two parents: (1) `5c9898611aa00d521dce2e757acddddaafd5550d` (combined WB-129 staging) and (2) `0494354ec40378e119b17c61fdf6e828844035e4` (full importer source history). The merge was **non-squashed**. Thus both branch ancestries remain reachable.
- Review and disposition: [Test_Vault_ draft PR #12](https://github.com/spencerskelly/Test_Vault_/pull/12), based on `integration/importer-wb129-acceptance-2026-10-09`; do not merge to `main`.

## Passing gated staging job

[Actions run 37976183783](https://github.com/spencerskelly/Test_Vault_/actions/runs/37976183783) completed **SUCCESS**, including:

1. Verified staging branch and starting-commit ancestry, source WB-129 commit ancestry, and frozen importer branch head; refused unreviewed source drift.
2. Executed `git merge --no-ff` in the runner; independently checked exact first and second commit parents; did not squash or copy files.
3. Ran `66_Testing/check_importer_workbench_localmodel.py` on the actual merged tree: **PASS** for Workbench read versions 0.1–0.5, write 0.5 and importer schema 0.5.
4. Ran importer v0.8.19 source-profile validator, release-gate regression suite and IMP-009 headless acceptance selftest: **PASS**.
5. Built a fresh candidate Base Vault from the merged tree, verifying `local-model.yaml` schema 0.5: **PASS**.
6. Ran Workbench TypeScript typecheck, `npm test` (**448 passing, 0 failing**) and `npm run build`: **PASS**. No authored source/tests/package metadata changed.
7. Only **after** all above passed, pushed the merged commit to `integration/importer-persisted-2026-10-09` with a non-forced ref update. Both original `main` branches and original importer feature branch have been verified unchanged.

**Important CI nuance:** The GitHub Actions bot push does not necessarily trigger additional `push` workflows. The authoritative evidence is the successful pre-push validation of the *same* locally created merge commit plus the GitHub API's verified persisted merge-parent ancestry. Do not assert any unobserved post-push workflow passed.

## Full-model evidence linked, not conflated with release

The earlier [Step 8 real-QEAX acceptance run 37974532073](https://github.com/spencerskelly/Test_Vault_/actions/runs/37974532073) used the same pinned importer and WB-129 source commits with a noncommitted merge. It passed source checksum, **35,969 objects / 21,822 connectors**, deterministic full import (**28,273 files in each inventory, zero mismatches**), IMP-009/010/011 topology, 209 `Interface.equals` pairs, 23 `Connection.exposes` relationships, and Workbench Local Model 0.5 candidate acceptance (803 regions, 0 parse errors, no-op samples without drift, source unmodified). This is strong evidence for source compatibility, but not full deployment, interactive Obsidian UI, or release acceptance.

## Remaining blockers / next bounded work

- **Release checker / documentation registry:** older imported `mdse-release.yaml` still needs classification and registration of new current/reference workspace recovery notes. Do not suppress checks; reconcile stale `00_Workspace` narrative vs schema source.
- **Bootstrap pin/lock:** release manifest pins 0.3.0 while plugin lock lists 0.3.1; generate the correct managed lock only through approved process.
- **BOM A-14:** `MDSE_Workbench/proposal/bom-a14-readonly-quantity-uom` is separate and divergent, so no assumption that the Workbench 0.5 and BOM improvements are all integrated.
- **Obsidian UI:** manual definitionless-Interface edit/restart persistence test remains unverified on the new importer output. Current 0.5 headless suite passing is not this manual check.
- **Directory migration:** approved `11_Definitions`, `22_Importer`, `33_Base Vault`, `44_Bootstrap`, `55_Workbench`, `66_Testing`, `88_Resources`, `99_System`. Do not rename without a staged path/reference migration and functional CI gates.
- **Workstation-local work:** no remote connector can verify unknown local uncommitted/untracked/unpushed changes; old repositories/branches remain accessible.
- **Dependency maintenance:** GitHub runtime Node 20 deprecation warnings, 3 moderate vulnerabilities from an observed `npm ci` output; triage separately without unrelated unsafe bulk upgrades.

**Next recommended Step 10:** inspect full release checker and the candidate's docs registry, establish an atomic fix for document authority and remaining release-pin drift, and plan subsequent BOM integration or path migration by risk. **Do not promote a release until the remaining gates pass.**
