import json, pathlib, sqlite3, tempfile, unittest, sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from verify_phase8_rows_against_qeax import verify_rows,sha
class RowReconciliationTests(unittest.TestCase):
 def setUp(self):
  tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup);p=pathlib.Path(tmp.name)
  self.db=p/'synthetic.qeax';self.ledger=p/'ledger.csv';self.reg=p/'registry.json';self.att=p/'att.json'
  with sqlite3.connect(self.db) as db:
   db.execute('CREATE TABLE t_connector (Connector_ID INTEGER, ea_guid TEXT, Start_Object_ID INTEGER, End_Object_ID INTEGER)')
   db.executemany('INSERT INTO t_connector VALUES(?,?,?,?)',[(1,'synthetic-A',10,20),(2,'synthetic-B',20,30)])
  self.reg.write_text('{}')
  self.att.write_text(json.dumps({'schema':'mdse-phase8-input-attestation/1','source_sha256':sha(self.db),'registry_sha256':sha(self.reg),'native_certified':0}))
  self.ledger.write_text('source_pk,source_guid,raw_from,raw_to,normalized_from,normalized_to\n1,synthetic-A,10,20,10,20\n2,synthetic-B,20,30,20,30\n')
 def check(self):return verify_rows(self.db,self.ledger,self.reg,self.att,2)
 def test_exact_complete_ledger(self):self.assertTrue(self.check()['verified'])
 def test_missing_row(self):
  self.ledger.write_text('source_pk,source_guid,raw_from,raw_to,normalized_from,normalized_to\n1,synthetic-A,10,20,10,20\n')
  self.assertEqual(self.check()['error_counts']['MISSING_LEDGER_ROWS'],1)
 def test_modified_raw_endpoint(self):
  s=self.ledger.read_text().replace('synthetic-B,20,30','synthetic-B,20,99');self.ledger.write_text(s)
  self.assertIn('SOURCE_ROW_MISMATCH',self.check()['error_counts'])
 def test_duplicate_row(self):
  with self.ledger.open('a') as f:f.write('1,synthetic-A,10,20,10,20\n')
  self.assertIn('DUPLICATE_OR_EMPTY_KEY',self.check()['error_counts'])
 def test_unknown_extra_row(self):
  with self.ledger.open('a') as f:f.write('3,synthetic-C,30,40,30,40\n')
  self.assertIn('UNKNOWN_LEDGER_KEY',self.check()['error_counts'])
 def test_stale_source_attestation(self):
  v=json.loads(self.att.read_text());v['source_sha256']='0'*64;self.att.write_text(json.dumps(v))
  self.assertIn('QEAX_HASH_MISMATCH',self.check()['error_counts'])
if __name__=='__main__': unittest.main()
