from pwn import xor

flag=bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
key='crypto{'.encode()
print(xor(flag,key).decode())#it says the new key is myXORkey
key='myXORkey'.encode()
print(xor(flag,key).decode())
