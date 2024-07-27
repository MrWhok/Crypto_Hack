# RSA ALGORITHM
1. Select prime numbers \( p \) and \( q \), \( p \neq q \)
2. \( N = p \times q \)
3. \( \phi(N) = (p-1) \times (q-1) \)
4. Select \( e \) for the public key, with rules:
   1. \( \text{GCD}(e, \phi(N)) = 1 \)
   2. \( 1 < e < \phi(N) \)
5. Calculate \( d \) for the private key, \( d = e^{-1} \mod \phi(N) \). We can use this code in Python:
    ```python
    d = pow(e, -1, phi_N)
    ```

# RSA Encryption
\( M \) = Plaintext, which is \( M < N \).
If we want to get the ciphertext, we can do \( C = M^e \mod N \). We can use this code in Python:
    ```python
    C = pow(M, e, N)
    ```

# RSA Decryption
\( C \) = Ciphertext.
If we want to get the plaintext, we can do \( M = C^d \mod N \). We can use this code in Python:
    ```python
    M = pow(C, d, N)
    ```
