import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from v2_step03e_identity_crosswalk import reconcile

class CrosswalkTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = Path(self.tmp.name) / "test.qeax"
        self.nodes = Path(self.tmp.name) / "nodes.jsonl"
        db = sqlite3.connect(self.db)
        db.execute("CREATE TABLE t_object(Object_ID integer,ea_guid text,Object_Type text)")
        db.executemany("INSERT INTO t_object VALUES(?,?,?)", [(1,"{ABC}","Class"),(2,"{DEF}","Artifact")])
        db.commit()
        db.close()
    def write(self, nodes):
        self.nodes.write_text("".join(json.dumps(item)+"\n" for item in nodes), encoding="utf-8")
    def test_full_match(self):
        self.write([{"id":"n1","eaGUID":"{abc}"},{"id":"n2","eaObjectID":2}])
        self.assertEqual(reconcile(self.db,self.nodes)["status"],"reconciled")
    def test_missing_one(self):
        self.write([{"id":"n1","eaGUID":"ABC"}])
        self.assertEqual([r["object_id"] for r in reconcile(self.db,self.nodes)["source_without_verified_node"]],[2])
    def test_no_guess_from_name(self):
        self.write([{"id":"node","name":"Class"}])
        self.assertEqual(reconcile(self.db,self.nodes)["graph_without_unique_source"][0]["reason"],"no_verified_source_identity")
    def test_duplicate_mapping(self):
        self.write([{"id":"n1","eaGUID":"ABC"},{"id":"n2","eaGUID":"ABC"}])
        self.assertEqual(len(reconcile(self.db,self.nodes)["multiply_represented_source_objects"]),1)
    def test_conflicting_identifiers(self):
        self.write([{"id":"n1","eaGUID":"ABC","eaObjectID":2}])
        self.assertEqual(reconcile(self.db,self.nodes)["graph_without_unique_source"][0]["reason"],"ambiguous")

if __name__ == "__main__":
    unittest.main()
