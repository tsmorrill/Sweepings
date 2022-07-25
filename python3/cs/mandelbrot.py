from math import sqrt
import numpy as np
from PIL import Image


def window(center: complex, radius: float, width: int, height: int) -> tuple:
    diagonal = sqrt(width**2 + height**2)
    delta_x = radius * width / diagonal
    delta_y = radius * height / diagonal
    x = center.real
    y = center.imag
    x_0 = x - delta_x
    x_1 = x + delta_x
    y_0 = y - delta_y
    y_1 = y + delta_y
    return x_0, x_1, y_0, y_1


def fractal(
    center: complex,
    radius: float,
    width: int,
    height: int,
    rounds: int,
    escape: float,
    color_wrap: int = 1,
    dither_size: int = 2,
):
    x_0, x_1, y_0, y_1 = window(center, radius, width, height)
    delta_x = (x_1 - x_0) / width
    delta_y = (y_1 - y_0) / height

    def sample(row: int, col: int) -> float:
        x = x_0 + delta_x / 2 + delta_x * col
        y = y_1 - delta_y / 2 - delta_y * row  # compensate for orientation
        return complex(x, y)

    denominator = rounds // color_wrap
    dither = noise(iter=dither_size)
    wrap = 2**dither_size
    escape = escape**2

    def color(row: int, col: int) -> tuple:
        if not col and not (row - 1) % (height // 8):
            print(f"{row} of {height} rows drawn.")
        z = 0j
        score = -1
        c = sample(row, col)
        bounded = True
        while bounded and score < rounds:
            z = z**2 + c
            z = z**2 + c
            z = z**2 + c
            z = z**2 + c
            score += 4
            bounded = z.real**2 + z.imag**2 - escape < 0
        hue = (score % denominator / denominator) / 6 + 2 / 3
        offset = dither[row % wrap, col % wrap]
        hue = 255 * hue + offset
        saturation = (6 - score / rounds) / 6
        saturation = 255 * saturation + offset
        value = 255 * (score < rounds)
        hsv_8bit = (int(hue), int(saturation), value)
        return hsv_8bit

    hsv_array = np.array(
        [[color(row, col) for col in range(width)] for row in range(height)],
        dtype="uint8"
    )
    image = Image.fromarray(hsv_array, mode="HSV")
    return image


def noise(iter: int):
    noise = np.array([[1]])
    for i in range(iter):
        noise = np.block(
            [[2 * i * noise, 2 * i * noise + 2],
             [2 * i * noise + 3, 2 * i * noise + 1]]
        )
    return noise / 2**(2 * iter + 1)


if __name__ == "__main__":
    image = fractal(
        center=-0.015583 + 0.660088j,
        radius=4E-5,
        width=2800,
        height=2800,
        rounds=2**9,
        escape=34,
        color_wrap=8,
    )
    image.show()
