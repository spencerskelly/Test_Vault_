# Final Consolidation — Step 8 Workbench CI and Runtime Comparison

Date: 2026-10-14
Target staging branch: `integration/final-preservation-stage-20261014`

## Compared exact Git blobs
| Path | Historical SHA | Stage SHA | Finding |
|---|---|---|---|
| `66_Testing/consolidation/test_p03_legacy_compat.py` | `90b8a6d7f5cc598a42dec6a1f77b972cc0244b62` | same | Test already preserved |
| `.github/workflows/p03-legacy-compat-tests.yml` | `a415194bee11f76db721aae881e269e8290b59ca` | `4b7f853a14d2dd2a355d6986199ad25099435f69` | Branch trigger differences |
| `.github/workflows/p04-workbench-readonly.yml` | `dcd76567f25e2a93c1529c001e00c8fe122e9dba` | `104b3ab11e2990b02e618488ba6fc180de43c734` | CI difference, still requires full semantic review |
| `Base Vault/Runtime/Plugins/mdse-workbench/main.js` | `b01400ad4a48e23168dae09dc44e0d0e3587de31` | `f8a0b6cfa454437e68edaff7d5adf21965606a3c` | Changed runtime binary, do not replace without provenance |
| `Base Vault/Runtime/Plugins/mdse-workbench/manifest.json` | `ec4c18a259d902b3f36bb60f324261e44d42c5f4` | `a5852e592eafa027f52c2d052497293aec51a107` | Historical plugin v0.1.17 vs stage v0.1.18 |
| `.obsidian/plugin-lock.yaml` | `5194497334e90b72f22575f514337b2bbd218e4c` | `c430670577318457972a154012d08c6d28e6d11b` | Requires controlled runtime consistency gate |
| `Base Vault/Definition/mdse-release.yaml` | `9793b4becbc19d138753549c86c37f4eb2b0d7b2` | `6d06db25ed50ff390460c567b8fa769981aacc9e` | Historical release candidate differs |

## Exact qualitative findings
- Historical `wb106-release-integration` plugin manifest version: `0.1.17`; staging plugin manifest: `0.1.18`. Preserve current staging build; historical material remains accessible by branch, do not replace.
- P03 isolated test source is byte-identical. Historical P03 workflow targets `integration/lean-test-infrastructure-20261013` and PRs to `main`, while staging workflow targets `integration/p03-legacy-compat-tests-20261013` and PRs to Step22. Cutover needs deliberate trigger normalization so required tests run on reviewed PRs against the eventual stable branch.
- Exact staging commit `d052d3d331869a7f8057d9a3c4de508d00e6fc56` had no workflow runs returned as of previous check. Do not claim CI green for staging.
- No complete P04 behavioral diff, plugin-lock SHA256 validation, or new full-tree CI has yet been executed. These are next controls, not silent assumptions.

## Follow-up
1. Confirm staged release-manifest pin equals staged Workbench plugin manifest, lock and runtime binary provenance using existing release check tooling.
2. Prepare reviewed, deliberate CI trigger simplification for `main` and eventual `develop`; preserve required path scopes and fail-closed gates.
3. Run CI at exact candidate staging SHA; only then request explicit approval for base branch promotion.
4. Keep real-QEAX generated vault 0.2 mismatch on open engineering issue list; it is not yet release-ready.

No merge, main modification, release promotion or branch deletion authorized.
