import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_nested_definition_projection import project
C={"id":"child","ownerId":"parent","kind":"PartDefinition"}
P={"id":"parent","kind":"PartDefinition"}
class ProjectionTests(unittest.TestCase):
 def test_unapproved_stays_review(self):
  r=project(C,P,"Source -> Destination")
  self.assertEqual(r["edges"],[])
  self.assertIn("DEFINITION_INTENT_UNAPPROVED",r["diagnostics"])
 def test_two_edges_separate(self):
  r=project(C,P,"Source -> Destination",True)
  self.assertEqual([x["kind"] for x in r["edges"]],["lexicalContainment","specialization"])
  self.assertFalse(r["nativeCertified"])
 def test_wrong_owner(self):
  self.assertIn("LEXICAL_OWNER_MISMATCH",project({**C,"ownerId":"other"},P,"Source -> Destination",True)["diagnostics"])
 def test_reversed_direction(self):
  self.assertIn("DIRECTION_NOT_VERIFIED",project(C,P,"Destination -> Source",True)["diagnostics"])
 def test_usage_not_definition(self):
  self.assertIn("DEFINITION_KIND_UNVERIFIED",project({**C,"kind":"PartUsage"},P,"Source -> Destination",True)["diagnostics"])
 def test_self_specialization(self):
  self.assertIn("SELF_SPECIALIZATION",project({**C,"id":"parent"},P,"Source -> Destination",True)["diagnostics"])
if __name__=="__main__":unittest.main()
