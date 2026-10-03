# MDSE Bootstrap

**Status:** active, version 0.3.0 (W-322). Source in `MDSE Bootstrap/plugin/`. Ships in every MDSE base vault.

## Purpose

The MDSE base vault is a **controlled release**: every person opens the same vault with the same plugins, the same versions and the same settings. Nothing is installed or updated per machine. MDSE Bootstrap is the small plugin that makes that visible and finishes the per-person setup.

It does two things:

1. **Release check.** On every start it compares the vault with `.obsidian/plugin-lock.yaml`: each plugin's version and the SHA-256 of its `main.js`, `manifest.json` and `styles.css`; that each locked plugin is enabled and nothing else is; the Obsidian version (`obsidianMinVersion`); required core plugins on (`bases`, `canvas`, `properties`, `file-explorer`, `command-palette`) and core Templates off; `mdse_release` and the vault identity in `.vault.yaml`; that the vault is a Git repository; that an author code is registered. The status bar shows **MDSE: release OK**, or the number of problems; click it for the table. Command: **MDSE Bootstrap: Show release check**.
2. **Author registration**, as specified in [[MDSE Bootstrap - Author Registration Spec]]. On first open on a computer it asks for first and last name, proposes the code, rejects a code that is taken or reserved, writes `.obsidian/author-code.txt` and creates the person note from the `Person` template through Templater (so `uid` and `id` come from the same snippets as every other note). A person whose note already exists keeps their code. Command: **MDSE Bootstrap: Register author code**.

It never downloads, installs, updates or changes plugins or settings. If the check reports drift, the fix is to restore the vault's own files with Git.

## How the controlled release is built

All in the methodology workspace (`Test_Vault_`); none of it is copied into an engineering vault except the outputs.

| Step | File | What it does |
|---|---|---|
| Plugin code | `99_System/09_Tools/runtime-plugins/<id>/` | Vendored `main.js`, `manifest.json`, `styles.css` for every runtime plugin: third-party plugins from their official GitHub release at the pinned version; Workbench and Bootstrap from their builds. |
| Settings | `99_System/09_Tools/build-plugin-config.py` | Generates the governed `data.json` for Templater, Fileclass, Breadcrumbs and Obsidian Git, the Fileclass schemas in `99_System/06_Fileclasses/` and their link-target Base, all from `relationships.yaml` and `element-types.yaml`. |
| Lock | `99_System/09_Tools/update-plugin-lock.py` | Writes `.obsidian/plugin-lock.yaml` (schema 2: version, source, settings policy, SHA-256 per file) and `.obsidian/community-plugins.json` (enabled list). |
| Base | `99_System/09_Tools/build-base.py <out>` | Copies the runtime file set and every locked plugin into `<out>/.obsidian/plugins/`, writes the base `.gitignore`, `README.md` and `.vault.yaml`. |
| Check | `99_System/09_Tools/check-release.py [--base <out>] [--workbench <clone>]` | Fails if generated settings or the lock are stale, a payload file does not match its hash, versions disagree, or the base differs from the release. |

### Changing a plugin version (a release decision)

1. Replace the plugin's files in `runtime-plugins/<id>/` (official release assets only; never a copy installed through Obsidian's browser, which appends `/* nosourcemap */`).
2. If it is a governed plugin, check its settings still apply and rerun `build-plugin-config.py`.
3. Run `update-plugin-lock.py`, then `check-release.py`.
4. Log the change as a `W-` decision and test with the [[Base First-Open Test Sheet]].

### Building Bootstrap

```
cd "MDSE Bootstrap/plugin"
npm install
npm test
npm run build
cp main.js manifest.json styles.css ../../99_System/09_Tools/runtime-plugins/mdse-bootstrap/
python3 ../../99_System/09_Tools/update-plugin-lock.py
```

`node_modules/` and the local `main.js` are git-ignored. The build is reproducible: rebuilding unchanged source gives the identical `main.js`. Raise the version in `manifest.json`, `package.json` and `mdse-release.yaml` together; `check-release.py` fails when they disagree.

## Files

- `plugin/src/core.ts`: pure logic (code rule, uniqueness, lock parsing, drift evaluation), unit-tested in `plugin/test/`.
- `plugin/src/main.ts`: Obsidian wiring (status bar, commands, modals, Templater call).
- [[MDSE Bootstrap - Author Registration Spec]]: the registration behavior (W-24, W-25).
- [[Base First-Open Test Sheet]]: what to check in Obsidian before a base is shared.

## History

- 0.2.0 was pinned in earlier plugin locks but no source or release existed; W-321 deferred it.
- 0.3.0 (W-322) is a new implementation built for the controlled release. It does not install plugins; the base ships them.
