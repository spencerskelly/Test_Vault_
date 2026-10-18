"""Fail-closed, source-independent BindingConnector topology invariants.

Pure validation helper for synthetic tests and future IMP-011 integration.
"""
from __future__ import annotations


def validate_binding(row: dict, endpoint_owner: dict, connection_info: dict) -> list[str]:
    errors = []
    guid = row.get("ea_guid", "<unknown>")
    relation = row.get("actual_relation", "")
    owner = row.get("owner_note", "")
    start = row.get("start_local", "")
    end = row.get("end_local", "")
    category = row.get("category", "")
    count = row.get("candidate_connection_count", "")
    connection_id = row.get("connection_local", "")
    exposed_id = row.get("exposes_local", "")

    def fail(message):
        errors.append(f"{guid}: {message}")

    if relation == "Connection.exposes":
        if category != "resolved Connection.exposes":
            fail("exposure category mismatch")
        if count != "1":
            fail("exposure requires exactly one candidate connection")
        info = connection_info.get(connection_id)
        if not info:
            fail("exposure references absent connection")
        else:
            if info.get("owner") != owner:
                fail("connection owner differs from review owner")
            if start not in info.get("endpoints", ()) and end not in info.get("endpoints", ()):
                fail("binding has no internal connection endpoint")
        if endpoint_owner.get(exposed_id) != owner:
            fail("exposed interface missing or on wrong owner")
        if exposed_id not in set(row.get("boundary_ids", ())):
            fail("exposed interface is not classified as assembly boundary")
        if row.get("also_equals", False):
            fail("exposure duplicated as equals")
    elif relation == "Interface.equals":
        if not category.startswith("canonical local equals - "):
            fail("equals category mismatch")
        if not start or not end or start == end:
            fail("equals requires two distinct endpoints")
        if endpoint_owner.get(start) != owner or endpoint_owner.get(end) != owner:
            fail("equals endpoints missing or cross-owner")
        if not row.get("explicit_binding", False):
            fail("equals lacks explicit source binding evidence")
        if not row.get("symmetric", False):
            fail("equals link is not symmetric")
        if row.get("also_exposes", False):
            fail("equals duplicated as exposure")
    elif relation == "":
        if category != "cross-owner binding":
            fail("unresolved relation must be explicitly cross-owner")
        if row.get("also_equals", False) or row.get("also_exposes", False):
            fail("unresolved cross-owner relation was persisted")
    else:
        fail("unsupported disposition")
    return errors
