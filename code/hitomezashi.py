import random


def hitomezashi(n):
    box_draw = ["┏", "┗", "┓", "┛",                         # default glyph
                "┓", "┛", "┏", "┗",                         # mirror vertical
                "┗", "┏", "┛", "┓",                         # mirror horizontal
                "┛", "┓", "┗", "┏"]                         # mirror v & h
    twos = random.choices([0, 1], k=n)
    ones = random.choices([0, 1], k=n)
    for row in range(n):
        pointers = []
        for col in range(n):
            pointer = 8*(row % 2) + 4*(col % 2) + 2*twos[row] + 1*ones[col]
            pointers.append(pointer)
        string = "".join(box_draw[p] for p in pointers)
        print(string)


if __name__ == "__main__":
    hitomezashi(50)
