import os
import collections

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

d = collections.defaultdict(list)
res = 0

for line in file:
    for i, val in enumerate(line):
        d[i].append(val)

c = 0
sign = ''
for v in d.values():
    if v[-1] in ["*", "+"]:
        res += c
        sign = v[-1]
        c = int("".join(v[:-1]))
    else:
        num = "".join(v)
        if num.strip():
            num = int(num)
            if sign == '+':
                c += num
            elif sign == '*':
                c *= num

res += c

print(res)