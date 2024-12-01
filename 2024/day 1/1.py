import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

l_list = []
r_list = []

for line in file:
    l, r = line.split()
    l_list.append(int(l))
    r_list.append(int(r))

l_list.sort()
r_list.sort()

s = 0

for l, r in zip(l_list, r_list):
    s += abs(l - r)

print(s)

