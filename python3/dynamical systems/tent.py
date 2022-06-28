import random


def tent(x):
    """Return a generator for the tent map."""
    m = 1.5

    while True:
        yield x
        x = m*min(x, 1-x)


if __name__ == "__main__":
    x = random.uniform(0, 1)
    tent_generator = tent(x)
    for _ in range(8):
        print(tent_generator.__next__())
