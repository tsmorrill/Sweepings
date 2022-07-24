from math import sqrt
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
    x_0, x_1, y_0, y_1 = window(center, radius, width, height)
    denominator = rounds // color_wrap

    def orbit_color(c: complex) -> float:
        inverse = 1 / denominator

        def hsv_8bit(score):
            frac = (score % denominator) * inverse
            hue = frac / 4 + 9 / 16
            hue = 255 * hue + 0.5
            saturation = (3 - frac) / 3
            saturation = 255 * saturation + 0.5
            value = 255 * (score < rounds)
            return int(hue), int(saturation), int(value)

        z = 0j
        score = 0
        while (
            -escape < z.real < escape
            and -escape < z.imag < escape
            and score < rounds
        ):
            z = z**2 + c
            score += 1
        return hsv_8bit(score)

    delta_x = (x_1 - x_0) / width
    delta_y = (y_1 - y_0) / height

    def sample(i: int, j: int) -> float:
        x = x_0 + delta_x / 2 + delta_x * i
        y = y_1 - delta_y / 2 - delta_y * j  # compensate for orientation
        return complex(x, y)

    image = Image.new("HSV", (width, height))
    pixel = image.load()
    for j in range(height):
        for i in range(width):
            c = sample(i, j)
            pixel[i, j] = orbit_color(c)
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
        color_wrap=4,
    )
    image.show()
