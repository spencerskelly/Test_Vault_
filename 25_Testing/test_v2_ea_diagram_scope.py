"""Fail closed if a V2 golden-import executable depends on EA diagrams.

Only examines active V2 importer, runtime, staging and Workbench sources.
Historical/v1 evidence documents are intentionally outside the executable gate.
"""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
POLICY = ROOT / "26_Definitions/v2_ea_diagram_scope_lock.v0.1.json"
PREFLIGHT = ROOT / "21_Importer/qeax_v2_preflight.py"
SOURCES = [
    ROOT / "21_Importer",
    ROOT / "24_Workbench/registry/runtime",
    ROOT / "20_Base Vault",
    ROOT / "23_Bootstrap",
]
EXTENSIONS = {".py", ".mjs", ".js", ".ts", ".html"}
FORBIDDEN_SQL = re.compile(r"\\bt_diagram(?:objects|links)?\\b", re.I)

class V2DiagramExclusionTests(unittest.TestCase):
    def test_source_tables_and_reopening_gates(self):
        policy = json.loads(POLICY.read_text(encoding="utf-8"))
        self.assertEqual(policy["decision"], "ADR-V2-05")
        self.assertEqual(policy["source_tables"]["allowed"],
                         ["t_object", "t_connector", "t_package"])
        self.assertEqual(set(policy["source_tables"]["excluded"]),
                         {"t_diagram", "t_diagramobjects", "t_diagramlinks"})
        self.assertIn("golden_import_explicitly_accepted", policy["reopen_only_after"])
        self.assertIn("all_planned_tools_implemented_and_tested", policy["reopen_only_after"])

    def test_active_v2_executables_do_not_query_ea_diagram_tables(self):
        violations = []
        for directory in SOURCES:
            for file in directory.rglob("*"):
                if not file.is_file() or file.suffix.lower() not in EXTENSIONS:
                    continue
                if any(part.lower() in {"fixtures", "__pycache__", "testing"} for part in file.relative_to(directory).parts):
                    continue
                text = file.read_text(encoding="utf-8", errors="replace")
                if FORBIDDEN_SQL.search(text):
                    violations.append(file.relative_to(ROOT).as_posix())
        self.assertEqual(violations, [], "EA diagram dependency introduced")

    def test_preflight_no_diagram_requirement(self):
        text = PREFLIGHT.read_text(encoding="utf-8")
        for table in ("t_diagram", "t_diagramobjects", "t_diagramlinks"):
            self.assertNotIn(table, text)
        self.assertIn('"ea_diagrams_in_scope":False', text)

if __name__ == "__main__":
    unittest.main()
