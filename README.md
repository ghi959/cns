# CNS Practical — Library-Enabled Code Pack (16 Separate Python Programs)

**Prepared for:** SPIT CNS practical revision. **UID in examples:** `2024300214`.

This is the **library-enabled companion** to the no-import pack. Each `.py` file is **standalone**; run any one of the 16 directly. Fixed classroom parameters are used wherever possible. Algorithms still execute their proper mathematical operations; they do not hardcode ciphertexts or verification results.

> **Exam warning:** If the practical actually prohibits all imports, use the **no-import** pack instead. This library-enabled pack is for understanding, comparison and use *only where the relevant libraries are allowed*.

## Getting started

Use Python 3.10+ (recent `liboqs-python` releases require 3.10+). For the first 14 scripts, only SymPy and `cryptography` require installation; `math`, `random`, `string`, `hashlib` and `secrets` come with Python.

**Windows PowerShell:**

```powershell
py -m pip install sympy cryptography
py 01_fermat.py
py 12_hill.py
py 13_rsa_pss.py
```

**Linux/Ubuntu:**

```bash
python3 -m pip install sympy cryptography
python3 01_fermat.py
python3 12_hill.py
python3 13_rsa_pss.py
```

For **15 and 16**, you also need the Open Quantum Safe Python bindings **and** their native C library:

```bash
python3 -m pip install liboqs-python
python3 -c 'import oqs; print(oqs.get_enabled_sig_mechanisms())'
python3 15_ml_dsa.py
python3 16_slh_dsa.py
```

`import oqs` does **not** work just because `cryptography` is installed. Depending on OS/setup, the first import may download and compile native `liboqs`, needing Internet access, CMake, a C compiler, and Git. The requested ML-DSA-44 or SLH-DSA-SHA2-128s variant must be enabled in the underlying native build. This can be less straightforward on restricted lab machines.

## The 16 scripts

| File | Algorithm | Library feature used | Hardcoded where suitable |
|---|---|---|---|
| `01_fermat.py` | Fermat test | `math.gcd`, `secrets.randbelow`, built-in `pow` | 5 rounds |
| `02_euler_jacobi.py` | Euler–Jacobi / Solovay–Strassen | `sympy.jacobi_symbol`, `math.gcd`, `secrets` | 5 rounds |
| `03_miller_rabin.py` | Miller–Rabin | `secrets` and built-in modular `pow` | Deterministic base set for 64-bit inputs |
| `04_rsa.py` | Textbook RSA encryption/decryption | `math.gcd`, modular `pow` | p=11, q=17, e=7 |
| `05_elgamal.py` | ElGamal encryption/decryption | `math.gcd`, modular `pow` | p=23, g=5, x=6, k=7 |
| `06_diffie_hellman.py` | Diffie–Hellman agreement | Built-in modular `pow` | p=23, g=5, a=6, b=15 |
| `07_ecc_ecdh.py` | **Real P-256 ECDH** | `cryptography` (EC + HKDF) | Demo scalars 5 and 7 (unsafe in production) |
| `08_caesar.py` | Caesar cipher | `string` | UID key=19 |
| `09_monoalphabetic.py` | Monoalphabetic | `random`, `string`, `str.translate` | UID seed; mapping reproducible |
| `10_vigenere.py` | Vigenère | `string` | UID keyword UYECO |
| `11_playfair.py` | Playfair | `string` | UID 5×5 grid |
| `12_hill.py` | Hill 2×2 | `sympy.Matrix.inv_mod` | Corrected invertible UID matrix |
| `13_rsa_pss.py` | **Real RSA-PSS** | `cryptography` | RSA 3072, e=65537, SHA-256, salt length=32 (key itself random) |
| `14_ecdsa.py` | **Real P-256 ECDSA** | `hashlib`, `cryptography` | UID-derived demo scalar per original worksheet (unsafe in production) |
| `15_ml_dsa.py` | **Real ML-DSA-44** | `liboqs-python` (`oqs.Signature`) | UID message only (key generated securely) |
| `16_slh_dsa.py` | **Real SLH-DSA-SHA2-128s** | `liboqs-python` (`oqs.Signature`) | UID message only (key generated securely) |

## Quick demonstrations and expected output

Press **Enter** at the prompt to use the built-in default.

- Fermat / Euler–Jacobi / Miller–Rabin: `17` -> probably prime / prime as applicable. Passing Fermat/Euler–Jacobi rounds **does not prove** primality.
- Textbook RSA: `8` -> ciphertext `134`, recovered `8`.
- ElGamal: `10` -> ciphertext `(17, 5)`, recovered `10`.
- Diffie–Hellman: public values `8`, `19`; shared value `2`.
- P-256 ECDH: both shared values equal; HKDF-derived 32-byte keys match.
- Caesar: `HELLO` -> `AXEEH` -> `HELLO`.
- Monoalphabetic: `HELLO` -> `VSJJH` -> `HELLO`. UID shuffle key: `KZDXSRPVAGNJMUHWCFQIOTBEYL`.
- Vigenère: `HELLO` -> `BCPNC` -> `HELLO`.
- Playfair: `HELLO` -> `KURCMC` -> prepared plaintext `HELXLO`. Filler removal is ambiguous.
- Hill: `HI` -> `BA` -> `HI`. A trailing `X` may be added for odd-length messages.
- RSA-PSS: signature length `384` bytes; original `PASS`, altered `FAIL`.
- ECDSA: DER signature length typically `70–72` bytes; original `PASS`, altered `FAIL`.
- ML-DSA: when installed/enabled, expected public key `1312` bytes, signature `2420` bytes; original `PASS`, altered `FAIL`.
- SLH-DSA-SHA2-128s: when installed/enabled, expected public key `32` bytes, signature `7856` bytes; original `PASS`, altered `FAIL`.

## Important differences from the no-import pack

1. `07_ecc_ecdh.py` uses the **standard P-256 curve**, so its enormous coordinates will **not** match the toy curve points `(9,16)` and `(0,6)`.
2. `13_rsa_pss.py` uses a **new 3072-bit RSA key and randomized PSS signing** rather than a static RSA key.
3. `14_ecdsa.py` performs actual **P-256/SHA-256** signing with the original lab's UID-specific scalar, not the toy 17-element curve.
4. `15_ml_dsa.py` and `16_slh_dsa.py` are **actual algorithms via liboqs**, not educational substitutes. They require compatible native libraries.
5. For Hill, the assignment's illustrated initial matrix has no valid inverse if you only increment its bottom-right entry. This pack uses `[[21,24],[4,3]]` as the tutorial's corrected example. Ask your instructor for clarification if the exam explicitly insists on the printed derivation rule.
6. The fixed prime numbers, exponents, key matrices and private scalars are **teaching-only constants**, never valid production security practices.
7. The signature workflows demonstrate integrity and verification but do not by themselves validate the claimed sender's identity. In a real application the public key must be authenticated, often through PKI.

## What was tested before packaging

All scripts 01–14 were executed successfully in the creation environment (Python 3 + installed SymPy and `cryptography`). ML-DSA/SLH-DSA code uses the documented `liboqs-python` API, but scripts 15 and 16 **could not be run here** because native `liboqs` was not installed. Check availability on your own machine using the `get_enabled_sig_mechanisms` command above.

## References

- Lab assignment: **CNS Experiment 8 — Evaluation of Classical and Post-Quantum Digital Signature Algorithms using Docker-Based Client–Server Communication**.
- Python `cryptography` documentation: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/
- Open Quantum Safe `liboqs-python`: https://github.com/open-quantum-safe/liboqs-python
- PyPI: https://pypi.org/project/liboqs-python/
