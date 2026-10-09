# GitHub Consolidation — Step 7: WB-129 Local Model 0.5 Source Integration

**Recorded:** 2026-10-09
**Status:** **PASS — history-preserving source staged and standalone regression tests passed.**
**Release approval:** NOT APPROVED; real-QEAX importer/Workbench combined acceptance and BOM reconciliation remain pending.
**Prior:** [[GitHub Consolidation Step 06 Importer Workbench Compatibility 2026-10-09]]

## Authoritative sources and exact commits

- Destination: `spencerskelly/Test_Vault_`, branch `integration/workbench-lm05-2026-10-09`; code under `55_Workbench/`.
- Original Workbench main preserved by Step 4B: `59fc6219b1d0586900aa7d38685e7087a9d47fec`.
- Source WB-129 recovery: `spencerskelly/MDSE_Workbench/recovery/wb129-test-alignment-2026-10-08` at `8097f383c41617f879eac8e4ca19fab1d0cb7657`.
- Imported source previously read/wrote Local Model 0.4; the WB-129 recovery brings Local Model 0.5 parser, mutation support, tests, source fixture and read-only real-vault acceptance script.
- Importer version 0.8.19 candidate (NOT merged into this branch): `spencerskelly/Test_Vault_/importer/baseline-contract-2026-10-05` at `0494354ec40378e119b17c61fdf6e828844035e4`, whose source schemas declare Local Model 0.5.
- Persisted Git subtree merge: [`5b761f14477afaba2177d157587c43f846aeee67`](https://github.com/spencerskelly/Test_Vault_/commit/5b761f14477afaba2177d157587c43f846aeee67).
- Git API independently confirms **two parents**, `2acb493a2a39beab155a2b104b0033c201c23c86` (combined integration staging) and `8097f383c41617f879eac8e4ca19fab1d0cb7657` (original WB-129 recovery history). Merge was **not squashed**; source commit history remains reachable.
- [Draft integration PR #10](https://github.com/spencerskelly/Test_Vault_/pull/10) targets the existing [WorkBench monorepo PR #8](https://github.com/spencerskelly/Test_Vault_/pull/8) feature branch, not main.

## Verified evidence

- [Read-only rehearsal run 37973237652](https://github.com/spencerskelly/Test_Vault_/actions/runs/37973237652): subtree pull without squash, no Git conflicts, TypeScript typecheck, full `npm test`, and production build all PASS. Test log **448 passing, 0 failing**.
- [Guarded persistence run 37973385600](https://github.com/spencerskelly/Test_Vault_/actions/runs/37973385600): original recovery SHA and frozen importer head verified; subtree pull preserved ancestry; compared actual Workbench source reader/writer to exact importer schema 0.5; typecheck/tests/build PASS (**448 passing, 0 failing**); source/test package diff check PASS. A non-forced push persisted *only* on the dedicated integration branch.
- Source `55_Workbench/src/core/localmodel.ts` at imported feature head now declares:
  - `READABLE_VERSIONS = ["0.1", "0.2", "0.3", "0.4", "0.5"]`;
  - `WRITABLE_VERSION = "0.5"`.
- The importer candidate at the pinned head declares `schemaVersion: "0.5"` and `writableVersion: "0.5"`.
- `55_Workbench/test/fixtures/local-model.yaml` is at schema 0.5; the source adds `scripts/real-vault-05-acceptance.ts` and the `accept:real-vault:05` npm command.
- The previous [Step 6 intentionally failing run 37972437540](https://github.com/spencerskelly/Test_Vault_/actions/runs/37972437540) used Workbench main/source 0.4 alongside the schema 0.5 importer. This Step 7 source patch fixes the identified **reader/writer declaration mismatch**. It **does not** by itself validate all real imported model topology or Obsidian UI behavior.

## Remaining blockers and explicit non-actions

1. **Importer integration:** v0.8.19 still resides only on importer PR #5. Run the fail-closed source/schema compatibility gate against the prospective true importer + WB-129 merged tree, and repeat importer regression/Base build. Do **not** merge the importer into protected main based only on identical version labels.
2. **Real QEAX + WB-129 acceptance:** exercise candidate's existing full real-QEAX workflow and `accept:real-vault:05` against identical frozen inputs. Workbench standalone tests do not replace this.
3. **BOM reconciliation:** `proposal/bom-a14-readonly-quantity-uom` has 32 commits above common Local Model 0.5 ancestry and diverges from the 23 additional WB-129 recovery commits. Preserve both; compare and resolve as a reviewed follow-on feature.
4. **Release checker / directory migration:** unresolved old paths, document registry, bootstrap 0.3.0 vs lock 0.3.1, unissued base. No directory moves or release promotion occurred in Step 7.
5. **Local workstation:** no proof of absence of uncommitted/untracked/unpushed modifications on user machines. Old Workbench repo and remote branches remain untouched until verification and complete disposition.

## Next bounded step — Step 8

Take the existing importer merge rehearsal from Step 6 and retarget its frozen baseline to the **new WB-129 staging source**. Run the same fail-closed `check_importer_workbench_localmodel.py` on the ephemeral combined candidate. Confirm the source/schema check becomes green **because the correct feature code exists**, then run importer regressions, Base build, Workbench tests and real-QEAX candidate acceptance as separate gates. Persist importer history and relocate roots only when compatible semantics and release blockers are dealt with.

**Do not equate a CI PASS on standalone Workbench with a unified MDSE release.**
