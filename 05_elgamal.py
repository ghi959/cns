"""Experiment 3 - ElGamal with small hardcoded parameters.

The ephemeral exponent k is FIXED for learning; real ElGamal must use a fresh
unpredictable k for every encryption. This is NOT secure encryption.
"""
import math

p, g = 23, 5
private_x = 6
k = 7
public_y = pow(g, private_x, p)
message = int(input("Message as integer (0..22) [10]: ") or "10")
if not 0 <= message < p:
    raise ValueError("The message must be between 0 and 22")
assert math.gcd(public_y, p) == 1

# Encrypt (two ciphertext components)
c1 = pow(g, k, p)
c2 = (message * pow(public_y, k, p)) % p

# Decrypt
shared = pow(c1, private_x, p)
recovered = (c2 * pow(shared, -1, p)) % p

print("Public (p, g, y):", (p, g, public_y))
print("Ciphertext (c1, c2):", (c1, c2))
print("Decrypted:", recovered)
