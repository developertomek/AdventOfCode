import os
import collections

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

res = 0
idx = set()
sid = file[0].index('S')

idx.add(sid)

for line in file[1:]:
    for i,ch in enumerate(line):
        if ch == '^' and i in idx:
            res += 1
            idx.remove(i)
            idx.add(i + 1)
            idx.add(i - 1)

print(res)