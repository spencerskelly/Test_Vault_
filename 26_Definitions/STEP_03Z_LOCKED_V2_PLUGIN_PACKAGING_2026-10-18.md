# STEP-03Z — Verified V2 plugin packaging gate

2026-10-18.

Added `20_Base Vault/stage_v2_locked_plugins.py` and 3 synthetic tests. The packager takes the generated STEP-03X test base, a pair of independently compiled plugin folders, and an explicit local evidence JSON. It demands matching plugin IDs, versions, main.js and manifest.json SHA-256 hashes, plus passed V2 editor and Bootstrap test claims in the evidence. It refuses existing destinations, stages only into a new folder, and cleans partial output on failure.

This is an **executable packaging implementation**, not evidence the real V2 plugin source or compiled runtime has been built, that native parsing works, or that Obsidian acceptance passed. Evidence JSON is a gating input and must be produced by actual automated tests, never fabricated just to pass the stage. The output lock records `runtime_observed_in_obsidian: false` and `native_import_ready: false` even when artifact hashes match.

## Verify tool on Mac

```bash
git pull --ff-only origin main
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03z_locked_plugin_stage.py' -v
```

Do not run the packager on STEP-03X until actual V2 plugin artifacts and test evidence exist. No manual Base Vault setup needed; do not use V1 plugin binaries. Never copy a source QEAX or per-note ledger into public repository. EA diagrams excluded.

Next: develop/build real V2 Workbench and Bootstrap runtime, run editor/source-note round-trip tests, generate evidence from those tests, stage plugin artifacts into the isolated test base and verify in Obsidian. Separately finish importer native parser, serializer and navigation parity before golden import acceptance.
