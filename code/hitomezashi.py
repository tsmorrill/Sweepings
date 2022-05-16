import random


def hitomezashi(twos, ones):
    if len(twos) != len(ones):
        raise Exception("lists must be the same length")
    n = len(twos)
    box_draw = ["┏", "┗", "┓", "┛",                         # default glyph
                "┓", "┛", "┏", "┗",                         # mirror vertical
                "┗", "┏", "┛", "┓",                         # mirror horizontal
                "┛", "┓", "┗", "┏"]                         # mirror v & h
    for row in range(len(twos)):
        pointers = []
        for col in range(n):
            pointer = 8*(row % 2) + 4*(col % 2) + 2*twos[row] + 1*ones[col]
            pointers.append(pointer)
        string = "".join(box_draw[p] for p in pointers)
        print(string)


if __name__ == "__main__":
    n = 40

    twos = ones = [n*n % 3 for n in range(n)]
    hitomezashi(twos, ones)

    print(" ")

    twos = random.choices([0, 1], k=n)
    ones = random.choices([0, 1], k=n)
    hitomezashi(twos, ones)
