"""Synthetic evidence-only shared ingestion tests."""
import pathlib
import sys
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from source_evidence_contract import ea_envelope,bom_envelope
from shared_source_ingestion import identity,audit,ingest_ea

class SharedIngestionTests(unittest.TestCase):
    def test_matching_source_keys_remain_distinct(self):
        e=ea_envelope("s","element",{"Object_ID":1,"Name":"Part X"})
        b=bom_envelope("s","part","1",{"part_number":"Part X"},"synthetic.xlsx","BOM",2)
        self.assertNotEqual(identity(e),identity(b))
        self.assertEqual(audit([e,b])["status"],"PASS")
        self.assertEqual(audit([e,b])["recordCount"],2)

    def test_duplicate_source_identity_blocks(self):
        e=ea_envelope("s","element",{"Object_ID":1})
        report=audit([e,e])
        self.assertEqual(report["status"],"BLOCKED")
        self.assertEqual(report["duplicateSourceIdentities"],1)

    def test_aggregate_does_not_disclose_source_fields(self):
        e=ea_envelope("s","element",{"Object_ID":42,"Name":"synthetic-private"})
        report=audit([e])
        self.assertNotIn("synthetic-private",str(report))
        self.assertNotIn("42",str(report))
        self.assertEqual(report["nativeCertified"],0)

    def test_invalid_ea_category_is_rejected(self):
        with self.assertRaises(ValueError):
            list(ingest_ea("/nonexistent","snapshot",categories=["not_known"]))

    def test_missing_snapshot_rejected(self):
        with self.assertRaises(ValueError):
            list(ingest_ea("/nonexistent","",categories=["elements"]))

if __name__=="__main__":unittest.main()
