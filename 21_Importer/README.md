# v2 Importer

Start here. The importer is **one HTML file** — [`mdse_v2_importer.html`](mdse_v2_importer.html). Open it in Chrome or Edge. No install, no network. Decision: [ADR-V2-07](../26_Definitions/ADR_V2_07_HTML_ONLY_IMPORTER_2026-10-18.md).

**Status:** steps 1 (analyze a QEAX) and 2 (check or choose a vault) work. Generating notes from a QEAX is milestone M2 and is not built.

Edit the sources in `src/`, never the HTML: `node 21_Importer/build_importer_html.mjs` rebuilds it, `--check` is the CI gate.

| Source | Role |
|---|---|
| `src/mdse_core.js` | note format, rerun merge, ZIP. Pure functions, node-tested |
| `src/qeax_reader.js` | streaming SQLite reader, extracted from V1 |
| `src/classes.json` | class, subtype, id prefix table, checked against `99_System/03_Schemas/element-types.yaml` |
| `src/importer.template.html` | page shell |

Python files in this folder (`v2_*.py`, `mdse_note_format.py`) are reference algorithms and test oracles. Format: [ADR-V2-06](../26_Definitions/ADR_V2_06_NOTE_FORMAT_2026-10-18.md).
