# Code
```python
from pwn import * 
import json
from Crypto.Cipher import AES
from Crypto.Util import number
import hashlib
from Crypto.Util.Padding import pad, unpad

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
    
r=remote('socket.cryptohack.org',13371)

#received
r.recvuntil(b'Intercepted from Alice: ') 
alice=json.loads(r.recvline())
print('Alice\'s message: ', alice)

#send
bob=alice
bob['p']='1'
r.sendline(json.dumps(bob))

#received
r.recvuntil(b'Intercepted from Bob:')

#send
r.sendline(r.recvline()) 

#received
r.recvuntil(b'Intercepted from Alice:')
alice=json.loads(r.recvline())
print('Alice\'s message: ', alice)

print(decrypt_flag(0,alice['iv'],alice['encrypted_flag']))
```
refrence:https://hackmd.io/@DSAteam/rJyr28GgA#Parameter-Injection

# Note
1. Why in this code `bob['p']='1'`?
   Because if p is set to 1, any number modulo 1 is 0.
   Remember this `shared secret=g^ab modulo p`
2. Why in this code we send `shared secret=0` to function?
   Referred to note 1, any number modulo 1 is 0 so shared secret is 0
