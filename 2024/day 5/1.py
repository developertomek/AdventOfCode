import os
from collections import defaultdict

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().split('\n\n')

rules, update = file[0].splitlines(), file[1].splitlines()

d = defaultdict(set)

for r in rules:
    x, y = r.split('|')
    x, y = int(x), int(y)
    d[y].add(x)


res = 0
for u_line in update:
    u_arr = [int(x) for x in u_line.split(',')]
    is_good = True

    for i, x in enumerate(u_arr):
        for j, y in enumerate(u_arr):
            if i < j and y in d[x]:
                is_good = False
    if is_good:
        res += u_arr[len(u_arr)//2]

print(res)