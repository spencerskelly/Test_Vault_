import importlib.util,sqlite3,tempfile,unittest
from pathlib import Path
p=Path(__file__).with_name("v2_step03o_attachment_ownership.py")
spec=importlib.util.spec_from_file_location("ownership",p)
tool=importlib.util.module_from_spec(spec);spec.loader.exec_module(tool)

class OwnershipTests(unittest.TestCase):
    def setUp(self):
        d=tempfile.TemporaryDirectory();self.addCleanup(d.cleanup)
        self.db=Path(d.name)/"test.qeax";self.ledger=Path(d.name)/"ledger.jsonl"
        with sqlite3.connect(self.db) as c:
            c.execute("CREATE TABLE t_object(Object_ID INTEGER,ParentID INTEGER,ea_guid TEXT,Object_Type TEXT,Stereotype TEXT,Name TEXT,Package_ID INTEGER)")
            c.executemany("INSERT INTO t_object VALUES(?,?,?,?,?,?,?)",[(1,0,"{a}","Class","","Owner",4),(2,1,"{b}","Artifact","Document","Nested",4),(3,0,"{c}","Artifact","Image","Linked",4),(4,0,"{d}","Artifact","Image","Unlinked",4)])
            c.execute("CREATE TABLE t_connector(Connector_ID INTEGER,Start_Object_ID INTEGER,End_Object_ID INTEGER,Connector_Type TEXT,Stereotype TEXT)")
            c.execute("INSERT INTO t_connector VALUES(100,3,1,?,?)",("Dependency","trace"))
    def test_classification(self):
        r=tool.analyze(self.db,self.ledger)
        self.assertEqual(r["categories"],{"parent_element_candidate":1,"connector_evidence_review":1,"no_element_owner_evidence":1})
        self.assertEqual(r["review_flags_created"],0)
        self.assertEqual(len(self.ledger.read_text().splitlines()),3)
    def test_existing_ledger_safe(self):
        self.ledger.write_text("safe")
        with self.assertRaisesRegex(ValueError,"exists"):tool.analyze(self.db,self.ledger)
        self.assertEqual(self.ledger.read_text(),"safe")
if __name__=="__main__":unittest.main()
