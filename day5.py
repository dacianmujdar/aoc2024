from collections import defaultdict


def test_rules(print, no_go):
    for i, value in enumerate(print):
        invalid = any([True if value in no_go[print[j]] else False for j in range(0, i)])
        if invalid:
            return 0
    return print[len(print) // 2]


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

    prints = [[int(value) for value in print.strip().split(',')] for print in prints]

    # Test if length of all prints is odd to make it easier to extract the middle
    print({len(p) % 2 for p in prints})

    result = sum([test_rules(print, no_go) for print in prints])
    print(result)
