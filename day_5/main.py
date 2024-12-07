# Day 5 -  AOC 2024 - https://adventofcode.com/2024/day/5

rules = {}
prints = []
rule = True

with open('input.txt', 'r') as f:

    for line in f.readlines():

        if line == '\n':
            rule = False
            pass

        if rule:
            l,r = line.strip().split('|')

            try:
                rules[l].append(r)
            except:
                rules[l] = [r]
        
        elif line != '\n':
            prints.append([x for x in line.strip().split(',')])

star1 = 0

incorrectly_ordered = []

for p in prints:

    correct = True

    for n, part in enumerate(p):
        i = 1
        while correct and n+i < len(p):
            try:
                correct = p[n:][i] in rules[part]
            except:
                correct = False
            i += 1
    
    if correct:
        star1 += int(p[int((len(p)-1)/2)])
    else:
        incorrectly_ordered.append(p)

star2 = 0

for p in incorrectly_ordered:

    ordered_prints = [0 for _ in p]
    l = len(p)

    for n, part in enumerate(p):

        list_wo_n = p[:n] + p[n+1:]
        try:
            n_position = l - len([x for x in list_wo_n if x in rules[part]]) - 1
        except:
            n_position = l - 1
        ordered_prints[n_position] = part
    
    star2 += int(ordered_prints[int((l-1)/2)])

print(f"Star 1: {star1}")
print(f"Star 2: {star2}")
