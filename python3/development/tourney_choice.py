from functools import reduce
from random import sample

def tourney_choice(seq):
    fighters = sample(seq, 4)
    return reduce(compare, fighters)


def compare(x, y):
    print("")
    print("Choose between")
    print(f"1: {x}")
    print(f"2: {y}")
    output = None
    while output is None:
        match input("Type 1 or 2: "):
            case "1":
                output = x
            case "2":
                output = y
    return output


def main():
    winner = tourney_choice(tuple(range(8)))
    print("")
    print(f"{winner} wins.")


if __name__ == "__main__":
    main()
