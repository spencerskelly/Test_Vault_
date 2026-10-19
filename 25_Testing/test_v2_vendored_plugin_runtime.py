"""Verify independent V2 plugin payloads and the pinned lock; no archive access."""
import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
PAYLOAD=ROOT/"20_Base Vault/Runtime/Plugins"
class V2VendorSmoke(unittest.TestCase):
 def test_owned_payloads(self):
  lock=json.loads((PAYLOAD/"plugin-lock.v2.json").read_text(encoding="utf-8"))
  self.assertEqual(lock["schema"],"mdse-v2-vendored-plugin-lock/1")
  self.assertEqual(len(lock["plugins"]),7)
  self.assertEqual(lock["status"],"unverified_v2_runtime")
  for name,entry in lock["plugins"].items():
   folder=PAYLOAD/name
   self.assertTrue((folder/"main.js").is_file())
   manifest=json.loads((folder/"manifest.json").read_text(encoding="utf-8"))
   self.assertEqual(manifest["id"],name)
   self.assertEqual(manifest["version"],entry["version"])
   for fn,digest in entry["sha256"].items():
    self.assertEqual(hashlib.sha256((folder/fn).read_bytes()).hexdigest(),digest)
 def test_no_archive_runtime_path(self):
  f=ROOT/"20_Base Vault/stage_v1_verified_plugins_for_v2.py"
  self.assertNotIn("100_Archive/",f.read_text(encoding="utf-8"))
if __name__=="__main__":unittest.main()
