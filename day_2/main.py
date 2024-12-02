# # Day 1 -  AOC 2024 - https://adventofcode.com/2024/day/2


def star(star_2: bool, report: list, removed_levels = 0) -> bool:

    is_asc = report[0] < report[1]

    for n, val_2 in enumerate(report[1:]):

        diff = val_2 - report[n]
        is_safe = True

        if is_asc and (1 <= diff <= 3) or not is_asc and (-3 <= diff <= -1):
                pass
        
        elif star_2:
                
            if removed_levels == 1:
                is_safe = False
                break

            else:
                is_safe = star(True, report[:n] + report[n+1:], 1)

                if not is_safe:
                    is_safe = star(True, report[:n+1] + report[n+2:], 1)

                if not is_safe and n > 0:
                    is_safe = star(True, report[:n-1] + report[n:], 1)
            
            return is_safe

        else:
            is_safe = False
            break
                
    return is_safe

star_1, star_2 = 0, 0

with open("input.txt", "r") as f:

    for line in f.readlines():

        report = [int(x) for x in line.split()]

        star_1 += int(star(False, report))
        star_2 += int(star(True, report))

print(f"Star 1 : {star_1}")
print(f"Star 2 : {star_2}")