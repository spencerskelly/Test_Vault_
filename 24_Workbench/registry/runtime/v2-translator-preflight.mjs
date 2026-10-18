#!/usr/bin/env node
// Mandatory pinned-registry preflight for prospective SysML v2 translator runs.
// No source rows, parser, or native emitter are invoked.
import {resolve} from 'node:path';
import {loadPinnedV2} from './pinned-v2-eligibility.mjs';

function main(args){
 if(args.length!==1)throw Error('USAGE: node v2-translator-preflight.mjs <checkout-root>');
 const result=loadPinnedV2(resolve(args[0]));
 if(result.target.automaticNativeEmission!==false)throw Error('UNSAFE_NATIVE_EMISSION');
 process.stdout.write(JSON.stringify({status:'PASS',mode:'PREVIEW_ONLY',
   relationshipFamilies:result.target.relationshipRules.length,
   semanticDecisions:result.decisions.records.length,nativeEmission:false})+'\n');
}
try{main(process.argv.slice(2));}catch(e){process.stderr.write(String(e.message)+'\n');process.exitCode=1;}
