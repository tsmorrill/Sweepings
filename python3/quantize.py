def quantizer(floats):
    ordered_list = sorted(floats)
    min_val = ordered_list[0]
    max_val = ordered_list[-1]

    def quantize(x):
        x = max(x, min_val)

        pairs = zip(ordered_list[:-1], ordered_list[1:])
        for a, b in pairs:
            if a <= x < b:
                midpoint = (a + b)/2
                x = a + (b - a)*int(x > midpoint)
                return x

        return max_val
    return quantize


if __name__ == "__main__":
    floats = [30.1, 40.2, 50.3, 60.4]
    quantize = quantizer(floats)
    for i in range(10):
        x = 99*i/10
        print(x, quantize(x))
