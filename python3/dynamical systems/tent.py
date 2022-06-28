import random


def p_generator(p_gen):
    """Wrap a parameterized generator in a function call."""
    def wrapper(*args, **kwargs):
        generator = p_gen(*args, **kwargs)

        def func():
            return next(generator)
        return(func)
    return wrapper


@p_generator
def tent(x, m=1.5):
    """Return a generator for the tent map."""

    while True:
        yield x
        x = m*min(x, 1-x)


if __name__ == "__main__":
    x = random.uniform(0, 1)
    generator = tent(x)
    for _ in range(8):
        print(generator())
