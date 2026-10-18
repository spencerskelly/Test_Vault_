import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_local_specialization_direction_handoff import assess
class DirectionHandoffTests(unittest.TestCase):
 def setUp(self):
  self.source={"Connector_Type":"Generalization","ea_guid":"synthetic-guid","Start_Object_ID":10,"End_Object_ID":20,"Direction":"Source -> Destination"}
  self.row={"source_guid":"synthetic-guid","raw_from":"10","raw_to":"20","source_direction":"Source -> Destination","normalized_from":"10","normalized_to":"20","family":"Generalization","rule":"GENERALIZE","role":"source-subtype-to-destination-supertype","status":"orientation_normalized"}
 def check(self):return assess(self.row,self.source)
 def test_matching_is_candidate_not_certification(self):self.assertEqual(self.check(),"STRUCTURAL_DIRECTION_CANDIDATE_ONLY")
 def test_missing_source(self):self.assertEqual(assess(self.row,None),"SOURCE_CONNECTOR_MISSING")
 def test_guid_tamper(self):
  self.row["source_guid"]="wrong";self.assertEqual(self.check(),"SOURCE_IDENTITY_MISMATCH")
 def test_raw_endpoint_tamper(self):
  self.row["raw_to"]="30";self.assertEqual(self.check(),"RAW_ENDPOINT_MISMATCH")
 def test_source_direction_unverified(self):
  self.source["Direction"]="Unspecified";self.assertEqual(self.check(),"SOURCE_DIRECTION_UNVERIFIED")
 def test_normalized_reversal(self):
  self.row["normalized_from"]="20";self.assertEqual(self.check(),"NORMALIZED_ENDPOINT_MISMATCH")
 def test_role_tamper(self):
  self.row["role"]="unknown";self.assertEqual(self.check(),"NORMALIZED_ROLE_UNVERIFIED")
 def test_review_not_promoted(self):
  self.row["status"]="deferred_review";self.assertEqual(self.check(),"REVIEW_STATUS")
if __name__=="__main__":unittest.main()
