from math import ceil

x_min = -2
x_max = 1

y_min = -1
y_max = 1

delta = 1/16
offset = delta/2

row_count = ceil((x_max - x_min)/delta)
col_count = ceil((y_max - y_min)/delta)

rows = [[(x_min + offset + delta*x) + (y_max - offset - delta*y)*1j for x in range(row_count)] for y in range(col_count)]

all_scores = []
for row in rows:
	scores = []
	for c in row:
		z = 0
		score = 0
		while score < 99 and abs(z) < 10:
			z = z**2 + c
			score += 1
		scores.append(score)
	all_scores.extend(scores)
print(set(sorted(all_scores)))