import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().split('\n\n')

fresh = file[0].splitlines()
ids = file[1].splitlines()

fresh_ranges = []

for f in fresh:
    n1, n2 = f.split('-')
    fresh_ranges.append((int(n1),int(n2)))

fresh_ranges.sort(key=lambda x: x[0])
combined_ranges = []
res = 0

for start, end in fresh_ranges:
    if not combined_ranges:
        combined_ranges.append((start,end))
        continue
    l,r = combined_ranges[-1]
    if l <= start <= r and r < end:
        combined_ranges[-1] = (l, end)
    elif l < start > r:
        combined_ranges.append((start,end))

for ranges in combined_ranges:
    res += ranges[1] - ranges[0] + 1
    
            
print(res)