import os
from collections import Counter
from math import gcd
file_path = os.path.join('./2023/day 8', 'input.txt')
file = open(file_path, 'r').read().strip()

def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x*ans)//gcd(x,ans)
    return ans

GO = {'L': {}, 'R': {}}

steps, rule = file.split('\n\n')

for line in rule.split('\n'):
    st, lr = line.split("=")
    st = st.strip()

    left, right = lr.split(",")
    left = left.strip()[1:].strip()
    right = right[:-1].strip()
    GO['L'][st] = left
    GO['R'][st] = right

def solve(part2):
    POS = []
    for s in GO['L']:
        if s.endswith('A' if part2 else 'AAA'):
            POS.append(s)
    T = {}
    t = 0

    while True:
        NP = []
        for i, p in enumerate(POS):
            p = GO[steps[t % len(steps)]][p]

            if p.endswith('Z'):
                T[i] = t + 1

                if len(T) == len(POS):
                    return lcm(T.values())
            NP.append(p)
        POS = NP

        t+= 1

print(solve(False))
print(solve(True))