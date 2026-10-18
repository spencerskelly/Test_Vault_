#!/usr/bin/env python3
"""EA source-only read adapter. No target semantics, note writing or network calls."""
import pathlib
import sqlite3

COLUMNS={
 "elements":("t_object",("Object_ID","ea_guid","Object_Type","Stereotype","Name","Alias","Author","CreatedDate","ModifiedDate","Package_ID","ParentID","Classifier","Note")),
 "connectors":("t_connector",("Connector_ID","ea_guid","Connector_Type","Stereotype","Direction","Start_Object_ID","End_Object_ID","SourceRole","DestRole","SourceCard","DestCard","SourceIsAggregate","DestIsAggregate","Notes")),
 "packages":("t_package",("Package_ID","ea_guid","Name","Parent_ID","Notes")),
 "tags":("t_objectproperties",("PropertyID","Object_ID","Property","Value","Notes","ea_guid")),
}
def open_source(path):
    path=pathlib.Path(path).resolve()
    connection=sqlite3.connect("file:"+str(path)+"?mode=ro",uri=True)
    connection.row_factory=sqlite3.Row
    return connection

def stream(connection,category,batch_size=500):
    """Yield raw evidence dictionaries, with raw source/destination, no inferred direction."""
    if category not in COLUMNS: raise ValueError("UNKNOWN_SOURCE_CATEGORY")
    if not isinstance(batch_size,int) or batch_size<1: raise ValueError("INVALID_BATCH_SIZE")
    table,names=COLUMNS[category]
    present={x[1] for x in connection.execute("PRAGMA table_info("+table+")")}
    absent=set(names)-present
    if absent: raise ValueError("MISSING_SOURCE_COLUMNS: "+",".join(sorted(absent)))
    query="SELECT "+",".join('"'+n+'"' for n in names)+" FROM "+table
    cursor=connection.execute(query)
    while True:
        batch=cursor.fetchmany(batch_size)
        if not batch: break
        for row in batch: yield dict(row)

def summarize(connection):
    return {category:connection.execute("SELECT COUNT(*) FROM "+table).fetchone()[0]
            for category,(table,_) in COLUMNS.items()}
