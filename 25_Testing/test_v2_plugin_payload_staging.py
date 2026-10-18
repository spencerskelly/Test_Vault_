"""Regression tests for one-time V1 plugin payload staging into V2 ownership."""
import importlib.util,pathlib,tempfile,json,hashlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("staging",ROOT/"20_Base Vault/stage_v1_verified_plugins_for_v2.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class TestStaging(unittest.TestCase):
 def test_staging_is_exact_and_non_overwriting(self):
  with tempfile.TemporaryDirectory() as t:
   target=pathlib.Path(t)/"V2_Plugins"
   a=m.stage(target)
   self.assertEqual(a["status"],"STAGED_NOT_ACTIVATED")
   lock=json.loads((target/"candidate-plugin-lock.json").read_text())
   self.assertEqual(set(lock["plugins"]),set(m.PLUGINS))
   self.assertNotIn("dataview",lock["plugins"])
   for pid,entry in lock["plugins"].items():
    for name,digest in entry["sha256"].items():
     self.assertEqual(hashlib.sha256((target/"plugins"/pid/name).read_bytes()).hexdigest(),digest)
   with self.assertRaisesRegex(ValueError,"DESTINATION_EXISTS"):m.stage(target)
 def test_repo_output_disallowed(self):
  with self.assertRaisesRegex(ValueError,"DESTINATION_INSIDE_REPO"):m.stage(ROOT/"20_Base Vault/unsafe-output")
if __name__=="__main__":unittest.main()
