"""Synthetic typed aggregation owner candidate decisions."""
import sys,pathlib,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from audit_ea_typed_ownership import classify
class OwnershipTests(unittest.TestCase):
 def setUp(self):
  self.objects={1:("Class","block"),2:("Part",""),3:("Port","proxy"),4:("Activity","")}
  self.row={"Connector_Type":"Aggregation","Start_Object_ID":1,"End_Object_ID":2,
   "Direction":"Source -> Destination","SourceIsAggregate":0,"DestIsAggregate":2}
 def test_candidate_still_not_certified(self):
  self.assertEqual(classify(self.row,self.objects),"typed_composite_owner_candidate")
 def test_shared_stays_review(self):
  self.row["DestIsAggregate"]=1
  self.assertEqual(classify(self.row,self.objects),"shared_or_ambiguous_ownership")
 def test_proxy_port_stays_distinct(self):
  self.row["End_Object_ID"]=3
  self.assertEqual(classify(self.row,self.objects),"port_interface_review")
 def test_invalid_type_stays_review(self):
  self.row["End_Object_ID"]=4
  self.assertEqual(classify(self.row,self.objects),"incompatible_endpoint_kinds")
 def test_direction_requires_evidence(self):
  self.row["Direction"]="Unspecified"
  self.assertEqual(classify(self.row,self.objects),"ownership_direction_review")
 def test_self_reference_rejected(self):
  self.row["End_Object_ID"]=1
  self.assertEqual(classify(self.row,self.objects),"self_reference_review")
if __name__=="__main__":unittest.main()
