from math import log, sqrt
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
    power: int = 2,
):
    x_0, x_1, y_0, y_1 = window(center, radius, width, height)
    delta_x = (x_1 - x_0) / width
    delta_y = (y_1 - y_0) / height

    def sample(row: int, col: int) -> float:
        x = x_0 + delta_x / 2 + delta_x * col
        y = y_1 - delta_y / 2 - delta_y * row  # compensate for orientation
        return complex(x, y)

    escape_squared = escape**2
    check_in = height >> 3

    def color(row: int, col: int) -> tuple:
        if not col and not row % check_in:
            print(f"{row} rows drawn.")
        z = 0j
        score = -1
        c = sample(row, col)
        bounded = True
        while bounded and score < rounds:
            z = z**power + c
            score += 1
            bounded = z.real**2 + z.imag**2 - escape_squared < 0
        if bounded:
            value = 1
        else:
            value = (score + offset(z)) / (rounds + 1) * color_wrap
        return int(255 * value)

    def offset(z: complex):
        # https://linas.org/art-gallery/escape/smooth.html
        frac = 1 - log(log(abs(z)), power)
        return max(0, min(frac, 1))

    pix_array = np.array(
        [[color(row, col) for col in range(width)] for row in range(height)],
        dtype="uint8"
    )
    image = Image.fromarray(pix_array, mode="L")
    return image


if __name__ == "__main__":
    image = fractal(
        center=-0.7434875 + 0.1313j,
        radius=8e-5,
        width=2000,
        height=2000,
        rounds=2**10,
        escape=2**10,
        color_wrap=48,
    )
    image.show()
