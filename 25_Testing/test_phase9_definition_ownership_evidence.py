import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_definition_ownership_evidence import evaluate,present
class EvidenceTests(unittest.TestCase):
 def test_empty_classifier(self):self.assertFalse(present(0))
 def test_string_zero(self):self.assertFalse(present("0"))
 def test_guid(self):self.assertTrue(present("synthetic-guid"))
 def test_absent_fields(self):
  a={"Classifier":0,"Classifier_guid":"","ParentID":0,"IsSpec":0,"Abstract":0}
  result=evaluate([(a,a)])
  self.assertEqual(result["counts"],{"candidate_edges":1})
  self.assertEqual(result["native_certified"],0)
 def test_source_parent_only(self):
  a={"Classifier":0,"Classifier_guid":"","ParentID":5,"IsSpec":0,"Abstract":0}
  b={"Classifier":0,"Classifier_guid":"","ParentID":0,"IsSpec":0,"Abstract":0}
  self.assertEqual(evaluate([(a,b)])["counts"]["source_ParentID_populated"],1)
 def test_classifier_is_not_auto_certification(self):
  a={"Classifier":23,"Classifier_guid":"synthetic","ParentID":0,"IsSpec":1,"Abstract":0}
  r=evaluate([(a,a)])
  self.assertEqual(r["counts"]["source_Classifier_populated"],1)
  self.assertEqual(r["native_certified"],0)
if __name__=="__main__":unittest.main()
