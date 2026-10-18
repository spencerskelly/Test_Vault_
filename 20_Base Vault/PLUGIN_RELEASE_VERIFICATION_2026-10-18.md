# V2 Base Vault — Plugin verification and deployment gates
2026-10-18 · Step 2 implementation evidence

## Verified upstream procedure
Obsidian community plugins are installed separately from core plugins. A release normally provides `manifest.json`, `main.js`, and optional `styles.css`; manifests and downloadable tagged release assets must agree. The official community plugin manager asks the user to enable plugins explicitly and does not automatically apply updates.

Primary references:
- https://obsidian.md/help/community-plugins
- https://github.com/obsidianmd/obsidian-releases
- https://docs.obsidian.md/Plugins/Releasing/Submit%20your%20plugin
- https://publish.obsidian.md/git-doc/Installation

## Candidate inventory — not an installation instruction
- Git (`obsidian-git`) — upstream plugin directory confirms existence; local plugin build and supported desktop Git environment unverified.
- Templater (`templater-obsidian`) — upstream directory lists 2.26.0, requiring Obsidian 1.13.0+. This is a directory observation, NOT a pinned, downloaded, hashed, installed or tested build.
- Dataview — source candidate; obtain exact upstream release artifact/version and verify.
- MDSE Bootstrap — custom plugin; establish its own build provenance and version compatibility.
- MDSE Workbench — custom plugin; establish its own build provenance and version compatibility.

## Mandatory verification before an installable Base Vault
1. Confirm IDs against upstream plugin manifests. Pin exact release tags and minimum Obsidian versions.
2. Fetch release artifacts; check `manifest.json` ID and version, required `main.js`, and any CSS; calculate SHA-256 and record upstream URL/license.
3. Check managed settings schema, compatibility on supported Windows/macOS versions, and security of scripts/permissions.
4. Confirm installed plugin loads in Obsidian, registers expected commands/views, saves settings and can be restarted.
5. Generate `.obsidian/community-plugins.json` using only approved, actually packaged plugins. The current builder intentionally produces `[]`.
6. Bootstrap preview/backups are required for existing-vault upgrades; preserve `.obsidian/plugins/*/data.json` until an explicit tested migration is available.
7. Test rollback to the prior verified release after simulated failed upgrade.

## Current result
Metadata research complete for the Obsidian packaging process and Templater directory compatibility; downloadable plugin binaries and installed runtime are NOT verified. Step 2 remains open; do not call the scaffold a deployable package.
