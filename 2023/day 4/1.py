from collections import defaultdict
import os
file_path = os.path.join('./2023/day 4', 'input.txt')
file = open(file_path, 'r').read().strip()
lines = file.split('\n')

p1 = 0
p2 = 0

arr = [1] * len(lines)

for i, line in enumerate(lines):
    line = line.split(':')[1].strip()
    
    winning_numbers, my_numbers = line.split("|")
    
    nums = 0
    for wn in winning_numbers.split(" "):
        if wn and wn in my_numbers.split(" "):
            nums += 1
    
    if nums:
        p1 += 2 ** (nums - 1)
        
        # part 2
        for j in range(i + 1, i + nums + 1):
            arr[j] += arr[i]
            
p2 = sum(arr)

print(p1)
print(p2)