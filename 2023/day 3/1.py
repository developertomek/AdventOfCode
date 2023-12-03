from collections import defaultdict
import os
file_path = os.path.join('./2023/day 3', 'input.txt')
file = open(file_path, 'r').read().strip()
lines = file.split('\n')

G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])

p1 = 0
nums = defaultdict(list)
for r in range(len(G)):
    gears = set()
    n = 0
    is_valid = False
    for c in range(len(G[r])+1):
        if c < C and G[r][c].isdigit():
            n = n * 10 + int(G[r][c])
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0<= r + rr < R and 0 <= c + cc < C:
                        ch = G[r+rr][c+cc]
                        if not ch.isdigit() and ch != '.':
                            is_valid = True
                        if ch == '*':
                            gears.add((r + rr, c + cc))
        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
            if is_valid:
                p1 += n
            n = 0
            is_valid = False
            gears = set()
print('part1 -', p1)

p2 = 0
for k,v in nums.items():
    if len(v) == 2:
        p2 += v[0] * v[1]
print('part2 -', p2)
