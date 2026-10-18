"""Synthetic structural semantic checks; never certify native emission."""
def validate(nodes, connections):
    by_id={n["id"]:n for n in nodes}
    issues=[]
    if len(by_id)!=len(nodes): issues.append("DUPLICATE_ID")
    for n in nodes:
        owner=n.get("owner")
        if owner and owner not in by_id: issues.append("MISSING_OWNER")
        if n["kind"]=="PortUsage" and owner in by_id:
            if by_id[owner]["kind"] not in ("PartDefinition","PartUsage"):
                issues.append("PORT_OWNER_NOT_PART")
        expected={"PortUsage":"PortDefinition","PartUsage":"PartDefinition"}.get(n["kind"])
        if expected and n.get("typed_by"):
            target=by_id.get(n["typed_by"])
            if target is None or target["kind"]!=expected: issues.append("INVALID_TYPE")
    for c in connections:
        if c.get("owner") not in by_id: issues.append("MISSING_CONNECTION_OWNER")
        for end in ("source","target"):
            n=by_id.get(c.get(end))
            if n is None: issues.append("MISSING_ENDPOINT")
            elif n["kind"] not in ("PartUsage","PortUsage"): issues.append("INVALID_ENDPOINT")
    return sorted(set(issues))

def workbench_view(kind):
    return {
        "PortUsage":("typed_port_usage","owner_boundary_port","owner_and_type"),
        "PartUsage":("typed_part_usage","contained_part","owner_and_type"),
        "ConnectionUsage":("owned_connection","endpoint_edge","source_and_target"),
    }.get(kind,("definition","definition_catalog","usages"))
