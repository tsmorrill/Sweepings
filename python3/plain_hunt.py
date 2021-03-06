def plain_hunt(list):
    """Calculate all plain hunt method ringing permutations of list."""
    length = len(list)
    l_mod_2 = length % 2
    list_copy = list.copy()
    seqs = [list_copy]
    pairs_count = length // 2
    for t in range(2 * length - 1):
        t_mod_2 = t % 2
        pairs_adjust = t_mod_2 * (1 - l_mod_2)  # don't adjust if length is odd
        for n in range(pairs_count - pairs_adjust):
            index = 2 * n + t_mod_2
            list[index], list[index + 1] = list[index + 1], list[index]
        list_copy = list.copy()
        seqs.append(list_copy)
    return seqs


if __name__ == "__main__":
    seq = [str(n) for n in range(5)]
    seqs = plain_hunt(seq)
    for seq in seqs:
        print(" ".join(seq))


"""
0 1 2 3 4
1 0 3 2 4
1 3 0 4 2
3 1 4 0 2
3 4 1 2 0
4 3 2 1 0
4 2 3 0 1
2 4 0 3 1
2 0 4 1 3
0 2 1 4 3
"""
