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
def gfrac(x):
    """Return a generator for the Gauss continued fraction map."""
    while True:
        yield x
        x = 1/x
        x -= int(x)


if __name__ == "__main__":
    x = random.uniform(0, 1)
    generator = gfrac(x)
    for _ in range(8):
        print(generator())
