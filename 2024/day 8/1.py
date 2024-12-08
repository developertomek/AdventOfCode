import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

antenas = {}

for r, line in enumerate(file):
    for c, char in enumerate(line):
        if char != '.':
            if char not in antenas:
                antenas[char] = []
            antenas[char].append((r, c))

vals = list(antenas.values())
nodes = set()
R = len(file)
C = len(file[0])

for arr in vals:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            r1, c1 = arr[i]
            r2, c2 = arr[j]
            nodes.add((2 * r1 - r2, 2 * c1 - c2))
            nodes.add((2 * r2 - r1, 2 * c2 - c1))

res = set()
for r, c in nodes:
    if 0 <= r < R and 0 <= c < C:
        res.add((r, c))

print(len(res))