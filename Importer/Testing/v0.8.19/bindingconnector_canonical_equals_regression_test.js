#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src=fs.readFileSync(importer,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": missing "+t);}
function forbid(t,m){if(src.includes(t))throw new Error(m+": forbidden "+t);}

need('const LOCAL_BODY_SCHEMA="0.5";',"0.5 writer");
need('one canonical symmetric',"canonical equals contract");
need('if(!ae.equalsRefs.some(x=>x.refKey===b.refKey))ae.equalsRefs.push(b);',"first direction");
need('if(!be.equalsRefs.some(x=>x.refKey===a.refKey))be.equalsRefs.push(a);',"second direction");
need('if(candidates.length===1){',"strong exposure precedence");
need('conn.exposesRefs.push(outer)',"exposure retained");
need('continue;\n        }\n      }\n      const ae=endpointBySource.get',"equals only after exposure does not resolve");
need('review-only evidence retained.',"unrepresentable/cross-owner review");
need('equals relation is not symmetric with ',"write-time symmetry check");
forbid('temporary equals/review evidence retained.',"temporary importer semantics removed");
forbid('is not a deterministic boundary-to-internal exposure; no exposes or equals relationship invented.',"same-owner nested/sibling suppression removed");

const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0)throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.19 Local Model 0.5 canonical BindingConnector equals regression: PASS");
