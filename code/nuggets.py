import math


def is_purchasable(a, b, n):
    if a <= 0:
        raise ValueError("a must be positive")
    if b <= 0:
        raise ValueError("b must be positive")
    if n == 0:
        return True
    d = math.gcd(a, b)
    if not n/d:
        return False
    a, b = max(a, b)//d, min(a, b)//d
    inv = pow(b, -1, a)
    mult = inv*n % a
    return n - mult*b >= 0


if __name__ == "__main__":
    for i in range(24):
        string = "" if is_purchasable(5, 7, i) else "not "
        print(f"{i} is {string}purchasable with five- and seven-packs")
