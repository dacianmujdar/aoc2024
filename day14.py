import operator
from functools import reduce


def get_quadrant(i, j):
    if i == mid_n or j == mid_m:
        return 4 # middle
    top_i = i > mid_n
    top_j = j > mid_m

    if top_i and top_j:
        return 0
    if not top_i and not top_j:
        return 1
    if not top_i and top_j:
        return 2
    if top_i and not top_j:
        return 3


if __name__ == '__main__':
    with open("./input/day14.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    robots = []
    for line in lines:
        inputs = line.split(" ")
        start = inputs[0][2:].split(",")
        x, y = int(start[0]), int(start[1])

        speed = inputs[1][2:].split(",")
        sx, sy = int(speed[0]), int(speed[1])
        robots.append((x, y, sx, sy))

    m, n = 101, 103
    # m, n = 11, 7
    mid_m, mid_n = m // 2, n // 2
    steps = 100

    new_robots = []
    for robot in robots:
        j, i, sj, si = robot
        end_i = (i + si * steps) % n
        end_j = (j + sj * steps) % m
        new_robots.append((end_i, end_j))

    quadrants = [0] * 5
    for robot in new_robots:
        i, j = robot
        quadrants[get_quadrant(i, j)] += 1

    print(quadrants)
    print(reduce(operator.mul, quadrants[:4], 1))

    result = [["." for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            occurrences = new_robots.count((i,j))
            if occurrences:
                result[i][j] = str(occurrences)

    for line in result:
        print("".join(line))




