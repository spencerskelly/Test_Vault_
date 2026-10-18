"""Fail-closed canonical projection for coincident lexical parent and generalization.

Pure synthetic contract: no QEAX rows, no native syntax or emission.
"""
def project(child,parent,source_direction,approved_definition=False):
    diagnostics=[]
    if not child or not parent:diagnostics.append("MISSING_ENDPOINT")
    else:
        if child.get("ownerId")!=parent.get("id"):diagnostics.append("LEXICAL_OWNER_MISMATCH")
        if child.get("kind")!="PartDefinition" or parent.get("kind")!="PartDefinition":
            diagnostics.append("DEFINITION_KIND_UNVERIFIED")
        if child.get("id")==parent.get("id"):diagnostics.append("SELF_SPECIALIZATION")
        if source_direction!="Source -> Destination":diagnostics.append("DIRECTION_NOT_VERIFIED")
        if not approved_definition:diagnostics.append("DEFINITION_INTENT_UNAPPROVED")
    if diagnostics:return {"status":"review","diagnostics":diagnostics,"edges":[],"nativeCertified":False}
    # Approved synthetic contract still creates a *candidate* graph, never an emitted native model.
    return {"status":"candidate","diagnostics":[],"edges":[
        {"kind":"lexicalContainment","from":parent["id"],"to":child["id"]},
        {"kind":"specialization","from":child["id"],"to":parent["id"]}],
        "nativeCertified":False}
