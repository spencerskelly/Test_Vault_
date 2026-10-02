# Base First-Open Test Sheet

Run on a freshly built base (`build-base.py`) before it is shared, on macOS and on Windows, with Obsidian at or above `obsidianMinVersion` in `.obsidian/plugin-lock.yaml` (currently 1.13.0). Record the date, machine and result of each line. W-322.

| # | Check | Expected |
|---|---|---|
| 1 | Open the folder as a vault | Obsidian offers **Trust author and enable plugins** |
| 2 | Trust and enable | No "plugin failed to load" notices; 11 community plugins listed as enabled |
| 3 | Status bar after a few seconds | **MDSE: release OK**, or only warnings for vault identity (pre-initialization) |
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
| 15 | Drift test: edit one byte of `.obsidian/plugins/dataview/main.js`, run **Show release check** | dataview reported as differing; restore with `git checkout` |
