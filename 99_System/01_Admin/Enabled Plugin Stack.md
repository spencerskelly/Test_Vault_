# Enabled Plugin Stack

Active community plugins. Versions are pinned in `.obsidian/plugin-lock.yaml`; the enabled list is `.obsidian/community-plugins.json`.

## Required baseline

| Plugin | Role |
|---|---|
| Nodian | Pinned but not relied on (W-275 trial). Its pairs need a class tag on both notes, which MDSE notes do not carry, and its pairs are local per machine. Inverses are written by the translator, Workbench or the regenerate script. Removal is decided after the trial. |
| Breadcrumbs | semantic relationship navigation |
| Dataview | dashboards and health queries; kept for functions core Bases cannot do. No Dataview queries exist in the vault yet, so the specific functions still need to be listed here. |
| Fileclass | typed property/schema editing |
| Advanced Canvas | model/architecture visualization |
| Templater | templates and ID helpers |
| Obsidian Git | visible Git sync/recovery during current rollout |

## Planned runtime addition

| Plugin | Role |
|---|---|
| MDSE Workbench | Required in the final v0.8 issued base once WB-106 is complete and a release is pinned. Not yet enabled in the pre-release baseline. |

## Deferred

| Plugin | Reason |
|---|---|
| MDSE Bootstrap | Deferred by W-321 because no retrievable source/release is available. Its specification remains in the methodology workspace, but the v0.8 runtime base does not enable or pin an unavailable plugin. |

## Optional but approved

| Plugin | Role |
|---|---|
| QuickAdd | fast creation/automation launcher |
| Table Exporter | engineering review/export |

Core Obsidian Canvas, Properties, Bases, Graph, backlinks, templates, and file recovery are enabled. Bases is the primary tool for tables and folder views.

## Archived

Ampure Cross-Vault Resolver and Multi-Vault Navigator were removed on 2026-09-28 when the vault became a single vault. What they did, why they existed, and how to restore them: see `Archived Plugins/Archived Plugins.md`.

## Packaging rule

Executable community-plugin files are not authoritative vault content. The shared configuration and pinned versions are authoritative. Plugin binaries should be installed through the normal approved deployment mechanism on each machine; no unavailable bootstrap plugin is assumed.

Exception: the Obsidian Git binary (2.40.0) stays committed under `.obsidian/plugins/obsidian-git/` because it is in use on the Mac. All other plugin binaries remain per-machine installs.

Plugin-specific `data.json` is local by default unless a setting is explicitly proven to be required shared behavior.
