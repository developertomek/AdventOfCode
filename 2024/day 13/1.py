import os

file_path = os.path.join('./', 'input.txt')
# file_path = os.path.join('./', 't.txt')
file = open(file_path, 'r').read().split('\n\n')

res = 0

for configurations in file:
    A = [0, 0]
    B = [0, 0]
    P = [0, 0]
    config = configurations.splitlines()
    a_split = config[0].split('+')
    b_split = config[1].split('+')
    c_split = config[2].split('=')
    
    A[0] = int(a_split[-2].split(',')[0])
    A[1] = int(a_split[-1])
    B[0] = int(b_split[-2].split(',')[0])
    B[1] = int(b_split[-1])
    P[0] = int(c_split[-2].split(',')[0])
    P[1] = int(c_split[-1])
    
    X, Y = 0, 0
    i = 0
    a, b = 1, 0
    if P[0] % A[0] == 0 and P[1] % A[1] == 0 and P[0] / A[0] == P[1] / A[1]:
        a = P[0] // A[0]
        res += a * 3
        continue
    elif P[0] % B[0] == 0 and P[1] % B[1] == 0 and P[0] / B[0] == P[1] / B[1]:
        b = P[0] // B[0]
        res += b
        continue

    while X <= P[0] and Y <= P[1] and i <= 100:
        X += A[0]
        Y += A[1]
        if (P[0] - X) % B[0] == 0 and (P[1] - Y) % B[1] == 0 and (P[0] - X) / B[0] == (P[1] - Y) / B[1]:
            b = (P[0] - X) // B[0]
            X += b * B[0]
            Y += b * B[1]
            break
        a += 1
        i += 1
    if X == P[0] and Y == P[1]:
        res += a  * 3
        res += b
print(res)