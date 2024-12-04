from functools import partial


def extract_diagonal(lines, i_start, j_start, i_step=1, j_step=1, size=4):
    result = set()
    i, j = i_start, j_start
    for k in range(size):
        result.add((i, j))
        i += i_step
        j += j_step

    rez = "".join([lines[i][j] for (i,j) in sorted(result)])
    if rez in ["XMAS", "SAMX"]:
        return result
    return set()


def get_column(lines, i_start, i_finish, j):
    if i_start > i_finish:
        i_start, i_finish = i_finish, i_start
    word = "".join([line[j] for line in lines[i_start:i_finish+1]])
    if word in ['XMAS', 'SAMX']:
        return {(i, j) for i in range(i_start, i_finish+1)}
    return set()

def get_row(lines, i, start, finish):
    if start > finish:
        start, finish = finish, start
    if lines[i][start:finish+1] in ['XMAS', 'SAMX']:
        return {(i, j) for j in range(start,finish+1)}
    return set()


def in_bounds(collection, i):
    return i >= 0 and i < len(collection)


if __name__ == '__main__':
    """ 
    I've also printed the matrix, this is not required and adds complexity to the solution
    """
    with open("./input/day4.txt", "r") as f:
        lines = f.readlines()

    i_bounds = partial(in_bounds, lines)
    j_bounds = partial(in_bounds, lines[0])
    diagonal = partial(extract_diagonal, lines)
    column = partial(get_column, lines)
    row = partial(get_row, lines)

    valid_points = set()
    solution = 0

    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch != 'X':
                continue
            if j_bounds(j+3):
                if word_indexes := row(i, j, j + 3):
                    solution += 1
                    valid_points = valid_points.union(word_indexes)
            if j_bounds(j-3):
                if word_indexes := row(i, j, j - 3):
                    solution += 1
                    valid_points = valid_points.union(word_indexes)
            if i_bounds(i+3):
                if word_indexes := column(i, i+3, j):
                    solution += 1
                    valid_points = valid_points.union(word_indexes)
            if i_bounds(i-3):
                if word_indexes := column(i, i-3, j):
                    solution += 1
                    valid_points = valid_points.union(word_indexes)
            if i_bounds(i+3) and j_bounds(j+3):
                if word_indexes := diagonal(i, j, 1, 1):
                    solution += 1
                    valid_points = valid_points.union(word_indexes)
            if i_bounds(i-3) and j_bounds(j-3):
                if word_indexes := diagonal(i, j, -1, -1):
                    solution += 1
                    valid_points = valid_points.union(word_indexes)
            if i_bounds(i+3) and j_bounds(j-3):
                if word_indexes := diagonal(i, j, 1, -1):
                    solution += 1
                    valid_points = valid_points.union(word_indexes)
            if i_bounds(i-3) and j_bounds(j+3):
                if word_indexes := diagonal(i, j, -1, 1):
                    solution += 1
                    valid_points = valid_points.union(word_indexes)

    for i, line in enumerate(lines):
        valid_line = [line[j] if (i,j) in valid_points else '.' for j in range(len(line))]
        print("".join(valid_line))
    print(solution)