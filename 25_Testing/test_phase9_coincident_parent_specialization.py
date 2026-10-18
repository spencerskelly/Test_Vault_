import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_coincident_parent_specialization import qualify
C={"Object_ID":1,"ParentID":2,"Object_Type":"Class","Stereotype":"Hardware Component"}
P={"Object_ID":2,"ParentID":0,"Object_Type":"Class","Stereotype":"Hardware Component"}
class Tests(unittest.TestCase):
 def test_coincidence_review(self):self.assertEqual(qualify(C,P,[(1,2,"Source -> Destination")]),"COINCIDENT_PARENT_AND_SUPERTYPE_REVIEW")
 def test_reverse(self):self.assertEqual(qualify(C,P,[(2,1,"Source -> Destination")]),"REVERSE_PARENT_GENERALIZATION_REVIEW")
 def test_missing(self):self.assertEqual(qualify(C,None,[]),"MISSING_CONTEXT_REVIEW")
 def test_wrong_parent(self):self.assertEqual(qualify(C,{**P,"Object_ID":3},[]),"NOT_LEXICAL_PARENT")
 def test_direction(self):self.assertEqual(qualify(C,P,[(1,2,"Unspecified")]),"MULTIPLE_OR_UNVERIFIED_DIRECTION_REVIEW")
 def test_duplicate(self):self.assertEqual(qualify(C,P,[(1,2,"Source -> Destination")]*2),"MULTIPLE_OR_UNVERIFIED_DIRECTION_REVIEW")
 def test_no_edge(self):self.assertEqual(qualify(C,P,[]),"NO_PARENT_GENERALIZATION")
 def test_stereotype(self):self.assertEqual(qualify(C,{**P,"Stereotype":"Module"},[]),"DIFFERENT_STEREOTYPE_REVIEW")
if __name__=="__main__":unittest.main()
