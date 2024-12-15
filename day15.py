WALL, ROBOT, BOX, SPACE = "#", "@", 'O', '.'

MOVES = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0)
}


def get_next_space(move, robot_i, robot_j):
    delta_i, delta_j = MOVES[move]
    i, j = robot_i + delta_i, robot_j + delta_j
    while matrix[i][j] == BOX:
        i += delta_i
        j += delta_j
    if matrix[i][j] == SPACE:
        return i, j
    return robot_i, robot_j  # no move possible


def make_move(move, robot_i, robot_j):
    delta_i, delta_j = MOVES[move]
    i, j = get_next_space(move, robot_i, robot_j)

    if i != robot_i or j != robot_j:
        matrix[i][j] = BOX
        matrix[robot_i + delta_i][robot_j + delta_j] = ROBOT
        matrix[robot_i][robot_j] = SPACE
        return robot_i + delta_i, robot_j + delta_j
    return robot_i, robot_j


if __name__ == '__main__':
    with open("./input/day15.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    blank_line = lines.index("")
    matrix = lines[:blank_line]
    moves = "".join(lines[blank_line:])

    n, m = len(matrix), len(matrix[0])
    start_i, start_j = [(i, j) for i, row in enumerate(matrix) for j, char in enumerate(row) if char == ROBOT][0]

    for i in range(n):
        matrix[i] = list(matrix[i])

    i, j = start_i, start_j
    for move in moves:
        i, j = make_move(move, i, j)
        # print(f"---- Move: {move}")
        # for line in matrix:
        #     print("".join(line))

    total = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == BOX:
                total += 100 * i + j
    print(total)
