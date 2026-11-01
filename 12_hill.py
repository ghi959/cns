"""Experiment 2 - Hill 2x2 cipher with SymPy modular matrix inverse.

Install: python -m pip install sympy
Important: the assignment's bottom-right-only correction cannot fix the
original UID matrix [[20,24],[4,2]] (its determinant is always even).
This demo uses the VALID corrected key [[21,24],[4,3]] with determinant 19
modulo 26. Use your instructor's matrix if the question specifies one.
"""
from sympy import Matrix

KEY = Matrix([[21, 24], [4, 3]])
KEY_INVERSE = KEY.inv_mod(26)


def hill(text, matrix):
    letters = "".join(c for c in text.upper() if "A" <= c <= "Z")
    if len(letters) % 2:
        letters += "X"
    result = ""
    for i in range(0, len(letters), 2):
        p = Matrix([ord(letters[i]) - 65, ord(letters[i + 1]) - 65])
        c = matrix * p
        result += chr(int(c[0]) % 26 + 65)
        result += chr(int(c[1]) % 26 + 65)
    return result


if __name__ == "__main__":
    message = input("Plaintext [HI]: ") or "HI"
    encrypted = hill(message, KEY)
    print("Key matrix:", KEY.tolist())
    print("Inverse matrix mod 26:", KEY_INVERSE.tolist())
    print("Encrypted:", encrypted)
    print("Decrypted (may include padding X):", hill(encrypted, KEY_INVERSE))
