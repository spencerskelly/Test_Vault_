"""Synthetic read-only EA cross-table audit fixture."""
import pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from audit_ea_source_references import audit

class SourceReferences(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup)
  self.path=pathlib.Path(t.name)/"synthetic.sqlite"
  c=sqlite3.connect(self.path)
  c.execute("CREATE TABLE t_object (Object_ID INTEGER, Package_ID INTEGER)")
  c.execute("CREATE TABLE t_connector (Start_Object_ID INTEGER, End_Object_ID INTEGER)")
  c.execute("CREATE TABLE t_package (Package_ID INTEGER, Parent_ID INTEGER)")
  c.execute("CREATE TABLE t_objectproperties (Object_ID INTEGER)")
  c.execute("INSERT INTO t_package VALUES (10,0)")
  c.execute("INSERT INTO t_object VALUES (1,10)")
  c.execute("INSERT INTO t_connector VALUES (1,1)")
  c.execute("INSERT INTO t_objectproperties VALUES (1)")
  c.commit();c.close()
 def test_fully_resolved(self):
  r=audit(self.path)
  self.assertEqual(r["unresolvedTotal"],0)
  self.assertEqual(r["status"],"PASS")
  self.assertEqual(r["nativeCertified"],0)
 def test_missing_connector_endpoint_detected(self):
  c=sqlite3.connect(self.path);c.execute("INSERT INTO t_connector VALUES (1,999)");c.commit();c.close()
  r=audit(self.path)
  self.assertEqual(r["unresolvedReferences"]["connector_target_missing"],1)
  self.assertEqual(r["status"],"REVIEW_REQUIRED")
 def test_missing_tag_owner_detected(self):
  c=sqlite3.connect(self.path);c.execute("INSERT INTO t_objectproperties VALUES (999)");c.commit();c.close()
  self.assertEqual(audit(self.path)["unresolvedReferences"]["tag_owner_missing"],1)
 def test_changed_snapshot_has_changed_digest(self):
  before=audit(self.path)["sourceSha256"]
  c=sqlite3.connect(self.path);c.execute("INSERT INTO t_object VALUES (2,10)");c.commit();c.close()
  self.assertNotEqual(before,audit(self.path)["sourceSha256"])
if __name__=="__main__":unittest.main()
