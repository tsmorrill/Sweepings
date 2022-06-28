def lfsr(n):
    """Return a generator for a linear feedback shift array."""
    while True:
        yield n
        bit = (n ^ (n >> 1) ^ (n >> 3) ^ (n >> 12)) & 1
        n = (n >> 1) | (bit << 15)


if __name__ == "__main__":
    n = 10
    lfsr_generator = lfsr(n)
    for _ in range(8):
        print(lfsr_generator.__next__())
