import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "26_Definitions/tools/audit_note_backlinks.py"
SPEC = importlib.util.spec_from_file_location("note_audit", SCRIPT)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

class NoteAuditTest(unittest.TestCase):
    def test_duplicate_and_references(self):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            files = ["source.md", "copy.md", "caller.md"]
            for name, body in zip(files, ["# source", "# source", "[[source]] source.md"]):
                (root/name).write_text(body)
            before = [(root/p).read_bytes() for p in files]
            result = mod.scan(root, "source.md", [pathlib.Path(x) for x in files])
            self.assertEqual(result["identical_content_candidates"], ["copy.md"])
            self.assertEqual(len(result["explicit_inbound_references"]), 1)
            self.assertEqual(result["status"], "REVIEW_REQUIRED_NO_AUTOMATIC_MUTATION")
            self.assertEqual(before, [(root/p).read_bytes() for p in files])

if __name__ == "__main__":
    unittest.main()
