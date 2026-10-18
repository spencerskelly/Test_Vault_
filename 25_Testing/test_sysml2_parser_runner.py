"""Synthetic parser-command execution tests; no native SysML parser assumed."""
import pathlib
import sys
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from sysml2_parser_runner import run_parser

class ParserRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.fixture=pathlib.Path(self.temp.name)/"test.sysml"
        self.fixture.write_text("package Example {}")
    def test_success_is_not_certification(self):
        report=run_parser(self.fixture,[sys.executable,"-c","import sys;sys.exit(0)","{fixture}"])
        self.assertEqual(report["status"],"ACCEPTED")
        self.assertFalse(report["nativeCertified"])
    def test_rejection(self):
        report=run_parser(self.fixture,[sys.executable,"-c","import sys;sys.exit(7)","{fixture}"])
        self.assertEqual(report["status"],"REJECTED")
        self.assertEqual(report["exitCode"],7)
    def test_missing_placeholder(self):
        with self.assertRaises(ValueError):
            run_parser(self.fixture,[sys.executable,"--version"])
    def test_timeout(self):
        report=run_parser(self.fixture,[sys.executable,"-c","import time;time.sleep(2)","{fixture}"],timeout=0.01)
        self.assertEqual(report["status"],"TIMEOUT")
if __name__=="__main__":
    unittest.main()
