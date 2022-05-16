def lfsr(int):                                    # linear feedback shift array
    bit = (int ^ (int >> 1) ^ (int >> 3) ^ (int >> 12)) & 1
    int = (int >> 1) | (bit << 15)
    return(int)


def xor_shift(int):
    int ^= int >> 7
    int ^= int << 9
    int ^= int >> 13
    int %= 1 << 16
    return(int)


if __name__ == "__main__":
    x = 1989
    binary = format(x, "016b")
    print(binary)
    for i in range(31):
        x = xor_shift(x)
        binary = format(x, "016b")
        print(binary)
