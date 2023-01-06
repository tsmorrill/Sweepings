def main(*args):
    terms = list(args)
    top = terms.pop()
    bottom = 1
    while len(terms) > 0:
        top, bottom = bottom, top
        top += terms.pop()*bottom
    if bottom == 1:
        print(top)
    else:
        print(f"{top} / {bottom}")


if __name__ == "__main__":
    main(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
