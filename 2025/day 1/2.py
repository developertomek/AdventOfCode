import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

s = 50
password = 0
for line in file:
    dir = line[:1]
    num = int(line[1:], 10)

    for _ in range(num):
        if dir == 'L':
            s = (s - 1 + 100) % 100
        elif dir == 'R':
            s = (s + 1) % 100
        if s == 0:
            password += 1
print(password)