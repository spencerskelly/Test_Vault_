"""Read-only readiness probe for official SysML v2 Jupyter kernel.

This checks installation only; it does not execute, parse or certify SysML.
"""
import json
import re
import shutil
import subprocess
import sys

def probe(which=shutil.which, run=subprocess.run):
    result={"schema":"mdse-sysml2-kernel-preflight/1",
            "javaAvailable":False,"javaCommandPresent":False,"javaMajorVersion":None,
            "jupyterAvailable":False,
            "sysmlKernelRegistered":False,"readyForManualPilotValidation":False,
            "nativeCertified":False}
    result["javaCommandPresent"]=bool(which("java"))
    result["jupyterAvailable"]=bool(which("jupyter"))
    if result["javaCommandPresent"]:
        try:
            java=run(["java","-version"],capture_output=True,text=True,timeout=10,check=False)
            version_text=(java.stderr or "")+"\n"+(java.stdout or "")
            match=re.search(r'(?i)(?:openjdk|java) version\s+"?(\d+)(?:\.(\d+))?',version_text)
            if not match:
                match=re.search(r'(?i)openjdk\s+(\d+)(?:\.(\d+))?',version_text)
            if java.returncode==0 and match:
                major=int(match.group(2)) if match.group(1)=="1" and match.group(2) else int(match.group(1))
                result["javaMajorVersion"]=major
                result["javaAvailable"]=major>=21
        except (OSError,subprocess.TimeoutExpired):
            pass
    if not (result["javaAvailable"] and result["jupyterAvailable"]):
        result["status"]="MISSING_DEPENDENCY"
        return result
    try:
        proc=run(["jupyter","kernelspec","list","--json"],
                 capture_output=True,text=True,timeout=20,check=False)
        if proc.returncode:
            result["status"]="KERNEL_QUERY_FAILED"
            return result
        details=json.loads(proc.stdout)
        kernels=details.get("kernelspecs",{})
        result["sysmlKernelRegistered"]="sysml" in kernels
        result["readyForManualPilotValidation"]=result["sysmlKernelRegistered"]
        result["status"]="KERNEL_FOUND" if result["sysmlKernelRegistered"] else "KERNEL_NOT_FOUND"
    except (OSError,ValueError,subprocess.TimeoutExpired):
        result["status"]="KERNEL_QUERY_FAILED"
    return result

if __name__=="__main__":
    print(json.dumps(probe(),indent=2,sort_keys=True))
