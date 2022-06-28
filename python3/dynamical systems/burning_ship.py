import random


def p_gen(gen):
    """Wrap a parameterized generator in a function call."""
    def wrapper(*args, **kwargs):
        generator = gen(*args, **kwargs)

        def func():
            return next(generator)
        return(func)
    return wrapper


@p_gen
def b_ship(z=0, c=0):
    """Return a generator for the burning ship map."""
    while True:
        yield z
        z = abs(z.real) + abs(z.imag)*1j
        z *= z
        z += c


if __name__ == "__main__":
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    c = x + y*1j
    generator = b_ship(c=c)
    for _ in range(8):
        print(generator())
