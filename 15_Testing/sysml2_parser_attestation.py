"""Record independently obtained parser results without certifying native semantics."""
import hashlib
from pathlib import Path

def fixture_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def parser_attestation(fixture,parser_name,parser_version,exit_code):
    if not parser_name or not parser_version:
        raise ValueError("PARSER_IDENTITY_REQUIRED")
    if type(exit_code) is not int:
        raise ValueError("INVALID_EXIT_CODE")
    return {"schema":"mdse-sysml2-parser-attestation/1",
            "fixtureSha256":fixture_digest(fixture),
            "parser":parser_name,"parserVersion":parser_version,
            "status":"PARSER_ACCEPTED" if exit_code==0 else "PARSER_REJECTED",
            "nativeCertified":False}
