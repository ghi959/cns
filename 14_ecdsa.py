"""Experiment 8 - REAL P-256 ECDSA (SHA-256) using cryptography.

Install: python -m pip install cryptography
The private scalar is UID-derived exactly as in the original lab assignment.
THIS IS INSECURE OUTSIDE THE LAB: actual secret keys require cryptographic RNGs.
"""
import hashlib
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

UID = "2024300214"
CURVE = ec.SECP256R1()
P256_ORDER = int(
    "FFFFFFFF00000000FFFFFFFFFFFFFFFF"
    "BCE6FAADA7179E84F3B9CAC2FC632551", 16
)

digest = hashlib.sha256((UID + "CNS-DSIG-ECDSA-KEY").encode()).digest()
private_number = (int.from_bytes(digest, "big") % (P256_ORDER - 1)) + 1
private = ec.derive_private_key(private_number, CURVE)
public = private.public_key()

amount = 1000 + int(UID) % 9000
MESSAGE = (f"Transfer Rs.{amount} to Account {UID[-4:]}\n"
           f"Issued by UID: {UID}\n").encode("utf-8")

signature = private.sign(MESSAGE, ec.ECDSA(hashes.SHA256()))


def verify(msg, sig, key=public):
    try:
        key.verify(sig, msg, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False


if __name__ == "__main__":
    print("Curve: P-256; hashing: SHA-256")
    print("DER signature size:", len(signature), "bytes (can vary slightly)")
    print("Original verification:", "PASS" if verify(MESSAGE, signature) else "FAIL")
    print("Tampered verification:", "PASS" if verify(MESSAGE + b"!", signature) else "FAIL")
