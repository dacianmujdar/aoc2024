from collections import deque, defaultdict

INFINITY = 10000000000000

def extract_numbers(line):
    expressions = line.split(',')
    index_a = expressions[0].index('+')
    index_b = expressions[1].index('+')
    return int(expressions[0][index_a:]), int(expressions[1][index_b:])


def extract_result(line):
    expressions = line.split(',')
    index_a = expressions[0].index('=')
    index_b = expressions[1].index('=')
    return int(expressions[0][index_a+1:]), int(expressions[1][index_b+1:])


def solve(a1, b1, a2, b2, p1, p2):
    q = deque()
    q.append((0, 0, 0))
    visited = defaultdict(lambda: defaultdict(bool))

    while q:
        i, j, cost = q.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = True
        # print(f"{i}, {j}, {cost}")
        if i == p1 and j == p2:
            return cost

        for k in range(1, 4):
            if i + k * a2 <= p1 and j + k * b2 <= p2:
                q.append((i + k * a2, j + k * b2, cost + k))

        if i + a1 <= p1 or j + b1 <= p2:
            q.append((i + a1, j + b1, cost + 3))

    return 0


if __name__ == '__main__':
    with open("./input/day13.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    problems = []
    for problem in range(0, len(lines), 4):
        a1, b1 = extract_numbers(lines[problem])
        a2, b2 = extract_numbers(lines[problem+1])
        p1, p2 = extract_result(lines[problem+2])
        problems.append((a1, b1, a2, b2, p1, p2))

    total = 0
    for a1, b1, a2, b2, p1, p2 in problems:
        total += solve(a1, b1, a2, b2, p1 + INFINITY, p2 + INFINITY)

    print(total)