"""Experiment 3 - Classical Diffie-Hellman with hardcoded tiny parameters.

This agrees on secret MATERIAL; it does not encrypt any messages.
"""

p, g = 23, 5
alice_private = 6
bob_private = 15

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

alice_shared = pow(bob_public, alice_private, p)
bob_shared = pow(alice_public, bob_private, p)

print("Alice public:", alice_public)
print("Bob public:", bob_public)
print("Alice shared:", alice_shared)
print("Bob shared:", bob_shared)
print("Agreement:", alice_shared == bob_shared)
