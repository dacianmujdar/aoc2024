from collections import defaultdict

GENERATION_CACHE = defaultdict(dict)


def split(nr):
    if not nr:
        return [1]
    nr_s = str(nr)
    if (size := len(nr_s)) % 2 == 0:
        stone1, stone2 = int(nr_s[:size//2]), int(nr_s[size//2:])
        return [stone1, stone2]

    return [nr * 2024]


def get_splits_for_generation(stone, generations):
    if stone in GENERATION_CACHE[generations]:
        return GENERATION_CACHE[generations][stone]
    if not generations:
        return 1

    split_result = split(stone)
    result = 0
    for s in split_result:
        result += get_splits_for_generation(s, generations - 1)
    GENERATION_CACHE[generations][stone] = result
    return result


if __name__ == '__main__':
    with open("./input/day11.txt", "r") as f:
        input = f.readline()
    numbers = [int(n) for n in input.split(" ")]

    total = 0
    for number in numbers:
        total += get_splits_for_generation(number, 75)
    print(total)

