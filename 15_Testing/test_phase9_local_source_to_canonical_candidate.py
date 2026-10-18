import unittest,sys,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_local_source_to_canonical_candidate import candidate
def fixtures():
 s=dict(Connector_ID=5,ea_guid='synthetic',Connector_Type='Generalization',Stereotype='',Direction='Source -> Destination',Start_Object_ID=1,End_Object_ID=2)
 l=dict(source_pk='5',source_guid='synthetic',raw_from='1',raw_to='2',normalized_from='1',normalized_to='2',role='source-subtype-to-destination-supertype',status='orientation_normalized',diagnostics='NATIVE_PARSER_AND_EVIDENCE_PENDING')
 nodes={'1':{'id':'child','kind':'PartDefinition'},'2':{'id':'parent','kind':'PartDefinition'}}
 return s,l,nodes
class BridgeTests(unittest.TestCase):
 def test_candidate_remains_uncertified(self):
  r=candidate(*fixtures());self.assertEqual(r['status'],'candidate');self.assertFalse(r['native_certified'])
 def test_direction_rejected(self):
  s,l,n=fixtures();s['Direction']='Unspecified';self.assertIn('EA_DIRECTION_NOT_EXPLICIT',candidate(s,l,n)['diagnostics'])
 def test_identity_rejected(self):
  s,l,n=fixtures();l['source_guid']='wrong';self.assertIn('SOURCE_LEDGER_IDENTITY_MISMATCH',candidate(s,l,n)['diagnostics'])
 def test_reversal_rejected(self):
  s,l,n=fixtures();l['normalized_from']='2';self.assertIn('LEDGER_DIRECTION_MISMATCH',candidate(s,l,n)['diagnostics'])
 def test_usage_rejected(self):
  s,l,n=fixtures();n['1']['kind']='PartUsage';self.assertIn('INCOMPATIBLE_CANONICAL_DEFINITION',candidate(s,l,n)['diagnostics'])
if __name__=='__main__':unittest.main()
