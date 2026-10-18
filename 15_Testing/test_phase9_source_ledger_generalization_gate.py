import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_source_ledger_generalization_gate import qualify
def source():return {'Connector_ID':1,'Connector_Type':'Generalization','Start_Object_ID':10,'End_Object_ID':20,'Direction':'Source -> Destination'}
def ledger():return {'source_pk':'1','raw_from':'10','raw_to':'20','normalized_from':'10','normalized_to':'20','family':'Generalization'}
class GateTests(unittest.TestCase):
 def test_consistent_row_is_review_only(self):self.assertEqual(qualify(source(),ledger(),True),'ORIENTATION_REVIEW_CANDIDATE')
 def test_replay_required(self):self.assertEqual(qualify(source(),ledger(),False),'REPLAY_REQUIRED')
 def test_missing_row(self):self.assertEqual(qualify(source(),None,True),'SOURCE_OR_LEDGER_MISSING')
 def test_identity_mismatch(self):
  x=ledger();x['source_pk']='2';self.assertEqual(qualify(source(),x,True),'IDENTITY_MISMATCH')
 def test_endpoint_mismatch(self):
  x=ledger();x['raw_to']='21';self.assertEqual(qualify(source(),x,True),'RAW_ENDPOINT_MISMATCH')
 def test_ambiguous_direction(self):
  x=source();x['Direction']='Unspecified';self.assertEqual(qualify(x,ledger(),True),'DIRECTION_REVIEW')
 def test_orientation_mismatch(self):
  x=ledger();x['normalized_from']='20';self.assertEqual(qualify(source(),x,True),'NORMALIZED_DIRECTION_REVIEW')
 def test_family_mismatch(self):
  x=ledger();x['family']='Aggregation';self.assertEqual(qualify(source(),x,True),'FAMILY_MISMATCH')
if __name__=='__main__':unittest.main()
