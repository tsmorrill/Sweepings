import math


def is_purchasable(a, b, n):
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive")
    if n == 0:
        return True
    d = math.gcd(a, b)
    if n % d != 0:
        return False
    a, b = max(a, b) // d, min(a, b) // d
    inv = pow(b, -1, a)
    mult = inv * n % a
    return n - mult * b >= 0


if __name__ == "__main__":
    for i in range(24):  # largest unpurchasable n is (a*b - a - b)
        string = "" if is_purchasable(5, 7, i) else "not "
        print(f"{i} is {string}purchasable with five- and seven-packs")
