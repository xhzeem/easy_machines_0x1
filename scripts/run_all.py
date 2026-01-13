#!/usr/bin/env python3
"""
Run All Exploits - Test all vulnerabilities across machines
"""

import subprocess
import sys
import os

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

EXPLOITS = [
    ("Machine 1 - Command Injection", "m1_cmd_injection.py", ["id"]),
    ("Machine 1 - Anonymous FTP", "m1_ftp_anon.py", []),
    ("Machine 2 - PHP Backdoor", "m2_php_backdoor.py", ["id"]),
    ("Machine 3 - Node.js RCE", "m3_nodejs_rce.py", ["id"]),
    ("Machine 3 - MongoDB NoAuth", "m3_mongodb_noauth.py", []),
    ("Machine 4 - Grafana LFI", "m4_grafana_lfi.py", ["etc/passwd"]),
    ("Machine 5 - Laravel Ignition", "m5_laravel_ignition.py", ["id"]),
]

def run_exploit(name, script, args):
    """Run a single exploit script"""
    print("\n" + "=" * 60)
    print(f"[TEST] {name}")
    print("=" * 60)
    
    script_path = os.path.join(SCRIPTS_DIR, script)
    cmd = [sys.executable, script_path] + args
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        print(result.stdout)
        if result.stderr:
            print(f"[STDERR] {result.stderr}")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print("[-] Timeout expired")
        return False
    except Exception as e:
        print(f"[-] Error: {e}")
        return False

def main():
    print("=" * 60)
    print("  EASY MACHINES 0x1 - EXPLOIT TEST SUITE")
    print("=" * 60)
    
    success = 0
    failed = 0
    
    for name, script, args in EXPLOITS:
        if run_exploit(name, script, args):
            success += 1
        else:
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"  RESULTS: {success} passed, {failed} failed")
    print("=" * 60)

if __name__ == "__main__":
    main()
