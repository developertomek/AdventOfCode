import os
import functools

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

sid = file[0].index('S')
lines = []

for line in file:
    if all('.' == ch for ch in line):
        continue
    else:
        lines.append(line)
splitters = set()

for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '^':
            splitters.add((r,c))   


@functools.cache
def dfs(r,c):
    global res
    if r >= len(lines) and c >= len(lines[0]) or c < 0:
        return 
    if r == len(lines) - 1:
        return 1 if (r, c) in splitters else 0
    
    current = 1 if (r, c) in splitters else 0
    if (r,c) in splitters:
        count_down_left = dfs(r + 1, c - 1)
        count_down_right = dfs(r + 1, c + 1)
        return current + count_down_left + count_down_right
    else:
        count_down = dfs(r + 1, c)
        return current + count_down


res = dfs(0,sid) + 1
print(res)