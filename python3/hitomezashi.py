import random


def hitomezashi(row_choices, col_choices):
    char_str = "┏┓┗┛"
    for row, row_offset in enumerate(row_choices):
        chars = []
        for col, col_offset in enumerate(col_choices):
            i = (row + col_offset) % 2
            j = (col + row_offset) % 2
            index = 2 * i + j
            chars.append(char_str[index])
        string = "".join(chars)
        print(string)


if __name__ == "__main__":
    row_pattern = [1, 1, 1]
    col_pattern = [1, 0, 1, 0, 0]
    row_choices = [row_pattern[n % 3] for n in range(20)]
    col_choices = [col_pattern[n % 5] for n in range(79)]
    hitomezashi(row_choices, col_choices)

    print(" ")

    twos = random.choices([0, 1], k=20)
    ones = random.choices([0, 1], k=79)
    hitomezashi(twos, ones)
