import heapq
import os

file_path = os.path.join('./', 'input.txt')
g = open(file_path, 'r').read().splitlines()

rows, cols = len(g), len(g[0])

for r in range(rows):
    for c in range(cols):
        if g[r][c] == 'S':
            sr = r
            sc = c
            break
    else:
        continue
    break

pq = [(0, sr, sc, 0, 1)]
seen = {(sr, sc, 0, 1)}

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    seen.add((r, c, dr, dc))
    if g[r][c] == 'E':
        print(cost)
        break
    for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if g[nr][nc] == "#":
            continue
        if (nr, nc, ndr, ndc) in seen:
            continue
        heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))