"""Synthetic tests for v2 source endpoint type audit."""
import importlib.util, pathlib, sqlite3, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("typed",ROOT/"21_Importer/inspect_v2_source_endpoint_types.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class TestEndpoints(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.db=pathlib.Path(self.tmp.name)/"fixture.qeax"
  with sqlite3.connect(self.db) as db:
   db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT)")
   db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,Connector_Type TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
   db.executemany("INSERT INTO t_object VALUES (?,?)",[(1,"Requirement"),(2,"Activity"),(3,"Port")])
   db.executemany("INSERT INTO t_connector VALUES (?,?,?,?)",[(1,"Dependency",2,1),(2,"Association",3,2),(3,"Generalization",1,99)])
 def test_roles_and_missing(self):
  r=m.inspect(self.db)
  self.assertEqual(r["missing_endpoints"],1)
  self.assertEqual(r["typed_pairs"][1]["ea_start_type"],"Activity")
  self.assertEqual(r["typed_pairs"][1]["ea_end_type"],"Requirement")
  self.assertEqual(r["native_relationships_emitted"],0)
 def test_read_only(self):
  b=self.db.read_bytes();m.inspect(self.db);self.assertEqual(b,self.db.read_bytes())
 def test_limits(self):
  with self.assertRaisesRegex(ValueError,"INVALID_LIMIT"):m.inspect(self.db,0)
  self.assertEqual(m.inspect(self.db,1)["source_connectors"],1)
if __name__=="__main__":unittest.main()
