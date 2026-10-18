import csv,pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_direction_evidence_gate import check
class DirectionTests(unittest.TestCase):
 def setUp(self):
  d=tempfile.TemporaryDirectory();self.addCleanup(d.cleanup);root=pathlib.Path(d.name)
  self.q=root/'fixture.qeax';self.l=root/'fixture.csv'
  with sqlite3.connect(self.q) as db:
   db.execute('CREATE TABLE t_connector(Connector_ID INTEGER,ea_guid TEXT,Connector_Type TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)')
   db.execute('INSERT INTO t_connector VALUES(1,?,?,?,?,?)',('synthetic','Generalization','Source -> Destination',2,3))
  self.row={'source_pk':'1','source_guid':'synthetic','raw_from':'2','raw_to':'3','source_direction':'Source -> Destination','normalized_from':'2','normalized_to':'3','family':'Generalization','status':'orientation_normalized'}
  self.write()
 def write(self):
  with self.l.open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(self.row));w.writeheader();w.writerow(self.row)
 def test_matching_evidence_only_candidate(self):
  r=check(self.q,self.l,1);self.assertEqual(r['status'],'direction_candidate');self.assertFalse(r['nativeCertified'])
 def test_tampered_orientation_rejected(self):
  self.row['normalized_to']='2';self.write();self.assertEqual(check(self.q,self.l,1)['reason'],'LEDGER_MISMATCH')
 def test_tampered_direction_rejected(self):
  self.row['source_direction']='Unspecified';self.write();self.assertEqual(check(self.q,self.l,1)['reason'],'LEDGER_MISMATCH')
 def test_unqualified_row_rejected(self):
  self.row['status']='deferred_review';self.write();self.assertEqual(check(self.q,self.l,1)['reason'],'LEDGER_NOT_QUALIFIED')
 def test_missing_source_rejected(self):
  self.assertEqual(check(self.q,self.l,42)['reason'],'SOURCE_CARDINALITY')
if __name__=='__main__':unittest.main()
