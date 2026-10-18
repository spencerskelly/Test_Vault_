"""Synthetic tests for read-only V2 QEAX slice selection."""
import importlib.util, pathlib, sqlite3, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("review_slice",ROOT/"21_Importer/review_v2_qeax_slice.py")
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
class SliceTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.p=pathlib.Path(t.name)/"synthetic.qeax"
  with sqlite3.connect(self.p) as db:
   db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Name TEXT,ea_guid TEXT)")
   db.executemany("INSERT INTO t_object VALUES(?,?,?,?)",[(1,"Class","A","a"),(2,"Class","B","b"),(3,"Class","C","c")])
   db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
   db.executemany("INSERT INTO t_connector VALUES(?,?,?)",[(10,1,2),(11,2,3)])
 def test_internal_and_boundary(self):
  x=module.collect(self.p,2)
  self.assertEqual(x["selected_elements"],2)
  self.assertEqual(x["internal_connectors_review_required"],1)
  self.assertEqual(x["boundary_connectors_review_required"],1)
  self.assertEqual(x["native_relationships_emitted"],0)
 def test_limit_guard(self):
  with self.assertRaisesRegex(ValueError,"LIMIT_OUT_OF_RANGE"):module.collect(self.p,101)
 def test_repeatable(self):
  self.assertEqual(module.collect(self.p,2),module.collect(self.p,2))
if __name__=="__main__":unittest.main()
