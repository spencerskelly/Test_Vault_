import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_generalization_family_matrix import assess,ea_kind
class HighVolumeTests(unittest.TestCase):
 def test_hardware_component_review(self):
  self.assertEqual(assess(("Class","Hardware Component"),("Class","Hardware Component"),"Source -> Destination"),"STEREOTYPE_MAPPING_REVIEW:PartDefinition")
 def test_physical_component_review(self):
  self.assertEqual(assess(("Class","Physical Component"),("Class","Physical Component"),"Source -> Destination"),"STEREOTYPE_MAPPING_REVIEW:PartDefinition")
 def test_module_review(self):
  self.assertEqual(assess(("Class","Module"),("Class","Module"),"Source -> Destination"),"STEREOTYPE_MAPPING_REVIEW:PartDefinition")
 def test_logical_signal_review(self):
  self.assertEqual(assess(("Signal","Logical Signal"),("Signal","Logical Signal"),"Source -> Destination"),"STEREOTYPE_MAPPING_REVIEW:ItemDefinition")
 def test_cross_family_rejected(self):
  self.assertEqual(assess(("Class","Hardware Component"),("Signal","Logical Signal"),"Source -> Destination"),"CROSS_KIND_REVIEW")
 def test_direction_rejected(self):
  self.assertEqual(assess(("Class","Module"),("Class","Module"),"Unspecified"),"DIRECTION_REVIEW")
 def test_usage_not_promoted(self):
  self.assertEqual(ea_kind("Object","Hardware Component"),"UNRESOLVED")
 def test_unmapped_stereotype_review(self):
  self.assertEqual(assess(("Class","System State"),("Class","System State"),"Source -> Destination"),"ENDPOINT_KIND_REVIEW")
if __name__=="__main__":unittest.main()
