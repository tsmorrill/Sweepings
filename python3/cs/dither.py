from random import random


def ordered_dither(list, threshold=0.5):
    noise = [
        15 / 32,
        -1 / 32,
        7 / 32,
        -9 / 32,
        11 / 32,
        -5 / 32,
        3 / 32,
        -13 / 32,
        13 / 32,
        -3 / 32,
        5 / 32,
        -11 / 32,
        9 / 32,
        -7 / 32,
        1 / 32,
        -15 / 32,
    ]
    noisy_list = [val + noise[i % 16] for i, val in enumerate(list)]
    trigs = [val > threshold for val in noisy_list]
    return trigs


if __name__ == "__main__":
    list = [random() for i in range(16)]
    trigs = ordered_dither(list)
    bits = [int(trig) for trig in trigs]
    print(list)
    print(bits)
