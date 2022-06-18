import numpy


def starts_ascent(list, index):
    length = len(list)
    next_index = (index + 1) % length
    return list[index] < list[next_index]


if __name__ == "__main__":
    list = numpy.random.permutation(8)
    print(list)
    for index, _ in enumerate(list):
        print(starts_ascent(list, index))
