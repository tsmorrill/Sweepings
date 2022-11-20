from random import randrange


def filter(raw_str: str):
    output = None
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if raw_str is not None:
        output = [char for char in raw_str.upper() if char in ALPHABET]
        return output


def convert(plaintext: str):  # A <-> 0
    output = None
    if plaintext is not None:
        output = [ord(char) - 65 for char in filter(test_str)]
        return output


def print_as_letters(res_list: list):
    output = None
    if res_list is not None:
        output = "".join([chr(residue + 65) for residue in res_list])
    return output


def one_time_pad(raw_str: str = None):
    plaintext = filter(raw_str)
    residues = convert(plaintext)

    print(f"Input: {raw_str}")

    print_as_letters(residues)
    print(residues)

    length = 20
    if residues is not None:
        length = len(plaintext)

    pad = [randrange(0, 26) for _ in range(length)]
    print(pad)
    print_as_letters(pad)

    ciphertext = [(residue + key) % 26 for (residue, key) in zip(residues, pad)]
    print(ciphertext)


if __name__ == "__main__":
    test_str = "Test test."
    one_time_pad(test_str)
