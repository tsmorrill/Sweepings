import random


def henon(x, y):
    """Return a generator for the Henon map."""
    a = 1.4
    b = 0.3

    while True:
        yield x
        x, y = 1 - a*x**2 + y, b*x


if __name__ == "__main__":
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    henon_generator = henon(x, y)
    for _ in range(8):
        print(henon_generator.__next__())
