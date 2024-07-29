from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
import primefac

e = 3
n = 742449129124467073921545687640895127535705902454369756401331
ct = 39207274348578481322317340648475596807303160111338236677373

while True:
    factors=list(primefac.primefac(n))
    p=factors[0]
    q=factors[1]
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    if d != -1 and GCD(e, phi) == 1:
        break

# flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
# pt = bytes_to_long(flag)

# print(f"n = {n}")
# print(f"e = {e}")
# print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
print(decrypted)
