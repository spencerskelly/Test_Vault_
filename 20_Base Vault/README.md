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
