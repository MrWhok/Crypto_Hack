import requests

temp=requests.get("https://aes.cryptohack.org/block_cipher_starter/encrypt_flag")
ciphertexts=temp.json()["ciphertext"]
print(ciphertexts)
temp=requests.get(f"https://aes.cryptohack.org/block_cipher_starter/decrypt/{ciphertexts}")
plaintext=temp.json()["plaintext"]
print(bytes.fromhex(plaintext))
