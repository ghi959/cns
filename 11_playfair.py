"""Experiment 2 - Playfair cipher using UID keyword UYECO.

The key grid is FIXED to make the practical shorter. I and J are combined.
Decryption recovers prepared plaintext (including any inserted filler X/Q).
"""
import string

KEYWORD = "UYECO"
MATRIX = ["UYECO", "ABDFG", "HIKLM", "NPQRS", "TVWXZ"]
POSITIONS = {ch: (r, c) for r, row in enumerate(MATRIX)
             for c, ch in enumerate(row)}


def clean(text):
    return "".join(ch for ch in text.upper().replace("J", "I")
                   if ch in string.ascii_uppercase)


def make_pairs(text):
    text = clean(text)
    pairs = []
    i = 0
    while i < len(text):
        first = text[i]
        if i + 1 == len(text) or text[i + 1] == first:
            second = "X" if first != "X" else "Q"
            i += 1
        else:
            second = text[i + 1]
            i += 2
        pairs.append(first + second)
    return pairs


def playfair(text, decrypt=False):
    if decrypt:
        clean_cipher = clean(text)
        if len(clean_cipher) % 2 != 0:
            raise ValueError("Ciphertext must have an even number of letters")
        pairs = [clean_cipher[i:i + 2] for i in range(0, len(clean_cipher), 2)]
        step = -1
    else:
        pairs = make_pairs(text)
        step = 1

    output = ""
    for first, second in pairs:
        r1, c1 = POSITIONS[first]
        r2, c2 = POSITIONS[second]
        if r1 == r2:
            output += MATRIX[r1][(c1 + step) % 5]
            output += MATRIX[r2][(c2 + step) % 5]
        elif c1 == c2:
            output += MATRIX[(r1 + step) % 5][c1]
            output += MATRIX[(r2 + step) % 5][c2]
        else:
            output += MATRIX[r1][c2] + MATRIX[r2][c1]
    return output


if __name__ == "__main__":
    message = input("Plaintext [HELLO]: ") or "HELLO"
    cipher = playfair(message)
    print("Keyword:", KEYWORD)
    print("Matrix:", MATRIX)
    print("Encrypted:", cipher)
    print("Decrypted prepared plaintext:", playfair(cipher, decrypt=True))
