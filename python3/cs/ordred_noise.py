import numpy as np


def noise(iter: int):
    noise = np.array([[1]])
    for i in range(iter):
        noise = np.block(
            [[2 * i * noise, 2 * i * noise + 2],
             [2 * i * noise + 3, 2 * i * noise + 1]]
        )
    denominator = 2**iter**2
    return noise/denominator


if __name__ == "__main__":
    noise = noise(2)
    print(noise)
