# Enabled Plugin Stack

## Required baseline

| Plugin | Role |
|---|---|
| MDSE Bootstrap | baseline/bootstrap support |
| Nodian | paired relationship inverse synchronization |
| Breadcrumbs | semantic relationship navigation |
| Dataview | dashboards and health queries |
| Fileclass | typed property/schema editing |
| Advanced Canvas | model/architecture visualization |
| Templater | templates and ID helpers |
| Obsidian Git | visible Git sync/recovery during current rollout |

## Optional but approved

| Plugin | Role |
|---|---|
| QuickAdd | fast creation/automation launcher |
| Table Exporter | engineering review/export |

Core Obsidian Canvas, Properties, Bases, Graph, backlinks, templates, and file recovery are enabled.

## Packaging rule

Executable community-plugin files are not authoritative vault content. The shared configuration and pinned versions are authoritative. Plugin binaries should be installed/bootstrap-managed on each machine.

Plugin-specific `data.json` is local by default unless a setting is explicitly proven to be required shared behavior.
