from random import random


def plain_hunt(list):
    """Calculate all plain hunt method ringing permutations of list."""
    length = len(list)
    list_copy = list.copy()
    seqs = [list_copy]
    pairs_count = (length//2)
    for t in range(2*length - 1):
        t_res = t % 2                                  # offset each other loop
        for i in range(pairs_count - t_res):
            list[t_res + 2*i], list[t_res + 2*i + 1] = (list[t_res + 2*i + 1],
                                                        list[t_res + 2*i])
        list_copy = list.copy()
        seqs.append(list_copy)
    return(seqs)


if __name__ == "__main__":
    seq = list(range(1, 6))
    seqs = plain_hunt(seq)
    for seq in seqs:
        print(seq)
