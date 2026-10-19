import json, sqlite3, tempfile, unittest
from pathlib import Path
from v2_step03h_raw_graph_export import export

class RawGraphExportTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.db=Path(self.temp.name)/'input.qeax'; self.output=Path(self.temp.name)/'output'
        with sqlite3.connect(self.db) as c:
            c.execute('CREATE TABLE t_object(Object_ID INTEGER, ea_guid TEXT, Name TEXT, Object_Type TEXT, Stereotype TEXT, Note TEXT)')
            c.execute('CREATE TABLE t_connector(Connector_ID INTEGER,ea_guid TEXT, Start_Object_ID INTEGER, End_Object_ID INTEGER, Connector_Type TEXT, Stereotype TEXT, Notes TEXT)')
            c.executemany('INSERT INTO t_object VALUES(?,?,?,?,?,?)',[(1,'{a}','Alpha','Class','','note'),(2,'{b}','Beta','Artifact','','')])
            c.execute('INSERT INTO t_connector VALUES(1,?,?,?,?,?,?)',('{c}',1,2,'Association','','edge note'))
    def test_counts_and_source_data(self):
        result=export(self.db,self.output)
        self.assertEqual((result['source_objects'],result['source_connectors']),(2,1))
        nodes=[json.loads(s) for s in (self.output/'nodes.jsonl').read_text().splitlines()]
        edge=json.loads((self.output/'edges.jsonl').read_text().strip())
        self.assertEqual(nodes[0]['source']['row']['Note'],'note')
        self.assertEqual(edge['sourceData']['row']['Notes'],'edge note')
        self.assertEqual((edge['source'],edge['target']),('1','2'))
    def test_missing_endpoint_fails(self):
        with sqlite3.connect(self.db) as c:c.execute('UPDATE t_connector SET End_Object_ID=99')
        with self.assertRaisesRegex(ValueError,'Broken connector'):export(self.db,self.output)
    def test_nonempty_output_protected(self):
        self.output.mkdir();(self.output/'keep.txt').write_text('keep')
        with self.assertRaisesRegex(ValueError,'empty'):export(self.db,self.output)
    def test_duplicate_object_fails(self):
        with sqlite3.connect(self.db) as c:c.execute('INSERT INTO t_object VALUES(1,?,?,?,?,?)',('{d}','Duplicate','Class','',''))
        with self.assertRaisesRegex(ValueError,'duplicate'):export(self.db,self.output)

if __name__=='__main__':unittest.main()
