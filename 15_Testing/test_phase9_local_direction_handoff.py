import csv,pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_local_direction_handoff import examine

class LocalDirectionTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);p=pathlib.Path(t.name)
  self.db=p/"synthetic.qeax";self.csv=p/"ledger.csv"
  with sqlite3.connect(self.db) as db:
   db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,ea_guid TEXT,Connector_Type TEXT,Stereotype TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
   db.execute("INSERT INTO t_connector VALUES(1,'test-guid','Generalization','','Source -> Destination',10,20)")
  self.row=dict(source_pk="1",source_guid="test-guid",family="Generalization",raw_from="10",raw_to="20",normalized_from="10",normalized_to="20",status="orientation_normalized")
  self.write()
 def write(self):
  with self.csv.open("w",newline="") as f:
   w=csv.DictWriter(f,fieldnames=self.row.keys());w.writeheader();w.writerow(self.row)
 def counts(self):return examine(self.db,self.csv)["counts"]
 def test_direction_candidate_not_certification(self):
  r=examine(self.db,self.csv)
  self.assertEqual(r["counts"]["SOURCE_DIRECTION_MATCH_CANDIDATE_ONLY"],1)
  self.assertFalse(r["canonical_mutation_authorized"])
  self.assertEqual(r["native_certified"],0)
 def test_reversed_normalized_endpoints(self):
  self.row["normalized_from"]="20";self.write()
  self.assertEqual(self.counts()["NORMALIZED_ORIENTATION_MISMATCH"],1)
 def test_forged_source_guid(self):
  self.row["source_guid"]="wrong";self.write()
  self.assertEqual(self.counts()["SOURCE_MISMATCH"],1)
 def test_disposition_cannot_promote(self):
  self.row["status"]="role_normalized";self.write()
  self.assertEqual(self.counts()["UNQUALIFIED_LEDGER_DISPOSITION"],1)
 def test_source_direction_override_rejected(self):
  with sqlite3.connect(self.db) as db:db.execute("UPDATE t_connector SET Direction='Unspecified'")
  self.assertEqual(self.counts()["DIRECTION_OR_STEREOTYPE_REVIEW"],1)
 def test_missing_rows_detected(self):
  self.csv.write_text(",".join(self.row)+"\n")
  self.assertEqual(self.counts()["missing_ledger_rows"],1)
if __name__=="__main__":unittest.main()
