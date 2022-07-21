from PIL import Image


def escapes(c: complex, iter: int, threshold: float = 10.0) -> float:
    z = 0j
    i = 0
    while abs(z) < threshold and i < iter:
        z = z**2 + c
        i += 1
    hue = i / iter / 3 + 0.52
    saturation = (3 - i / iter) / 3
    value = int(i < iter)
    return hue, saturation, value


def int_tuple(floats: tuple[float]) -> tuple[int]:
    return tuple(round(255 * float) for float in floats)


def mandelbrot(
    width: int,
    iter: int,
    x_0: float,
    x_1: float,
    y_0: float,
    y_1: float,
):
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
            hsv = int_tuple(escapes(c=c, iter=iter))
            pixel[i, j] = hsv
        if not i % width >> 4:
            print(f"{round(i / width * 100)}% done")
    return image


if __name__ == "__main__":
    image = mandelbrot(
        width=600,
        iter=64,
        x_0=-1.3,
        x_1=-0.5,
        y_0=0,
        y_1=0.4
    )
    image.show()
