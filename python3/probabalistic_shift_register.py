import random


def p_gen(gen):
    """Wrap a parameterized generator in a function call."""

    def wrapper(*args, **kwargs):
        generator = gen(*args, **kwargs)

        def func():
            return next(generator)

        return func

    return wrapper


@p_gen
def pfsa(n, len=8, prob=0.5):
    """Return a generator for a probabalistic feedback shift array."""
    modulus = 1 << len
    n %= modulus

    while True:
        yield n
        bit = n & 1
        n >>= 1
        if random.uniform(0, 1) < prob:
            bit = 1 - bit
        bit <<= len - 1
        n += bit


if __name__ == "__main__":
    n = 0b10010110
    generator = pfsa(n)
    for _ in range(8):
        print(generator())
