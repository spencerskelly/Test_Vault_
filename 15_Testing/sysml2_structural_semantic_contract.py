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
    for n in nodes:
        visited={n["id"]}
        cursor=n
        while cursor.get("owner") in by_id:
            parent=cursor["owner"]
            if parent in visited:
                issues.append("OWNERSHIP_CYCLE")
                break
            visited.add(parent)
            cursor=by_id[parent]
        multiplicity=n.get("multiplicity")
        if multiplicity is not None:
            if not isinstance(multiplicity,(list,tuple)) or len(multiplicity)!=2:
                issues.append("INVALID_MULTIPLICITY")
            else:
                lower,upper=multiplicity
                if type(lower) is not int or lower<0 or (upper!="*" and (type(upper) is not int or upper<lower)):
                    issues.append("INVALID_MULTIPLICITY")
        if n.get("source_ref") is not None and not str(n["source_ref"]).strip():
            issues.append("INVALID_PROVENANCE")
    for c in connections:
        if c.get("owner") not in by_id: issues.append("MISSING_CONNECTION_OWNER")
        elif by_id[c["owner"]]["kind"] not in ("PartDefinition","PartUsage"):
            issues.append("INVALID_CONNECTION_OWNER_KIND")
        if c.get("direction") not in (None,"source_to_target","target_to_source","bidirectional","undirected"):
            issues.append("INVALID_DIRECTION")
        if c.get("source_ref") is not None and not str(c["source_ref"]).strip():
            issues.append("INVALID_PROVENANCE")
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
