from collections import Counter


def move_robots(robots):
    new_robots = []
    for robot in robots:
        j, i, sj, si = robot
        end_i = (i + si) % n
        end_j = (j + sj) % m
        new_robots.append((end_j, end_i, sj, si))
    return new_robots



def save_robots_to_file(robots, steps):
    result = [["." for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            occurrences = robots.count((i, j))
            if occurrences:
                result[i][j] = str(occurrences)

    with open("day_14_robots.txt", "a") as file:
        file.write("\n")
        file.write(str(steps))
        file.write("\n")
        for line in result:
            file.write("".join(line) + "\n")
        file.write("\n")


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

    for i in range(10_000):
        robots = move_robots(robots)
        j_values = [j for _, j, _, _ in robots]
        j_counts = Counter(j_values)
        most_common_j, occurrences = j_counts.most_common(1)[0]
        if occurrences > 30: # There is a line of robots > 30 maybe root of a tree ?
            save_robots_to_file([(robot[1], robot[0]) for robot in robots], i)
