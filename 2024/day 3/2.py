import os
import re

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read()


pattern = r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"
matches = re.finditer(pattern, file)

do = True
res = 0
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
for match in matches:
    m = match.group()
    if m == "do()":
        do = True
    elif m == "don't()":
        do = False
    else:
        if do:
            nums = re.findall(mul_pattern, m)
            res += int(nums[0][0]) * int(nums[0][1])

print(res)
