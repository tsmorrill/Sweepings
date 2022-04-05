def euclid(t, k, n):
    """Determine whether a pulse occurs on beat t in the (k,n) Euclidean rhythm.
    """
    rollover = (k*(t) % n) > (k*(t+1) % n)
    return(rollover)


if __name__ == "__main__":
    for t in range(16):
        print(t, euclid(t, 3, 8))
