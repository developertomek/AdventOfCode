import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().split('\n\n')

fresh = file[0].splitlines()
ids = file[1].splitlines()

res = 0
fresh_ranges = []

for f in fresh:
    n1, n2 = f.split('-')
    fresh_ranges.append((int(n1),int(n2)))


for id in ids:
    for ranges in fresh_ranges:
        if ranges[0] <= int(id) <= ranges[1]:
            res += 1
            break
            
print(res)