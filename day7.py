from functools import lru_cache


@lru_cache
def combine(a, b, goal):
    nr_a = len(str(a))
    nr_b = len(str(b))
    nr_goal = len(str(goal))

    if nr_goal < nr_a + nr_b:
        return None
    result = 10 ** nr_b * a + b
    return result if result <= goal else None


if __name__ == '__main__':
    with open("./input/day7.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip().split(":") for line in lines]
    operations = [(int(line[0]), [int(n) for n in line[1].strip().split(" ")]) for line in lines]

    total = 0
    for op in operations:
        goal = op[0]
        results = {op[1][0]}
        for nr in op[1][1:]:
            new_results_add = {nr + result for result in results if nr + result <= goal}
            new_results_multiply = {nr * result for result in results if nr * result <= goal}
            new_results_combine = {combine(result, nr, goal) for result in results if combine(result, nr, goal)}
            results = new_results_add.union(new_results_multiply).union(new_results_combine)

        if goal in results:
            total += goal
    print(total)
