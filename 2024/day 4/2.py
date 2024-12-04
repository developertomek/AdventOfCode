import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

res = 0

R = len(file)
C = len(file[0])

for r in range(R):
    for c in range(C):
        if r + 2 < R and c + 2 < C and file[r][c] == 'M' and file[r+1][c+1] == 'A' and file[r+2][c+2] == 'S' and file[r][c+2] == 'M' and file[r+1][c+1] == 'A' and file[r+2][c] == 'S':
            res += 1

        if r + 2 < R and c + 2 < C and file[r][c] == 'S' and file[r+1][c+1] == 'A' and file[r+2][c+2] == 'M' and file[r][c+2] == 'M' and file[r+1][c+1] == 'A' and file[r+2][c] == 'S':
            res += 1

        if r + 2 < R and c + 2 < C and file[r][c] == 'S' and file[r+1][c+1] == 'A' and file[r+2][c+2] == 'M' and file[r][c+2] == 'S' and file[r+1][c+1] == 'A' and file[r+2][c] == 'M':
            res += 1
        
        if r + 2 < R and c + 2 < C and file[r][c] == 'M' and file[r+1][c+1] == 'A' and file[r+2][c+2] == 'S' and file[r][c+2] == 'S' and file[r+1][c+1] == 'A' and file[r+2][c] == 'M':
            res += 1

print(res)