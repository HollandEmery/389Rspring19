#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open("hashes.txt", 'r')# open and read hashes.txt
    passwords = open("passwords.txt", 'r')# open and read passwords.txt
    characters = string.ascii_lowercase
    
    for c in characters:
        for p in passwords:
            for has in hashes:
            # crack hashes
                y = c+p
                y = y.strip()
                has = has.strip()
                h = hashlib.sha256(y).hexdigest()
                if h == has:
                    print(y+":"+h)
            hashes = open("hashes.txt", 'r')

        passwords = open("passwords.txt", 'r')
            

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
