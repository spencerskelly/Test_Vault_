"""Run a SysML v2 fixture through an installed Jupyter SysML kernel.

Exit nonzero on kernel error, timeout, or missing explicit completion.
All inputs should be synthetic and public; stdout prints aggregate statuses only.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

def diagnostic_categories(text):
    if not isinstance(text,str):
        return []
    rules={
        'error_marker':r'(?i)\b(?:error|errors|syntaxerror)\b\s*[:\[]',
        'parser_recovery':r'(?i)\b(?:mismatched input|extraneous input|no viable alternative)\b',
        'syntax_problem':r'(?i)\b(?:syntax error|parse error|parsing error)\b',
    }
    return [name for name,pattern in rules.items() if re.search(pattern,text)]

def execute_fixture(path, timeout=90):
    from jupyter_client import KernelManager
    source=Path(path).read_text(encoding="utf-8")
    result={"schema":"mdse-sysml2-real-kernel/1",
            "fixtureSha256":hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "kernel":"sysml","status":"FAIL","nativeCertified":False}
    manager=KernelManager(kernel_name="sysml")
    client=None
    try:
        manager.start_kernel()
        client=manager.client()
        client.start_channels()
        client.wait_for_ready(timeout=timeout)
        request=client.execute(source,store_history=False,allow_stdin=False,stop_on_error=True)
        execute_reply=None
        error=False
        idle=False
        observed_types={}
        stream_keyword_hits=0
        diagnostic_counts={}
        shell_reply_type=None
        while not idle:
            msg=client.get_iopub_msg(timeout=timeout)
            if msg.get("parent_header",{}).get("msg_id")!=request:
                continue
            msg_type=msg.get("msg_type")
            observed_types[msg_type]=observed_types.get(msg_type,0)+1
            if msg_type=="error":
                error=True
            if msg_type=="stream":
                text=msg.get("content",{}).get("text","")
                found=diagnostic_categories(text)
                if found:
                    stream_keyword_hits+=1
                    error=True
                    for category in found:
                        diagnostic_counts[category]=diagnostic_counts.get(category,0)+1
            if msg_type=="status" and msg.get("content",{}).get("execution_state")=="idle":
                idle=True
        # Ignore unmatched shell replies left over from kernel initialization.
        import time
        deadline=time.monotonic()+timeout
        while time.monotonic()<deadline:
            reply=client.get_shell_msg(timeout=max(0.1,deadline-time.monotonic()))
            if (reply.get("msg_type")=="execute_reply" and
                    reply.get("parent_header",{}).get("msg_id")==request):
                shell_reply_type=reply.get("msg_type")
                execute_reply=reply.get("content",{}).get("status")
                break
        result["diagnosticSummary"]={"iopubMessageCounts":observed_types,
          "streamKeywordHits":stream_keyword_hits,"diagnosticCategories":diagnostic_counts,"iopubError":observed_types.get("error",0)>0,
          "sawIdle":idle,"shellReplyType":shell_reply_type,"shellReplyStatus":execute_reply}
        result["status"]="ACCEPTED" if idle and not error and execute_reply=="ok" else "REJECTED"
    except Exception as exc:
        result["status"]="RUNNER_ERROR"
        result["errorCategory"]=type(exc).__name__
    finally:
        if client is not None:
            client.stop_channels()
        try:
            manager.shutdown_kernel(now=True)
        except Exception:
            pass
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--fixture",required=True)
    parser.add_argument("--expect",choices=["ACCEPTED","REJECTED"],required=True)
    args=parser.parse_args()
    report=execute_fixture(args.fixture)
    print(json.dumps(report,sort_keys=True))
    raise SystemExit(0 if report["status"]==args.expect else 1)
if __name__=="__main__":
    main()
