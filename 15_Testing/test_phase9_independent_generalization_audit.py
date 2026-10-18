import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_independent_generalization_audit import decision
def conn(**kw):
    return {"Connector_Type":"Generalization","Stereotype":"","Direction":"Source -> Destination",**kw}
class IndependentGeneralizationTests(unittest.TestCase):
    def test_block_candidate(self):
        self.assertEqual(decision(conn(),("Class","block"),("Class","block")),"ORIENTATION_AND_BLOCK_KINDS_CANDIDATE")
    def test_ambiguous_direction_rejected(self):
        c=conn();c["Direction"]="Unspecified"
        self.assertEqual(decision(c,("Class","block"),("Class","block")),"DIRECTION_UNVERIFIED")
    def test_reverse_direction_rejected(self):
        c=conn();c["Direction"]="Destination -> Source"
        self.assertEqual(decision(c,("Class","block"),("Class","block")),"DIRECTION_UNVERIFIED")
    def test_unsupported_endpoint(self):
        self.assertEqual(decision(conn(),("Activity",""),("Class","block")),"ENDPOINT_SEMANTICS_REVIEW")
    def test_unstereotyped_class_not_inferred(self):
        self.assertEqual(decision(conn(),("Class",""),("Class","")),"ENDPOINT_SEMANTICS_REVIEW")
    def test_missing_endpoint(self):
        self.assertEqual(decision(conn(),None,("Class","block")),"MISSING_ENDPOINT")
    def test_stereotyped_connector_review(self):
        c=conn();c["Stereotype"]="special"
        self.assertEqual(decision(c,("Class","block"),("Class","block")),"STEREOTYPED_GENERALIZATION_REVIEW")
    def test_other_family(self):
        c=conn();c["Connector_Type"]="Aggregation"
        self.assertEqual(decision(c,("Class","block"),("Class","block")),"NOT_GENERALIZATION")
if __name__=="__main__":unittest.main()
