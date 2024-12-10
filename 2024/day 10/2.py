import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

R = len(file)
C = len(file[0])
g = [[-1] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        g[r][c] = int(file[r][c])

ans = 0

for r in range(R):
    for c in range(C):
        def dfs(x, y):
            if g[x][y] == 9:
                return 1
            res = 0
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if g[nx][ny] == 1 + g[x][y]:
                        res += dfs(nx, ny)
            return res
        if g[r][c] == 0:
            ans  += dfs(r, c)

print(ans)
