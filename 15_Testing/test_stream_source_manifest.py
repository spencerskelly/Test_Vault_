"""Synthetic atomic EA manifest tests (no proprietary source rows)."""
import json,pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from stream_source_manifest import write_manifest,TABLES
class StreamManifestTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.root=pathlib.Path(self.tmp.name)
  self.db=self.root/"source.sqlite";self.out=self.root/"manifest.jsonl"
  c=sqlite3.connect(self.db)
  for table,key in TABLES.values():
   c.execute(f"CREATE TABLE {table} ({key} INTEGER PRIMARY KEY, ea_guid TEXT)")
  c.execute("INSERT INTO t_object VALUES (1,'synthetic')");c.commit();c.close()
 def test_valid_manifest(self):
  result=write_manifest(self.db,"fixture",self.out)
  self.assertEqual(result["total"],1)
  self.assertEqual(result["nativeCertified"],0)
  rows=[json.loads(x) for x in self.out.read_text().splitlines()]
  self.assertEqual(rows[0]["disposition"],"uninterpreted")
 def test_existing_destination_is_refused(self):
  self.out.write_text("unchanged")
  with self.assertRaisesRegex(ValueError,"DESTINATION_EXISTS"):
   write_manifest(self.db,"fixture",self.out)
  self.assertEqual(self.out.read_text(),"unchanged")
 def test_duplicate_source_id_fails_cleanly(self):
  c=sqlite3.connect(self.db)
  c.execute("DROP TABLE t_object")
  c.execute("CREATE TABLE t_object (Object_ID INTEGER, ea_guid TEXT)")
  c.executemany("INSERT INTO t_object VALUES (?,?)",[(1,"a"),(1,"b")])
  c.commit();c.close()
  with self.assertRaisesRegex(ValueError,"INVALID_OR_DUPLICATE_ID"):
   write_manifest(self.db,"fixture",self.out)
  self.assertFalse(self.out.exists())
  self.assertFalse(list(self.root.glob(".source-manifest-*")))
 def test_missing_snapshot_refused(self):
  with self.assertRaisesRegex(ValueError,"MISSING_SNAPSHOT_ID"):
   write_manifest(self.db,"",self.out)
if __name__=="__main__":unittest.main()
