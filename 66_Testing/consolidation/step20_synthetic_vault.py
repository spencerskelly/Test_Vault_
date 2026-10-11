#!/usr/bin/env python3
"""Build an isolated synthetic GUI fixture from an uninitialized MDSE Base.

No QEAX, real BOM, schema change, plugin overlay or repository modification.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[2]
FOLDER="88_Step20_Synthetic_GUI_Model"
AUTHOR="testfixturexx"
PREFIX="Step20 - "
SCHEMAS={
 "relationships":("99_System/03_Schemas/relationships.yaml","1.36"),
 "element-types":("99_System/03_Schemas/element-types.yaml","1.18"),
 "local-model":("99_System/03_Schemas/local-model.yaml","0.5"),
}
ELEMENTS=[
 ("Assembly","Object","electrical","OBJ"),
 ("Controller","Object","electrical","OBJ"),
 ("CAN Transceiver","Object","electrical","OBJ"),
 ("HMI","Object","electrical","OBJ"),
 ("CAN Interface","Object","interface","OBJ"),
 ("CAN Status Flow","Item Flow","information","IFLOW"),
 ("Report Charger Status","Behavior","function","BEH"),
 ("Status Requirement","Requirement","functional","REQ"),
 ("Status Link Test","Verification","test","VER"),
 ("Status Indication Design","Condition","design","COND"),
 ("Review Status Use Case","Use Case","what","UC"),
 ("Test Operator","Actor",None,"ACT"),
]
def name(key): return PREFIX+key
def wikilink(key): return "[["+name(key)+"]]"
def uid(i):
    value=f"202610111620{i:05d}"+AUTHOR
    if re.fullmatch(r"[0-9]{17}[a-z-]{13}",value) is None:
        raise ValueError("Invalid synthetic identity")
    return value
def local(kind,i,alias):
    return "[[#^"+kind+"-"+uid(i)+"|"+alias+"]]"

RELATIONS={
 "Assembly":{
   "hasPart":["Controller","CAN Transceiver","HMI"],
   "performs":["Report Charger Status"],
   "hasDesign":["Status Indication Design"]},
 "Controller":{"partOf":["Assembly"]},
 "CAN Transceiver":{"partOf":["Assembly"]},
 "HMI":{"partOf":["Assembly"]},
 "Report Charger Status":{"performedBy":["Assembly"],"satisfies":["Status Requirement"],"realizes":["Review Status Use Case"]},
 "Status Requirement":{"satisfiedBy":["Report Charger Status","Status Indication Design"],"verifiedBy":["Status Link Test"]},
 "Status Link Test":{"verifies":["Status Requirement"]},
 "Status Indication Design":{"designOf":["Assembly"],"satisfies":["Status Requirement"]},
 "Review Status Use Case":{"realizedBy":["Report Charger Status"],"participants":["Test Operator","Assembly"]},
}
def model_region():
    p1,p2,p3=[uid(i) for i in (101,102,103)]
    e1,e2,e3=[uid(i) for i in (104,105,106)]
    c1,f1=uid(107),uid(108)
    return f"""
## Local Model
<!-- MDSE:LOCAL-MODEL START schema=0.5 -->
### Parts
#### Controller
- definition: {wikilink("Controller")}
- identifier: CTRL-1
^part-{p1}
#### CAN Transceiver
- definition: {wikilink("CAN Transceiver")}
- identifier: CAN-1
^part-{p2}
#### HMI
- definition: {wikilink("HMI")}
- multiplicity: 2
^part-{p3}
### Interfaces
#### Controller CAN
- definition: {wikilink("CAN Interface")}
- part: {local("part",101,"Controller")}
- identifier: CAN-TX
^ep-{e1}
#### Transceiver CAN
- definition: {wikilink("CAN Interface")}
- part: {local("part",102,"CAN Transceiver")}
- identifier: CAN-RX
^ep-{e2}
#### Assembly Boundary CAN
- definition: {wikilink("CAN Interface")}
- identifier: CAN-EXT
^ep-{e3}
### Connections
#### Controller CAN to Transceiver
- endpointA: {local("ep",104,"Controller CAN")}
- endpointB: {local("ep",105,"Transceiver CAN")}
- exposes: {local("ep",106,"Boundary CAN")}
- identifier: CAN-CABLE-1
^conn-{c1}
##### Status information
- definition: {wikilink("CAN Status Flow")}
- endpointA: transmit
- endpointB: receive
^flow-{f1}
<!-- MDSE:LOCAL-MODEL END -->
"""
def make_note(key,index,kind,subtype,prefix):
    meta=["type: "+kind]
    if subtype is not None: meta.append("subtype: "+subtype)
    meta+=["id: "+prefix+"-"+str(99000+index),"uid: "+uid(index),
           "status: Draft","tags: []"]
    for field,targets in RELATIONS.get(key,{}).items():
        meta.append(field+":")
        meta.extend("  - "+json.dumps(wikilink(t)) for t in targets)
    body=("---\n"+"\n".join(meta)+"\n---\n\n# "+name(key)+
          "\n\n## Definition\n\nSynthetic Step 20 test case; not actual charger engineering data.\n\n"+
          "## Notes\n\n## Aliases\n\n## Former ids\n")
    return body+(model_region() if key=="Assembly" else "")
README="""# Step 20 — synthetic MDSE GUI model (test only)

All model notes in this folder are fabricated. No real BOM, EA/QEAX model, customer
information, actual product requirement, or approved design has been included.

Open a disposable generated Base Vault containing this folder. Use the controlled
locked Workbench 0.1.18 runtime and the governed Local Model 0.5 schema.
There is no test-only relationships version, candidate plugin overlay, quantity
or unitOfMeasure extension, or Local Model 0.6 writer.

Navigation: [[Step20 - Assembly]] has three contextual Parts, three contextual/
boundary Interfaces, one internal Connection exposing the assembly boundary
Interface, and one nested information Flow. Open [[Step20 - Controller]] for
Where Used; [[Step20 - Report Charger Status]] and [[Step20 - Status Requirement]]
for function satisfaction; [[Step20 - Status Link Test]] for verifies;
and [[Step20 - Review Status Use Case]] for behavior realization.

Expected local kinds: Parts 3, Interfaces 3, Connections 1, Flows 1.
HMI multiplicity is 2. Exposes is on the Connection and is NOT a second
Connection. No GUI acceptance has been performed. Read STEP20_GUI_ACCEPTANCE.md
for operator tests and the required evidence fields. Do not merge these notes
into a production MDSE vault.
"""
def validate_source(base):
    if not base.is_dir() or not (base/".vault.yaml").exists():
        raise ValueError("Existing uninitialized generated Base required")
    if "vault_uid: UNINITIALIZED" not in (base/".vault.yaml").read_text():
        raise ValueError("Refusing to seed an initialized/user vault")
    original=(ROOT/".obsidian/plugin-lock.yaml").read_bytes()
    if (base/".obsidian/plugin-lock.yaml").read_bytes()!=original:
        raise ValueError("Runtime plugin lock differs from controlled source")
    for key,(p,version) in SCHEMAS.items():
        if (base/p).read_bytes()!=(ROOT/p).read_bytes():
            raise ValueError("Controlled schema file drift: "+key)
        if str(yaml.safe_load((base/p).read_bytes())["schemaVersion"])!=version:
            raise ValueError("Unexpected schema: "+key)
    if yaml.safe_load(original)["plugins"]["mdse-workbench"]["version"]!="0.1.18":
        raise ValueError("Unexpected Workbench release")
def seed(base,out):
    base=Path(base);out=Path(out)
    if out.exists() or out.resolve() in {ROOT.resolve(),base.resolve()}:
        raise ValueError("Refusing to overwrite existing output")
    validate_source(base)
    shutil.copytree(base,out,symlinks=False,ignore=shutil.ignore_patterns(".git",".DS_Store","workspace.json"))
    fixture=out/FOLDER
    fixture.mkdir(parents=True,exist_ok=False)
    for i,(key,kind,subtype,prefix) in enumerate(ELEMENTS,1):
        (fixture/(name(key)+".md")).write_text(
            make_note(key,i,kind,subtype,prefix),encoding="utf-8",newline="\n")
    (fixture/"README_TEST_ONLY.md").write_text(README,encoding="utf-8",newline="\n")
    shutil.copy2(ROOT/"66_Testing/consolidation/STEP20_GUI_ACCEPTANCE.md",
                 fixture/"STEP20_GUI_ACCEPTANCE.md")
    locksha=hashlib.sha256((out/".obsidian/plugin-lock.yaml").read_bytes()).hexdigest()
    report={"status":"GUI_NOT_EXECUTED","fixtureFolder":FOLDER,
      "syntheticNoteCount":len(ELEMENTS),"localRecordCounts":{"part":3,"endpoint":3,"connection":1,"flow":1},
      "schemaVersions":{k:v for k,(_,v) in SCHEMAS.items()},
      "lockedWorkbenchVersion":"0.1.18","pluginLockSha256":locksha,
      "hasQEAX":False,"hasRealBOM":False,"guiResults":{},
      "issuedRelease":False,"archivalApproved":False}
    (fixture/"FIXTURE_PROVENANCE.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    if (out/".obsidian/plugin-lock.yaml").read_bytes()!=(base/".obsidian/plugin-lock.yaml").read_bytes():
        raise ValueError("Plugin lock changed during fixture generation")
    print("STEP20_SYNTHETIC_MODEL="+json.dumps(report,sort_keys=True))
    return report
def main():
    a=argparse.ArgumentParser();a.add_argument("--base",required=True);a.add_argument("--out",required=True)
    args=a.parse_args();seed(args.base,args.out)
if __name__=="__main__":main()
