"""Synthetic tests for isolated V2 base; no Obsidian or real EA model needed."""
import importlib.util, pathlib, tempfile, unittest, json
ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("v2_base",ROOT/"20_Base Vault/build_v2_test_base.py")
module=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(module)
class V2BaseTest(unittest.TestCase):
    def test_build_and_no_archive(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=pathlib.Path(tmp)/"Base_V2"
            result=module.build(dest)
            self.assertEqual(result["status"],"PASS")
            self.assertFalse(result["native_import_ready"])
            manifest=json.loads((dest/".mdse_v2_test_base.json").read_text())
            self.assertEqual(manifest["schema"],"mdse-v2-test-base/1")
            self.assertTrue(manifest["files"])
            self.assertFalse(any("100_Archive" in p for p in manifest["files"]))
            self.assertTrue((dest/"99_System/Approved_V2_Translation_Baseline.md").exists())
            with self.assertRaisesRegex(ValueError,"OUTPUT_ALREADY_EXISTS"):module.build(dest)
    def test_disallow_output_in_source(self):
        with self.assertRaisesRegex(ValueError,"NO_BUILD_INSIDE_REPOSITORY"):
            module.build(ROOT/"20_Base Vault"/"improper-generated-output")
if __name__=="__main__":unittest.main()
