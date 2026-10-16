# MDSE v2 Workbench MVP 0.1

Open [v2-workbench.html](v2-workbench.html) in a modern local browser. It is self-contained and requires no installation or web service. Use **Load Golden Charger** to restore the built-in sample; **Open .sysml files** to browse local files; **Export combined source** to save a combined textual source. The explorer and inspector are read-only.

Source model: the committed [Golden Charger v2 fixture](../25_Testing/Fixtures/Golden%20Charger%20v2/README.md), represented as built-in example text. The Workbench's lightweight recognizer currently handles simple package declarations, part/port definitions, part/port usages, and plain connect statements. It is **not** an OMG SysML parser; it does not enforce semantic validity or preserve rich syntax structure. Use the pinned independent-parser workflow for conformance checks.

Upcoming vertical slices: CSV input preview, EA identity linking, mapping-table-based v1→v2/MDSE previews, editable model hierarchy, deterministic note and SysML exports. Keep v1 files unchanged. Mapping authority lives under [26_Definitions](../26_Definitions/README.md) and tests under [25_Testing](../25_Testing/Fixtures/Golden%20Charger%20v2/README.md).

Acceptance for the first prototype: file opens offline, sample tree visible, clicking a node updates the inspector and source panel, multiple SysML files load locally, and combined source downloads. Browser interaction has not yet been independently exercised in this environment; user evaluation is the next gate.
