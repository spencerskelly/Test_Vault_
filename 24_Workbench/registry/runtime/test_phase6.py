import json,unittest,tempfile,pathlib,csv
from evidence_contract import validate
from reconcile_fixture import reconcile
P=pathlib.Path(__file__).resolve().parent.parent
R=json.loads((P/'family_disposition_registry.v0.2.json').read_text())
class Phase6Tests(unittest.TestCase):
 def valid(self):return {'family':'Dependency','connectorId':'synthetic','sourceId':'a','targetId':'b','roles':{'orientation':'source-to-target','meaning':'client-to-supplier'},'evidence':{'direction':'source-to-target'}}
 def test_family_count(self):self.assertEqual(len(R['families']),26)
 def test_unique(self):self.assertEqual(len({v['family'] for v in R['families']}),26)
 def test_no_automatic_native_for_new_families(self):self.assertTrue(all(not v['rule_ids'] for v in R['families'] if v['disposition']!='existing_rule'))
 def test_valid(self):self.assertEqual(validate(self.valid()),[])
 def test_direction_conflict(self):
  row=self.valid();row['evidence']['direction']='target-to-source';self.assertIn('DIRECTION_CONFLICT',validate(row))
 def test_unknown(self):
  row=self.valid();row['surprise']=1;self.assertIn('UNKNOWN_SURPRISE',validate(row))
 def test_invalid_orientation(self):
  row=self.valid();row['roles']['orientation']='guess';self.assertIn('INVALID_ORIENTATION',validate(row))
 def test_missing_source(self):
  row=self.valid();del row['sourceId'];self.assertIn('MISSING_SOURCEID',validate(row))
 def test_fixture_summary_only(self):
  with tempfile.TemporaryDirectory() as tmp:
   path=pathlib.Path(tmp)/'synthetic.csv'
   with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['connector_type','connector_stereotype','count']);w.writeheader();w.writerow({'connector_type':'Dependency','connector_stereotype':'','count':7});w.writerow({'connector_type':'UseCase','connector_stereotype':'include','count':2})
   result=reconcile(R,path);self.assertEqual(result['total_connectors'],9);self.assertEqual(result['unknown_families'],[])
if __name__=='__main__':unittest.main()
