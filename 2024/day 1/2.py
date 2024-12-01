import os
from collections import defaultdict

file_path = os.path.join('./', 'input2.txt')
file = open(file_path, 'r').read().splitlines()

l_set = set()

d = defaultdict(int)

for line in file:
    l, r = line.split()
    l_set.add(int(l))
    d[int(r)] += 1

s = 0

for l in l_set:
    s += l * d[l]
    
print(s)