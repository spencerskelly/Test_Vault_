# Obsidian Workbench contextual actions popup — test handoff

Date: 2026-10-17. Implemented in `14_Workbench/src/main.ts` on Test_Vault_ main. This is source code, **not a deployed Obsidian plugin bundle**. TypeScript build and runtime interaction are not yet verified.

## Implemented
- New settings toggle: `Automatically show Workbench actions`, default OFF.
- New command: `Open Workbench actions for selected note` (manual invocation regardless of toggle).
- On selection/open of a different Markdown note, option ON opens a Workbench actions modal.
- Clicking a note card within a generated Workbench Canvas opens the same actions modal with toggle ON; existing details popup behavior persists with toggle OFF.
- Modal shows selected note name and a basic element dropdown populated from recognized one-line declarations in the note's final `## SysML v2` fenced `sysml` block. Dropdown is informational at this stage and does not yet perform element-specific editing.
- Existing actions exposed: note details; structure view; choose view; relate to another note. Advanced Merge Notes remains visibly planned, not operable.
- No duplicate vault explorer is added. No writes to native syntax or YAML in this slice.

## Installation/test
1. Build the plugin from the current repository with its documented Node/TypeScript toolchain; deploy generated `main.js`, `manifest.json` and stylesheet if required to the Obsidian plugin folder. Merely pulling `main.ts` does NOT update a running Obsidian plugin.
2. Open Obsidian settings → Community plugins → MDSE Workbench settings. Confirm `Automatically show Workbench actions` defaults OFF.
3. With toggle OFF, open a Markdown note. No automatic actions popup. Invoke the command manually and verify modal.
4. Enable toggle; open one Markdown note and then a different Markdown note. Verify one popup per selection change, not a popup loop.
5. Click a note card in a generated Workbench Canvas; verify popup targets the selected card's note, not the Canvas source file.
6. Verify notes with and without a bottom `## SysML v2` fenced block; only recognized declarations appear in dropdown. Confirm original note bytes are unchanged.
7. Disable toggle and confirm automatic opening stops; manual command still works; existing Canvas detail interaction remains available.
8. Check no double modals after reload, clean dismissal with Escape, and no conflicts with existing note editor or plugin settings.

## Remaining work
- Formal parser-driven element selection (current recognizer is limited, dropdown selection does not drive element-specific editors).
- Source-span-aware native editing and atomic note writes, guarded by pinned SysML v2 parser.
- Replace any remaining duplicate explorer surfaces in the separately maintained UI; this commit changes only the plugin actions popup.
- Typecheck, bundle, Obsidian runtime manual acceptance and rollback/staged release. No CI success claimed.
