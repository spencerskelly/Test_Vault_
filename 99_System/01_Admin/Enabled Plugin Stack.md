# Enabled Plugin Stack

Active community plugins. Versions are pinned in `.obsidian/plugin-lock.yaml`; the enabled list is `.obsidian/community-plugins.json`.

## Required baseline

| Plugin | Role |
|---|---|
| MDSE Bootstrap | On a new machine, installs the vault's plugins automatically from the pinned list. This is how the vault is rolled out to the team. Its source is not in this repo. |
| Nodian | Pinned but not relied on (W-275 trial). Its pairs need a class tag on both notes, which MDSE notes do not carry, and its pairs are local per machine. Inverses are written by the translator, Workbench or the regenerate script. Removal is decided after the trial. |
| Breadcrumbs | semantic relationship navigation |
| Dataview | dashboards and health queries; kept for functions core Bases cannot do. No Dataview queries exist in the vault yet, so the specific functions still need to be listed here. |
| Fileclass | typed property/schema editing |
| Advanced Canvas | model/architecture visualization |
| Templater | templates and ID helpers |
| Obsidian Git | visible Git sync/recovery during current rollout |

## Optional but approved

| Plugin | Role |
|---|---|
| QuickAdd | fast creation/automation launcher |
| Table Exporter | engineering review/export |

Core Obsidian Canvas, Properties, Bases, Graph, backlinks, templates, and file recovery are enabled. Bases is the primary tool for tables and folder views.

## Archived

Ampure Cross-Vault Resolver and Multi-Vault Navigator were removed on 2026-09-28 when the vault became a single vault. What they did, why they existed, and how to restore them: see `Archived Plugins/Archived Plugins.md`.

## Packaging rule

Executable community-plugin files are not authoritative vault content. The shared configuration and pinned versions are authoritative. Plugin binaries should be installed/bootstrap-managed on each machine.

Exception: the Obsidian Git binary (2.40.0) stays committed under `.obsidian/plugins/obsidian-git/` because it is in use on the Mac. All other plugin binaries remain per-machine installs.

Plugin-specific `data.json` is local by default unless a setting is explicitly proven to be required shared behavior.
