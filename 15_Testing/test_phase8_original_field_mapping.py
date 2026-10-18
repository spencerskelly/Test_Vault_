"""Synthetic tests for original-field name mapping and evidence value sufficiency."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase8_deferred_evidence_compat import adapt,PHASE8_REQUIRED
class OriginalEvidence(unittest.TestCase):
 def setUp(self):
  self.row={k:"synthetic" for k in PHASE8_REQUIRED}
  self.row["raw_source_type"]="Class"
  self.row["raw_source_stereotype"]="Hardware Component"
  self.row["source_direction"]="Source -> Destination"
  self.row["source_role"]=""
  self.row["target_role"]=""
 def test_original_type_and_stereotype_are_recognized(self):
  result=adapt(self.row,"fixture")
  self.assertNotIn("source_type",result["unattestedFields"])
  self.assertNotIn("source_stereotype",result["unattestedFields"])
 def test_blank_optional_roles_remain_unattested(self):
  result=adapt(self.row,"fixture")
  self.assertIn("source_role",result["unattestedFields"])
  self.assertIn("target_role",result["unattestedFields"])
  self.assertFalse(result["nativeCertified"])
 def test_semantic_assertion_not_fabricated(self):
  self.assertIn("source_semantic_assertion",adapt(self.row,"fixture")["unattestedFields"])
 def test_missing_original_kind_reports_source_type(self):
  self.row.pop("raw_source_type")
  self.assertIn("source_type",adapt(self.row,"fixture")["unattestedFields"])
if __name__=="__main__":unittest.main()
