from Crypto.Cipher import AES
import hashlib
import random


# @chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    return decrypted  #it returns with byte type

with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()

for i in range(len(words)):
    temp_key = hashlib.md5(words[i].encode()).digest()
    ciphertext="c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
    plaintext=decrypt(ciphertext, temp_key)
    if b'crypto' in plaintext:
        print(plaintext)
        




