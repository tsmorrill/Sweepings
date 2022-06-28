import random


def logistic(x):
    """Return a generator for the logistic map."""
    r = 3.56995
    while True:
        yield x
        x = r*x*(1-x)


if __name__ == "__main__":
    x = random.uniform(0, 1)
    logistic_generator = logistic(x)
    for _ in range(8):
        print(logistic_generator.__next__())
