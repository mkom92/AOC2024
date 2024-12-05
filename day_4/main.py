# Day 4 -  AOC 2024 - https://adventofcode.com/2024/day/4

from re import findall

rows = []

with open("input.txt", "r") as f:

    for line in f.readlines():
        rows.append([x for x in line.strip()])

columns = [[] for x in rows[0]]
x,y = len(rows[0]), len(rows)

xmas_ct = 0
x_mas_ct = 0
for m, row in enumerate(rows):
    xmas_ct += len([x for x in findall(r'(?=(XMAS|SAMX))', ''.join(row))])

    for n, val in enumerate(row):
        columns[n].append(val)

        if n < x - 3 and m < y - 3:

            word = rows[m][n] + rows[m+1][n+1] + rows[m+2][n+2] + rows[m+3][n+3]
            if word == 'XMAS' or word == 'SAMX':
                xmas_ct += 1

        if n > 2 and m < y - 3:

            word = rows[m][n] + rows[m+1][n-1] + rows[m+2][n-2] + rows[m+3][n-3]
            if word == 'XMAS' or word == 'SAMX':
                xmas_ct += 1

        if val == 'A' and 0 < n < x - 1 and 0 < m < y - 1:

            cross = [rows[m - 1][n - 1], rows[m - 1][n + 1], rows[m + 1][n - 1], rows[m + 1][n + 1]]
            if cross.count('M') == 2 and cross.count('S') == 2 and cross[0] != cross[3]:
                x_mas_ct += 1

for col in columns:
    xmas_ct += len([x for x in findall(r'(?=(XMAS|SAMX))', ''.join(col))])


print(f"Star 1: {xmas_ct}")
print(f"Star 2: {x_mas_ct}")

