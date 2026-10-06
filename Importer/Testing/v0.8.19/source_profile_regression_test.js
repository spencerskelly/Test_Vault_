#!/usr/bin/env node
"use strict";

const fs=require("fs");
const path=require("path");

const root=path.resolve(__dirname,"../../..");
const profilePath=path.join(root,"Importer/Definition/Source Profiles/EA8647-2026-09-06-v1.json");
const importerPath=path.join(root,"Importer/Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");

const profile=JSON.parse(fs.readFileSync(profilePath,"utf8"));
const html=fs.readFileSync(importerPath,"utf8");

if(profile.schema!=="mdse-ea-source-profile/1")throw new Error("unexpected source profile schema");
if(profile.sourceModelId!=="EA8647")throw new Error("unexpected source model id");
for(const section of ["tables","elementTypes","connectorTypes","diagramTypes"]){
  const values=profile.expected&&profile.expected[section];
  if(!values||typeof values!=="object"||Array.isArray(values)||!Object.keys(values).length){
    throw new Error("missing source profile section "+section);
  }
  for(const [key,value] of Object.entries(values)){
    if(!key||!Number.isSafeInteger(value)||value<0)throw new Error("invalid "+section+" count "+key);
  }
}
for(const name of ["t_object","t_connector","t_package","t_diagram"]){
  if(!Object.prototype.hasOwnProperty.call(profile.expected.tables,name))throw new Error("required table absent: "+name);
}

const open='<script id="mdse-source-profile" type="application/json">\n';
const start=html.indexOf(open);
const end=start<0?-1:html.indexOf("\n</script>",start+open.length);
if(start<0||end<0)throw new Error("embedded source profile block missing");
const embeddedText=html.slice(start+open.length,end);
const embedded=JSON.parse(embeddedText);
if(JSON.stringify(embedded)!==JSON.stringify(profile))throw new Error("embedded source profile differs from authority JSON");

for(const legacy of [
  "const EXPECTED_TABLES = {",
  "const EXPECTED_ELEMENT_TYPES = {",
  "const EXPECTED_CONNECTOR_TYPES = {",
  "const EXPECTED_DIAGRAM_TYPES = {",
  'const SOURCE_MODEL_ID="EA8647"'
]){
  if(html.includes(legacy))throw new Error("legacy compiled source contract remains: "+legacy);
}
for(const token of [
  "function loadSourceProfile()",
  "const SOURCE_PROFILE=loadSourceProfile();",
  "const SOURCE_MODEL_ID=SOURCE_PROFILE.sourceModelId;",
  "const EXPECTED_TABLES=SOURCE_PROFILE.expected.tables;",
  "const EXPECTED_ELEMENT_TYPES=SOURCE_PROFILE.expected.elementTypes;",
  "const EXPECTED_CONNECTOR_TYPES=SOURCE_PROFILE.expected.connectorTypes;",
  "const EXPECTED_DIAGRAM_TYPES=SOURCE_PROFILE.expected.diagramTypes;",
  '"- Source profile: "+SOURCE_PROFILE.profileId+" ("+SOURCE_PROFILE.schema+")"'
]){
  if(!html.includes(token))throw new Error("source profile runtime token missing: "+token);
}

const canonical=JSON.stringify(profile,null,2);
if(embeddedText!==canonical)throw new Error("embedded source profile is not canonical JSON");

console.log("IMP-007 source profile regression: PASS");
