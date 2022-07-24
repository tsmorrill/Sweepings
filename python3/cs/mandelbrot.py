from math import sqrt
from PIL import Image


def tuple_8bit(floats: tuple[float]) -> tuple[int]:
    return tuple(round(255 * float) for float in floats)


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
):
    x_0, x_1, y_0, y_1 = window(center, radius, width, height)
    image = Image.new("HSV", (width, height))
    pixel = image.load()

    delta_x = (x_1 - x_0) / width
    delta_y = (y_1 - y_0) / height

    def sample_x(i: int) -> float:
        return x_0 + delta_x / 2 + delta_x * i

    def sample_y(j: int) -> float:
        return y_1 - delta_y / 2 - delta_y * j  # compensate for orientation

    def hsv(c: complex) -> float:
        inverse = 1 / rounds

        def hue(score: int) -> float:
            frac = score * inverse
            return (frac) / 4 + 0b101 / 0b1000

        def saturation(score: int) -> float:
            frac = score * inverse
            return (3 - frac) / 3

        def value(score: int) -> float:
            return int(score < rounds)
        z = 0j
        score = 0
        while (
            -escape < z.real < escape
            and -escape < z.imag < escape
            and score < rounds
        ):
            z = z**2 + c
            score += 1
        floats = hue(score), saturation(score), value(score)
        return tuple_8bit(floats)

    for j in range(height):
        for i in range(width):
            c = complex(sample_x(i), sample_y(j))
            pixel[i, j] = hsv(c)
        if not j % round(height / 20):
            print(f"{round(j / height * 100)}% of rows drawn")
    return image


if __name__ == "__main__":
    image = fractal(
        center=-0.01558 + 0.6601j,
        radius=4E-5,
        width=1400,
        height=1400,
        rounds=2**9,
        escape=34,
    )
    image.show()
