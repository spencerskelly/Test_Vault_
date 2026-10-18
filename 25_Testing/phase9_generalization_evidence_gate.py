"""Fail closed on unverified local reconciliation; no native emission."""
from replay_phase8_local_normalization import check

def gate(qeax, ledger, registry):
    result=check(qeax, ledger, registry)
    if not result['valid'] or result['source_count'] != result['ledger_count']:
        return {'review':False,'native_certified':0,'diagnostic':'SOURCE_REPLAY_INVALID'}
    return {'review':True,'native_certified':0,'diagnostic':'SOURCE_CONSISTENCY_ONLY_SEMANTIC_REVIEW_REQUIRED'}
