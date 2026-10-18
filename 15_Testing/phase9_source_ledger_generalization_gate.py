"""Fail-closed, local-only normalization-to-review handoff."""
def qualify(source, ledger, replay_ok):
    if not replay_ok: return 'REPLAY_REQUIRED'
    if not source or not ledger: return 'SOURCE_OR_LEDGER_MISSING'
    if source.get('Connector_Type')!='Generalization': return 'NOT_GENERALIZATION'
    if str(source.get('Connector_ID'))!=ledger.get('source_pk'): return 'IDENTITY_MISMATCH'
    if str(source.get('Start_Object_ID'))!=ledger.get('raw_from'): return 'RAW_ENDPOINT_MISMATCH'
    if str(source.get('End_Object_ID'))!=ledger.get('raw_to'): return 'RAW_ENDPOINT_MISMATCH'
    if source.get('Direction')!='Source -> Destination': return 'DIRECTION_REVIEW'
    if ledger.get('normalized_from')!=ledger.get('raw_from') or ledger.get('normalized_to')!=ledger.get('raw_to'): return 'NORMALIZED_DIRECTION_REVIEW'
    if ledger.get('family')!='Generalization': return 'FAMILY_MISMATCH'
    return 'ORIENTATION_REVIEW_CANDIDATE'
