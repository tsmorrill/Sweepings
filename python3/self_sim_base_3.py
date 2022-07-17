iter = 1


def self_sim(iter=1):
    pattern = [2, 0, 1]
    old_list = pattern.copy()
    for _ in range(iter):
        new_list = []
        for val in old_list:
            new_list.extend([3*val]*3)
        new_list = [val + pattern[i % 3] for i, val in enumerate(new_list)]
        old_list = new_list
    return old_list


if __name__ == "__main__":
    print(self_sim(1))
    lengths = self_sim(3)
    for length in lengths:
        print("#"*length)
