dict = {0:  "C", 1: "Db",  2:  "D",  3: "Eb",
        4:  "E", 5:  "F",  6: "Gb",  7:  "G",
        8: "Ab", 9:  "A", 10: "Bb", 11:  "B"}

if __name__ == "__main__":
    for n in range(12, 128):
        letter = dict[n % 12]
        number = str(n//12 - 1)
        print(f"{letter}{number} = {n}")
