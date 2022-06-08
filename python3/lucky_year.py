"""Find all nontrivial lucky years.

A year is lucky if its probabilty of appearing uninterrupted on a Powerball
ticket matches itself modulo 100. All years ending in '00' are trivially lucky.

https://mathsfeed.blog/problem-its-my-lucky-year/"""

import numpy
import scipy.special


def count_outcomes(century, decade):
    if century >= decade:
        return 0
    pool_size = 69 - (decade - century + 1)
    return scipy.special.binom(pool_size, 3)


def prob(century, decade):
    outcomes = count_outcomes(century, decade)
    SIXTY_NINE_CHOOSE_FIVE = 11238513
    return outcomes/SIXTY_NINE_CHOOSE_FIVE


def two_sig_figures(t):
    if t == 0:
        return 0
    exp = 2 - int(numpy.log10(t))
    return int(t * 10**exp)


def is_lucky(century, decade):
    chance = prob(century, decade)
    return decade == two_sig_figures(chance)


def all_years():
    for century in range(1, 70):
        for decade in range(century, 70):
            if is_lucky(century, decade):
                pad = "0" * int(century < 10)

                year = 100*century + decade

                chance = prob(century, decade)
                chance = numpy.format_float_scientific(chance, precision=4)

                print(f"Probability to see {pad}{year}: {chance}")


if __name__ == "__main__":
    all_years()


"""
Probability to see 0118: 1.8530e-03
Probability to see 0239: 3.9996e-04
Probability to see 0319: 1.9665e-03
Probability to see 0520: 2.0844e-03
Probability to see 0822: 2.2071e-03
Probability to see 0844: 4.4134e-04
Probability to see 0960: 6.0506e-05
Probability to see 1023: 2.3344e-03
Probability to see 1224: 2.4665e-03
Probability to see 1348: 4.8547e-04
Probability to see 1526: 2.6035e-03
Probability to see 1727: 2.7456e-03
Probability to see 1928: 2.8926e-03
Probability to see 1953: 5.3245e-04
Probability to see 2230: 3.0449e-03
Probability to see 2532: 3.2024e-03
Probability to see 2558: 5.8237e-04
Probability to see 2733: 3.3652e-03
Probability to see 3035: 3.5335e-03
Probability to see 3163: 6.3532e-04
Probability to see 3337: 3.7073e-03
Probability to see 3538: 3.8866e-03
Probability to see 3840: 4.0717e-03
Probability to see 3869: 6.9137e-04
Probability to see 4142: 4.2626e-03
"""
