"""Experiment 1 - Miller-Rabin primality test using standard Python libraries.

For n < 2**64, the specific seven bases below yield deterministic results.
For larger n, this file uses random rounds (probable-prime output only).
"""
import secrets


def miller_rabin(n, rounds=10):
    if rounds <= 0:
        raise ValueError("Rounds must be positive")
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    if n < 2**64:
        bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
    else:
        bases = [2 + secrets.randbelow(n - 3) for _ in range(rounds)]

    for base in bases:
        a = base % n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Enter n [17]: ") or "17")
    status = "Prime (n < 2^64) / probably prime" if miller_rabin(n) else "Composite / not prime"
    print(status)
