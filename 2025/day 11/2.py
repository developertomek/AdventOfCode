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
def check(x, seen_dac, seen_fft):
    if x == 'out':
        return 1 if seen_dac and seen_fft else 0
    ans = 0
    for y in P[x]:
        new_seen_dac = seen_dac or y == 'dac'
        new_seen_fft = seen_fft or y == 'fft'
        ans += check(y, new_seen_dac, new_seen_fft)
    return ans

print(check('svr', False, False))