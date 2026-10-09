#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const importer = path.resolve(__dirname, "../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src = fs.readFileSync(importer, "utf8");

function need(text, label) { if (!src.includes(text)) throw new Error(label + ": missing " + text); }
function forbid(text, label) { if (src.includes(text)) throw new Error(label + ": forbidden " + text); }

need('const localId=stableLocalId("part",raw,raw.Object_ID);', "Part stable local ID");
need('const localId=stableLocalId("ep",raw,raw.Object_ID),path=parentPath.concat([localId]);', "Interface stable local ID");
need("The shared baseCount/used pool spans note UIDs", "vault-global local identity allocation");
need('definitionKey:(p.targetKey&&entities.has(p.targetKey))?p.targetKey:""', "Part definition reference");
need('lines.push("- definition: "+entityWiki(entities,r.definitionKey));', "rendered definition link");
need("if(q&&q.resolvedKey&&entities.has(q.resolvedKey))definitionKey=q.resolvedKey;", "Interface definition resolution");
need('return "[[#^"+ref.anchor+"|"+ref.address+"]]";', "same-note block reference");
need('if(parentId.startsWith("part-"))lines.push("- part: [[#^"+parentId+"]]");', "Interface part ownership reference");
need('else if(parentId.startsWith("ep-"))lines.push("- parent: [[#^"+parentId+"]]");', "nested Interface parent reference");
need('if(r.multiplicity)lines.push("- multiplicity: "+mdInline(r.multiplicity));', "occurrence multiplicity");
forbid("entityCtx.portOwner", "stale Port owner dependency");

const s1 = src.indexOf("<script>");
const s2 = src.lastIndexOf("</script>");
if (s1 < 0 || s2 < 0) throw new Error("embedded script missing");
new Function(src.slice(s1 + 8, s2));
console.log("v0.8.19 Local Model Parts/Interfaces regression: PASS");
