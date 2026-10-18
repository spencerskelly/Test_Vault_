"""Deterministic, source-only manifest. Keep row-level manifest outside GitHub."""
import hashlib
import json
from collections import Counter
from shared_source_ingestion import identity

SCHEMA="mdse-source-manifest/1"
DISPOSITIONS={"uninterpreted","deferred_review","source_excluded","invalid_source"}
def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,default=str)

def make_manifest(records):
    entries=[]
    seen=set()
    for record in records:
        record.validate()
        key=identity(record)
        if key in seen:raise ValueError("DUPLICATE_SOURCE_IDENTITY")
        seen.add(key)
        key_fields=list(key)
        fingerprint=hashlib.sha256(canonical({"identity":key_fields,"raw":record.raw,
                     "provenance":record.provenance}).encode("utf-8")).hexdigest()
        entries.append({"sourceKind":record.source_kind,"snapshotId":record.snapshot_id,
                        "recordKind":record.record_kind,"sourceKey":record.source_key,
                        "fingerprint":fingerprint,"disposition":"uninterpreted",
                        "reason":"SOURCE_INGESTED_NOT_TRANSLATED"})
    entries.sort(key=lambda e:(e["sourceKind"],e["snapshotId"],e["recordKind"],e["sourceKey"]))
    return {"schema":SCHEMA,"entries":entries,"status":"SOURCE_ONLY"}

def validate(manifest):
    if manifest.get("schema")!=SCHEMA:raise ValueError("UNKNOWN_MANIFEST_SCHEMA")
    entries=manifest.get("entries")
    if not isinstance(entries,list):raise ValueError("INVALID_MANIFEST_ENTRIES")
    seen=set()
    for item in entries:
        key=tuple(item.get(k) for k in ("sourceKind","snapshotId","recordKind","sourceKey"))
        if any(not v for v in key):raise ValueError("MISSING_MANIFEST_IDENTITY")
        if key in seen:raise ValueError("DUPLICATE_MANIFEST_ENTRY")
        seen.add(key)
        if item.get("disposition") not in DISPOSITIONS:raise ValueError("INVALID_DISPOSITION")
        if not item.get("reason"):raise ValueError("MISSING_DISPOSITION_REASON")
        digest=item.get("fingerprint")
        if not isinstance(digest,str) or len(digest)!=64 or any(c not in "0123456789abcdef" for c in digest):
            raise ValueError("INVALID_SOURCE_FINGERPRINT")
    return True

def aggregate(manifest):
    validate(manifest)
    counts=Counter((x["sourceKind"],x["recordKind"],x["disposition"]) for x in manifest["entries"])
    return {"schema":"mdse-source-manifest-aggregate/1",
            "total":len(manifest["entries"]),
            "byKindAndDisposition":{"/".join(k):v for k,v in sorted(counts.items())},
            "nativeCertified":0}
