import os

file_path = os.path.join('./', 'input.txt')
# file_path = os.path.join('./', 't.txt')
file = open(file_path, 'r').read().splitlines()

R = len(file)
C = len(file[0])

file_arr = []
for r in file:
    l = []
    for c in r:
        l.append(c)
    file_arr.append(l)

guard = [0,0]

for r in range(R):
    for c in range(C):
        if file[r][c] == '^':
            guard = [r, c]
            break



# r, c = guard
positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
i = 0

res = 0

def loop(file_arr, r, c):
    i = 0
    seen = set()
    while r >= 0 and c >= 0 and r < R and c < C:
        if file_arr[r][c] == '#':
            r = r - positions[i%4][0]
            c = c - positions[i%4][1]
            i += 1
        if (r, c, i%4) not in seen:
            seen.add((r, c, i%4))
        r, c = r + positions[i%4][0], c + positions[i%4][1]
        if (r, c, i%4) in seen:
            return True
    return False

for x in range(R):
    for y in range(C):
        if file_arr[x][y] == '.':
            file_arr[x][y] = '#'
            if loop(file_arr, guard[0], guard[1]):
                res += 1
            file_arr[x][y] = '.'

print(res)