"""Fail-closed original Phase 8 value checks; no model data."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase8_deferred_evidence_compat import EXTENDED_RAW_FIELDS,raw_evidence_values
class EvidenceValues(unittest.TestCase):
 def setUp(self):
  self.row={k:"" for k in EXTENDED_RAW_FIELDS}
  self.row.update(raw_source_type="Class",raw_target_type="Class",source_aggregation_flag="0",target_aggregation_flag="2")
 def test_valid_optional_blanks_not_invented(self):
  r=raw_evidence_values(self.row)
  self.assertEqual(r["status"],"raw_values_present")
  self.assertFalse(r["nativeCertified"])
 def test_missing_endpoint_kind(self):
  self.row["raw_source_type"]=""
  self.assertEqual(raw_evidence_values(self.row)["status"],"review_required")
 def test_bad_aggregation_flag(self):
  self.row["target_aggregation_flag"]="7"
  self.assertIn("INVALID_TARGET_AGGREGATION_FLAG",raw_evidence_values(self.row)["diagnostics"])
 def test_missing_column_blocks(self):
  self.row.pop("raw_target_type")
  self.assertEqual(raw_evidence_values(self.row)["status"],"schema_incomplete")
if __name__=="__main__":unittest.main()
