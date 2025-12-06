import os
import collections

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

d = collections.defaultdict(list)
res = 0

for line in file:
    for i, val in enumerate(line.split()):
        if val not in ["*", "+"]:
            val = int(val)
        d[i].append(val)

for line in d.values():
    sign = line[-1]
    vals = line[:-1]
    m = 1
    s = 0
    
    for v in vals:
        if sign == '+':
            s += v
        elif sign == '*':
            m *= v
            
    res += s 
    res += m if m > 1 else 0

print(res)