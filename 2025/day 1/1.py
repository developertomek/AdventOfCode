import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

s = 50
password = 0
for line in file:
    dir = line[:1]
    num = int(line[1:], 10)

    if dir == 'L':
        s -= num
    elif dir == 'R':
        s += num
    
    if s % 100 == 0:
        password += 1 
    
print(password)
