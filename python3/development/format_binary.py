if __name__ == "__main__":
    for n in range(32):
        print("{:08b}".format(n))

# explanation:
# : - the next characters are formatting arguments
# 0 - fill with this character
# 8 - string is this many characters long
# b - display n in base 2
