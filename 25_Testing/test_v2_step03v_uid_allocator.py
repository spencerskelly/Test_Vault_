import importlib.util,json,sqlite3,tempfile,unittest
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"21_Importer"/"v2_step03v_uid_allocator.py"
spec=importlib.util.spec_from_file_location("uidalloc",p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class UIDTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.root=Path(t.name)
  self.db=self.root/"a.qeax";self.cross=self.root/"in.jsonl";self.out=self.root/"ids.jsonl"
  with sqlite3.connect(self.db) as c:
   c.execute("CREATE TABLE t_object(Object_ID INTEGER, ea_guid TEXT, CreatedDate TEXT, Author TEXT)")
   c.executemany("INSERT INTO t_object VALUES(?,?,?,?)",[(1,"{A}","2026-10-01 12:13:14",""),(2,"{B}","2026-10-01 12:13:14",None),(3,"{C}",None,"")])
 def rows(self,data):
  self.cross.write_text("".join(json.dumps(x)+"\n" for x in data))
 def test_uid_uniqueness_and_hold(self):
  self.rows([{"eaObjectID":1,"eaGUID":"{A}","migrationStatus":"identity_and_placement_pending"},{"eaObjectID":2,"eaGUID":"{B}","migrationStatus":"identity_and_placement_pending"},{"eaObjectID":3,"eaGUID":"{C}","migrationStatus":"folder_mapping_pending"}])
  r=mod.allocate(self.db,self.cross,self.out)
  rec=[json.loads(x) for x in self.out.read_text().splitlines()]
  self.assertEqual(r["uids_allocated"],2)
  self.assertEqual(len({x["uid"] for x in rec[:2]}),2)
  self.assertIsNone(rec[2]["uid"])
 def test_id_mismatch(self):
  self.rows([{"eaObjectID":1,"eaGUID":"wrong","migrationStatus":"identity_and_placement_pending"}])
  with self.assertRaisesRegex(ValueError,"mismatch"):mod.allocate(self.db,self.cross,self.out)
 def test_no_overwrite(self):
  self.rows([{"eaObjectID":1,"eaGUID":"{A}","migrationStatus":"identity_and_placement_pending"}])
  self.out.write_text("safe")
  with self.assertRaisesRegex(ValueError,"exists"):mod.allocate(self.db,self.cross,self.out)
if __name__=="__main__":unittest.main()
