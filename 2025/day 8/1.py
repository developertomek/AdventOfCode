import collections
import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()


P = []
D = []
for line in file:
    x,y,z = [int(x) for x in line.split(',')]
    P.append((x,y,z))

for i, (x1,y1,z1) in enumerate(P):
    for j, (x2,y2,z2) in enumerate(P):
        if i < j:
            distance = (x1 - x2)**2 + (y1-y2)**2 + (z1-z2)**2
            D.append((distance, i, j))

U = {i: i for i in range(len(P))}

def find(x):
    if x == U[x]:
        return x
    U[x] = find(U[x])
    return U[x]

def mix(x,y):
    U[find(x)] = find(y)

D = sorted(D)
for d, i, j in D[:1000]:
    mix(i,j)

SZ = collections.defaultdict(int)
for x in range(len(P)):
    SZ[find(x)] += 1
S = sorted(SZ.values())

print(S[-1] * S[-2] * S[-3]) 
