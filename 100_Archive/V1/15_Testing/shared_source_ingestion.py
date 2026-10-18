"""Single neutral ingestion boundary for EA and BOM source envelopes.

Do not join, deduplicate or infer semantic relationships across sources.
"""
from collections import Counter
from ea_source_reader import open_source, stream
from source_evidence_contract import ea_envelope
from bom_xlsx_reader import iter_bom

EA_CATEGORIES={"elements":"element","connectors":"connector","packages":"package","tags":"tag"}

def ingest_ea(path,snapshot_id,categories=None):
    requested=tuple(categories) if categories is not None else tuple(EA_CATEGORIES)
    if not snapshot_id: raise ValueError("MISSING_SNAPSHOT_ID")
    if any(c not in EA_CATEGORIES for c in requested):raise ValueError("UNKNOWN_EA_CATEGORY")
    connection=open_source(path)
    try:
        for category in requested:
            for row in stream(connection,category):
                yield ea_envelope(snapshot_id,EA_CATEGORIES[category],row)
    finally:
        connection.close()

def ingest_bom(path,sheet,columns,snapshot_id,workbook_id,header_row=1):
    if not snapshot_id:raise ValueError("MISSING_SNAPSHOT_ID")
    yield from iter_bom(path,sheet,columns,snapshot_id,workbook_id,header_row)

def identity(record):
    record.validate()
    # Source kind and kind of record are part of identity. Never join EA and BOM
    # merely because their source keys or human-readable part names match.
    return (record.source_kind,record.snapshot_id,record.record_kind,record.source_key)

def audit(records):
    """Aggregate-only metrics; never produce source keys or source rows."""
    types=Counter()
    seen=set()
    duplicates=0
    for record in records:
        key=identity(record)
        types[(record.source_kind,record.record_kind)]+=1
        if key in seen:duplicates+=1
        seen.add(key)
    return {"status":"PASS" if duplicates==0 else "BLOCKED",
            "recordCount":sum(types.values()),"duplicateSourceIdentities":duplicates,
            "byKind":{a+":"+b:n for (a,b),n in sorted(types.items())},
            "nativeCertified":0}
