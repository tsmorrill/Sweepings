import random


def gfrac(x):
    """Return a generator for the Gauss continued fraction map."""
    while True:
        yield x
        x = 1/x
        x -= int(x)


if __name__ == "__main__":
    x = random.uniform(0, 1)
    gfrac_generator = gfrac(x)
    for _ in range(8):
        print(gfrac_generator.__next__())
