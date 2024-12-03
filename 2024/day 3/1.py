import os
import re

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read()


pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, file)

res = 0
for m in matches:
    res += int(m[0]) * int(m[1])

print(res)
