# MDSE v2 Base Vault

**Status: pilot configuration scaffold — not a deployable team release.**

`build_v2_test_base.py <new-output-folder>` creates a new standalone test vault, copies pinned V2 definitions and generates minimal Obsidian configuration under `.obsidian/`. It refuses to overwrite existing folders.

`v2_base_release_manifest.json` is the candidate release authority. Community plugins intentionally remain disabled and have no verified binaries, package hashes, or supported Obsidian version; Workbench and Bootstrap are not installed. Do not distribute this as the controlled team setup.

## Next requirements
1. Inventory and pin actual plugin IDs, versions and package hashes from a designated working reference vault; independently verify artifacts and licenses.
2. Include supported plugin settings, shared navigation and templates, UI configuration, and Windows/macOS acceptance.
3. Test opening in Obsidian and note creation, then hand management of installed configurations to Bootstrap.
4. Never write into a populated engineering vault from this test builder; all updates require Bootstrap preview, backup, migration and rollback.

Validation is in `25_Testing/test_v2_test_base_builder.py`. CI execution remains to be confirmed.

## V1 implementation reuse — 2026-10-18
The archived v0.8.x Base Vault already has a controlled plugin release, manifest, lock/hash strategy, plugin configuration generator, and startup/author registration functions. **Reuse these**, not a new unrelated stack. Original reference: `100_Archive/V1/10_Base Vault/Definition/Enabled Plugin Stack.md`, `Definition/mdse-release.yaml`, and `Tools/v0.8.0-r2/`.

A new one-time migration tool `stage_v1_verified_plugins_for_v2.py <unused-output-folder>` stages seven core V1 plugin artifacts with SHA-256 verification. Candidate package is **inactive** and isolated outside the repo; no V2 runtime reads from V1. Re-evaluate V1 Workbench 0.1.18 and Bootstrap manifest 0.3.1 for V2 compatibility before loading; do not silently reuse V1 schema assumptions. Keep original metadata and hashes for provenance.

V1 decisions carried forward: Dataview intentionally retired after startup-performance evidence, Fileclass and Breadcrumbs transitional, Nodian/QuickAdd/Table Exporter optional; do not re-add them by accident. Plugin settings/data are not imported in the staging tool, because identity and private machine state need a separate migration.
