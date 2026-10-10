#!/usr/bin/env python3
"""Fail-closed BOM proposal reconciliation. Does NOT authorize schema promotion."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROPOSALS = ROOT / "99_System/03_Schemas/Proposals"


def checked(condition: bool, meaning: str) -> None:
    if not condition:
        raise SystemExit("BLOCKED: " + meaning)
    print("PASS:", meaning)


def blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def active(path: str, expected_sha: str) -> dict:
    raw = (ROOT / path).read_bytes()
    checked(blob_sha(raw) == expected_sha, f"governing {path} is unchanged")
    return yaml.safe_load(raw)


lm = active("99_System/03_Schemas/local-model.yaml", "361dee8269f9fbdfd16bcee33a1b808015f7ba5a")
rel = active("99_System/03_Schemas/relationships.yaml", "413fd5d32d12331413fda30653c7a3a38ac2d2ab")
ele = active("99_System/03_Schemas/element-types.yaml", "3f694feadb2eafd41498aff5ebc24946b9715f6d")
release = active("Base Vault/Definition/mdse-release.yaml", "ce556ade56b5bd9650ccc659f1b41bf2ca411c10")
checked(lm["schemaVersion"] == "0.5" and lm["compatibility"]["writableVersion"] == "0.5", "governed Local Model still 0.5")
checked("0.6" not in lm["compatibility"]["readableVersions"], "active schema does not quietly advertise unapproved 0.6")
checked("quantity" not in lm["records"]["part"]["optional"] and "unitOfMeasure" not in lm["records"]["part"]["fields"],
        "0.6-only fields are not written in 0.5 records")
checked(rel["schemaVersion"] == "1.36" and all(row["field"] != "variantOf" for row in rel["oneWay"]),
        "active relationships remain 1.36 with variantOf unapproved")
checked(ele["schemaVersion"] == "1.18" and not any(row.get("allowSubtypeOmission") for row in ele["classes"]),
        "Object family omission is not silently approved")
checked(release["releaseStatus"] == "pre-release" and release["schemas"] ==
        {"relationships": "1.36", "elementTypes": "1.18", "localModel": "0.5"},
        "controlled release schema versions are unchanged")

lmprop = yaml.safe_load((PROPOSALS / "bom-local-model-06-readonly.yaml").read_text())
vprop = yaml.safe_load((PROPOSALS / "bom-variantof-oneway.yaml").read_text())
checked(lmprop["status"] == "proposal-only" and vprop["status"] == "proposal-only",
        "candidate files are marked proposal only")
checked(lmprop["authority"]["activeGitBlob"] == "361dee8269f9fbdfd16bcee33a1b808015f7ba5a"
        and vprop["authority"]["activeGitBlob"] == "413fd5d32d12331413fda30653c7a3a38ac2d2ab",
        "proposed deltas are anchored to actual frozen governing sources")

candidate = lmprop["candidate"]
checked(candidate["readerOnly"] is True and candidate["markerVersion"] == "0.6"
        and candidate["readerVersion"] == "0.6" and candidate["writableVersion"] == "0.5"
        and candidate["changedRecordKind"] == "part"
        and candidate["partFieldsAdded"] == ["quantity", "unitOfMeasure"],
        "Local Model proposal extends only read-only Parts in 0.6")
checked(candidate["lowerReadableVersions"] == lm["compatibility"]["readableVersions"]
        and candidate["preserveOriginalMarker"] is True and candidate["noImplicitUpgradeOrDowngrade"] is True,
        "0.1-0.5 semantics and file markers are preserved")
amount = lmprop["partAmount"]
checked(amount["parentOwned"] is True
        and amount["childReverseBOMFieldsPersisted"] is False
        and amount["quantityAndUnitMustBothBePresentOrBothAbsent"] is True
        and amount["countedEaDoubleCountPolicy"] == "rejectWithoutSeparateFactorEvidence"
        and amount["ifBothFactorsSupported"] == "exactDecimalProductMultiplicityTimesQuantity",
        "quantity/UOM and multiplicity rules preserve parent ownership and prevent double counts")
checked(amount["provisionalUnitSymbols"] == ["ea", "in", "m", "kg"]
        and amount["unitRegistryApproved"] is False
        and amount["aliasesAndImplicitConversionsAllowed"] is False,
        "reader UOM examples are explicitly provisional, not released")

rx = re.compile(amount["positiveExactDecimal"]["plainAsciiPattern"])
valid = ["1", "0.35", "2.000", "10.125"]
invalid = ["0", "00.2", "-1", "1e-3", "NaN", "+1", "1-2", " 1"]
checked(all(rx.fullmatch(n) and any(c in "123456789" for c in n) for n in valid)
        and all(not (rx.fullmatch(n) and any(c in "123456789" for c in n)) for n in invalid),
        "candidate decimal lexer rejects zero, leading-zero, signs, exponents and invalid input")

relationship = vprop["relationship"]
checked(relationship["field"] == "variantOf" and relationship["category"] == "oneWay"
        and relationship["from"] == ["Object"] and relationship["to"] == ["Object"]
        and relationship["optional"] is True and relationship["maxForwardTargets"] == 1
        and relationship["storedInverse"] is False,
        "variantOf is a single forward Object-to-Object link without inverse")
checked(all(relationship[k] is True for k in
            ["noCycles", "noSelfLink", "noDanglingLinks", "noDuplicateLinks",
             "noImplicitSubtypeOf", "noImplicitPartOf", "noImplicitReplacementOrSubstitutability"]),
        "variantOf graph safety and separation from other relations")
checked(vprop["prerequisite"]["proposedObjectSubtypeOmission"]["status"] == "needs-independent-approval",
        "family Object subtype omission remains a separate decision")

wb = (ROOT / "55_Workbench/src/core/localmodel.ts").read_text(encoding="utf-8")
variant = (ROOT / "55_Workbench/src/core/variantof.ts").read_text(encoding="utf-8")
variantshape = (ROOT / "55_Workbench/src/core/variantof-format.ts").read_text(encoding="utf-8")
checked(bool(re.search(r'WRITABLE_VERSION\s*=\s*"0\.5"', wb))
        and bool(re.search(r'READABLE_VERSIONS\s*=\s*\[[^\]]*"0\.6"', wb))
        and 'version === "0.6" && r.kind === "part"' in wb,
        "actual Workbench code reads experimental 0.6 Parts but writes only 0.5")
checked(all(code in variant for code in
            ["variant.self", "variant.multiple", "variant.cycle", "variant.endpoint-invalid",
             "variant.duplicate", "variant.unresolved"])
        and "single wikilink scalar" in variantshape,
        "actual Workbench contains read-only variantOf shape and graph checks")
checked((ROOT / "55_Workbench/test/fixtures/local-model.yaml").read_bytes() ==
        (ROOT / "99_System/03_Schemas/local-model.yaml").read_bytes(),
        "Workbench canonical 0.5 fixture still mirrors authority exactly")

inventory = (ROOT / "55_Workbench/docs/bom/A01-A14_ARTIFACT_SHA256.md").read_text(encoding="utf-8")
entries = re.findall(r"(?m)^([0-9a-f]{64})\s{2}(\S+)\s*$", inventory)
checked(len(entries) == 31, "frozen BOM artifact inventory has exactly 31 entries")
for digest, name in entries:
    item = ROOT / "55_Workbench/docs/bom/a01-a14" / name
    checked(item.is_file() and hashlib.sha256(item.read_bytes()).hexdigest() == digest,
            "original BOM source bytes verified: " + name)
print("PASS: Step 16 candidates reconciled without active schema, writer or release mutation")
