import os
from functools import cache 

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

P = {}
for line in file:
    x, ys = line.split(':')
    ys = ys.split()
    P[x] = ys

@cache
def check(x):
    if x == 'out':
        return 1
    return sum(check(y) for y in P[x])

print(check('you'))