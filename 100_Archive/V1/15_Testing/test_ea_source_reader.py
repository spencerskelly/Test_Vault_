"""Synthetic source-only EA adapter tests; no imported model rows."""
import pathlib
import sqlite3
import sys
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from ea_source_reader import COLUMNS,open_source,stream,summarize

class ReaderTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path=pathlib.Path(self.tmp.name)/"test.qeax"
        c=sqlite3.connect(self.path)
        for _,(table,cols) in COLUMNS.items():
            c.execute("CREATE TABLE "+table+" ("+", ".join('"'+n+'" TEXT' for n in cols)+")")
        table,cols=COLUMNS["connectors"]
        values={n:"" for n in cols}
        values.update(Connector_ID="11",ea_guid="synthetic-guid",Connector_Type="Aggregation",
                      Direction="Unspecified",Start_Object_ID="2",End_Object_ID="3",
                      SourceIsAggregate="0",DestIsAggregate="2")
        c.execute("INSERT INTO "+table+" VALUES ("+",".join("?" for _ in cols)+")",[values[n] for n in cols])
        c.commit();c.close()
    def test_counts(self):
        c=open_source(self.path)
        try:self.assertEqual(summarize(c)["connectors"],1)
        finally:c.close()
    def test_preserves_raw_orientation_and_evidence(self):
        c=open_source(self.path)
        try:
            row=next(stream(c,"connectors"))
            self.assertEqual(row["Start_Object_ID"],"2")
            self.assertEqual(row["End_Object_ID"],"3")
            self.assertEqual(row["DestIsAggregate"],"2")
            self.assertEqual(row["Direction"],"Unspecified")
        finally:c.close()
    def test_unknown_category_blocks(self):
        c=open_source(self.path)
        try:
            with self.assertRaises(ValueError):list(stream(c,"unsupported"))
        finally:c.close()
    def test_bad_batch_size_blocks(self):
        c=open_source(self.path)
        try:
            with self.assertRaises(ValueError):list(stream(c,"connectors",0))
        finally:c.close()
    def test_database_open_is_read_only(self):
        c=open_source(self.path)
        try:
            with self.assertRaises(sqlite3.OperationalError):
                c.execute("INSERT INTO t_object DEFAULT VALUES")
        finally:c.close()
if __name__=="__main__":unittest.main()
