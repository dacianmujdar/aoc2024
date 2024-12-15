WALL, ROBOT, BOX, SPACE = "#", "@", 'O', '.'
BIG_BOX = ['[', ']']

MOVES = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0)
}


def get_box_other_coordinates(i, j):
    if matrix[i][j] == '[':
        return i, j + 1
    return i, j - 1


def next_move(move, i, j, do_move=False):
    delta_i, delta_j = MOVES[move]

    # Up and down - We may have multiple boxes on the same level
    if move in ['^', 'v'] and matrix[i + delta_i][j + delta_j] in BIG_BOX:
        box1 = i + delta_i, j + delta_j
        box2 = get_box_other_coordinates(i + delta_i, j + delta_j)
        if next_move(move, box1[0], box1[1], do_move) and next_move(move, box2[0], box2[1], do_move):
            if do_move:
                matrix[i + delta_i][j + delta_j] = matrix[i][j]
                matrix[i][j] = SPACE
            return True
        else:
            return False
    elif matrix[i + delta_i][j + delta_j] in BIG_BOX and next_move(move, i + delta_i, j + delta_j, do_move):
        if do_move:
            matrix[i + delta_i][j + delta_j] = matrix[i][j]
            matrix[i][j] = SPACE
        return True

    if matrix[i + delta_i][j + delta_j] == WALL:
        return False
    if matrix[i + delta_i][j + delta_j] == SPACE:
        if do_move:
            matrix[i + delta_i][j + delta_j] = matrix[i][j]
            matrix[i][j] = SPACE
        return True


if __name__ == '__main__':
    with open("./input/day15.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    blank_line = lines.index("")
    matrix = lines[:blank_line]
    moves = "".join(lines[blank_line:])

    for i, line in enumerate(matrix):
        new_line = []
        for ch in line:
            if ch == WALL:
                new_line.extend(2 * [WALL])
            elif ch == BOX:
                new_line.extend(['[', ']'])
            elif ch == SPACE:
                new_line.extend(2 * [SPACE])
            elif ch == ROBOT:
                new_line.extend([ROBOT, SPACE])
        matrix[i] = new_line

    n, m = len(matrix), len(matrix[0])
    start_i, start_j = [(i, j) for i, row in enumerate(matrix) for j, char in enumerate(row) if char == ROBOT][0]

    for line in matrix:
        print("".join(line))

    i, j = start_i, start_j
    for move in moves:
        if next_move(move, i, j):
            next_move(move, i, j, True)
            delta_i, delta_j = MOVES[move]
            i += delta_i
            j += delta_j
        # print(f"---- Move: {move}")
        # for line in matrix:
        #     print("".join(line))
    total = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '[':
                total += 100 * i + j
    print(total)
