"""Experiment 2 - Caesar cipher using your UID-derived key 19.

Use the standard string character functions; no third-party packages required.
"""
import string

KEY = 19
ALPHABET = string.ascii_uppercase


def caesar(text, key=KEY, decrypt=False):
    if decrypt:
        key = -key
    out = ""
    for ch in text.upper():
        if ch in ALPHABET:
            index = ALPHABET.index(ch)
            out += ALPHABET[(index + key) % 26]
        else:
            out += ch
    return out


if __name__ == "__main__":
    message = input("Plaintext [HELLO]: ") or "HELLO"
    encrypted = caesar(message)
    print("Key:", KEY)
    print("Encrypted:", encrypted)
    print("Decrypted:", caesar(encrypted, decrypt=True))
