def p_gen(gen):
    """Wrap a parameterized generator in a function call."""
    def wrapper(*args, **kwargs):
        generator = gen(*args, **kwargs)

        def func():
            return next(generator)
        return(func)
    return wrapper


@p_gen
def xor_shift(n):
    """Return a generator for an xor shift pseudorandom number generator."""
    len = 16
    modulus = 1 << len
    while True:
        yield n
        n ^= n >> 7
        n ^= n << 9
        n ^= n >> 13
        n %= modulus


if __name__ == "__main__":
    n = 1
    generator = xor_shift(n)
    for _ in range(8):
        print(generator())
