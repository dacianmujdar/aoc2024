from collections import deque


def in_bounds(i,j):
    return i >= 0 and j >= 0 and i < n and j < m


def bf(start_i, start_j):
    q = deque()
    step = 0
    q.append((start_i, start_j, step))

    while q and step < 9:
        step += 1
        while q and q[0][2] == step - 1:
            prev_node = q.popleft()
            i, j, trail = prev_node
            if in_bounds(i + 1, j) and lines[i+1][j] == str(step):
                q.append((i + 1, j, step))
            if in_bounds(i - 1, j) and lines[i-1][j] == str(step):
                q.append((i - 1, j, step))
            if in_bounds(i, j + 1) and lines[i][j+1] == str(step):
                q.append((i, j + 1, step))
            if in_bounds(i, j - 1) and lines[i][j-1] == str(step):
                q.append((i, j - 1, step))
    if step == 9:
        # return len(set(q)) for part 1
        return len(q)
    return 0


if __name__ == '__main__':
    with open("./input/day10.txt", "r") as f:
        lines = [line.strip() for line in f]
    m, n = len(lines), len(lines[0])

    total = 0
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if lines[i][j] == '0':
                total += bf(i, j)
    print(total)
