# RSA ALGORITHM
1. Select prime number between p and q, p!=q
2. N=p*q
3. ϕ(N)=(p-1)*(q-1)
4. Select e for `public key`, with rules:
                                     1. GCD(e,ϕ(N))=1
                                     2. 1<e<ϕ(N)
5. Calculate d for `private key`, d=e^-1 mod N. We can use this code in python
     ```
     pow(e,-1,N)
     ```c

# RSA Encryption
M = Plaintext, which is M < N.
If we want to get the ciphertext, we can do C=M^e mod N. We can use this code in python
  ```
  C=pow(M,e,N)
  ```c
