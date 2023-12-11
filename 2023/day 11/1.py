import os
from collections import deque

file_path = os.path.join('./2023/day 11', 'input.txt')
grid = open(file_path, 'r').read().strip().splitlines()

emptyr = [r for r, row in enumerate(grid) if all (ch == '.' for ch in row)]
emptyc = [c for c, col in enumerate(zip(*grid)) if all (ch == '.' for ch in col)]

points = []

for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c != '.':
            points.append((i,j))


def count(part2):
    total = 0
    scale = 1000000 if part2 else 2
    for i, (r1, c1) in enumerate(points):
        for (r2,c2) in points[:i]:
            for r in range(min(r1,r2), max(r1,r2)):
                total += scale if r in emptyr else 1
            for c in range(min(c1,c2), max(c1,c2)):
                total += scale if c in emptyc else 1
    return total

for p in [False, True]:
    print(count(p))