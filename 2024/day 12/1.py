import os
from collections import defaultdict

file_path = os.path.join('./', 'input.txt')
# file_path = os.path.join('./', 't.txt')
file = open(file_path, 'r').read().splitlines()

R = len(file)
C = len(file[0])


seen = {}

def dfs(r, c, ch, i):
    if r in range(R) and c in range(C):
        if (r, c) in seen:
            return
        if ch == file[r][c]:
            seen[r, c] = i
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc, ch, i)

nxt = 0
for i in range(R):
    for j in range(C):
        if (i, j) not in seen:
            dfs(i, j, file[i][j], nxt)
            nxt += 1

seen_s = defaultdict(set)

for k, v in seen.items():
    seen_s[v].add(k)

res = 0
for k, nodes in seen_s.items():
    area = len(nodes)
    p = 0
    for no in nodes:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = no[0] + dr, no[1] + dc
            if nr not in range(R) or nc not in range(C) or (nr, nc) not in nodes:
                p += 1
    res += p * area
print(res)
