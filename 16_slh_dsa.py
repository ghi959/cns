"""Experiment 8 - REAL SLH-DSA-SHA2-128s (FIPS 205) via liboqs-python.

Install: python -m pip install liboqs-python
Native liboqs must support this stateless, pure-message SLH-DSA variant.
Do NOT use a similarly named SHAKE or prehash variant as a substitute.
Never hardcode signature private keys or randomness in real security uses.
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
    # Exact names are version-dependent. Only select the requested SHA2-128s.
    preferred = ("SLH_DSA_PURE_SHA2_128S", "SLH-DSA-SHA2-128s",
                 "SLH-DSA-PURE-SHA2-128s", "SLH_DSA_SHA2_128S")
    for name in preferred:
        if name in enabled:
            return name
    # Normalize only punctuation and case (not SHA2 vs SHAKE or prehash).
    for name in enabled:
        norm = name.upper().replace("_", "-")
        if ("SLH-DSA" in norm and "SHA2-128S" in norm
                and "PREHASH" not in norm and "-PH-" not in norm):
            return name
    raise RuntimeError("SLH-DSA-SHA2-128s not enabled in liboqs. Available: " + str(enabled))


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
