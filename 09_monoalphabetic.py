"""Experiment 2 - Monoalphabetic substitution with UID-based shuffle.

The assignment specifically says random.seed(UID), then shuffle the alphabet.
This demo uses a local random.Random instance with that same seed, avoiding
alteration of the global generator. Predictable shuffled keys are NOT secure.
"""
import random
import string

UID = 2024300214
ALPHABET = string.ascii_uppercase
letters = list(ALPHABET)
random.Random(UID).shuffle(letters)
KEY = "".join(letters)


def mono(text, decrypt=False):
    source, target = (KEY, ALPHABET) if decrypt else (ALPHABET, KEY)
    table = str.maketrans(source, target)
    return text.upper().translate(table)


if __name__ == "__main__":
    message = input("Plaintext [HELLO]: ") or "HELLO"
    encrypted = mono(message)
    print("UID shuffle key:", KEY)
    print("Encrypted:", encrypted)
    print("Decrypted:", mono(encrypted, decrypt=True))
