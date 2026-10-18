"""Synthetic integrity tests for versioned SysML v2 registry pins."""
import hashlib
import pathlib
import sys
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from verify_sysml_v2_registry_pins import verify

class PinTests(unittest.TestCase):
    def test_matching_file_passes(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d)
            (root/"registry.json").write_bytes(b"synthetic")
            expected=hashlib.sha256(b"synthetic").hexdigest()
            self.assertEqual(verify(root,{"files":{"registry.json":expected}})["status"],"PASS")
    def test_changed_file_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d)
            (root/"registry.json").write_bytes(b"changed")
            expected=hashlib.sha256(b"synthetic").hexdigest()
            self.assertEqual(verify(root,{"files":{"registry.json":expected}})["status"],"BLOCKED")
    def test_missing_file_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(verify(pathlib.Path(d),{"files":{"missing.json":"0"*64}})["status"],"BLOCKED")
    def test_empty_pinset_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(verify(pathlib.Path(d),{"files":{}})["status"],"BLOCKED")

if __name__=="__main__":
    unittest.main()
