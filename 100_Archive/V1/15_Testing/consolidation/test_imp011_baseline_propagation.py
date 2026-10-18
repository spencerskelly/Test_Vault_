"""Prove IMP-011 topology wrapper cannot mask original validator failures."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch, Mock
import imp011_topology_acceptance as m

class BaselinePropagationTests(unittest.TestCase):
    def test_missing_baseline_fails_closed(self):
        with patch.object(sys, 'argv', ['imp011_topology_acceptance.py','missing.qeax','missing_vault']):
            with patch.object(Path, 'is_file', return_value=False):
                with patch.object(m.subprocess, 'run') as runner:
                    self.assertEqual(2,m.main())
                    runner.assert_not_called()

    def test_baseline_nonzero_is_preserved_and_topology_is_not_run(self):
        with patch.object(sys, 'argv', ['imp011_topology_acceptance.py','missing.qeax','missing_vault']):
            with patch.object(Path, 'is_file', return_value=True):
                with patch.object(m.subprocess, 'run', return_value=Mock(returncode=7)) as runner:
                    with patch.object(m, 'check') as topology:
                        self.assertEqual(7,m.main())
                        runner.assert_called_once()
                        topology.assert_not_called()

if __name__ == '__main__':
    unittest.main()
