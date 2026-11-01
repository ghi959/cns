"""Experiment 2 - Vigenere cipher with your UID-derived keyword UYECO."""
import string

KEYWORD = "UYECO"
ALPHABET = string.ascii_uppercase


def vigenere(text, key=KEYWORD, decrypt=False):
    result = ""
    key_position = 0
    key = key.upper()
    for ch in text.upper():
        if ch not in ALPHABET:
            result += ch
            continue
        p = ALPHABET.index(ch)
        shift = ALPHABET.index(key[key_position % len(key)])
        c = (p - shift if decrypt else p + shift) % 26
        result += ALPHABET[c]
        key_position += 1
    return result


if __name__ == "__main__":
    message = input("Plaintext [HELLO]: ") or "HELLO"
    cipher = vigenere(message)
    print("Key:", KEYWORD)
    print("Encrypted:", cipher)
    print("Decrypted:", vigenere(cipher, decrypt=True))
