# RSA Implementation (Simple Version)
p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 3  # Public key

# Find d
for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break

print("Public Key (e,n):", (e, n))
print("Private Key (d,n):", (d, n))

# Message
M = 7

# Encryption
C = (M ** e) % n
print("Encrypted message:", C)

# Decryption
M1 = (C ** d) % n
print("Decrypted message:", M1)
