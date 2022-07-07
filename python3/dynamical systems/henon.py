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
def henon(x, y, a=1.4, b=0.3):
    """Return a generator for the Henon map."""
    while True:
        yield x
        x, y = 1 - a * x**2 + y, b * x


if __name__ == "__main__":
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    generator = henon(x, y)
    for _ in range(8):
        print(generator())
