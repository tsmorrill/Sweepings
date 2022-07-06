note_to_residue = {"C":   0,
                   "Cs":  1, "Db":  1,
                   "D":   2,
                   "Ds":  3, "Eb":  3,
                   "E":   4,
                   "F":   5,
                   "Fs":  6, "Gb":  6,
                   "G":   7,
                   "Gs":  8, "Ab":  8,
                   "A":   9,
                   "As": 10, "Bb": 10,
                   "B":  11}

residue_to_note = {0:  ("C",  None),
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
        letter, enharmonic = residue_to_note[n % 12]
        octave = str(n//12 - 1)
        if enharmonic:
            print(f"{letter}{octave} = {enharmonic}{octave} = {n}")
        else:
            print(f"{letter}{octave} = {n}")
