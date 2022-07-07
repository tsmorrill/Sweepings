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
def mandelbrot(z=0, c=0):
    """Return a generator for the Mandelbrot map."""
    while True:
        yield z
        z *= z
        z += c


if __name__ == "__main__":
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    c = x + y * 1j
    generator = mandelbrot(c=c)
    for _ in range(8):
        print(generator())
