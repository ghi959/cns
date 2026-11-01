"""Experiment 8 - REAL ML-DSA-44 (FIPS 204 algorithm) through liboqs-python.

Install: python -m pip install liboqs-python
Requires native liboqs with ML-DSA-44 enabled; first import may need to
build liboqs (C compiler + CMake, internet). This is an OQS lab integration,
not a production endorsement. Never hardcode post-quantum private keys.
"""
try:
    import oqs
except ImportError as exc:
    raise SystemExit("Install liboqs-python (and native liboqs); see README.md") from exc

UID = "2024300214"
amount = 1000 + int(UID) % 9000
MESSAGE = (f"Transfer Rs.{amount} to Account {UID[-4:]}\n"
           f"Issued by UID: {UID}\n").encode("utf-8")


def mechanism():
    enabled = oqs.get_enabled_sig_mechanisms()
    # Do not silently switch to a prehash or external-mu variant.
    for name in ("ML-DSA-44", "ML_DSA_44"):
        if name in enabled:
            return name
    raise RuntimeError("ML-DSA-44 not enabled in liboqs. Available: " + str(enabled))


def run():
    name = mechanism()
    with oqs.Signature(name) as signer:
        public_key = signer.generate_keypair()
        signature = signer.sign(MESSAGE)
    with oqs.Signature(name) as verifier:
        good = verifier.verify(MESSAGE, signature, public_key)
        bad = verifier.verify(MESSAGE + b"!", signature, public_key)
    print("Algorithm:", name)
    print("Public key:", len(public_key), "bytes")
    print("Signature:", len(signature), "bytes")
    print("Original verification:", "PASS" if good else "FAIL")
    print("Tampered verification:", "PASS" if bad else "FAIL")
    assert good and not bad, "Unexpected verification outcome"


if __name__ == "__main__":
    run()
