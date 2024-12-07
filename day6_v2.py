from collections import defaultdict
import bisect

import sys
sys.setrecursionlimit(10000)


DIRECTIONS = [
    lambda i, j: (jump(obs_j[j], i, False), j), # UP
    lambda i, j: (i, jump(obs_i[i], j)), # RIGHT
    lambda i, j: (jump(obs_j[j], i), j), # DOWN
    lambda i, j: (i, jump(obs_i[i], j, False))  # LEFT
]

MOVE_DIRECTIONS = [
    (-1, 0), # UP
    (0, 1), # RIGHT
    (1, 0), # DOWN
    (0, -1)  # LEFT
]

def reach_margin(i,j):
    return not i or not j or i == m or j == n


def in_bounds(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def move(i, j, direction):
    first_visited[i][j].add(direction)
    # print(f"{i}, {j}, {direction}")

    next_i = i + MOVE_DIRECTIONS[direction][0]
    next_j = j + MOVE_DIRECTIONS[direction][1]

    if not in_bounds(next_i, next_j):
        return True

    # Change direction
    if lines[next_i][next_j] == '#':
        new_direction = (direction + 1) % len(MOVE_DIRECTIONS)
        return move(i, j, new_direction)
    else:
        # Already visited, we are entering a loop
        if direction in first_visited[next_i][next_j]:
            return False
        return move(next_i, next_j, direction)


def jump(obst, pos, incr=True):
    # where would pos be inserted in the sorted list O(logN)
    index = bisect.bisect(obst, pos)
    if incr:
        if index == len(obst):
            return None
        next_position = obst[index] - 1
        return next_position

    else:
        if index == 0:
            return None
        next_position = obst[index-1]+1
        return next_position


def teleport(i, j):
    direction = 0

    while True:
        if (i, j, direction) in visited:
            return False
        visited.append((i, j, direction))
        i, j = DIRECTIONS[direction](i, j)

        if reach_margin(i, j):
            return True
        direction = (direction + 1) % len(DIRECTIONS)


if __name__ == '__main__':
    with open("./input/day6.txt", "r") as f:
        lines = f.readlines()
    n, m = len(lines), len(lines[0])
    obstacles = []
    start_i, start_j = 0, 0
    for i, line in enumerate(lines):
        if '^' in line:
            start_i = i
            start_j = line.index("^")
        obstacles.extend([(i, j) for j, value in enumerate(line) if value == '#'])

    first_visited = [[set() for _ in range(m)] for _ in range(n)]

    # Original run
    move(start_i, start_j, 0)

    obs_i, obs_j = defaultdict(list), defaultdict(list)
    visited = []
    for i,j in obstacles:
        bisect.insort(obs_i[i], j)
        bisect.insort(obs_j[j], i)

    # Look where we add obstacles
    results = 0
    for i in range(n):
        original_line = lines[i]
        for j in range(m):
            if first_visited[i][j] and lines[i][j] == '.':
                visited = []
                lines[i] = lines[i][:j] + '#' + lines[i][j+1:]

                bisect.insort(obs_i[i], j)
                bisect.insort(obs_j[j], i)

                if not teleport(start_i, start_j):
                    results += 1

                lines[i] = original_line
                obs_i[i].remove(j)
                obs_j[j].remove(i)
    print(results)