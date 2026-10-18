import csv,pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_source_direction_bridge import audit
class BridgeTests(unittest.TestCase):
 def setUp(self):
  tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup);p=pathlib.Path(tmp.name)
  self.q=p/'synthetic.qeax';self.ledger=p/'ledger.csv'
  with sqlite3.connect(self.q) as db:
   db.execute('CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)')
   db.executemany('INSERT INTO t_object VALUES(?,?,?)',[(1,'Class','block'),(2,'Class','block')])
   db.execute('CREATE TABLE t_connector(Connector_ID INTEGER,ea_guid TEXT,Connector_Type TEXT,Stereotype TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)')
   db.execute("INSERT INTO t_connector VALUES(1,'synthetic','Generalization','','Source -> Destination',1,2)")
  self.row={'source_pk':'1','source_guid':'synthetic','family':'Generalization','raw_from':'1','raw_to':'2','normalized_from':'1','normalized_to':'2','source_direction':'Source -> Destination','role':'source-subtype-to-destination-supertype','status':'orientation_normalized'}
  self.write()
 def write(self):
  with self.ledger.open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=self.row.keys());w.writeheader();w.writerow(self.row)
 def test_review_only(self):
  r=audit(self.q,self.ledger);self.assertTrue(r['valid']);self.assertEqual(r['categories']['direction_and_family_review_candidate'],1);self.assertFalse(r['may_emit_native'])
 def test_wrong_direction(self):
  self.row['source_direction']='Unspecified';self.write()
  self.assertEqual(audit(self.q,self.ledger)['errors']['RAW_SOURCE_MISMATCH'],1)
 def test_wrong_normalized_endpoint(self):
  self.row['normalized_to']='3';self.write()
  self.assertEqual(audit(self.q,self.ledger)['errors']['NORMALIZED_ENDPOINT_MISMATCH'],1)
 def test_wrong_role(self):
  self.row['role']='other';self.write()
  self.assertEqual(audit(self.q,self.ledger)['errors']['ROLE_OR_FAMILY_MISMATCH'],1)
 def test_missing_ledger_row(self):
  self.ledger.write_text(','.join(self.row.keys())+'\n')
  self.assertEqual(audit(self.q,self.ledger)['errors']['MISSING_LEDGER_ROWS'],1)
 def test_tampered_guid(self):
  self.row['source_guid']='bogus';self.write()
  self.assertEqual(audit(self.q,self.ledger)['errors']['RAW_SOURCE_MISMATCH'],1)
 def test_review_status_not_promoted(self):
  self.row['status']='deferred_review';self.write()
  r=audit(self.q,self.ledger)
  self.assertTrue(r['valid'])
  self.assertEqual(r['categories']['ledger_status_review'],1)
  self.assertNotIn('direction_and_family_review_candidate',r['categories'])
 def test_source_connector_stereotype_review(self):
  with sqlite3.connect(self.q) as db:db.execute("UPDATE t_connector SET Stereotype='special' WHERE Connector_ID=1")
  r=audit(self.q,self.ledger)
  self.assertTrue(r['valid'])
  self.assertEqual(r['categories']['connector_stereotype_review'],1)
  self.assertFalse(r['may_emit_native'])
if __name__=='__main__':unittest.main()
