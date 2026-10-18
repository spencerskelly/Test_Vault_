"""Synthetic GUID and containment integrity tests."""
import pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from audit_ea_identity_containment import audit,parent_audit
class IdentityTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.p=pathlib.Path(self.tmp.name)/"sample.sqlite"
  c=sqlite3.connect(self.p)
  for table,key,parent in (("t_object","Object_ID","ParentID"),("t_package","Package_ID","Parent_ID"),("t_connector","Connector_ID",None)):
   c.execute(f"CREATE TABLE {table} ({key} INTEGER, ea_guid TEXT"+(f", {parent} INTEGER" if parent else "")+")")
  c.execute("INSERT INTO t_package VALUES (10,'P10',0)")
  c.execute("INSERT INTO t_object VALUES (1,'E1',0)")
  c.execute("INSERT INTO t_object VALUES (2,'E2',1)")
  c.execute("INSERT INTO t_connector VALUES (5,'C5')")
  c.commit();c.close()
 def test_valid(self):
  self.assertEqual(audit(self.p)["status"],"PASS")
 def test_cycle_and_self_parent(self):
  a=parent_audit([(1,2),(2,1),(3,3)])
  self.assertEqual(a["parentCycles"],2)
  self.assertEqual(a["selfParentLinks"],1)
 def test_missing_parent(self):
  self.assertEqual(parent_audit([(1,9)])["unresolvedParents"],1)
 def test_duplicate_and_blank_guid(self):
  c=sqlite3.connect(self.p)
  c.execute("INSERT INTO t_object VALUES (3,'E1',0)")
  c.execute("INSERT INTO t_connector VALUES (6,'')")
  c.commit();c.close()
  r=audit(self.p)
  self.assertEqual(r["status"],"REVIEW_REQUIRED")
  self.assertEqual(r["categories"]["element"]["duplicateGuidGroups"],1)
  self.assertEqual(r["categories"]["connector"]["blankGuids"],1)
if __name__=="__main__":unittest.main()
