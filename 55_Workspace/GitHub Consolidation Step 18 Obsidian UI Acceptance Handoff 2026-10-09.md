# GitHub Consolidation — Step 18: Obsidian Desktop Acceptance Kit Ready

**Recorded:** 2026-10-09 PDT (CI execution 2026-10-10 UTC)
**Status:** **PASS — reproducible two-vault acceptance package created and fixture/parser checked. MANUAL OBSIDIAN UI: NOT RUN.**
**Previous:** [[GitHub Consolidation Step 17 Post-BOM Real QEAX 2026-10-09]]
**Review:** [draft Test_Vault_ PR #18](https://github.com/spencerskelly/Test_Vault_/pull/18)
**Successful Actions:** [run 38013751270](https://github.com/spencerskelly/Test_Vault_/actions/runs/38013751270)

## Source and acceptance boundary

Step 18 branches from Step 17 source `12d36de03cdeb10fe88cc6cc8c15823abd90e3f5` and prepares **interactive manual acceptance only**, without changing the successful full-QEAX model importer, Workbench plugin source, governing schema, the release manifest, or any `main` branch.

The isolated branch `integration/obsidian-ui-acceptance-step18-2026-10-09` head is `602fc8e7a023cb102bf06dc0bf30bb092ada200f`.

Added:
1. `66_Testing/Step18_Obsidian_UI_Acceptance.md`: manual execution and evidence matrix (B01–B06, M01–M04, Q01–Q03, V01–V03, S01). Tests real Bootstrap first-open/author registration, controlled plugin release check, Workbench diagnostics and edit/restart behavior, candidate BOM quantity/UOM and variantOf errors, and **required source real-QEAX definitionless Interface UI edit**.
2. `66_Testing/build_step18_ui_kit.py`: generates **two separate, disposable** vaults from a controlled Base and a newly built candidate Workbench. It makes a standalone ZIP and an exact candidate-versus-controlled plugin hash provenance manifest. All artificial note IDs and 30-character UID tokens are fixture-only, never claimed to be from EA.
3. `.github/workflows/step18-obsidian-ui-kit.yml`: preflight release/authoritative source, TypeScript and Workbench 462-test suite, production build, vault generation, byte-lock preservation and **actual candidate Local Model parser** tests on the synthetic 0.5 definitionless Interface and 0.6 quantity/UOM Parts; publishes downloadable ZIP and release-check log.

## CI evidence and downloadable payload

[Final Actions run 38013751270](https://github.com/spencerskelly/Test_Vault_/actions/runs/38013751270) **completed SUCCESS**, head `602fc8e7a023cb102bf06dc0bf30bb092ada200f`; all jobs/steps successful:

- Workbench **462/462 tests passed, 0 failed** plus typecheck and candidate production build; original release checker **0 fail / 4 expected pre-release warnings**; plugin-lock generator `--check` passed.
- Controlled Workbench plugin main.js SHA-256: `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`, identical to original lock.
- Newly compiled experimental BOM Workbench main.js SHA-256: `d2c4d90142718f3363196f0c5e7663cc9d87fc22655b62bfbc2887a69d2dec13`; intentionally *different* from lock. The original lock is **unchanged** in both vaulted copies; the candidate is not misrepresented as a controlled plugin release.
- The generated **0.5** fixture includes a real contextual definitionless Interface occurrence (synthetic source), and the **0.6 reader-only** fixture includes Part `multiplicity: 2`, `quantity: 0.3500000001`, `unitOfMeasure: m`; the actual candidate parser reported them valid; **writer remains 0.5**.
- The candidate copy has clearly marked experimental oneWay `variantOf` relationships (test-only version **1.37**) for manual UI observation. The real governed schema in the controlled Base and canonical repository remains **relationships 1.36**.
- **Eight** synthetic fixture notes added only under `02_BOM_Candidate_Test_Only/88_Step18_Disposable_UI_Fixtures/`.
- ZIP source name: `step18-obsidian-ui-acceptance-kit.zip` (**SHA-256 `986113f1b69b59145a7ed87c0791b3d7262a52bb4d409832dc525e84c039000c`**). The enclosing GitHub Actions artifact (wrapper) is named **`step18-obsidian-ui-acceptance-kit`**, artifact ID **`11654467712`**, size **4,233,184 bytes**, wrapper digest **`sha256:9b13e7f9ca4e92b9b9d9e22b3d5e745d28ff3f7cf6b52a128aa0a11541cf33fd`**. The original inner ZIP checksum and the artifact-wrapper checksum differ by design.
- [Download from run's **Artifacts** section](https://github.com/spencerskelly/Test_Vault_/actions/runs/38013751270) (30-day retention). A separate `step18-controlled-preflight-log` artifact preserves the release checker warning output.

**Note:** The intermediate [run 38013601750](https://github.com/spencerskelly/Test_Vault_/actions/runs/38013601750) and [run 38013681225](https://github.com/spencerskelly/Test_Vault_/actions/runs/38013681225) failed on *new assertion harness wiring* (TSX CommonJS exports and double-escaped literal YAML regex), **not** source BOM compatibility or manual Obsidian behavior. The final check uses module-safe import and literal YAML line matching; it passed. These failures remain in Actions history; they were fixed rather than hidden.

## Manual work explicitly pending

No desktop Obsidian session, author-registration popup, actual plugin command, real-world file edit, restart or graphical Review/Canvas inspection was executed in Step 18. **Do not mark any B/M/Q/V/S acceptance row as PASS from CI output.** The kit contains **no actual source QEAX** and **no 28,273-file imported model**; M04 requires a separate, carefully assembled disposable copy of the frozen full-model output. Controlled Bootstrap first-open must record the known manifest 0.3.0 versus lock 0.3.1 warning; experimental candidate must record deliberate main.js digest/schema mismatch rather than changing lock or release pins.

**Recommended next bounded Step 19:** A human executes the controlled Base first-open rows (B01–B06) in a truly isolated local vault, then the candidate rows M01–M03/Q/V and finally the real-QEAX M04. Submit timestamped observed results/screenshots/logs; only after witnessed UI acceptance should release governance/Bootstrap candidate promotion be reviewed.

**No `main` branch, generated lock, controlled schema or original BOM source was changed. All PRs stay drafts.**
