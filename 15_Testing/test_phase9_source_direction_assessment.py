import csv,pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_source_direction_assessment import assess
class DirectionTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);p=pathlib.Path(t.name)
  self.db=p/"synthetic.qeax";self.ledger=p/"ledger.csv"
  with sqlite3.connect(self.db) as db:
   db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,ea_guid TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,Direction TEXT,Connector_Type TEXT)")
   db.execute("INSERT INTO t_connector VALUES(1,'synthetic-guid',10,20,'Source -> Destination','Generalization')")
  self.row=dict(source_pk="1",source_guid="synthetic-guid",raw_from="10",raw_to="20",normalized_from="10",normalized_to="20",source_direction="Source -> Destination",family="Generalization")
  self.write()
 def write(self):
  with self.ledger.open("w",newline="") as f:
   w=csv.DictWriter(f,fieldnames=self.row.keys());w.writeheader();w.writerow(self.row)
 def errors(self):return assess(self.db,self.ledger)["error_counts"]
 def test_matching_raw_direction(self):self.assertEqual(self.errors(),{"EXPLICIT_DIRECTION_NOT_PRESENT":0,"MISSING_GENERALIZATIONS":0} if False else {"MISSING_GENERALIZATIONS":0})
 def test_tampered_direction(self):
  self.row["source_direction"]="Unspecified";self.write()
  self.assertIn("SOURCE_EVIDENCE_MISMATCH",self.errors())
 def test_reversed_endpoints(self):
  self.row["normalized_from"]="20";self.write()
  self.assertIn("ORIENTATION_MISMATCH",self.errors())
 def test_missing_row(self):
  self.ledger.write_text(",".join(self.row)+"\n")
  self.assertEqual(self.errors()["MISSING_GENERALIZATIONS"],1)
 def test_semantics_never_certified(self):self.assertFalse(assess(self.db,self.ledger)["direction_semantics_certified"])
if __name__=="__main__":unittest.main()
