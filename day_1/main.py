# Day 1 -  AOC 2024 - https://adventofcode.com/2024/day/1

# Read input

l_col, r_col = [], []

with open("input.txt", 'r') as f:
    for line in f.readlines():
        l = line.split()

        l_col.append(int(l[0]))
        r_col.append(int(l[1]))

l_col.sort()
r_col.sort()

# Calculate results

star1 = sum([ abs(x-y) for x,y in zip(l_col, r_col)])

print(star1)

star2 = 0
occurrences = {}

for val in l_col:

    try:
        star2 += occurrences[val]
    except:
        occurrences[val] = r_col.count(val) * val
        star2 += occurrences[val]

print(star2)