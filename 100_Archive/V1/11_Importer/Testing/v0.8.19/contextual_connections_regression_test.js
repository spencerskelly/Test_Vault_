#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const importer = path.resolve(__dirname, "../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src = fs.readFileSync(importer, "utf8");

function need(text,label){ if(!src.includes(text)) throw new Error(label+": missing "+text); }
function forbid(text,label){ if(src.includes(text)) throw new Error(label+": forbidden "+text); }

need('if(a.kind!=="endpoint"||b.kind!=="endpoint"){', "connection requires two contextual Interfaces");
need('const ownerKey=commonConnectionOwner(a,b);', "connection endpoints resolve through lowest common owner");
need('const localId=stableLocalId("conn",c,n2(c.Connector_ID));', "stable contextual Connection ID");
need('const pk=ownerKey+"|"+pairForRefs(a,b);', "connection indexed by owner and endpoint pair");
need('if(candidates.length===1){', "reuse one deterministic existing Connection");
need('else if(candidates.length===0){', "synthesize Connection only when none exists");
need('matches "+candidates.length+" existing Local Model Connections', "ambiguous multi-connection warning");
forbid('if(!a.ownerKey||a.ownerKey!==b.ownerKey){', "old immediate-owner Connection restriction");

need('const conveyedItems=(conveyed.byConnector.get(normGuid(c.ea_guid))||[]).slice().sort(', "deterministic conveyed item ordering");
need('definitionKey:defKey,roleA:roleForA(c,conn,start,end)', "conveyed flow definition and endpoint role");
need('if(d==="destination -> source"){tx=endRef;rx=startRef;}', "InformationFlow direction handling");
need('if(d.includes("bi")||d.includes("both"))return "exchange";', "bidirectional flow handling");
need('if(!d||d==="unspecified")return "unspecified";', "unspecified flow handling");

need('lines.push("- endpointA: "+localRefLink(localModel,conn.endpointA,e));', "render Connection endpointA");
need('lines.push("- endpointB: "+localRefLink(localModel,conn.endpointB,e));', "render Connection endpointB");
need('lines.push("##### "+(mdInline(fl.identifier)||"Flow"));', "render conveyed Flow under Connection");
need('lines.push("- endpointA: "+fl.roleA);', "render flow endpointA role");
need('lines.push("- endpointB: "+complementRole(fl.roleA));', "render complementary endpointB role");

const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0) throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.19 contextual Connections regression: PASS");
