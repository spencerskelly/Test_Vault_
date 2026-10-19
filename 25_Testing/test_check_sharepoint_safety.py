import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check_sharepoint_safety as sp  # noqa: E402


def make(root, rels):
    for r in rels:
        p = root / r
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("x", encoding="utf-8")


class SharePointSafety(unittest.TestCase):
    def run_scan(self, rels, **kw):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            make(root, rels)
            return sp.scan(root, **kw)

    def reasons(self, r):
        return " | ".join(w for _, w in r["blocking"])

    def test_clean_vault_has_no_findings(self):
        r = self.run_scan(["10_Model/Charger/Charger.md", "99_System/AI.md"])
        self.assertEqual(r["blocking"], [])

    def test_invalid_characters_and_names(self):
        self.assertIn("invalid character", self.reasons(self.run_scan(["a/Port: CAN.md"])))
        self.assertIn("starts with ~$", self.reasons(self.run_scan(["a/~$lock.docx"])))
        self.assertIn("contains _vti_", self.reasons(self.run_scan(["a/x_vti_y.md"])))

    def test_trailing_space_in_a_folder_name(self):
        self.assertIn("leading or trailing space", self.reasons(self.run_scan(["pad /f.md"])))

    def test_reserved_names(self):
        self.assertIn("reserved name", self.reasons(self.run_scan(["a/CON.md"])))
        self.assertIn("reserved name", self.reasons(self.run_scan(["a/desktop.ini"])))

    def test_forms_at_library_root_only(self):
        self.assertIn("forms", self.reasons(self.run_scan(["Forms/x.md"])))
        self.assertEqual(self.run_scan(["a/Forms/x.md"])["blocking"], [])

    def test_path_limit_counts_the_leading_slash(self):
        name = "n" * 20 + ".md"
        self.assertEqual(self.run_scan([f"{name}"], path_limit=len(name) + 1)["blocking"], [])
        self.assertIn("SharePoint limit", self.reasons(self.run_scan([f"{name}"], path_limit=len(name))))

    def test_sync_root_is_added_to_the_520_limit(self):
        rel = "d/" + "n" * 100 + ".md"
        self.assertEqual(self.run_scan([rel], sync_root_length=100)["blocking"], [])
        self.assertIn("limit 520", self.reasons(self.run_scan([rel], sync_root_length=500)))

    def test_case_insensitive_collisions(self):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            make(root, ["a/Charger.md", "a/charger.md"])
            names = {p.name for p in (root / "a").iterdir()}
            if len(names) == 2:  # case-sensitive filesystem
                self.assertIn("collision", self.reasons(sp.scan(root)))

    def test_long_segment(self):
        # Linux cannot create a >255-byte name, so test the segment check directly.
        self.assertTrue(any("limit 255" in p for p in sp.segment_problems("n" * 260)))
        self.assertEqual(sp.segment_problems("n" * 255), [])


if __name__ == "__main__":
    unittest.main()
