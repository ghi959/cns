"""Experiment 1 - Fermat probable-prime test (standard Python libraries).

Usage: python 01_fermat.py
A passing test means PROBABLY prime, not a proof. Never use this as your
sole primality test in a real cryptographic key generator.
"""
import math
import secrets


def fermat(n, k=5):
    if k <= 0:
        raise ValueError("Rounds k must be positive")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = 2 + secrets.randbelow(n - 3)  # 2 <= a <= n-2
        if math.gcd(a, n) != 1:
            return False
        if pow(a, n - 1, n) != 1:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Enter n [17]: ") or "17")
    print("Probably prime" if fermat(n) else "Composite / not prime")
