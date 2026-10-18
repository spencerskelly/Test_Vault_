"""Synthetic Phase 8 ledger bridge tests; never attest missing EA fields."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase8_deferred_evidence_compat import adapt,aggregate_compatibility,PHASE8_REQUIRED
class CompatibilityTests(unittest.TestCase):
 def setUp(self):
  self.row={k:"synthetic" for k in PHASE8_REQUIRED}
  self.row["status"]="owner_endpoint_identified"
 def test_missing_schema_column_fails(self):
  self.row.pop("raw_to")
  with self.assertRaisesRegex(ValueError,"INVALID_PHASE8_LEDGER_FIELDS"):
   adapt(self.row,"fixture")
 def test_no_imputed_original_direction(self):
  result=adapt(self.row,"fixture")
  self.assertIn("source_direction",result["unattestedFields"])
  self.assertNotIn("source_direction",result)
  self.assertFalse(result["nativeCertified"])
 def test_no_auto_approval(self):
  result=aggregate_compatibility([self.row],"fixture")
  self.assertEqual(result["sourceEvidenceAutoApproved"],0)
  self.assertEqual(result["total"],1)
 def test_missing_snapshot_fails(self):
  with self.assertRaisesRegex(ValueError,"MISSING_SNAPSHOT_ID"):
   adapt(self.row,"")
 def test_review_and_parser_are_required(self):
  r=adapt(self.row,"fixture")
  self.assertIn("parser_result",r["requiredManualEvidence"])
  self.assertIn("reviewer_decision",r["requiredManualEvidence"])
if __name__=="__main__":unittest.main()
