from math import sqrt
from PIL import Image


def tuple_8bit(floats: tuple[float]) -> tuple[int]:
    return tuple(round(255 * float) for float in floats)


def hsv(c: complex, rounds: int, escape: float) -> float:
    def hue(score: int) -> float:
        frac = score / rounds
        return sqrt(frac) / 4 + 0b101 / 0b1000

    def saturation(score: int) -> float:
        frac = score / rounds
        return (3 - frac) / 3

    def value(score: int) -> float:
        return int(score < rounds)
    z = 0j
    score = 0
    while abs(z) < escape and score < rounds:
        z = z**2 + c
        score += 1
    floats = hue(score), saturation(score), value(score)
    return tuple_8bit(floats)


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


def mandelbrot(
    center: complex,
    radius: float,
    width: int,
    height: int,
    rounds: int,
    escape: float,
):
    x_0, x_1, y_0, y_1 = window(center, radius, width, height)
    run = x_1 - x_0
    rise = y_1 - y_0
    height = round(rise / run * width)
    image = Image.new("HSV", (width, height))
    pixel = image.load()

    def affine_x(i: int) -> float:
        delta = (x_1 - x_0) / width
        return x_0 + delta / 2 + delta * i

    def affine_y(j: int) -> float:
        delta = (y_1 - y_0) / height
        return y_1 - delta / 2 - delta * j

    for i in range(width):
        for j in range(height):
            c = complex(affine_x(i), affine_y(j))
            pixel[i, j] = hsv(c=c, rounds=rounds, escape=escape)
        if not i % width >> 4:
            print(f"{round(i / width * 100)}% done")
    return image


if __name__ == "__main__":
    image = mandelbrot(
        center=0,
        radius=2,
        width=800,
        height=600,
        rounds=48,
        escape=100,
    )
    image.show()
