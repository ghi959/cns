"""Experiment 8 - REAL RSA-PSS with cryptography, matching lab settings.

Install: python -m pip install cryptography
RSA-3072, e=65537, SHA-256, MGF1-SHA256, salt length 32 bytes.
Private key and PSS salt are securely generated, NOT hardcoded.
"""
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

UID = "2024300214"
amount = 1000 + int(UID) % 9000
MESSAGE = (f"Transfer Rs.{amount} to Account {UID[-4:]}\n"
           f"Issued by UID: {UID}\n").encode("utf-8")

private = rsa.generate_private_key(public_exponent=65537, key_size=3072)
public = private.public_key()

pss = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32)
signature = private.sign(MESSAGE, pss, hashes.SHA256())


def verify(msg, sig, key=public):
    try:
        key.verify(sig, msg, pss, hashes.SHA256())
        return True
    except InvalidSignature:
        return False


if __name__ == "__main__":
    print("RSA-PSS signed document:\n", MESSAGE.decode())
    print("Signature size:", len(signature), "bytes")
    print("Original verification:", "PASS" if verify(MESSAGE, signature) else "FAIL")
    changed = MESSAGE.replace(b"3214", b"3215", 1)
    print("Tampered verification:", "PASS" if verify(changed, signature) else "FAIL")
