import os

file_path = os.path.join('./', 'input.txt')
# file_path = os.path.join('./', 't.txt')
file = open(file_path, 'r').read().splitlines()

Y = 103
X = 101

quads = [0, 0, 0, 0]

for line in file:
    l = line.split('p=')
    l = l[1].split('v=')
    px, py = l[0].split(',')
    vx, vy = l[1].split(',')
    
    nx = (int(px) + 100 * int(vx)) % X
    ny = (int(py) + 100 * int(vy)) % Y

    if nx < 50 and ny < 51:
        quads[0] += 1
    elif nx > 50 and ny < 51:
        quads[1] += 1
    elif nx < 50 and ny > 51:
        quads[2] += 1
    elif nx > 50 and ny > 51:
        quads[3] += 1
ans = quads[0] * quads[1] * quads[2] * quads[3]
print(ans)