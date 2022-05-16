import random


def hitomezashi(twos, ones):
    box_draw = ["┏", "┗", "┓", "┛",                         # default glyph
                "┓", "┛", "┏", "┗",                         # mirror vertical
                "┗", "┏", "┛", "┓",                         # mirror horizontal
                "┛", "┓", "┗", "┏"]                         # mirror v & h
    for row in range(len(twos)):
        pointers = []
        for col in range(len(ones)):
            pointer = 8*(row % 2) + 4*(col % 2) + 2*twos[row] + 1*ones[col]
            pointers.append(pointer)
        string = "".join(box_draw[p] for p in pointers)
        print(string)


if __name__ == "__main__":
    n = 30
    twos = ones = [n*n % 3 for n in range(n)]
    hitomezashi(twos, ones)

    print(" ")

    twos = random.choices([0, 1], k=10)
    ones = random.choices([0, 1], k=50)
    hitomezashi(twos, ones)
