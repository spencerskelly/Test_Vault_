import unittest
from phase8_deferred_evidence_compat import raw_evidence_coverage, EXTENDED_RAW_FIELDS

class EvidenceTests(unittest.TestCase):
    def test_all_fields_present(self):
        row={field:'synthetic' for field in EXTENDED_RAW_FIELDS}
        self.assertEqual(raw_evidence_coverage(row)['status'],'raw_fields_retained')
    def test_missing_fields_detected(self):
        self.assertEqual(raw_evidence_coverage({})['status'],'schema_incomplete')

if __name__=='__main__': unittest.main()
