from collections import defaultdict


def in_bounds(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def is_same_region_up(i, j):
    return in_bounds(i - 1, j) and lines[i][j] == lines[i - 1][j]


def is_same_region_left(i, j):
    return in_bounds(i, j - 1) and lines[i][j] == lines[i][j - 1]


def right_fence(i, j):
    return not in_bounds(i, j + 1) or lines[i][j] != lines[i][j + 1]


def left_fence(i, j):
    return not in_bounds(i, j - 1) or lines[i][j] != lines[i][j - 1]


def top_fence(i, j):
    return not in_bounds(i - 1, j) or lines[i][j] != lines[i - 1][j]


def bottom_fence(i, j):
    return not in_bounds(i + 1, j) or lines[i][j] != lines[i + 1][j]


def fence(i, j):
    result = 0
    # TOP
    if top_fence(i, j) and not (in_bounds(i, j - 1) and top_fence(i, j - 1) and lines[i][j] == lines[i][j - 1]):
        result += 1
    # BOTTOM
    if bottom_fence(i, j) and not (in_bounds(i, j - 1) and bottom_fence(i, j - 1) and lines[i][j] == lines[i][j - 1]):
        result += 1
    # LEFT
    if left_fence(i, j) and not (in_bounds(i - 1, j) and left_fence(i - 1, j) and lines[i][j] == lines[i - 1][j]):
        result += 1
    # RIGHT
    if right_fence(i, j) and not (in_bounds(i - 1, j) and right_fence(i - 1, j) and lines[i][j] == lines[i - 1][j]):
        result += 1
    return result


def get_region_id(i, j):
    return overwrite_ids.get(region[i][j], region[i][j])


def update_overwrites(old_id, new_id):
    for key in overwrite_ids:
        if overwrite_ids[key] == old_id:
            overwrite_ids[key] = new_id


if __name__ == '__main__':
    with open("./input/day12.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    n, m = len(lines), len(lines[0])

    regions_stats = defaultdict(tuple)
    ids = 0
    region = [[0 for _ in range(m)] for _ in range(n)]
    overwrite_ids = defaultdict(dict)

    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if is_same_region_up(i, j) and not is_same_region_left(i, j):
                # merge region up
                region_id = get_region_id(i - 1, j)
                region[i][j] = region_id
                regions_stats[region_id] = (regions_stats[region_id][0] + 1, regions_stats[region_id][1] + fence(i, j))
            if is_same_region_left(i, j) and not is_same_region_up(i, j):
                region_id = get_region_id(i, j - 1)
                region[i][j] = region_id
                regions_stats[region_id] = (regions_stats[region_id][0] + 1, regions_stats[region_id][1] + fence(i, j))

            if is_same_region_left(i, j) and is_same_region_up(i, j):
                # Merge both to north
                region_id = get_region_id(i - 1, j)
                left_region_id = get_region_id(i, j - 1)
                region[i][j] = region_id
                if region_id == left_region_id:
                    regions_stats[region_id] = (
                        regions_stats[region_id][0] + 1, regions_stats[region_id][1] + fence(i, j))
                else:
                    regions_stats[region_id] = (
                        regions_stats[region_id][0] + regions_stats[left_region_id][0] + 1,
                        regions_stats[region_id][1] + regions_stats[left_region_id][1] + fence(i, j)
                    )
                    update_overwrites(left_region_id, region_id)
                    overwrite_ids[left_region_id] = region_id
                    del regions_stats[left_region_id]

            if not is_same_region_left(i, j) and not is_same_region_up(i, j):
                ids += 1
                new_region_id = ids
                region[i][j] = new_region_id
                regions_stats[new_region_id] = (1, fence(i, j))

    total = 0
    for r in regions_stats.values():
        total += r[0] * r[1]

    print(total)
    # print(regions_stats)
    # for i in range(n):
    #     print(" ".join([str(get_region_id(i, j)) for j in range(m)]))
