def plain_hunt(list):
    """Calculate all plain hunt method ringing permutations of list."""
    length = len(list)
    list_copy = list.copy()
    seqs = [list_copy]
    for t in range(2*length - 1):
        t_res = t % 2                                                  # offset
        pairs_count = (length//2) - t_res
        for i in range(pairs_count):
            list[t_res + 2*i], list[t_res + 2*i + 1] = (list[t_res + 2*i + 1],
                                                        list[t_res + 2*i])
        list_copy = list.copy()
        seqs.append(list_copy)
    return(seqs)


if __name__ == "__main__":
    seqs = plain_hunt([1, 2, 3, 4])
    for seq in seqs:
        print(seq)
