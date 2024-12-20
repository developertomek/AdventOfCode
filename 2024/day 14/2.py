import os

file_path = os.path.join('./', 'input.txt')
# file_path = os.path.join('./', 't.txt')
file = open(file_path, 'r').read().splitlines()

Y = 103
X = 101

quads = [0, 0, 0, 0]

total = len(file)
for steps in range(1, 100000):
    seen = set()
    for line in file:
        l = line.split('p=')
        l = l[1].split('v=')
        px, py = l[0].split(',')
        vx, vy = l[1].split(',')
        
        nx = (int(px) + steps * int(vx)) % X
        ny = (int(py) + steps * int(vy)) % Y

        seen.add((nx,ny)) 
    if len(seen) == total:
        print(steps)
        break
