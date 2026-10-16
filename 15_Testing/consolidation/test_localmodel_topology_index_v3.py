"""Regression for v0.8.19 connection followed by nested Flow headings."""
import tempfile
import unittest
from pathlib import Path
from localmodel_topology_index_v3 import parse_index

A="ep-20261014130000001skellyspencer"
B="ep-20261014130000002skellyspencer"
C="conn-20261014130000003skellyspencer"
F="flow-20261014130000004skellyspencer"
START="<!-- MDSE:LOCAL-MODEL START schema=0.5 -->"
END="<!-- MDSE:LOCAL-MODEL END -->"

class FlowIsolation(unittest.TestCase):
    def test_flow_fields_separate_from_connection(self):
        text=f"""{START}
### Interfaces
#### Outside
^{A}
#### Inside
- part: [[#^part-20261014130000005skellyspencer]]
^{B}
### Connections
#### Wire
- endpointA: [[#^{A}]]
- endpointB: [[#^{B}]]
- exposes: [[#^{A}]]
^{C}
##### Transfer
- endpointA: transmit
- endpointB: receive
^{F}
{END}"""
        with tempfile.TemporaryDirectory() as d:
            Path(d,"Assembly.md").write_text(text,encoding="utf-8")
            i=parse_index(Path(d))
        self.assertEqual([],i["errors"])
        self.assertEqual((A,B),i["connections"][C]["endpoints"])
        self.assertEqual([A],i["connections"][C]["exposes"])

    def test_duplicate_connection_field_remains_rejected(self):
        text=f"""{START}
### Connections
#### Wire
- endpointA: [[#^{A}]]
- endpointA: [[#^{A}]]
- endpointB: [[#^{B}]]
^{C}
{END}"""
        with tempfile.TemporaryDirectory() as d:
            Path(d,"Assembly.md").write_text(text,encoding="utf-8")
            i=parse_index(Path(d))
        self.assertTrue(any("duplicate field endpointA" in e for e in i["errors"]))

if __name__=="__main__":
    unittest.main()
