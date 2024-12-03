# Day 1 -  AOC 2024 - https://adventofcode.com/2024/day/3

from re import findall, compile

with open("input.txt", "r") as f:
    inp = f.read()

    m = findall('mul\([0-9]{1,3},[0-9]{1,3}\)', inp)
    star_1 = sum([int(x)*int(y) for x,y in [mul.strip("mul(").strip(")").split(",") for mul in m]])


    p_mul = compile("mul\([0-9]{1,3},[0-9]{1,3}\)")
    p_dont = compile("don't\(\)")
    p_do = compile("do\(\)")

    dont_positions = [r.start() for r in p_dont.finditer(inp)]+[len(inp)]
    do_positions = [0]+[r.start() for r in p_do.finditer(inp)]

    star_2 = 0
    for r in p_mul.finditer(inp):

        if do_positions[0] <= r.start() < dont_positions[0]:
            star_2 += sum([int(x)*int(y) for x,y in [r.group().strip("mul(").strip(")").split(",")]])

        elif r.start() > dont_positions[0]:

            try:
                while do_positions[0] < dont_positions[0]:
                    do_positions.pop(0)
            except:
                break

            dont_positions.pop(0)

    print(f"Star 1: {star_1}")
    print(f"Star 2: {star_2}")
