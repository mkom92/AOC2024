# Day 6 -  AOC 2024 - https://adventofcode.com/2024/day/6

# Global variables
directions = {'^': (0,-1), 'v': (0,1), '<': (-1,0), '>': (1,0)}
curr_dir = (0,0)
dir_keys = directions.keys()
position = [0,0]
area = []

with open('input.txt','r') as f:

    for n,  line in enumerate(f.readlines()):

        line = list(line.strip())
        
        for m, item in enumerate(line):

            if item in dir_keys:
                position = [m,n]
                curr_dir = directions[item]

        area.append(line)

def star_1(area, position, curr_dir):

    visited = set()
    move = True

    while move:

        move = False
        area[position[1]][position[0]] = 'X'
        visited.add((position[0], position[1]))

        next_position = [position[0] + curr_dir[0], position[1] + curr_dir[1]]

        try:
            if area[next_position[1]][next_position[0]] == '#':
                curr_dir = (-curr_dir[1], curr_dir[0])  # turn right
                position = [position[0] + curr_dir[0], position[1] + curr_dir[1]]
            else:
                position = next_position

            move = True
        except:
            break

    return len(visited)

def star_2(area, position, curr_dir):

    """
    1. Start the path
    2. Collect the blockade positions in an array
    3. Once 3 blocades are collected, start checking for loops
    3.1. Get a temp array arr = [x[hor_or_ver] for x in blocades[(len(blocades)+1)%4::4]]
    3.2. Keep on moving in the current direction until you face a blocade or get into a position that would result in a loop
    3.3. If you face a blocade, turn right and continue
    3.4. If you can place an obstacle to cause a loop, add its position to an obstacle array and carry on
    4. Return the number of obstacles placed

    5. Thing to considered - an obstacle can be placed towards a blocade used for any turn, not only 'next right'
    5.1. This mean that another iteration may be needed to check if that results in a loop or not
    """

    blocades = []
    obstacles = set()
    hor_or_ver = 0 if curr_dir[0] != 0 else 1
    move = True

    while move:

        move = False
        # area[position[1]][position[0]] = 'X' # Uncomment to visualize the path

        next_position = [position[0] + curr_dir[0], position[1] + curr_dir[1]]

        try:
            if area[next_position[1]][next_position[0]] == '#':

                blocades.append(next_position.copy())
                curr_dir = (-curr_dir[1], curr_dir[0])  # turn right
                position = [position[0] + curr_dir[0], position[1] + curr_dir[1]]
                hor_or_ver = 1 if hor_or_ver == 0 else 0

            else:

                if len(blocades) >= 3:
                    valid_blocades = [x[hor_or_ver] for x in blocades[(len(blocades)+1)%4::4]]
                    pos_to_check = position[hor_or_ver]

                    if pos_to_check in valid_blocades:
                        obstacles.add((next_position[0], next_position[1]))
                
                position = next_position
            move = True
        except:
            break

    print("Obstacles placed at positions:", obstacles)

    return len(obstacles)

if __name__ == "__main__":

    print(f"Visited positions: {star_1(area, position, curr_dir)}")
    print(f"Obstacles placed: {star_2(area, position, curr_dir)}")