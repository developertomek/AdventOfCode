import os

file_path = os.path.join('./', 'input.txt')
s1, s2 = open(file_path, 'r').read().split("\n\n")
g = [list(r) for r in s1.splitlines()]
n, m = len(g), len(g[0])

g2 = []
for row in g:
    nrow = []
    for cx in row:
        if cx == '#':
            nrow.append('#')
            nrow.append('#')
        elif cx == 'O':
            nrow.append('[')
            nrow.append(']')
        elif cx == '@':
            nrow.append('@')
            nrow.append('.')
        elif cx == '.':
            nrow.append('.')
            nrow.append('.')
    g2.append(nrow)
g = g2
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

    c2m = [(cx, cy)]
    i = 0
    impos = False
    while i < len(c2m):
        x, y = c2m[i]
        nx, ny = x + dx, y + dy
        if g[nx][ny] in 'O[]':
            if (nx, ny) not in c2m:
                c2m.append((nx, ny))
            if g[nx][ny] == '[':
                if (nx, ny+1) not in c2m:
                    c2m.append((nx, ny+1))
            if g[nx][ny] == ']':
                if (nx, ny-1) not in c2m:
                    c2m.append((nx, ny-1))

        elif g[nx][ny] == '#':
            impos = True
            break
        i += 1
    if impos:
        continue
    
    new_g = [[g[i][j] for j in range(m)] for i in range(n)]
    for x, y in c2m:
        new_g[x][y] = "."
    for x, y in c2m:
        new_g[x+dx][y+dy] = g[x][y]
    
    g = new_g

    cx += dx
    cy += dy

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] != '[':
            continue
        ans += 100 * i + j
print(ans)