"""Synthetic neutral source-evidence contract tests."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from source_evidence_contract import ea_envelope,bom_envelope,envelope

class EvidenceContractTests(unittest.TestCase):
 def test_ea_keeps_original_orientation(self):
  e=ea_envelope("synthetic-snapshot","connector",{"Connector_ID":7,"ea_guid":"synthetic","Start_Object_ID":2,"End_Object_ID":3})
  self.assertEqual(e.source_kind,"EA")
  self.assertEqual(e.raw["Start_Object_ID"],2)
  self.assertEqual(e.provenance["source_pk"],7)
 def test_bom_keeps_source_row_and_workbook_identity(self):
  e=bom_envelope("synthetic-bom","bom_line","row-5",{"Part":"P-01","Quantity":3},"synthetic.xlsx","Bill",5)
  self.assertEqual(e.source_kind,"BOM")
  self.assertEqual(e.provenance["row_number"],5)
  self.assertEqual(e.disposition,"uninterpreted")
 def test_no_namespace_collision(self):
  a=ea_envelope("same-snapshot","element",{"Object_ID":1})
  b=bom_envelope("same-snapshot","part","1",{"Part":"1"},"test.xlsx","Items",1)
  self.assertNotEqual((a.source_kind,a.record_kind,a.source_key),(b.source_kind,b.record_kind,b.source_key))
 def test_preapproved_semantics_rejected(self):
  with self.assertRaises(ValueError):
   envelope("EA","test","element","1",{},{}).__class__("EA","test","element","1",{},{},"accepted_native").validate()
 def test_missing_bom_lineage_rejected(self):
  with self.assertRaises(ValueError):
   bom_envelope("test","part","x",{},"","Items",1)
 def test_cross_source_record_kind_rejected(self):
  with self.assertRaises(ValueError):
   envelope("BOM","s","connector","1",{},{})

if __name__=="__main__": unittest.main()
