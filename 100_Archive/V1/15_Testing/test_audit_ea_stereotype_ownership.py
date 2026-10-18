import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit_ea_stereotype_ownership import classify
RULES=[
 {"type":"Class","stereotype":"block","kind":"PartDefinition","status":"provisional_typed"},
 {"type":"Class","stereotype":"Hardware Component","kind":"PartDefinition","status":"candidate_review"},
 {"type":"Activity","stereotype":"*","kind":"ActionDefinition","status":"separate_behavior_review"},
 {"type":"Port","stereotype":"*","kind":None,"status":"distinct_port_classification_review"}]
class TaxonomyTests(unittest.TestCase):
 def test_explicit_hardware(self):
  self.assertEqual(classify("Class","Hardware Component",RULES)["kind"],"PartDefinition")
 def test_unknown_stereotype_is_deferred(self):
  self.assertIsNone(classify("Class","Mystery",RULES))
 def test_activity_not_part(self):
  self.assertEqual(classify("Activity","function",RULES)["kind"],"ActionDefinition")
 def test_port_kept_distinct(self):
  self.assertIsNone(classify("Port","proxy",RULES)["kind"])
if __name__=="__main__":unittest.main()
