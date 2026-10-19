import importlib.util
import sqlite3
import tempfile
import unittest
from pathlib import Path

GENERATOR=Path(__file__).resolve().parents[1]/"21_Importer"/"v2_step03s_generate_notes.py"
spec=importlib.util.spec_from_file_location("interim_generator",GENERATOR)
generator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)

class InterimVaultTests(unittest.TestCase):
    def setUp(self):
        t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup)
        self.root=Path(t.name);self.db=self.root/"source.qeax";self.out=self.root/"vault"
        with sqlite3.connect(self.db) as c:
            c.execute("CREATE TABLE t_object(Object_ID INTEGER,ea_guid TEXT,Name TEXT,Alias TEXT,Object_Type TEXT,Stereotype TEXT,Note TEXT,ParentID INTEGER,Package_ID INTEGER)")
            c.executemany("INSERT INTO t_object VALUES(?,?,?,?,?,?,?,?,?)",[
                (1,"{g1}","Owner",None,"Class",None,"hello",0,0),
                (2,"{g2}","Attachment",None,"Artifact","Document",None,1,0),
                (3,"{g3}","Unattached",None,"Artifact","Image",None,0,0)])
            c.execute("CREATE TABLE t_connector(Connector_ID INTEGER,ea_guid TEXT,Name TEXT,Connector_Type TEXT,Stereotype TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,Notes TEXT)")
            c.execute("INSERT INTO t_connector VALUES(10,?,?,?,?,?,?,?)",("{c1}",None,"Dependency","trace",1,2,None))
            c.execute("CREATE TABLE t_document(ElementID TEXT,ElementType TEXT,DocType TEXT)")
    def test_note_graph_and_attachment_index(self):
        result=generator.go(self.db,self.out)
        self.assertEqual((result["source_elements"],result["source_connectors"],result["generated_element_notes"]),(3,1,1))
        self.assertEqual((result["artifacts_total"],result["artifacts_as_separate_notes"],result["artifacts_in_review"]),(2,0,1))
        note=(self.out/"10_Elements"/"EA-1.md").read_text()
        self.assertIn("[[90_Review/Attachment_Ownership|Artifact 2:",note)
        self.assertIn("EA attachment candidate",note)
        self.assertFalse((self.out/"10_Elements"/"EA-2.md").exists())
        self.assertFalse(result["diagram_imported"])
    def test_refuses_overwrite(self):
        self.out.mkdir();(self.out/"sentinel").write_text("safe")
        with self.assertRaisesRegex(ValueError,"new/empty"):
            generator.go(self.db,self.out)
        self.assertEqual((self.out/"sentinel").read_text(),"safe")
    def test_bad_endpoint_rejected(self):
        with sqlite3.connect(self.db) as c:c.execute("UPDATE t_connector SET End_Object_ID=999")
        with self.assertRaisesRegex(ValueError,"endpoint"):
            generator.go(self.db,self.out)
        self.assertFalse(self.out.exists())

if __name__=="__main__":
    unittest.main()
