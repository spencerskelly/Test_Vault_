import csv,pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_source_bound_specialization_review import inspect
class SourceBoundTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup)
  p=pathlib.Path(t.name);self.db=p/'synthetic.qeax';self.csv=p/'ledger.csv'
  with sqlite3.connect(self.db) as db:
   db.execute('CREATE TABLE t_connector(Connector_ID INTEGER,ea_guid TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,Direction TEXT,Connector_Type TEXT)')
   db.execute("INSERT INTO t_connector VALUES(1,'synthetic',10,20,'Source -> Destination','Generalization')")
  self.row={'source_pk':'1','source_guid':'synthetic','raw_from':'10','raw_to':'20','family':'Generalization','normalized_from':'10','normalized_to':'20','status':'orientation_normalized'}
  self.nodes=[{'id':'child','sourceId':10,'kind':'PartDefinition'},{'id':'parent','sourceId':20,'kind':'PartDefinition'}]
  self.write()
 def write(self):
  with self.csv.open('w',newline='') as f:
   writer=csv.DictWriter(f,fieldnames=self.row);writer.writeheader();writer.writerow(self.row)
 def runcheck(self):return inspect(self.db,self.csv,{'nodes':self.nodes})
 def test_source_bound_candidate(self):
  r=self.runcheck();self.assertEqual(r['errors'],{});self.assertFalse(r['may_emit_native'])
 def test_tampered_endpoint(self):
  self.row['normalized_from']='20';self.write()
  self.assertIn('NORMALIZATION_DIRECTION_MISMATCH',self.runcheck()['errors'])
 def test_tampered_guid(self):
  self.row['source_guid']='wrong';self.write()
  self.assertIn('RAW_SOURCE_MISMATCH',self.runcheck()['errors'])
 def test_missing_mapping(self):
  self.nodes.pop()
  self.assertIn('CANONICAL_NODE_MAPPING_MISSING',self.runcheck()['errors'])
 def test_usage_rejected(self):
  self.nodes[0]['kind']='PartUsage'
  self.assertIn('DEFINITION_COMPATIBILITY_UNVERIFIED',self.runcheck()['errors'])
 def test_native_never_certified(self):
  self.assertEqual(self.runcheck()['native_certified'],0)
if __name__=='__main__':unittest.main()
