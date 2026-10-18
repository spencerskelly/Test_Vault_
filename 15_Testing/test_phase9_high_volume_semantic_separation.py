import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_high_volume_semantic_separation import classify
class SeparationTests(unittest.TestCase):
 def test_hardware_candidate(self):self.assertEqual(classify(("Class","Hardware Component"),("Class","Hardware Component")),"SAME_STEREOTYPE_DEFINITION_CANDIDATE")
 def test_signal_candidate(self):self.assertEqual(classify(("Signal","Logical Signal"),("Signal","Logical Signal")),"SAME_STEREOTYPE_DEFINITION_CANDIDATE")
 def test_cross_stereotype_review(self):self.assertEqual(classify(("Class","Hardware Component"),("Class","Module")),"CROSS_STEREOTYPE_OR_KIND_REVIEW")
 def test_usage_source(self):self.assertEqual(classify(("Object",""),("Class","Hardware Component")),"USAGE_OR_OCCURRENCE_REVIEW")
 def test_usage_target(self):self.assertEqual(classify(("Class","Module"),("Part","")),"USAGE_OR_OCCURRENCE_REVIEW")
 def test_out_of_scope(self):self.assertEqual(classify(("Class","System Function"),("Class","System Function")),"OUTSIDE_SCOPE")
if __name__=="__main__":unittest.main()
