"""Step20 repeatable structural synthetic-model tests; NO Obsidian GUI execution."""
from __future__ import annotations
import json
import os
import re
import unittest
from contextlib import contextmanager
from pathlib import Path
import yaml

from step20_synthetic_vault import ELEMENTS,FOLDER,ROOT,uid,name
from step20_validate_fixture import BLOCK_RE,FRONT,validate

@contextmanager
def temporary_edit(path):
    original=path.read_bytes()
    try:
        yield original
    finally:
        path.write_bytes(original)

class Step20SyntheticFixture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path=os.environ.get("STEP20_SYNTHETIC_VAULT")
        if not path:
            raise RuntimeError("STEP20_SYNTHETIC_VAULT missing")
        cls.base=Path(path)
        cls.folder=cls.base/FOLDER
        if not cls.folder.is_dir() or cls.base.resolve()==ROOT.resolve():
            raise RuntimeError("Disposable synthetic base missing")

    def assembly(self):
        return self.folder/(name("Assembly")+".md")

    def test_complete_structural_graph(self):
        result=validate(self.base)
        self.assertEqual(result["noteCount"],12)
        self.assertEqual(result["contextual"],{"part":3,"ep":3,"conn":1,"flow":1})

    def test_every_governed_type_is_present(self):
        types=set()
        for (k,*_) in ELEMENTS:
            text=(self.folder/(name(k)+".md")).read_text()
            types.add(yaml.safe_load(FRONT.match(text).group(1))["type"])
        self.assertTrue({"Object","Behavior","Requirement","Verification","Condition",
                         "Use Case","Actor","Item Flow"}.issubset(types))

    def test_all_twelve_unique_uid_tokens(self):
        tokens=[uid(i) for i in range(1,len(ELEMENTS)+1)]
        self.assertEqual(len(tokens),len(set(tokens)))
        self.assertTrue(all(re.fullmatch(r"[0-9]{17}[a-z-]{13}",x) for x in tokens))

    def test_exact_local_token_counts(self):
        values=BLOCK_RE.findall(self.assembly().read_text())
        self.assertEqual({kind:sum(k==kind for k,_ in values)
                          for kind in ("part","ep","conn","flow")},
                         {"part":3,"ep":3,"conn":1,"flow":1})

    def test_context_connection_exposes_boundary(self):
        t=self.assembly().read_text()
        self.assertIn("- exposes: [[#^ep-",t)
        self.assertEqual(t.count("- exposes: "),1)
        self.assertEqual(t.count("- endpointA: [[#^ep-"),1)
        self.assertEqual(t.count("- endpointB: [[#^ep-"),1)

    def test_one_nested_status_information_flow(self):
        t=self.assembly().read_text()
        self.assertEqual(t.count("##### Status information"),1)
        self.assertIn("- endpointA: transmit",t)
        self.assertIn("- endpointB: receive",t)

    def test_controller_to_transceiver_context(self):
        t=self.assembly().read_text()
        self.assertIn("#### Controller CAN",t)
        self.assertIn("#### Transceiver CAN",t)
        self.assertIn("#### Assembly Boundary CAN",t)

    def test_hmi_multiplicity_two(self):
        self.assertIn("- multiplicity: 2",self.assembly().read_text())

    def test_no_unapproved_quantity_variant_or_localmodel06(self):
        for path in self.folder.glob("Step20 - *.md"):
            t=path.read_text()
            for denied in ("schema=0.6","variantOf:","- quantity:","- unitOfMeasure:"):
                self.assertNotIn(denied,t)

    def test_synthetic_notice(self):
        self.assertIn("fabricated",(self.folder/"README_TEST_ONLY.md").read_text())

    def test_gui_not_executed_manifest(self):
        meta=json.loads((self.folder/"FIXTURE_PROVENANCE.json").read_text())
        self.assertEqual(meta["status"],"GUI_NOT_EXECUTED")
        self.assertEqual(meta["guiResults"],{})
        self.assertFalse(meta["issuedRelease"])

    def test_all_sixteen_gui_cases_pending(self):
        runbook=(self.folder/"STEP20_GUI_ACCEPTANCE.md").read_text()
        self.assertIn("NOT EXECUTED",runbook)
        lines=[line for line in runbook.splitlines() if line.startswith("| G20-")]
        self.assertEqual(len(lines),16)
        self.assertTrue(all(line.endswith("| NOT RUN |") for line in lines))

    def test_generated_lock_matches_source(self):
        self.assertEqual((self.base/".obsidian/plugin-lock.yaml").read_bytes(),
                         (ROOT/".obsidian/plugin-lock.yaml").read_bytes())

    def test_schema_paths_unchanged(self):
        for p in ("relationships.yaml","element-types.yaml","local-model.yaml"):
            rel="99_System/03_Schemas/"+p
            self.assertEqual((self.base/rel).read_bytes(),(ROOT/rel).read_bytes())

    def test_bad_requirement_target_is_detected(self):
        p=self.folder/(name("Status Link Test")+".md")
        with temporary_edit(p) as original:
            p.write_bytes(original.replace(b"Step20 - Status Requirement",
                                            b"Step20 - Undefined Requirement",1))
            with self.assertRaisesRegex(ValueError,"Authored relationships differ"):
                validate(self.base)
        validate(self.base)

    def test_broken_local_part_target_is_detected(self):
        p=self.assembly()
        with temporary_edit(p) as original:
            p.write_bytes(original.replace(b"^part-20261011162000101",
                                            b"^part-20261011162000109",1))
            with self.assertRaises(ValueError):
                validate(self.base)
        validate(self.base)

    def test_missing_context_endpoint_is_detected(self):
        p=self.assembly()
        with temporary_edit(p) as original:
            p.write_bytes(original.replace(b"^ep-20261011162000106",
                                            b"^ep-20261011162000108",1))
            with self.assertRaises(ValueError):
                validate(self.base)
        validate(self.base)

    def test_duplicate_note_uid_is_detected(self):
        p=self.folder/(name("Controller")+".md")
        with temporary_edit(p) as original:
            p.write_bytes(original.replace(uid(2).encode(),uid(1).encode(),1))
            with self.assertRaises(ValueError):
                validate(self.base)
        validate(self.base)

    def test_unapproved_actor_subtype_is_detected(self):
        p=self.folder/(name("Test Operator")+".md")
        with temporary_edit(p) as original:
            p.write_bytes(original.replace(b"type: Actor\n",b"type: Actor\nsubtype: electrical\n",1))
            with self.assertRaises(ValueError):
                validate(self.base)
        validate(self.base)

    def test_duplicate_expose_is_detected(self):
        p=self.assembly()
        with temporary_edit(p) as original:
            x=b"- exposes: [[#^ep-"
            p.write_bytes(original.replace(x,x+b"test\n- exposes: [[#^ep-",1))
            with self.assertRaises(ValueError):
                validate(self.base)
        validate(self.base)

    def test_missing_model_note_is_detected(self):
        p=self.folder/(name("HMI")+".md")
        with temporary_edit(p) as original:
            p.unlink()
            with self.assertRaises(ValueError):
                validate(self.base)
        validate(self.base)

    def test_no_public_source_archive_present(self):
        self.assertFalse((self.base/"EA_2026_09_06_endgame.qeax.zip").exists())

    def test_no_gui_success_claimed(self):
        self.assertFalse(validate(self.base)["guiAccepted"])

if __name__=="__main__": unittest.main()
