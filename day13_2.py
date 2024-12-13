# pip install z3-solver
from z3 import Ints, solve, Solver, sat


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


def solve_z3(xa, ya, xb, yb, x, y):
    a, b = Ints('a, b')

    solver = Solver()
    solver.add(xa * a + xb * b == x)
    solver.add(ya * a + yb * b == y)
    solver.add(a > 0)
    solver.add(b > 0)

    if solver.check() == sat:
        # Get the solution
        model = solver.model()
        return 3 * model[a].as_long() + model[b].as_long()
    else:
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
        total += solve_z3(a1, b1, a2, b2, p1 + INFINITY, p2 + INFINITY)

    print(total)