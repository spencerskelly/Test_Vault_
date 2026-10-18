import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_generalization_structural_risk_screen import assess,cycles
H=("Class","Hardware Component")
def e(a,b,d="Source -> Destination",s=""):return (a,b,H,H,d,s)
class StructuralRiskTests(unittest.TestCase):
 def test_acyclic(self):self.assertFalse(cycles([("a","b"),("b","c")]))
 def test_direct_cycle(self):self.assertTrue(cycles([("a","b"),("b","a")]))
 def test_transitive_cycle(self):self.assertTrue(cycles([("a","b"),("b","c"),("c","a")]))
 def test_candidate_count(self):self.assertEqual(assess([e("a","b")])["counts"]["screened_candidates"],1)
 def test_self_link(self):self.assertEqual(assess([e("a","a")])["counts"]["self_generalization"],1)
 def test_direction_review(self):self.assertEqual(assess([e("a","b","Unspecified")])["counts"]["direction_unverified"],1)
 def test_connector_stereotype(self):self.assertEqual(assess([e("a","b",s="custom")])["counts"]["connector_stereotype_review"],1)
 def test_no_native_certification(self):self.assertEqual(assess([e("a","b")])["native_certified"],0)
 def test_usage_excluded(self):
  self.assertEqual(assess([("a","b",("Object",""),H,"Source -> Destination","")])["counts"].get("screened_candidates",0),0)
if __name__=="__main__":unittest.main()
