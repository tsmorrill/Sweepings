import math

spam = "spam"


def eggs(t):
    return math.sin(t)


if __name__ == "__main__":
    names = [name for name in dir() if not name.startswith("_")]
    imports = ["math"]
    for name in imports:
        names.remove(name)
    print(", ".join(names))
