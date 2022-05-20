jan = list(range(1, 32))
feb = list(range(1, 29))
mar = list(range(1, 32))
apr = list(range(1, 31))
may = list(range(1, 32))
jun = list(range(1, 31))
jul = list(range(1, 32))
aug = list(range(1, 32))
spt = list(range(1, 31))
oct = list(range(1, 32))
nov = list(range(1, 31))
dec = list(range(1, 32))

year = []
for month in [jan, feb, mar, apr, may, jun, jul, aug, spt, oct, nov, dec]:
    year.extend(month)


def res_count(modulus, leap_year=False):
    year_reduced = [day % modulus for day in year]
    if leap_year:
        year_reduced.append(29 % modulus)
    for res in range(modulus):
        count = year_reduced.count(res)
        print(f"There are {count} days congruent to {res} mod {modulus}.")


if __name__ == "__main__":
    res_count(8)
