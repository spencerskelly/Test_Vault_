#!/usr/bin/env node
"use strict";

const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.14/EA_to_MDSE_Native_Importer_v0.8.14.html");
const src=fs.readFileSync(importer,"utf8");

function need(text,msg){if(!src.includes(text))throw new Error(msg+": "+text);}
function forbid(text,msg){if(src.includes(text))throw new Error(msg+": "+text);}

need('version: "0.8.14"',"wrong importer version");
need('const LOCAL_MODEL_SCHEMA_VERSION="0.3";',"base Local Model schema is not 0.3");
need('const LOCAL_BODY_SCHEMA="0.3";',"rendered Local Model schema is not 0.3");
need('outcome:"local-endpoint-only"',"W-377 contextual-only Port outcome missing");
need('key:"localendpoint:"+id',"contextual-only endpoint planning key missing");
need('if(r.definitionKey&&defType(r.definitionKey)!=="Port")',"definitionless endpoint validation is not allowed");
need('Review - Definitionless Local Endpoints.csv',"definitionless endpoint review evidence missing");
need('"ea_guid","source_object_id","ea_type","ea_name"',"definitionless endpoint source Object_ID is not persisted");
need('trim2(raw.ea_guid),n2(raw.Object_ID),trim2(raw.Object_Type)',"definitionless endpoint Object_ID row writer missing");
need('touches a W-377 definitionless contextual endpoint; note-level relationship is review-only',"connector review boundary missing");
need('(p.detail?"; "+p.detail:"")',"connector planner detail is not persisted in semantic review evidence");
need('definitionlessContextualEndpoints:definitionlessEndpointCount',"definitionless endpoint run statistic missing");

forbid('outcome:"added-port-group"',"legacy added-Port outcome remains");
forbid('entities.set("portgroup:"',"synthetic reusable Port entity creation remains");
forbid('Review - Added Ports.csv',"legacy Added Ports review output remains");

const scripts=[...src.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)].map(m=>m[1]);
if(scripts.length!==1)throw new Error("expected exactly one embedded script, found "+scripts.length);
new Function(scripts[0]);

console.log("v0.8.14 W-377/W-380 evidence checks: PASS");
