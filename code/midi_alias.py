dict = {0:  ("C",  None),
        1:  ("Cs", "Db"),
        2:  ("D",  None),
        3:  ("Ds", "Eb"),
        4:  ("E",  None),
        5:  ("F",  None),
        6:  ("Fs", "Gb"),
        7:  ("G",  None),
        8:  ("Gs", "Ab"),
        9:  ("A",  None),
        10: ("As", "Bb"),
        11: ("B",  None)}

if __name__ == "__main__":
    for n in range(12, 128):
        letter, enharmonic = dict[n % 12]
        octave = str(n//12 - 1)
        if enharmonic:
            print(f"{letter}{octave} = {enharmonic}{octave} = {n}")
        else:
            print(f"{letter}{octave} = {n}")
