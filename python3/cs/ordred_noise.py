import numpy as np


def noise(iter: int):
    if iter == 0:
        noise = np.array([[0]])
    else:
        noise = np.array([[0, 2], [3, 1]])
        for i in range(1, iter):
            noise = np.block(
                [[4 * noise, 4 * noise + 2],
                 [4 * noise + 3, 4 * noise + 1]]
            )
        noise = noise / 2**(2 * iter)
    return noise


if __name__ == "__main__":
    noise = noise(3)
    print(noise)
