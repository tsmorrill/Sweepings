from math import gcd


def rho(n: int) -> int:
    def poly(t: int) -> int:
        return (t**2 + 1) % n
    x = 0
    y = 0
    d = 1
    iter = 0
    while d == 1:
        x = poly(x)
        y = poly(poly(y))
        d = gcd(abs(x-y), n)
        iter += 1
    if d != n:
        judgement = "succeeded"
    else:
        judgement = "failed"
    print(f"Algorithm {judgement} after {iter} steps.")
    return d


if __name__ == "__main__":
    N = 122333444455555
    print(rho(N))
