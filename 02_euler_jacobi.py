"""Experiment 1 - Euler-Jacobi / Solovay-Strassen probable-prime test.

Install once: python -m pip install sympy
The Jacobi symbol is calculated by SymPy (a mathematics library).
"""
import math
import secrets
from sympy import jacobi_symbol


def euler_jacobi(n, k=5):
    if k <= 0:
        raise ValueError("Rounds k must be positive")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = 2 + secrets.randbelow(n - 3)
        if math.gcd(a, n) != 1:
            return False
        j = int(jacobi_symbol(a, n))
        if j == 0 or pow(a, (n - 1) // 2, n) != j % n:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Enter n [17]: ") or "17")
    print("Probably prime" if euler_jacobi(n) else "Composite / not prime")
