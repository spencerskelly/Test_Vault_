"""Synthetic parser-stream diagnostic classification tests."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from sysml2_jupyter_fixture_gate import diagnostic_categories
class DiagnosticTests(unittest.TestCase):
 def test_error_marker(self):
  self.assertIn("error_marker",diagnostic_categories("Error: missing terminator"))
 def test_syntax_error(self):
  self.assertIn("syntax_problem",diagnostic_categories("Syntax error near part usage"))
 def test_parser_recovery(self):
  self.assertIn("parser_recovery",diagnostic_categories("mismatched input }"))
 def test_harmless_stream(self):
  self.assertEqual(diagnostic_categories("0 errors found; execution complete"),[])
 def test_empty(self):
  self.assertEqual(diagnostic_categories(None),[])
if __name__=="__main__":unittest.main()
