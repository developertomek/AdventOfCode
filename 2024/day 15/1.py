import os

file_path = os.path.join('./', 'input.txt')
s1, s2 = open(file_path, 'r').read().split("\n\n")
g = [list(r) for r in s1.splitlines()]
n, m = len(g), len(g[0])

cx, cy = 0, 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '@':
            cx, cy = i, j
            break

for move in s2.replace('\n', ''):
    dx, dy = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }[move]

    bxs = []
    nx, ny = cx + dx, cy + dy
    while  g[nx][ny] == 'O':
        bxs.append((nx, ny))
        nx, ny = nx + dx, ny + dy
    
    if g[nx][ny] == '#':
        pass
    else:
        assert g[nx][ny] == '.'
        target = [(cx, cy)] + bxs + [(nx, ny)]
        for (x1, y1), (x2, y2) in list(zip(target, target[1:]))[::-1]:
            g[x2][y2] = g[x1][y1]
        g[cx][cy] = '.'
        cx, cy = cx + dx, cy + dy

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] != 'O':
            continue
        ans += 100 * i + j
print(ans)