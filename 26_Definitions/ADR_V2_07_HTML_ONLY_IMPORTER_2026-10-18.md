# ADR-V2-07 — The importer is one HTML file: no install, new vault or add onto an existing one

Date: 2026-10-18. Status: **ACCEPTED by owner** ("no installs, HTML tools only"). Supersedes the Python-importer direction implied by `21_Importer/v2_step03*.py`; those scripts stay as reference algorithms and test oracles, not as the product.

## Decision

1. The importer is a **single self-contained HTML file**, [`21_Importer/mdse_v2_importer.html`](../21_Importer/mdse_v2_importer.html). It runs from a double-click, offline, with no network request and no dependency (a browser test fails on any non-`file:` request).
2. It has two output modes. **New vault** writes a ZIP. **Add to existing vault** writes into a folder the user chooses and never deletes.
3. The page is *built*, not hand-edited: [`build_importer_html.mjs`](../21_Importer/build_importer_html.mjs) inlines `21_Importer/src/{mdse_core.js, qeax_reader.js, classes.json, importer.template.html}`. CI runs it with `--check`, so a stale page fails the build.
4. Python and Java are **development and CI tools only** (oracles, parser gate). Users never run them.

## Add-onto-existing rules

Ruleset §16.4, implemented in `MDSE.mergeNote()` and covered by 13 node tests:

| Part | Rerun behaviour |
|---|---|
| Note found by `uid` (even if the user moved it) | matched; path is not the identity |
| User zone (everything above the first managed heading) | kept |
| `id`, `uid` | never change |
| `status`, `tags`, any other key | kept |
| `subtype`, `eaType`, `sourceRole`, `primarySymbol` | refreshed from EA; each change logged |
| `## Source: EA`, `## SysML v2` | replaced |
| Same `uid`, different `type`, or `uid` mismatch | **conflict**: nothing written, reported |
| Merging identical input | `unchanged`, byte-identical (idempotence test) |
| Note has no managed footer yet | footer appended, user text untouched |

Two known limits: the merge normalises trailing blank lines at the join between user zone and footer, and it preserves CRLF notes as CRLF.

## What exists and what is proven (2026-10-18)

| Piece | State | Evidence |
|---|---|---|
| Streaming SQLite reader (extracted from V1 v0.8.5 sqlite.js) | working | rows identical to `sqlite3` on a 1.3 MB file with overflow chains, interior pages, NULLs, Unicode, blobs, negative and 2^40 integers; non-SQLite file rejected with EA guidance |
| Note format validator in JS | working | agrees with the Python validator on 20 mutated notes; embedded class table checked against `element-types.yaml` |
| `replaceSysmlBlock` | working | byte-identical to Python, LF and CRLF |
| ZIP writer (stored) | working | read back by Python `zipfile`, `testzip()` clean |
| Page shell: analyze QEAX, check a vault, report issues | working | real Chromium test: counts, diagram exclusion, offline, `ID_PREFIX` detection (mutation-checked) |
| QEAX to notes (typed graph, approved families, uid/id allocation) | **not built (M2)** | — |
| SysML v2 writer, Bootstrap packaging, parser gate | **not built (M3 to M5)** | — |
| Real QEAX | **never run here** | the reduced and full QEAX are not in this repository or sandbox |

## Milestones

| | Scope | Done when |
|---|---|---|
| M2 | Port the approved-family resolver, typed relationship gates and uid/id allocation to JS; emit ADR-V2-06 notes; id allocation continues from the highest existing id per prefix | JS output equals the Python oracle on the same synthetic QEAX; add-onto run twice is a no-op |
| M3 | Typed canonical graph to SysML v2 text, one block per note; emit the parser-check report format | pinned parser accepts every block in CI; report lists each note |
| M4 | Package V2 Bootstrap and Workbench into the new-vault ZIP; fail readiness when binaries are missing | extracted ZIP starts Bootstrap on first open in Obsidian |
| M5 | Run on the reduced QEAX, then the full one | binary acceptance list in the [recovery handoff](MDSE_V2_RECOVERY_HANDOFF_2026-10-18.md) |

## Consequences and open questions

- **Parser gate (owner accepted 2026-10-19).** The pinned official SysML v2 parser is a Java program and cannot run inside the page. It runs in CI and on a maintainer's machine against the generated vault. The ZIP carries a **parser-check report** (parser version, per-note result, date). Workbench marks that report **stale** whenever a SysML block changes after it was produced, and never presents unchecked SysML as verified. Consequence: users get a vault whose SysML was checked at release time, not on their own machine. M3 must emit the report format and M4 must make Workbench read it.
- **Browser support.** Writing into an existing folder needs the File System Access API (Chrome, Edge). Firefox and Safari can only build ZIPs and run the read-only check.
- **SharePoint.** A vault opened from a synced SharePoint folder is just a local folder, so the same page works; Rovo indexing of Markdown remains unverified (see the [organization proposal](V2_FILE_ORGANIZATION_PROPOSAL_2026-10-18.md)).
