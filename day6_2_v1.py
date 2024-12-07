import copy

DIRECTIONS = [
    (-1, 0), # UP
    (0, 1), # RIGHT
    (1, 0), # DOWN
    (0, -1)  # LEFT
]

import sys
sys.setrecursionlimit(10000)


def in_bounds(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def move(i, j, direction):
    visited[i][j].add(direction)
    # print(f"{i}, {j}, {direction}")

    next_i = i + DIRECTIONS[direction][0]
    next_j = j + DIRECTIONS[direction][1]

    if not in_bounds(next_i, next_j):
        return True

    # Change direction
    if lines[next_i][next_j] == '#':
        new_direction = (direction + 1) % len(DIRECTIONS)
        return move(i, j, new_direction)
    else:
        # Already visited, we are entering a loop
        if direction in visited[next_i][next_j]:
            return False
        return move(next_i, next_j, direction)


if __name__ == '__main__':
    with open("./input/day6.txt", "r") as f:
        lines = f.readlines()
    n, m = len(lines), len(lines[0])
    start_i, start_j = 0, 0
    for i, line in enumerate(lines):
        if '^' in line:
            start_i = i
            start_j = line.index("^")

    visited = [[set() for _ in range(m)] for _ in range(n)]

    # Original run
    move(start_i, start_j, 0)

    first_visited = copy.deepcopy(visited)
    results = 0
    for i in range(n):
        original_line = lines[i]
        for j in range(m):
            if first_visited[i][j] and lines[i][j] == '.':
                visited = [[set() for _ in range(m)] for _ in range(n)]
                lines[i] = lines[i][:j] + '#' + lines[i][j+1:]
                if not move(start_i, start_j, 0):
                    results += 1
                lines[i] = original_line
    print(results)


