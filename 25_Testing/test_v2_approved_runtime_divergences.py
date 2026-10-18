"""Validate open, evidence-linked V2 runtime divergence register."""
import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
PATH=ROOT/"26_Definitions/v2_approved_runtime_divergences.v0.1.json"
class RuntimeDivergenceLedgerTests(unittest.TestCase):
 def test_ids_and_traceable_authority(self):
  data=json.loads(PATH.read_text(encoding="utf-8"))
  self.assertEqual(data["schema"],"mdse-v2-implementation-divergence-register/1")
  entries=data["items"]
  self.assertEqual({i["id"] for i in entries},{"DEF-01","DEF-02","DEF-03","DEF-04"})
  self.assertEqual(len(entries),4)
  for item in entries:
   self.assertTrue((ROOT/item["approved"]).is_file())
   self.assertTrue((ROOT/item["runtime"]).is_file())
   self.assertIn(item["status"],("open_review","open_implementation_alignment","implementation_updated_tests_pending","resolved_verified"))
   self.assertTrue(item["required_fixture"])
   if item["status"]=="implementation_updated_tests_pending":
    self.assertTrue((ROOT/item["fix_evidence"]["code"]).is_file())
    self.assertTrue((ROOT/item["fix_evidence"]["test"]).is_file())
    self.assertFalse(item["fix_evidence"]["native_parser_accepted"])
   if item["status"]=="resolved_verified":
    self.fail("A resolved status requires a verified test+commit attestation contract before closure")
if __name__=="__main__": unittest.main()
