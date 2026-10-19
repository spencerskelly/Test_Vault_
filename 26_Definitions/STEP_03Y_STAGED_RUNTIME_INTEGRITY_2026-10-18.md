# STEP-03Y — V2 staged runtime integrity and readiness

2026-10-18. Added read-only runtime integrity checker and two synthetic regression tests.

The current V2 test base includes 8 pinned reference/rule files but does NOT include a synchronized runnable Workbench or Bootstrap plugin runtime. The test base is not a production Base Vault and cannot be represented as plugin-ready. The validator checks each file against its generated SHA-256 manifest, inspects `.obsidian/plugins/mdse-bootstrap` and `mdse-workbench` for a plugin manifest and compiled main.js, and reports readiness blocked. It does not fake passing native parser, Workbench editing or runtime QA.

## Mac commands

```bash
git pull --ff-only origin main
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03y_runtime_integrity.py' -v
python3 "20_Base Vault/verify_v2_staged_runtime.py" "$HOME/Documents/MDSE_Local_STEP03X_Base"
```

Expected the 8 staged files hash clean, both plugins absent, plugin_ready and native_import_ready false, status BLOCKED_RUNTIME. If file hashes mismatch, status FAIL_BASE_INTEGRITY.

## Critical path

Next STEP-03Z must stage and pin **actual compiled and tested V2** Bootstrap and Workbench artifacts, including manifests, plugin configuration, checksums, explicit release identifier, lock generation and verification. Do not copy pre-v2 V1 runtime or archive into the V2 test base or simply update version strings. Then connect native SysML v2 serialization/parsing and plugin edit round-trip. Continue retaining the local interim EA note vault and excluding EA diagrams until golden import.
