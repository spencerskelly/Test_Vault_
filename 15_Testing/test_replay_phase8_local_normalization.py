import csv,json,pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import replay_phase8_local_normalization as replay
class ReplayTests(unittest.TestCase):
 def setUp(self):
  temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);root=pathlib.Path(temp.name)
  self.db=root/"synthetic.qeax";self.ledger=root/"ledger.csv";self.registry=root/"registry.json"
  self.registry.write_text(json.dumps({"families":[]}))
  with sqlite3.connect(self.db) as db:
   db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
   db.executemany("INSERT INTO t_object VALUES(?,?,?)",[(1,"Class","block"),(2,"Class","block")])
   db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,ea_guid TEXT,Connector_Type TEXT,Stereotype TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,SourceIsAggregate INTEGER,DestIsAggregate INTEGER,SourceRole TEXT,DestRole TEXT,SourceCard TEXT,DestCard TEXT)")
   db.execute("INSERT INTO t_connector VALUES(1,?,?,?,?,?,?,?,?,?,?,?,?)",("synthetic-connector","Generalization","","Source -> Destination",1,2,0,0,"","","",""))
   db.row_factory=sqlite3.Row
   src=db.execute("SELECT * FROM t_connector").fetchone()
   predicted=replay.mod.decide(src,("Class","block"),("Class","block"),set())
  self.row={"source_pk":"1","source_guid":"synthetic-connector","raw_from":"1","raw_to":"2","source_direction":"Source -> Destination","source_role":"","target_role":"","source_cardinality":"","target_cardinality":"","source_aggregation_flag":"0","target_aggregation_flag":"0"}
  self.row.update({k:";".join(v) if isinstance(v,list) else str(v) for k,v in predicted.items()})
  self.headers=list(self.row)
  self.write()
 def write(self):
  with self.ledger.open("w",newline="") as f:
   w=csv.DictWriter(f,fieldnames=self.headers);w.writeheader();w.writerow(self.row)
 def result(self):return replay.check(self.db,self.ledger,self.registry)
 def test_exact_replay(self):self.assertTrue(self.result()["valid"])
 def test_changed_direction(self):
  self.row["source_direction"]="Unspecified";self.write()
  self.assertIn("RAW_SOURCE_DIRECTION_MISMATCH",self.result()["error_counts"])
 def test_changed_normalized_role(self):
  self.row["role"]="incorrect";self.write()
  self.assertIn("NORMALIZED_ROLE_MISMATCH",self.result()["error_counts"])
 def test_changed_orientation(self):
  self.row["normalized_from"]="2";self.write()
  self.assertIn("NORMALIZED_NORMALIZED_FROM_MISMATCH",self.result()["error_counts"])
 def test_missing_row(self):
  self.ledger.write_text(",".join(self.headers)+"\n")
  self.assertIn("MISSING_SOURCE_ROWS",self.result()["error_counts"])
 def test_missing_column(self):
  self.headers.remove("diagnostics");self.write()
  self.assertIn("LEDGER_FIELDS_MISSING",self.result()["error_counts"])
if __name__=="__main__":unittest.main()
