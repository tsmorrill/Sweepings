from fractions import Fraction
from math import log

x = 0.1
y = Fraction(1, 10)

print(f"x = {x}", f"y = {y}", sep="\n")
print()
print("x == y", x == y, sep=" --> ")
print("Fraction(x)==y", Fraction(x) == y, sep=" --> ")
print("x == float(y)", x == float(y), sep=" --> ")
print()
print(f"Fraction(x)={Fraction(x)}")
print(f"float(y)={float(y)}")
print()

exponent = log(Fraction(x).denominator, 2)

print(f"Denominator of Fraction(x) is 2^{exponent}.")
print(f"And even that's supposed to be {int(exponent)}, dammit!")
