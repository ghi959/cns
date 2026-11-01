"""Experiment 3 - TEXTBOOK RSA encryption/decryption with small fixed numbers.

Toy integers only; no OAEP padding. Do not use this for real encryption.
"""
import math

p, q, e = 11, 17, 7  # fixed classroom parameters
n = p * q
phi = (p - 1) * (q - 1)
assert math.gcd(e, phi) == 1
d = pow(e, -1, phi)  # d is e inverse modulo PHI (not n)

message = int(input("Message as integer [8]: ") or "8")
if not 0 <= message < n:
    raise ValueError(f"Message must be in 0..{n-1}")

ciphertext = pow(message, e, n)
recovered = pow(ciphertext, d, n)

print("Public key (e, n):", (e, n))
print("Private key (d, n):", (d, n))
print("Ciphertext:", ciphertext)
print("Decrypted:", recovered)
