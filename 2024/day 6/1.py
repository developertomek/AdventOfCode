import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

R = len(file)
C = len(file[0])

guard = [0,0]

for r in range(R):
    for c in range(C):
        if file[r][c] == '^':
            guard = [r, c]
            break


seen = set()
r, c = guard
positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
i = 0
while r >= 0 and c >= 0 and r < R and c < C:
    if file[r][c] == '#':
        r = r - positions[i%4][0]
        c = c - positions[i%4][1]
        i += 1
    if (r, c) not in seen:
        seen.add((r, c))
    r, c = r + positions[i%4][0], c + positions[i%4][1]

print(len(seen))