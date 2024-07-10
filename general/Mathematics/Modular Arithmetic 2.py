#so it have 2 conditions:
# 1. a^p mod p =a
# 2. a^p-1 mod p=1
#note that p is prime number
#so we only read the power of a and the mod

def Fermats_little_theorem(a,power,mod):
    if power==mod:return a
    elif power==mod-1:return 1 
    
print(Fermats_little_theorem(273246787654,65536,65537))
