"""Importer v0.8.19 renderer-shape regression: nested Flow must not corrupt Connection."""
import tempfile
import unittest
from pathlib import Path
from localmodel_topology_index_v2 import parse_index

A="ep-20261014130000001skellyspencer"
B="ep-20261014130000002skellyspencer"
C="conn-20261014130000003skellyspencer"
F="flow-20261014130000004skellyspencer"

class ImporterRendererShape(unittest.TestCase):
    @unittest.expectedFailure
    def test_flow_roles_do_not_overwrite_connection_endpoint_links(self):
        # Exact structural shape emitted by renderLocalModel in v0.8.19.
        note=f"""## Local Model
<!-- MDSE:LOCAL-MODEL START schema=0.5 -->

### Interfaces

#### A
^{A}

#### B
- part: [[#^part-20261014130000005skellyspencer]]
^{B}

### Connections

#### Wire
- endpointA: [[#^{A}]]
- endpointB: [[#^{B}]]
- exposes: [[#^{A}]]
^{C}

##### Item flow
- endpointA: transmit
- endpointB: receive
^{F}

<!-- MDSE:LOCAL-MODEL END -->
"""
        with tempfile.TemporaryDirectory() as d:
            Path(d, "Assembly.md").write_text(note,encoding="utf-8")
            result=parse_index(Path(d))
        self.assertEqual([],result["errors"])
        self.assertEqual((A,B),result["connections"][C]["endpoints"])
        self.assertEqual([A],result["connections"][C]["exposes"])

if __name__=="__main__":
    unittest.main()
