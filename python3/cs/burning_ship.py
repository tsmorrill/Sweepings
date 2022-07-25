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
):

    denominator = rounds // color_wrap

    def color(row: int, col: int) -> float:
        x_0, x_1, y_0, y_1 = window(center, radius, width, height)
        delta_x = (x_1 - x_0) / width
        delta_y = (y_1 - y_0) / height

        def sample(row: int, col: int) -> float:
            x = x_0 + delta_x / 2 + delta_x * col
            y = y_1 - delta_y / 2 - delta_y * row  # compensate for orientation
            return complex(x, y)
        z = 0j
        score = 0
        c = sample(row, col)
        while (
            z.real**2 + z.imag**2 < escape**2
            and score < rounds
        ):
            z = complex(abs(z.real), abs(z.imag))
            z = z**2 + c
            score += 1

        inverse = 1 / denominator

        def hsv_8bit(score):
            hue = (score % denominator) * inverse / 6
            hue = 255 * hue + 0.5
            saturation = (4 - score * inverse) / 4
            saturation = 255 * saturation + 0.5
            value = (255 - 8) * (score < rounds)
            return int(hue), int(saturation), int(value)

        return hsv_8bit(score)

    hsv_array = np.array(
        [[color(row, col) for col in range(width)] for row in range(height)],
        dtype="uint8"
    )
    image = Image.fromarray(hsv_array, mode="HSV")
    return image


if __name__ == "__main__":
    image = fractal(
        center=-1.75 - 0.05j,
        radius=0.1,
        width=800,
        height=600,
        rounds=2**9,
        escape=16,
        color_wrap=16,
    )
    image.show()
