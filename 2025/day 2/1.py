import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

content = file[0]
content_arr = content.split(',')

sum_ids = 0

for ids in content_arr:
    l_str, r_str = ids.split('-')
    l,r = int(l_str.strip()), int(r_str.strip())

    for id in range(l, r + 1):
        len_id = len(str(id))
        if len_id % 2 == 0:
            num1 = str(id)[:len_id//2]
            num2 = str(id)[len_id//2:]

            sum_ids += int(num1 + num2) if num1 == num2 else 0



print(sum_ids)