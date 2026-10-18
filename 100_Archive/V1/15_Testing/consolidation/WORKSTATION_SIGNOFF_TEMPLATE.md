# MDSE consolidation — per-workstation Git sign-off template

**This file is a blank template; it is not an audit result.** Keep completed forms in an approved private location. Never commit machine names, people, local paths, unpublished branch names, or unpushed patch contents to the public project.

## Inventory register (repeat rows for every independent clone AND linked worktree)

| Internal audit ID | Repository | Local owner verified? | Script report reviewed? | Unpushed and dirty work disposition | Remote-current check done? | Final status |
|---|---|---|---|---|---|---|
| [internal ID] | `MDSE_Workbench` | No | No | Open | No | **OPEN** |
| [internal ID] | `Test_Vault_` | No | No | Open | No | **OPEN** |

Rows are examples only. Do not assume exactly two clones exist. The auditor must inventory each contributor machine, separate local clones, and extra linked worktrees, including machines that have no remote access.

## Per-clone checklist — complete privately

- Internal machine/clone audit identifier (not public path): `[private ID]`
- Repository verified by owner: `[Test_Vault_ / MDSE_Workbench / other]`
- Auditor and local-owner acknowledgment: `[private identities]`
- Audit date and exact script revision: `[date/time and Git commit]`
- Local HEAD SHA and current branch or detached state: `[reviewed privately]`
- All tracked dirty entries: `[count, backup/recovery evidence, resolved or retained]`
- All untracked files: `[count, backup/recovery evidence, resolved or retained]`
- Ignored/non-Git files manually reviewed, where appropriate: `[Yes/No]`
- Local branches lacking upstream: `[all enumerated and classified]`
- Branches ahead of their configured upstream: `[all local-only commits preserved or dispositioned]`
- Branches behind/diverged/unresolvable/local-upstream: `[all individually reviewed]`
- Detached HEAD and any unreferenced work reviewed: `[Yes/No/not applicable]`
- Every Git stash reviewed and preserved/dispositioned: `[Yes/No]`
- Every linked worktree separately inventoried: `[Yes/No]`
- Submodules and nested repositories inventoried, if present: `[Yes/No/not applicable]`
- Shallow/sparse checkout limitations addressed: `[Yes/No/not applicable]`
- Remote-tracking freshness verified through separately approved, safe remote synchronization or independent GitHub commit comparison **after protection of local data**: `[Yes/No]`
- GitHub branches/PRs required for migration or future recovery identified and preserved: `[Yes/No]`
- Private evidence link / change ticket (never raw proprietary paths in public): `[private reference]`
- Owner confirms any remaining work is accessible from the designated authoritative repository or a documented protected recovery source: `[Yes/No]`
- Final determination: `OPEN / CLEARED / ESCALATE` (default `OPEN`)
- Local owner sign-off + independent approver: `[private identities, dates]`

## Rules for marking CLEARED

`CLEARED` requires **all** above applicable items to be reviewed; each dirty/untracked/unpushed/unknown/stashed/unreferenced source must be preserved or explicitly dispositioned. An apparent `AHEAD=0` from the script never means remote synchronization was verified: the script intentionally does not fetch. Do not force/reset/delete to make a log clean.

A complete workstation register is **necessary but not sufficient** to archive `MDSE_Workbench`: the QEAX content classification and public-exposure response, single-repository authority promotion, complete integrated CI, and real Obsidian acceptance are separate gates.
