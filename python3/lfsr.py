def p_gen(gen):
    """Wrap a parameterized generator in a function call."""
    def wrapper(*args, **kwargs):
        generator = gen(*args, **kwargs)

        def func():
            return next(generator)
        return(func)
    return wrapper


@p_gen
def lfsr(n):
    """Return a generator for a linear feedback shift array."""
    n += int(n == 0)                        # correct degenerate initialization
    while True:
        yield n
        bit = (n ^ (n >> 1) ^ (n >> 3) ^ (n >> 12)) & 1
        n = (n >> 1) | (bit << 15)


if __name__ == "__main__":
    n = 1
    generator = lfsr(n)
    for _ in range(8):
        print(generator())
