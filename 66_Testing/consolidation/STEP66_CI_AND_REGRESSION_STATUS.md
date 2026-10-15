# Step 66 — CI verification and targeted regression tests (2026-10-14)

## Verified passing CI

At commit `d2a28450cd56c001c1a7a80ede8f23ba68e8e550`, all five PR #43 read-only GitHub Actions workflows passed. P04 run `38606858528`, job `115999859823` specifically passed two consecutive clean builds and the new separate gates:
- Governed Git-tracked `main.js`, `manifest.json`, `styles.css`: SHA-256 integrity PASS.
- Current candidate bundle SHA-256: `d2c4d90142718f3363196f0c5e7663cc9d87fc22655b62bfbc2887a69d2dec13`; reproduced identically in both builds.
- Historical governed bundle SHA-256: `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7`. DIFFERENT is explicitly reported as a **new candidate requiring separate release qualification**, not historical integrity failure.

## Regression additions

Added `55_Workbench/test/localmodel06-quantity.test.ts`, commits `0bb26ef5cc4d8e2f91529b9f2436391aa9fe0b64` and `e1e77e988632f00d459b6a1d8c61aee22d092514`.

Tests target:
1. Schema 0.6 read-only parsing of multiplicity, quantity and unitOfMeasure, while `WRITABLE_VERSION` remains 0.5.
2. Schema 0.5 reports `record.unknown-field` when quantity and unitOfMeasure are used in unsupported contexts.

The tests were committed, but their CI result **was not available at the time of this checkpoint**. Do not call the new tests passing until the next run is observed.

## Next checkpoint

Retrieve the latest P04 run after `e1e77e9` and fix test assumptions only if necessary. Continue targeted variantOf and cache assertions. No governed binary, hash manifest, model archive, release tag, branch deletion, or main promotion.
