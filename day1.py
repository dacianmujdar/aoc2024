if __name__ == '__main__':
    with open("./input/day1.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip().split("   ") for line in lines]

    v1 = sorted([int(value[0]) for value in lines])
    v2 = sorted([int(value[1]) for value in lines])

    print(sum(abs(v1[i] - v2[i]) for i in range(len(v1))))

    total = 0
    for value in v1:
        freq = len([v for v in v2 if v == value])
        total += freq * value
    print(total)
