from collections import defaultdict


def check_broken_print(print, no_go):
    for i, value in enumerate(print):
        for j in range(0, i):
            if value in no_go[print[j]]:
                # Return first broken rule
                return i, j

        invalid = any([True if value in no_go[print[j]] else False for j in range(0, i)])
        if invalid:
            return 0
    return None


if __name__ == '__main__':
    with open("./input/day5.txt", "r") as f:
        lines = f.readlines()

    separator = lines.index("\n")
    rules, prints = lines[:separator], lines[separator+1:]

    no_go = defaultdict(set)
    rules = [rule.strip().split("|") for rule in rules]
    for rule in rules:
        a, b = int(rule[0]), int(rule[1])
        no_go[b].add(a)

    prints = [[int(value) for value in pr.strip().split(',')] for pr in prints]

    result = 0

    # We assume based on the wording of the problem that every print is 'fixable', therefore we swap elements that brake
    # a rule until we reach a correct state. If this assumption is not correct, this will get stuck in an infinite loop.
    for pr in prints:
        broken_pair = check_broken_print(pr, no_go)
        if not broken_pair:
            continue

        while True:
            i, j = broken_pair
            pr[i], pr[j] = pr[j], pr[i]
            broken_pair = check_broken_print(pr, no_go)

            if not broken_pair:
                result += pr[len(pr) // 2]
                break

    print(result)