"""Step19 generated Base Vault: positive checks and disposable tamper negatives."""
from __future__ import annotations
import os
import unittest
from contextlib import contextmanager
from pathlib import Path
from step19_generated_base import (
    ROOT, MANIFEST_PATH, LOCK_PATH, CONTROLLED_GUIDE, WORKBENCH_GUIDE,
    MAPPED_GUIDE, EXPECTED_GUIDE_BLOB, EXPECTED_LOCK_BLOB,
    EXPECTED_MANIFEST_BLOB, blob, check_equal, digest, inspect,
)

@contextmanager
def changed_file(path: Path):
    before=path.read_bytes()
    try:
        yield before
    finally:
        path.write_bytes(before)

class Step19GeneratedBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        value=os.environ.get("STEP19_BASE_DIR")
        if not value:
            raise RuntimeError("STEP19_BASE_DIR is required (disposable build path)")
        cls.base=Path(value)
        if not cls.base.is_dir() or ROOT.resolve() == cls.base.resolve():
            raise RuntimeError("Expected separate generated Base directory")
    def test_approved_source_manifest_blob(self):
        self.assertEqual(blob(MANIFEST_PATH.read_bytes()),EXPECTED_MANIFEST_BLOB)
    def test_approved_plugin_lock_blob(self):
        self.assertEqual(blob(LOCK_PATH.read_bytes()),EXPECTED_LOCK_BLOB)
    def test_guide_source_blob(self):
        self.assertEqual(blob(CONTROLLED_GUIDE.read_bytes()),EXPECTED_GUIDE_BLOB)
    def test_w341_both_guides_exact(self):
        check_equal(CONTROLLED_GUIDE.read_bytes(),WORKBENCH_GUIDE.read_bytes(),"W341")
    def test_generated_guide_exact(self):
        check_equal(CONTROLLED_GUIDE.read_bytes(),(self.base/MAPPED_GUIDE).read_bytes(),"generated")
    def test_full_independent_payload_validation(self):
        output=inspect(self.base)
        self.assertTrue(output["userGuideByteExact"])
        self.assertTrue(output["lockByteExact"])
        self.assertEqual(output["pluginCount"],10)
        self.assertGreater(output["pluginFileHashesVerified"],20)
        self.assertEqual(output["vaultUid"],"UNINITIALIZED")
        self.assertFalse(output["guiAcceptancePerformed"])
    def test_generated_output_is_not_a_git_repo(self):
        self.assertFalse((self.base/".git").exists())
    def test_no_qeax_archive_in_generated_output(self):
        self.assertFalse(any(x.suffix.lower()==".qeax" for x in self.base.rglob("*") if x.is_file()))
        self.assertFalse((self.base/"EA_2026_09_06_endgame.qeax.zip").exists())
    def test_workbench_plugin_exact_sha(self):
        import yaml
        lock=yaml.safe_load(LOCK_PATH.read_text(encoding="utf-8"))
        expected=lock["plugins"]["mdse-workbench"]["sha256"]["main.js"]
        self.assertEqual(digest((self.base/".obsidian/plugins/mdse-workbench/main.js").read_bytes()),expected)
    def test_w341_rejects_one_byte_guide_drift_then_restores(self):
        p=self.base/MAPPED_GUIDE
        with changed_file(p) as before:
            p.write_bytes(before+b"test-change")
            with self.assertRaisesRegex(ValueError,"W341 generated guide byte mismatch"):
                inspect(self.base)
        self.assertEqual(p.read_bytes(),before)
        inspect(self.base)
    def test_w342_rejects_plugin_byte_drift_then_restores(self):
        p=self.base/".obsidian/plugins/mdse-workbench/main.js"
        with changed_file(p) as before:
            p.write_bytes(before+b"test-change")
            with self.assertRaisesRegex(ValueError,"SHA-256 differs from pinned plugin lock"):
                inspect(self.base)
        self.assertEqual(p.read_bytes(),before)
        inspect(self.base)
    def test_w341_negative_byte_helper(self):
        with self.assertRaises(ValueError):
            check_equal(b"abc",b"abd","guide")
    def test_sha256_change_detected(self):
        self.assertNotEqual(digest(b"abc"),digest(b"abd"))
    def test_release_pre_release_is_not_gui_acceptance(self):
        report=inspect(self.base)
        self.assertEqual(report["releaseStatus"],"pre-release")
        self.assertFalse(report["guiAcceptancePerformed"])
        self.assertFalse(report["archiveApproved"])
    def test_workspace_docs_absent(self):
        for p in ("00_Workspace","Importer","Base Vault","55_Workbench"):
            with self.subTest(path=p):
                self.assertFalse((self.base/p).exists())

if __name__=="__main__":
    unittest.main()
