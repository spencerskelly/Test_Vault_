# MDSE Bootstrap

**Status:** runtime release 0.3.0 is pinned in the current base. Candidate 0.3.1 implements W-330 safe activation repair and is under test in `Bootstrap/Tools/v0.3.1`.

## Purpose

The MDSE base vault is a **controlled release**: every person opens the same vault with the same plugins, the same versions and the same settings. Nothing is installed or updated per machine. MDSE Bootstrap is the small plugin that makes that visible and finishes the per-person setup.

It does three things:

1. **Safe activation repair (W-330).** After Obsidian's required **Trust author and enable plugins** step, Bootstrap enables a disabled locked community plugin only when its version and every locked file already match the release; it enables required core plugins and disables explicitly prohibited core plugins. It does not download/replace plugin code, rewrite governed settings, or disable unrelated extra community plugins.
2. **Release check.** On every start it compares the vault with `.obsidian/plugin-lock.yaml`: each plugin's version and the SHA-256 of its locked runtime files; governed plugins also lock `data.json`; that each locked plugin is enabled and nothing else is; the Obsidian version (`obsidianMinVersion`); required core plugins on (`bases`, `canvas`, `properties`, `file-explorer`, `command-palette`) and core Templates off; `mdse_release` and the vault identity in `.vault.yaml`; that the vault is a Git repository; that an author code is registered. Candidate 0.3.1 stages this work (W-347): disabled locked plugins are fully hashed before any automatic enablement, author registration is then surfaced, and the normal whole-release hash scan waits for Obsidian's metadata pass so it does not compete with the heaviest startup work. **Show release check** still performs an immediate full verification. The status bar shows **MDSE: release OK**, or the number of problems; click it for the table.
3. **Author registration**, as specified in [[MDSE Bootstrap - Author Registration Spec]]. On first open on a computer it asks for first and last name, proposes the code, rejects a code that is taken or reserved, writes `.obsidian/author-code.txt` and creates the person note from the `Person` template through Templater (so `uid` and `id` come from the same snippets as every other note). A person whose note already exists keeps their code. Command: **MDSE Bootstrap: Register author code**.

It never downloads, replaces or updates plugin files and never silently repairs governed configuration content. Safe activation state is repaired automatically only for intact locked plugins. A disabled plugin with file/configuration drift stays disabled and is reported for restoration from the controlled vault/Git. Staged startup changes *when* normal full verification runs, not what is verified.

## How the controlled release is built

All in the methodology workspace (`Test_Vault_`); none of it is copied into an engineering vault except the outputs.

| Step | File | What it does |
|---|---|---|
| Plugin code | `Base Vault/Runtime/Plugins/<id>/` | Vendored `main.js`, `manifest.json`, `styles.css` for every runtime plugin: third-party plugins from their official GitHub release at the pinned version; Workbench and Bootstrap from their builds. |
| Settings | `Base Vault/Tools/v0.8.0-r2/build-plugin-config.py` | Generates the governed `data.json` for Templater, Fileclass, Breadcrumbs and Obsidian Git, the Fileclass schemas in `99_System/06_Fileclasses/` and their link-target Base, all from `relationships.yaml` and `element-types.yaml`. |
| Lock | `Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py` | Writes `.obsidian/plugin-lock.yaml` (schema 2: version, source, settings policy, SHA-256 per file) and `.obsidian/community-plugins.json` (enabled list). |
| Base | `Base Vault/Tools/v0.8.0-r2/build-base.py <out>` | Copies the runtime file set and every locked plugin into `<out>/.obsidian/plugins/`, writes the base `.gitignore`, `README.md` and `.vault.yaml`. |
| Check | `Base Vault/Testing/check-release.py [--base <out>] [--workbench <clone>]` | Fails if generated settings or the lock are stale, a payload file does not match its hash, versions disagree, or the base differs from the release. |

### Changing a plugin version (a release decision)

1. Replace the plugin's files in `Base Vault/Runtime/Plugins/<id>/` (official release assets only; never a copy installed through Obsidian's browser, which appends `/* nosourcemap */`).
2. If it is a governed plugin, check its settings still apply and rerun `build-plugin-config.py`.
3. Run `update-plugin-lock.py`, then `check-release.py`.
4. Log the change as a `W-` decision and test with the [[Base First-Open Test Sheet]].

### Building Bootstrap

```
cd "Bootstrap/Tools/v0.3.1"
npm install
npm test
npm run build
cp main.js manifest.json styles.css ../../../Base\ Vault/Runtime/Plugins/mdse-bootstrap/
python3 ../../../Base\ Vault/Tools/v0.8.0-r2/update-plugin-lock.py
```

`node_modules/` and the local `main.js` are git-ignored. The build is reproducible: rebuilding unchanged source gives the identical `main.js`. Raise the version in `manifest.json`, `package.json` and `mdse-release.yaml` together; `check-release.py` fails when they disagree.

## Files

- `Tools/v0.3.1/src/core.ts`: pure logic (code rule, uniqueness, lock parsing, drift evaluation), unit-tested in `Tools/v0.3.1/test/`.
- `Tools/v0.3.1/src/main.ts`: Obsidian wiring (status bar, commands, modals, Templater call).
- [[MDSE Bootstrap - Author Registration Spec]]: the registration behavior (W-24, W-25).
- [[Base First-Open Test Sheet]]: what to check in Obsidian before a base is shared.

## History

- 0.2.0 was pinned in earlier plugin locks but no source or release existed; W-321 deferred it.
- 0.3.0 (W-322) is a new implementation built for the controlled release. It does not install plugins; the base ships them.


## Promotion rule

A candidate revision is not the shipped runtime merely because its source exists. Promote a Bootstrap candidate only after automated tests/build and the first-open test sheet pass, then copy its built payload into `Base Vault/Runtime/Plugins/mdse-bootstrap`, regenerate the plugin lock, and update `Base Vault/Definition/mdse-release.yaml`.
