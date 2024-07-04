from pwn import xor

flag=""
for i in 'label':
    temp=xor(i.encode(),13) #xor function expects bytes so we need to convert it first 
    temp=temp.decode()
    flag+=temp
print(flag)
# the answer is crypto{aloha}
