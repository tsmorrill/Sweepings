def Bresenham(k, n):
    """Compute Euclidean rhythm of k pulses and length n."""
    list = []
    cumDiff = -k

    for x in range(n):
        if cumDiff < 0:
            cumDiff += n
            list.append(1)
        else:
            list.append(0)
        cumDiff -= k
    return list


if __name__ == "__main__":
    for k in range(17):
        print(k, 16, Bresenham(k, 16))
