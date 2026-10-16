# Step 55 — PR #43 CI failure evidence (2026-10-14)

Status: **diagnosed; release hold remains**. No binary, hash manifest, model, or workflow changed.

## Observed runs at commit b89f9664004f1b676e9b8f6499a194435bfbcf1b

- Run 38601600859 P03 legacy compatibility synthetic tests: SUCCESS
- Run 38601601026 MDSE consolidated read-only integration gate: SUCCESS
- Run 38601601253 P04 Workbench read-only build and tests: FAILURE
- Failed job 115981960497, step: `Require reproduced artifacts to match governed Workbench baseline`. All prior P04 build, tests, tree inventory and two-build consistency steps succeeded.

## Exact hashes in P04 log

- First fresh `55_Workbench/main.js`: `d2c4d90142718f3363196f0c5e7663cc9d87fc22655b62bfbc2887a69d2dec13`
- Second fresh `55_Workbench/main.js`: `d2c4d90142718f3363196f0c5e7663cc9d87fc22655b62bfbc2887a69d2dec13`
- Tracked, governed `55_Workbench/main.js`: `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`
- First mismatch offset: **13,733 bytes**.
- Failed command: `sha256sum --check artifact-sha256.txt`; output `main.js: FAILED` / `1 computed checksum did NOT match`.

## Interpretation

Current CI toolchain builds consistently, but its output differs from the governed committed bundle. This does not prove whether toolchain patch-level drift, source/artifact provenance or intentional original build differences caused the mismatch. The existing controlled artifact is not authorized to be regenerated or overwritten.

## Next atomic step

1. Capture full commit and source manifests for governed bundle versus original Workbench build commit `b0c4e2c6bdfb96d36f51d8152b17be22592ef174`, with exact Node/npm/esbuild version evidence where available.
2. Compare compiled bundle content and source histories read-only, inspecting first difference near byte 13,733; avoid uploading entire binaries or model data.
3. Classify mismatch: historical provenance gap versus changed source/toolchain; require independent approval before hash-baseline changes.
4. Only after controlled reproduction, update tests to separately report **candidate reproducibility** and **governed release equivalence**. Never silently mark a mismatch as success.

No merge, release, branch deletion, historical archive manipulation, or QEAX content checkout authorized.
