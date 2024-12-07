
DIRECTIONS = [
    (-1, 0), # UP
    (0, 1), # RIGHT
    (1, 0), # DOWN
    (0, -1)  # LEFT
]

import sys
sys.setrecursionlimit(20000)

def in_bounds(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def move(i, j, direction):
    visited[i][j] = True
    print(i, j)

    next_i = i + DIRECTIONS[direction][0]
    next_j = j + DIRECTIONS[direction][1]

    if not in_bounds(next_i, next_j):
        return

    # Change direction
    if lines[next_i][next_j] == '#':
        new_direction = (direction + 1) % len(DIRECTIONS)
        move(i, j, new_direction)
    else:
        delta_i, delta_j = DIRECTIONS[direction]
        move(i + delta_i, j + delta_j, direction)



if __name__ == '__main__':
    with open("./input/day6.txt", "r") as f:
        lines = f.readlines()
    n, m = len(lines), len(lines[0])
    start_i, start_j = 0, 0
    for i, line in enumerate(lines):
        if '^' in line:
            start_i = i
            start_j = line.index("^")

    visited = [[False for _ in range(m)] for _ in range(n)]
    move(start_i, start_j, 0)

    print(sum(row.count(True) for row in visited))
