import unittest
from v2_flag_fallback import build

class TestFallback(unittest.TestCase):
    def setUp(self):
        self.row=dict(source_pk='1',source_guid='synthetic-guid',family='Aggregation',disposition='flaglink_candidate',reason='synthetic owner ambiguity',raw_from='11',raw_to='12',source_direction='Source -> Destination')
    def test_flaglink(self):
        flags,_=build([self.row])
        self.assertEqual(flags[0]['type'],'flagLink')
        self.assertFalse(flags[0]['nativeSyntax'])
    def test_no_false_flag(self):
        row={**self.row,'disposition':'native_candidate_unverified'}
        flags,_=build([row])
        self.assertEqual(flags,[])
    def test_stable_identity(self):
        self.assertEqual(build([self.row]),build([self.row]))
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):build([self.row,self.row])
    def test_flag_note(self):
        flags,_=build([],[dict(sourceElementId='17',reason='unknown stereotype')])
        self.assertEqual(flags[0]['type'],'flagNote')

if __name__=='__main__':unittest.main()
