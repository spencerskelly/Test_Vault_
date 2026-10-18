#!/usr/bin/env python3
"""Static safeguards for pre-copy Base Vault checks; run with Python unittest.
These tests do not replace the actual disposable build + hash tamper test.
"""
import ast
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parent.parent
BUILDER=ROOT/"10_Base Vault/Tools/v0.8.0-r2/build-base.py"

class BaseBuilderPreflightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=BUILDER.read_text(encoding="utf-8")
        cls.tree=ast.parse(cls.source,filename=str(BUILDER))
        cls.lines=cls.source.splitlines()

    def location(self, text):
        return next(i for i,s in enumerate(self.lines) if text in s)

    def test_current_manifest_path(self):
        self.assertIn('MANIFEST=os.path.join(ROOT,"10_Base Vault","Definition","mdse-release.yaml")',self.source)
        self.assertNotIn('MANIFEST=os.path.join(ROOT,"Base Vault"',self.source)

    def test_preflight_precedes_output_directory_creation(self):
        preflight=self.location('missing_files=[p for p in required_files')
        hash_guard=self.location('if digest != expected:')
        output=self.location('if os.path.exists(out):')
        self.assertLess(preflight,hash_guard)
        self.assertLess(hash_guard,output)

    def test_hash_check_uses_binary_file_bytes(self):
        self.assertIn('hashlib.sha256(plugin_file.read()).hexdigest()',self.source)
        self.assertIn('if digest != expected:',self.source)
        self.assertIn('BLOCKER plugin SHA256 mismatch:',self.source)

    def test_copy_does_not_touch_input_plugin_sources(self):
        self.assertIn('shutil.copy2(os.path.join(src,n),os.path.join(dst,n))',self.source)
        self.assertIn('Output directory is not empty; refusing to overwrite:',self.source)

    def test_script_parses(self):
        self.assertTrue(isinstance(self.tree,ast.Module))

if __name__=="__main__":
    unittest.main()
