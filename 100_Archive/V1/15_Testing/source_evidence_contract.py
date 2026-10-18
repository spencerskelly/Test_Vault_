"""Neutral source evidence envelopes; never assert target SysML/MDSE semantics."""
from dataclasses import dataclass, asdict
from typing import Any

KINDS={"EA","BOM"}
RECORDS={"element","connector","package","tag","part","bom_line","revision"}
@dataclass(frozen=True)
class SourceEvidence:
    source_kind: str
    snapshot_id: str
    record_kind: str
    source_key: str
    raw: dict[str,Any]
    provenance: dict[str,Any]
    disposition: str="uninterpreted"
    def validate(self):
        if self.source_kind not in KINDS: raise ValueError("INVALID_SOURCE_KIND")
        if self.record_kind not in RECORDS: raise ValueError("INVALID_RECORD_KIND")
        if (self.source_kind=="EA" and self.record_kind in {"part","bom_line","revision"}) or (self.source_kind=="BOM" and self.record_kind in {"element","connector","package","tag"}):
            raise ValueError("SOURCE_RECORD_KIND_MISMATCH")
        if not self.snapshot_id or not self.source_key: raise ValueError("MISSING_SOURCE_IDENTITY")
        if not isinstance(self.raw,dict) or not isinstance(self.provenance,dict): raise ValueError("INVALID_EVIDENCE_PAYLOAD")
        if self.disposition!="uninterpreted": raise ValueError("SEMANTIC_PREAPPROVAL_FORBIDDEN")
        return self

def envelope(source_kind,snapshot_id,record_kind,source_key,raw,provenance):
    return SourceEvidence(source_kind,snapshot_id,record_kind,str(source_key),dict(raw),dict(provenance)).validate()

def ea_envelope(snapshot_id,record_kind,row):
    ids={"element":"Object_ID","connector":"Connector_ID","package":"Package_ID","tag":"PropertyID"}
    if record_kind not in ids: raise ValueError("INVALID_EA_RECORD_KIND")
    key=row.get(ids[record_kind])
    if key is None or str(key)=="": raise ValueError("MISSING_EA_PRIMARY_KEY")
    return envelope("EA",snapshot_id,record_kind,key,row,{"ea_guid":row.get("ea_guid"),"source_pk":key})

def bom_envelope(snapshot_id,record_kind,source_key,row,workbook_id,sheet,row_number):
    if record_kind not in {"part","bom_line","revision"}: raise ValueError("INVALID_BOM_RECORD_KIND")
    if not workbook_id or not sheet or not isinstance(row_number,int) or row_number<1:
        raise ValueError("MISSING_BOM_PROVENANCE")
    return envelope("BOM",snapshot_id,record_kind,source_key,row,
        {"workbook_id":workbook_id,"sheet":sheet,"row_number":row_number})
