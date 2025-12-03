import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

res = 0

for line in file:
    max_one = 0

    line_num_str = ''
    i = 0
    lastidx = 0

    while i < 12:
        chunk = line[lastidx:len(line)-11 + i]
        if chunk:
            max_num = max(chunk)
            line_num_str += max_num

            idx = chunk.index(max_num)
            lastidx += idx + 1
        i+= 1
    
    res += int(line_num_str)
print(res)