# Consolidation Step 19 — Disposable generated Base Vault and Obsidian GUI acceptance handoff

**Prepared:** 2026-10-11. **Status:** build/packaging candidate only, not an issued MDSE 0.8.0 release and not a completed Obsidian GUI acceptance.
**Parent candidate:** Step 18 `cf47ab37fe549312669ad76095a2b229a2ee6b0e`. **No public-main merge or standalone Workbench archive permitted.**

## Build and independent verification (CI)

From repository root, on a **disposable** branch runner checkout excluding the known public QEAX ZIP:

```sh
python3 -m pip install 'PyYAML==6.0.2'
mkdir -p "$RUNNER_TEMP/step19-base"
python3 'Base Vault/Tools/v0.8.0-r2/build-base.py' "$RUNNER_TEMP/step19-base"
python3 'Base Vault/Testing/check-release.py' --workbench 55_Workbench --base "$RUNNER_TEMP/step19-base"
python3 66_Testing/consolidation/step19_generated_base.py --base "$RUNNER_TEMP/step19-base"
STEP19_BASE_DIR="$RUNNER_TEMP/step19-base" python3 -m unittest discover -s 66_Testing/consolidation -p 'test_step19_generated_base.py' -v
```

The existing builder creates an uninitialized lean base: `.vault.yaml` has UID `UNINITIALIZED`; no Git metadata or author registration is created. The build includes governed schemas/templates/rules, locked plugins and mapped admin guides, and should exclude the workspace and importer implementation.

**Independent verification scope:**

- Confirm `55_Workbench/docs/User Guide/MDSE Workbench User Guide.md` and `Base Vault/Definition/MDSE Workbench User Guide.md` are byte-identical to the **actual generated** `99_System/01_Admin/MDSE Workbench User Guide.md`.
- Confirm generated `.obsidian/plugin-lock.yaml` matches source byte-for-byte and the **ten locked plugins** are present. Compare each generated `main.js`, `manifest.json`, `styles.css` or governed `data.json` against both its source runtime payload and the release-lock SHA-256.
- Check actual plugin `manifest.json` version against its individual locked version (particularly Workbench `0.1.18`), the enabled plugin order, schema `1.36/1.18/0.5`, source manifest SHA, and generated vault uninitialized identity.
- Verify no workspace-only, importer, Workbench development, `Base Vault/` methodology, Git, or QEAX archive files appear in the generated product.
- Run the original `check-release.py --base` on the **same output directory**, not on a guessed or previously generated folder. All native FAIL are blockers; pre-release WARN are recorded separately.
- Negative regression tests mutate the **temporary generated** guide or Workbench JavaScript, verify detection, restore original bytes in `finally`, and rerun the independent inspector. They do not mutate the release payload, locked source files, or Git contents.

**Artifact handling:** CI must not upload the generated vault, binary plugins, source archive, proprietary model, private workstation logs, or user identity information. It emits counts and checksum evidence only. The disposable build should be automatically deleted with its GitHub-hosted runner.

## Human Obsidian GUI acceptance record — NOT EXECUTED

This procedure is an approval **handoff**, not automatic acceptance. Do not claim a successful UI launch, macOS or Windows compatibility without an operator running it. Execute on a fresh copy of the accepted generated base **after** release owner and QEAX-security review; never open the protected historical QEAX artifact to perform UI smoke tests.

| ID | GUI scenario | Explicit operator check | Actual / evidence | Result |
| --- | --- | --- | --- | --- |
| G19-01 | Prepare disposable vault | Record exact tested Git commit, base build evidence, plugin lock SHA, Obsidian application version, host OS and test vault path in a private acceptance record | **Pending** | NOT RUN |
| G19-02 | Release-owner identity initialization | On a separate copy, run `Initialize-Vault.sh` on macOS or `Initialize-Vault.ps1` on Windows; verify valid 13-character author code and stable UID; preserve source uninitialized artifact | **Pending** | NOT RUN |
| G19-03 | First opening | Open initialized folder as an Obsidian vault; inspect the Restricted Mode trust prompt and choose to enable the controlled plugins only on this trusted test copy | **Pending** | NOT RUN |
| G19-04 | Bootstrap and lock check | Verify plugin stack loads, Bootstrap release check identifies pinned plugins, and no arbitrary plugin updates or rewrite prompts are required | **Pending** | NOT RUN |
| G19-05 | Workbench basic readiness | Confirm Workbench reaches usable READY state/status and core commands appear. Record defects, startup warnings and console messages without private model data | **Pending** | NOT RUN |
| G19-06 | W-341 guide navigation | Open `99_System/01_Admin/MDSE Workbench User Guide.md` within Obsidian and confirm readable content and matching title | **Pending** | NOT RUN |
| G19-07 | Schemas/templates | Navigate governed schema notes, generated templates and definitions; verify no broken paths or missing plugin requirements | **Pending** | NOT RUN |
| G19-08 | Author registration and new element | Complete one safe test author registration and create a scratch engineering note with a governed template. Verify YAML/type/UID conventions using a disposable test note | **Pending** | NOT RUN |
| G19-09 | Read/edit persistence | Edit the scratch note's allowed property, save it, close/reopen and verify persistence. Check Workbench index/health rather than assuming 'READY' proves full semantic hydration | **Pending** | NOT RUN |
| G19-10 | Workbench navigation | Test where-used, structure and interface views on a **separately approved synthetic fixture**. An empty clean base alone cannot validate imported-model relationships | **Pending** | NOT RUN |
| G19-11 | Restart and recovery | Close/reopen Obsidian, verify Bootstrap and Workbench startup/reindex, retained authored data, no extra per-machine state committed to Git | **Pending** | NOT RUN |
| G19-12 | Cross-platform repeat | Repeat the applicable tests independently on macOS and Windows, document OS version, Obsidian version and any deviations | **Pending** | NOT RUN |

**Acceptance rule:** No row may be changed to PASS without the actual result, tested commit, applicable acceptance evidence and reviewer; partial completion, platform mismatch or missing synthetic model fixture remains OPEN. Store private paths, personal identifiers or screenshots containing model data outside the public repository.

## Nontechnical gates still mandatory

- Review-only document registry classifications are not ratified; Step 15 holds twelve governance gates as NOT APPROVED.
- Source-data owner/security must classify the existing publicly reachable QEAX ZIP and approve the appropriate response.
- Contributors must sign off local-only branches, unpushed/stashed work and workstation clones.
- Final importer/Base/Workbench/Bootstrap end-to-end validation and generated-base GUI acceptance must be re-run against the **exact eventual promotion commit**.
- Only after these requirements and protected PR review may main be promoted. Standalone repository read-only archival requires an independent explicit authorization.

**Next bounded step:** record verified generated-base build counts and tool output; prepare human GUI acceptance bundle using only synthetic model data, leaving all G19 UI results pending until an actual operator completes them.

## Verified Step 19 CI result (GitHub-hosted disposable runner)

**GitHub Actions:** [run 38183598705](https://github.com/spencerskelly/Test_Vault_/actions/runs/38183598705), completed successfully on source commit `fa0c9d693f663d020fcc24d4d47f01925c1547e4`.

| Actual automated check | Observed result |
| --- | --- |
| Controlled r2 base builder | SUCCESS; uninitialized MDSE 0.8.0 lean runtime base produced |
| Original native release checker with `--base` and `--workbench` | **0 fail, 4 warn** (pre-release) |
| Generated W-341 Workbench user guide | **Byte-identical** to development and controlled Base Vault guides |
| Generated guide SHA-256 | `01120e6ba09fba38ab6cee943cb95f7a2f40eac1904be90b2af252c52e55598f` |
| Generated `.obsidian/plugin-lock.yaml` | Byte-identical to controlled source |
| Runtime plugins | **10/10 packaged** |
| Locked plugin payload files | **34/34 SHA-256 source/generated matches** |
| Step 18 registry regression | **23/23 passed** |
| Step 19 independent build/tamper regression | **15/15 passed** |
| Development source (00_Workspace/Importer) | Excluded from generated base |
| QEAX archive | Excluded from runner worktree and generated base |
| Generated vault identity | `vault_uid: UNINITIALIZED` |
| Mac/Windows Obsidian first-open, edit and restart | **NOT RUN** |
| Source-data security, public-main promotion and standalone archive | **NOT APPROVED** |

The tamper tests changed **only temporary generated** guide and Workbench `main.js` bytes, verified detection, restored the originals, then verified the generated base again. The tested source lock and runtime payload were not rewritten.

This evidence applies to the tested source commit; it does not certify an issued MDSE 0.8.0 release. Human GUI cases G19-01 through G19-12 above remain unexecuted and require separate operator evidence.
