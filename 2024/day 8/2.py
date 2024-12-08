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
        for j in range(len(arr)):
            if i == j:
                continue
            r1, c1 = arr[i]
            r2, c2 = arr[j]
            dr = r2 - r1
            dc = c2 - c1
            while 0 <= r1 < R and 0 <= c1 < C:
                nodes.add((r1, c1))
                r1 += dr
                c1 += dc



print(len(nodes))