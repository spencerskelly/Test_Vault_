#!/usr/bin/env python3
"""Synthetic regression test for imp009_output_acceptance.py."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
VALIDATOR = HERE / "imp009_output_acceptance.py"
TOKEN_A = "20261005190000000skellyspencer"
TOKEN_B = "20261005190000001skellyspencer"
TOKEN_C = "20261005190000002skellyspencer"
TOKEN_D = "20261005190000003skellyspencer"
EP1 = "ep-" + TOKEN_A
EP2 = "ep-" + TOKEN_B
CONN = "conn-" + TOKEN_C
OWNER_UID = TOKEN_D
GUID_EP = "{11111111-1111-1111-1111-111111111111}"
GUID_CON = "{22222222-2222-2222-2222-222222222222}"


def write(root: Path, rel: str, text: str) -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def make_fixture(root: Path, bad_definition: bool = False) -> None:
    state = {
        "schemaVersion": "1.0",
        "status": "IMPORT_COMPLETE",
        "importer": {"name": "EA to MDSE Native Importer", "version": "0.8.14"},
        "mdseRelease": "0.8.0",
        "source": {"name": "EA8647.qeax", "size": 1234, "sha256": "a" * 64},
        "scope": "WHOLE MODEL",
        "runStatus": {
            "source": "SOURCE_PASS",
            "plan": "PLAN_PASS",
            "write": "WRITE_PASS",
            "semantic": "SEMANTIC_REVIEW_REQUIRED",
            "acceptance": "ACCEPTANCE_PENDING",
        },
    }
    write(root, "99_System/11_Import/Import State.json", json.dumps(state, indent=2) + "\n")
    write(
        root,
        "99_System/11_Import/Run Manifest.md",
        "\n".join(
            [
                "# Run Manifest",
                "",
                "- Importer: EA to MDSE Native Importer 0.8.14",
                "- Local Model schema: 0.3",
                "- Definitionless contextual endpoints (W-377): 1",
                "",
            ]
        ),
    )
    write(
        root,
        "99_System/11_Import/Review - Definitionless Local Endpoints.csv",
        "ea_guid,source_object_id,ea_type,ea_name,category,owner_note,local_id,assembly,block_note,block_ports,reason\n"
        f'"{GUID_EP}",42,Port,P1,named contextual Port; no deterministic reusable Port match,Assembly,{EP1},Assembly,Reusable Block,,W-377 definitionless contextual endpoint\n',
    )
    write(
        root,
        "99_System/11_Import/Local Model Source Map.csv",
        "source_model_id,source_key,owner_uid,local_id,local_kind,ea_guid,ea_source_kind,ea_owner_guid\n"
        f'EA8647,"EA8647|{GUID_EP}",{OWNER_UID},{EP1},endpoint,"{GUID_EP}",t_object,"{{33333333-3333-3333-3333-333333333333}}"\n',
    )
    write(
        root,
        "99_System/11_Import/Ledger.csv",
        "ea_guid,source_kind,ea_type,ea_name,outcome,rule,uid,id,folded_into_uid\n"
        f'"{GUID_EP}",element,Port,P1,local endpoint,W-377,,,\n',
    )
    write(
        root,
        "99_System/11_Import/Review - Semantic and Connectors.csv",
        "source_guid,category,relationship,from_type,from_name,to_type,to_name,detail\n"
        f'"{GUID_CON}",connector review,connectsTo,Port,localendpoint:42,Port,object:99,"review-only source connector; not written to canonical YAML; W-377; touches a W-377 definitionless contextual endpoint; note-level relationship is review-only while Local Model preserves supported occurrence topology"\n',
    )

    definition = "- definition: [[Synthetic Port]]\n" if bad_definition else ""
    note = (
        "---\n"
        f"uid: {OWNER_UID}\n"
        "type: Object\n"
        "---\n\n"
        "# Assembly\n\n"
        "## Local Model\n"
        "<!-- MDSE:LOCAL-MODEL START schema=0.3 -->\n\n"
        "### Local Interfaces\n\n"
        "#### P1\n"
        f"{definition}"
        "- kind: proxy\n"
        f"^{EP1}\n\n"
        "#### P2\n"
        "- definition: [[Reusable Port]]\n"
        "- kind: proxy\n"
        f"^{EP2}\n\n"
        "### Connections\n\n"
        "#### C1\n"
        f"- endpointA: [[#^{EP1}|P1]]\n"
        f"- endpointB: [[#^{EP2}|P2]]\n"
        f"^{CONN}\n\n"
        "<!-- MDSE:LOCAL-MODEL END -->\n"
    )
    write(root, "10_Product/Assembly.md", note)


def run(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(root)],
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "valid"
        make_fixture(root)
        good = run(root)
        if good.returncode != 0 or "RESULT: HEADLESS PASS" not in good.stdout or "MANUAL SAMPLE:" not in good.stdout:
            print(good.stdout)
            print(good.stderr, file=sys.stderr)
            raise SystemExit("valid synthetic IMP-009 fixture did not pass")

        bad = Path(td) / "bad-definition"
        shutil.copytree(root, bad)
        model = bad / "10_Product/Assembly.md"
        txt = model.read_text(encoding="utf-8")
        txt = txt.replace("#### P1\n- kind: proxy\n", "#### P1\n- definition: [[Synthetic Port]]\n- kind: proxy\n", 1)
        model.write_text(txt, encoding="utf-8")
        rejected = run(bad)
        if rejected.returncode == 0 or "unexpectedly has a reusable definition" not in rejected.stdout:
            print(rejected.stdout)
            print(rejected.stderr, file=sys.stderr)
            raise SystemExit("invalid synthetic definitionless endpoint was not rejected")

    print("IMP-009 output validator synthetic self-test: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
