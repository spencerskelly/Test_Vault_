"""Synthetic source manifest determinism and strict disposition checks."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from source_evidence_contract import ea_envelope,bom_envelope
from source_disposition_manifest import make_manifest,validate,aggregate

class SourceManifestTests(unittest.TestCase):
 def setUp(self):
  self.a=ea_envelope("ea-snapshot","element",{"Object_ID":2,"Name":"Synthetic"})
  self.b=bom_envelope("bom-snapshot","bom_line","Items:3",{"part_number":"Synthetic","quantity":"2"},"synthetic.xlsx","Items",3)
 def test_order_independence(self):
  self.assertEqual(make_manifest([self.a,self.b]),make_manifest([self.b,self.a]))
 def test_cross_source_no_merging(self):
  result=aggregate(make_manifest([self.a,self.b]))
  self.assertEqual(result["total"],2)
  self.assertEqual(result["nativeCertified"],0)
 def test_duplicate_fails(self):
  with self.assertRaisesRegex(ValueError,"DUPLICATE_SOURCE_IDENTITY"):
   make_manifest([self.a,self.a])
 def test_unapproved_disposition_fails(self):
  m=make_manifest([self.a]);m["entries"][0]["disposition"]="accepted_native"
  with self.assertRaisesRegex(ValueError,"INVALID_DISPOSITION"):validate(m)
 def test_missing_reason_fails(self):
  m=make_manifest([self.a]);m["entries"][0]["reason"]=""
  with self.assertRaisesRegex(ValueError,"MISSING_DISPOSITION_REASON"):validate(m)
 def test_aggregate_does_not_expose_identifiers(self):
  result=aggregate(make_manifest([self.a,self.b]))
  self.assertNotIn("Items:3",str(result))
  self.assertNotIn("Synthetic",str(result))
if __name__=="__main__":unittest.main()
