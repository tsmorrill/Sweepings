def xor_shift(n):
    """Return a generator for an xor shift pseudorandom number generator."""
    while True:
        yield n
        n ^= n >> 7
        n ^= n << 9
        n ^= n >> 13
        n %= 1 << 16


if __name__ == "__main__":
    n = 10
    xshift_generator = xor_shift(n)
    for _ in range(8):
        print(xshift_generator.__next__())
