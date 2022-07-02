def valuation(n):
    if n == 0:
        return float('inf')

    valuation = 0

    while n & 1 == 0:
        valuation += 1
        n >>= 1
    return valuation


if __name__ == "__main__":
    for n in range(9):
        print(n, valuation(n), sep=' -> ')
