from pwn import * 
import json
from Crypto.Cipher import AES
from Crypto.Util import number
import hashlib
from Crypto.Util.Padding import pad, unpad
from sympy.ntheory import discrete_log


def get_a(g,p,A):
    a = discrete_log(p, A, g)
    print("Private key a:", a)
    return a

def get_shared_secret(B,a,p):
    shared_secret = pow(B, a, p)
    print("Shared secret:", shared_secret)
    return shared_secret

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
    
#step 1: intercept
r=remote('socket.cryptohack.org',13379)

r.recvuntil(b'Intercepted from Alice:')
r.sendline(json.dumps({"supported": ["DH64"]}))
r.recvuntil(b'Intercepted from Bob:')
r.sendline(r.recvline())
r.recvuntil(b'Intercepted from Alice:')
alice=json.loads(r.recvline())
r.recvuntil(b'Intercepted from Bob:')
bob=json.loads(r.recvline())
r.recvuntil(b'Intercepted from Alice:')
Fiv=json.loads(r.recvline())

p=int(alice['p'],16)
g=int(alice['g'],16)
A=int(alice['A'],16)
B=int(bob['B'],16)
iv=Fiv['iv']
ciphertext=Fiv['encrypted_flag']

print("p:",p)
print("g:",g)
print("A:",A)
print("B:",B)
print("iv:",iv)
print("ciphertext:",ciphertext)

#step 2:get private key
a=get_a(g,p,A)

#step 3: get shared key
shared_secret=get_shared_secret(B,a,p)

#step 4: decrypt the flag
print(decrypt_flag(shared_secret,iv,ciphertext))
