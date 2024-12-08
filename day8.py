from collections import defaultdict
from itertools import combinations


def in_bounds(node):
    i, j = node
    return i >= 0 and j >= 0 and i < n and j < m


def get_antinodes(node1, node2):
    results = []

    delta_i = node1[0] - node2[0]
    delta_j = node1[1] - node2[1]
    small_node = node1[0] + delta_i, node1[1] + delta_j
    big_node = node2[0] - delta_i, node2[1] - delta_j

    if in_bounds(small_node):
        results.append(small_node)
    if in_bounds(big_node):
        results.append(big_node)
    return results



if __name__ == '__main__':
    with open("./input/day8.txt", "r") as f:
        lines = [line.strip() for line in f]
    m, n = len(lines), len(lines[0])

    antennas = defaultdict(list)
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if lines[i][j] != '.':
                antennas[lines[i][j]].append((i,j))

    antinodes = []
    for antenna in antennas:
        print(antenna)
        if len(antennas[antenna]) < 2:
            continue
        for pair in combinations(sorted(antennas[antenna]), 2):
            antinodes.extend(get_antinodes(pair[0], pair[1]))

    antinodes = set(antinodes)
    print(len(antinodes))
