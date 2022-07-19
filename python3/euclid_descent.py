def starts_descent(list, index):
    length = len(list)
    next_index = (index + 1) % length
    return list[index] > list[next_index]


def euclid(pulses, length):
    """Calculate Euclidean rhythms"""
    res_list = [pulses * t % length for t in range(-1, length - 1)]
    bool_list = [starts_descent(res_list, index) for index in range(length)]
    return bool_list


if __name__ == "__main__":
    symbols = ["X" if bool else "." for bool in euclid(12, 19)]
    print("".join(symbols))
