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
def logistic(x, r=3.56995):
    """Return a generator for the logistic map."""
    while True:
        yield x
        x = r * x * (1 - x)


if __name__ == "__main__":
    x = random.uniform(0, 1)
    generator = logistic(x)
    for _ in range(8):
        print(generator())
