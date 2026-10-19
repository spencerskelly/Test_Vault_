"""Smoke test two V2-owned custom plugin payloads, independent from the archive."""
import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
PAYLOAD=ROOT/"20_Base Vault/Runtime/Plugins"
class V2CustomPluginPayloads(unittest.TestCase):
 def test_custom_packages_have_local_entrypoints(self):
  for plugin in ("mdse-bootstrap","mdse-workbench"):
   with self.subTest(plugin=plugin):
    folder=PAYLOAD/plugin
    meta=json.loads((folder/"manifest.json").read_text())
    self.assertEqual(meta["id"],plugin)
    self.assertTrue(meta["version"])
    self.assertTrue((folder/"main.js").is_file())
    self.assertGreater((folder/"main.js").stat().st_size,1000)
    self.assertTrue((folder/"styles.css").exists())
 def test_packager_has_no_archive_dependency(self):
  s=(ROOT/"20_Base Vault/stage_v1_verified_plugins_for_v2.py").read_text()
  self.assertNotIn("100_Archive/",s)
if __name__=="__main__":unittest.main()
