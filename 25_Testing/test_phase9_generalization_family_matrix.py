import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_generalization_family_matrix import assess,ea_kind
class MatrixTests(unittest.TestCase):
 def test_part(self):self.assertEqual(assess(("Class","block"),("Class","block"),"Source -> Destination"),"SAME_DEFINITION_FAMILY_CANDIDATE:PartDefinition")
 def test_action(self):self.assertEqual(assess(("Activity",""),("Activity",""),"Source -> Destination"),"SAME_DEFINITION_FAMILY_CANDIDATE:ActionDefinition")
 def test_state(self):self.assertEqual(assess(("State",""),("State",""),"Source -> Destination"),"SAME_DEFINITION_FAMILY_CANDIDATE:StateDefinition")
 def test_requirement(self):self.assertEqual(assess(("Requirement",""),("Requirement",""),"Source -> Destination"),"SAME_DEFINITION_FAMILY_CANDIDATE:RequirementDefinition")
 def test_item(self):self.assertEqual(assess(("Signal",""),("InformationItem",""),"Source -> Destination"),"SAME_DEFINITION_FAMILY_CANDIDATE:ItemDefinition")
 def test_port_unresolved(self):self.assertEqual(assess(("Port",""),("Port",""),"Source -> Destination"),"ENDPOINT_KIND_REVIEW")
 def test_usage_not_definition(self):self.assertEqual(assess(("Object",""),("Object",""),"Source -> Destination"),"ENDPOINT_KIND_REVIEW")
 def test_cross_kind(self):self.assertEqual(assess(("Activity",""),("State",""),"Source -> Destination"),"CROSS_KIND_REVIEW")
 def test_reverse_direction(self):self.assertEqual(assess(("Class","block"),("Class","block"),"Destination -> Source"),"DIRECTION_REVIEW")
 def test_stereotyped_connector(self):self.assertEqual(assess(("Class","block"),("Class","block"),"Source -> Destination","custom"),"CONNECTOR_STEREOTYPE_REVIEW")
 def test_unstereotyped_class(self):self.assertEqual(ea_kind("Class",""),"UNRESOLVED")
if __name__=="__main__":unittest.main()
