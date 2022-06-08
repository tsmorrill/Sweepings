def plain_hunt(list):
    """Calculate all plain hunt method ringing permutations of list."""
    length = len(list)
    l_res = length % 2
    list_copy = list.copy()
    seqs = [list_copy]
    pairs_count = length // 2
    for t in range(2*length - 1):
        t_res = t % 2
        pairs_adjust = t_res * (1 - l_res)      # don't adjust if length is odd
        for n in range(pairs_count - pairs_adjust):
            index = 2*n + t_res
            list[index], list[index + 1] = (list[index + 1], list[index])
        list_copy = list.copy()
        seqs.append(list_copy)
    return(seqs)


if __name__ == "__main__":
    seq = list(range(6))
    seqs = plain_hunt(seq)
    for seq in seqs:
        print(seq)
