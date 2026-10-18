# Base First-Open Test Sheet

> [!WARNING] V1 baseline acceptance with explicit V2 extension pending. Rows 8–11 exercise legacy MDSE Port/Fileclass/Breadcrumbs schemas, not the approved native SysML v2 note writer or Workbench. This sheet alone cannot approve a v2 import kit. Test the v2 `## SysML v2` bottom section and four Workbench dropdowns in a separate v2 acceptance sheet. The earlier row 15 incorrectly targeted Dataview, which is not in the current controlled plugin lock; it has been corrected to use a locked plugin in a disposable vault.


Run on an **initialized candidate/model repository made from a validated clean Base Vault artifact**, not on the raw `build-base.py` output (W-334). Before this sheet: `check-release.py --base` has passed on the clean artifact, `.vault.yaml` has been initialized once by the release owner, and Git is initialized; use a remote for rows that exercise pull/push. Run on macOS and Windows with Obsidian at or above `obsidianMinVersion` in `.obsidian/plugin-lock.yaml` (currently 1.13.0). Record the date, machine and result of each line. W-322, amended by W-330/W-334.

| # | Check | Expected |
|---|---|---|
| 1 | Open the folder as a vault | Obsidian offers **Trust author and enable plugins** |
| 2 | Trust and enable | No "plugin failed to load" notices; Bootstrap starts and all locked community plugins are enabled |
| 3 | Status bar after a few seconds | No release/configuration errors. Before author registration the expected remaining warning is the missing per-computer author code; vault identity and Git are already valid at this stage |
| 4 | Registration popup | Asks for name; proposes the code; **Register** creates `99_System/04_People/First Last.md` with `code`, `name`, `timezone`, a `uid` ending in the code and an `INFO-` id |
| 5 | Register again with the same name | Accepted; reports the person note already exists; no second note |
| 6 | Try a code used by another person or `claudeai-----` | Rejected with a reason |
| 7 | `git status` right after first open | Only the new person note. Any change to a tracked `data.json` means a plugin rewrote its settings on load: record which plugin |
| 8 | **Templater: Create new note from template** → `Port` | New note has `type: Port`, a `PORT-#####` id and a uid; title heading filled |
| 9 | Fileclass on that note | Properties show guided input; `subtype` offers proxy/full; `status` offers Draft/Active/Retired |
| 10 | Fileclass `hasPort` picker on an Object note | Offers only Port notes (from `MDSE Link Targets.base`); `hasChild` on an Object offers no Object/State/State Machine notes |
| 11 | Breadcrumbs matrix on a note with `hasPart` and `partOf` | Fields appear under the ups/downs groups; implied inverse shown where missing |
| 12 | Core Templates | Off (Settings → Core plugins) |
| 13 | Obsidian Git | Pulls on start; Commit-and-sync works against the remote |
| 14 | MDSE Workbench | **Show diagnostics** runs; Review screen opens |
| 15 | Drift test: in a disposable test vault only, back up and edit one byte of `.obsidian/plugins/mdse-bootstrap/styles.css`, then run **Show release check** | The locked `mdse-bootstrap` file is reported as differing; restore the exact original bytes before proceeding |

| 16 | Safe repair: disable one locked community plugin, then run **MDSE Bootstrap: Show release check** | Bootstrap re-enables it before reporting release state |
| 17 | Safe repair: turn off one required core plugin | Bootstrap re-enables it |
| 18 | Safe repair: turn on core Templates | Bootstrap turns it back off |
| 19 | Extra community plugin enabled | Bootstrap reports it as extra but does not automatically disable/uninstall it |
| 20 | Modify governed `data.json` or a locked plugin file | Bootstrap does not overwrite the change; release check reports drift requiring Git restoration |

| 21 | Disable a locked community plugin, then modify one of its locked files before running Bootstrap | Bootstrap does **not** re-enable it; release check reports the file/configuration drift |
