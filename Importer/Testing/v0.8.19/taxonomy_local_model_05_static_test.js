#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const schemaPath=path.resolve(__dirname,"../../../99_System/03_Schemas/local-model.yaml");
const src=fs.readFileSync(importer,"utf8");
const schema=fs.readFileSync(schemaPath,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": "+t);}
function sneed(t,m){if(!schema.includes(t))throw new Error(m+": "+t);}
function forbid(t,m){if(src.includes(t))throw new Error(m+": "+t);}
function sforbid(t,m){if(schema.includes(t))throw new Error(m+": "+t);}

need('version: "0.8.19"',"version");
need('const REL_SCHEMA_VERSION="1.36";',"relationship schema");
need('const ELEMENT_SCHEMA_VERSION="1.18";',"element schema");
need('const LOCAL_MODEL_SCHEMA_VERSION="0.5";',"base local schema");
need('const LOCAL_BODY_SCHEMA="0.5";',"rendered local schema");
need('Local records use schema 0.5 native block IDs.',"0.5 implementation comment");

sneed('schemaVersion: "0.5"',"schema authority version");
sneed('readableVersions: ["0.1", "0.2", "0.3", "0.4", "0.5"]',"historical readable versions");
sneed('writableVersion: "0.5"',"writer version");
sneed('version04Compatibility:',"0.4 frozen compatibility");
sneed('temporary review-only endpoint equals',"0.4 equals meaning frozen");
sneed('startMarker: "<!-- MDSE:LOCAL-MODEL START schema=0.5 -->"',"0.5 marker");
sneed('sourceMeaning: "BindingConnector equality/binding"',"canonical equals source meaning");
sneed('transitive equality closure is derived, never persisted.',"no persisted transitive closure");
sforbid('equals: {value: "localBlockLinkOrList", targetLocalKind: "endpoint", temporary: true',"0.5 equals is not temporary");

need('if(!ae.equalsRefs.some(x=>x.refKey===b.refKey))ae.equalsRefs.push(b);',"forward canonical equals");
need('if(!be.equalsRefs.some(x=>x.refKey===a.refKey))be.equalsRefs.push(a);',"inverse canonical equals");
need('cannot be represented as same-owner Local Model 0.5 equals or deterministic Connection.exposes; review-only evidence retained.',"cross-owner review boundary");
forbid('temporary equals/review evidence retained.',"temporary equals importer wording removed");
need('equals relation is not symmetric with ',"symmetry validation");

need('lines.push("### Parts","");',"Parts heading");
need('lines.push("### Interfaces","");',"Interfaces heading");
need('if(r.equalsRefs&&r.equalsRefs.length)lines.push("- equals: "+r.equalsRefs.map(x=>localRefLink(localModel,x,e)).join(", "));',"equals rendering");
need('if(conn.exposesRefs&&conn.exposesRefs.length)lines.push("- exposes: "+conn.exposesRefs.map(x=>localRefLink(localModel,x,e)).join(", "));',"Connection owns exposes");

const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0)throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.19 taxonomy/Local Model 0.5 regression: PASS");
