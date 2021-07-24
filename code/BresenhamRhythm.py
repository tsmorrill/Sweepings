def Bresenham(k,n):
    """Compute Euclidean rhythm of k pulses and length n."""
    list = []
    cumDiff = n - k
    pulse = True
    if k == 0:
        pulse = False
    for x in range(n):
        if cumDiff < 0:
            pulse = True
            cumDiff += n
        list.append(int(pulse))
        pulse = False
        cumDiff -= k
    return(list)

for k in range(17):
    print(k, 16, Bresenham(k, 16))
