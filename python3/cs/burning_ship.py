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
        y = y_0 + delta_y / 2 + delta_y * row  # upside-down; intentional
        return complex(x, y)

    denominator = rounds // color_wrap
    dither = noise(iter=dither_size)
    wrap = 2**dither_size
    escape = escape**2
    check_in = height // 8

    def color(row: int, col: int) -> tuple:
        if not col and not row % check_in:
            print(f"{row} rows drawn.")
        z = 0j
        score = -1
        c = sample(row, col)
        bounded = True
        while bounded and score < rounds:
            z = complex(abs(z.real), abs(z.imag))
            z = z**2 + c
            score += 1
            bounded = z.real**2 + z.imag**2 - escape < 0
        hue = (score % denominator / denominator) / 6
        offset = dither[row % wrap, col % wrap]
        hue = 255 * hue + offset
        saturation = (1 - score / rounds)
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
        center=-1.75 - 0.05j,
        radius=0.1,
        width=1000,
        height=1000,
        rounds=2**9,
        escape=16,
        color_wrap=32,
    )
    image.show()
