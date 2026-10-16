import tempfile
import unittest
from pathlib import Path
from localmodel_topology_index_v2 import parse_index

A = "ep-20261014130000001skellyspencer"
B = "ep-20261014130000002skellyspencer"
C = "conn-20261014130000003skellyspencer"
START = "<!-- MDSE:LOCAL-MODEL START schema=0.5 -->"
END = "<!-- MDSE:LOCAL-MODEL END -->"

class TopologyIndexV2Tests(unittest.TestCase):
    def index(self, text):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "Assembly.md").write_text(text, encoding="utf-8")
            return parse_index(Path(d))

    def test_multiline_equals_and_exposes(self):
        x = f"""{START}
### Interfaces
#### J1
- equals:
  - [[#^{B}]]
^{A}
#### J2
- equals:
  - [[#^{A}]]
^{B}
### Connections
#### Wire
- endpointA: [[#^{A}]]
- endpointB: [[#^{B}]]
- exposes:
  - [[#^{A}]]
^{C}
{END}"""
        i = self.index(x)
        self.assertEqual([], i["errors"])
        self.assertIn((A, B), i["equality"])
        self.assertIn((B, A), i["equality"])
        self.assertEqual([A], i["connections"][C]["exposes"])

    def test_duplicate_field_rejected(self):
        x = f"""{START}
### Interfaces
#### J1
- equals: [[#^{B}]]
- equals: [[#^{B}]]
^{A}
{END}"""
        self.assertTrue(any("duplicate field equals" in e for e in self.index(x)["errors"]))

    def test_missing_connection_endpoint_rejected(self):
        x = f"""{START}
### Connections
#### W
- endpointA: [[#^{A}]]
^{C}
{END}"""
        self.assertTrue(any("invalid endpointB" in e for e in self.index(x)["errors"]))

if __name__ == "__main__":
    unittest.main()
