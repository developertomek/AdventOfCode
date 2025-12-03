import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

res = 0

for line in file:
    max_one = 0
    max_two = 0

    for i, ch in enumerate(line):
        num = int(ch)
        if num > max_one and i < len(line) - 1:
            max_one = num
            max_two = int(line[i + 1])
        elif num > max_two:
            max_two = num
    str_num = str(max_one) + str(max_two)
    res += int(str_num)
            
print(res)