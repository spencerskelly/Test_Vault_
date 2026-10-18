"""Execute a configured SysML v2 parser with strict evidence-only outcomes."""
import argparse
import json
import hashlib
import pathlib
import subprocess

def run_parser(fixture, command, timeout=120):
    path=pathlib.Path(fixture).resolve(strict=True)
    if not path.is_file() or not command or command.count("{fixture}")!=1:
        raise ValueError("PARSER_COMMAND_REQUIRES_ONE_FIXTURE_PLACEHOLDER")
    args=[word.replace("{fixture}",str(path)) for word in command]
    try:
        process=subprocess.run(args, capture_output=True, timeout=timeout, check=False)
        outcome="ACCEPTED" if process.returncode==0 else "REJECTED"
        exit_code=process.returncode
    except subprocess.TimeoutExpired:
        outcome="TIMEOUT"
        exit_code=None
    return {"schema":"mdse-parser-execution/1",
            "fixtureSha256":hashlib.sha256(path.read_bytes()).hexdigest(),
            "parserCommandName":pathlib.Path(args[0]).name,
            "status":outcome,"exitCode":exit_code,
            "nativeCertified":False}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--fixture",required=True)
    p.add_argument("--parser-command",nargs="+",required=True)
    a=p.parse_args()
    print(json.dumps(run_parser(a.fixture,a.parser_command),indent=2))
if __name__=="__main__":
    main()
