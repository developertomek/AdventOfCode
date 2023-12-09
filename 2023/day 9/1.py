import os
from collections import Counter
from math import gcd
file_path = os.path.join('./2023/day 9', 'input.txt')
file = open(file_path, 'r').read().strip()

lines = file.split('\n')

def f(xs, part2):
    D = []
    for i in range(len(xs)- 1):
        D.append(xs[i+1]-xs[i])
    if all(y==0 for y in D):
        return xs[0 if part2 else -1]
    else:
        return xs[0] - f(D,part2) if part2 else xs[-1] + f(D,part2)

for part2 in [False, True]:
    ans = 0
    for line in lines:
        xs = [int(x) for x in line.split()]
        ans += f(xs, part2)

    print(ans)