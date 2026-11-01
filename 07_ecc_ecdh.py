"""Experiment 3 - REAL P-256 ECDH calculation using cryptography.

Install: python -m pip install cryptography
Private scalars 5 and 7 are FIXED just to make this classroom demonstration
repeatable. NEVER use such predictable keys for real ECDH.
"""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

curve = ec.SECP256R1()  # P-256 curve, rather than the old 17-element toy curve
alice_private = ec.derive_private_key(5, curve)
bob_private = ec.derive_private_key(7, curve)

alice_public = alice_private.public_key()
bob_public = bob_private.public_key()

alice_shared = alice_private.exchange(ec.ECDH(), bob_public)
bob_shared = bob_private.exchange(ec.ECDH(), alice_public)

# A key-derivation function turns the ECDH shared bytes into an encryption key.
# Constant salt/info are for repeatable demonstration only.
alice_key = HKDF(algorithm=hashes.SHA256(), length=32,
                 salt=b"CNS-EXAM-DEMO", info=b"ECDH-AES-KEY").derive(alice_shared)
bob_key = HKDF(algorithm=hashes.SHA256(), length=32,
               salt=b"CNS-EXAM-DEMO", info=b"ECDH-AES-KEY").derive(bob_shared)

print("Curve: P-256")
print("Alice public x:", alice_public.public_numbers().x)
print("Bob public x:", bob_public.public_numbers().x)
print("Shared values equal:", alice_shared == bob_shared)
print("Derived keys match:", alice_key == bob_key)
print("Key length:", len(alice_key), "bytes")
