import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

res = 0

R = len(file)
C = len(file[0])

for r in range(R):
    for c in range(C):
        if c + 3 < C and file[r][c] == 'X' and file[r][c + 1] == 'M' and file[r][c + 2] == 'A' and file[r][c + 3] == 'S':
            res += 1
        if r + 3 < R and file[r][c] == 'X' and file[r+1][c] == 'M' and file[r+2][c] == 'A' and file[r+3][c] == 'S':
            res += 1
        if r + 3 < R and c + 3 < C and file[r][c] == 'X' and file[r+1][c+1] == 'M' and file[r+2][c+2] == 'A' and file[r+3][c+3] == 'S':
            res += 1

        if c + 3 < C and file[r][c] == 'S' and file[r][c + 1] == 'A' and file[r][c + 2] == 'M' and file[r][c + 3] == 'X':
            res += 1
        if r + 3 < R and file[r][c] == 'S' and file[r+1][c] == 'A' and file[r+2][c] == 'M' and file[r+3][c] == 'X':
            res += 1
        if r + 3 < R and c + 3 < C and file[r][c] == 'S' and file[r+1][c+1] == 'A' and file[r+2][c+2] == 'M' and file[r+3][c+3] == 'X':
            res += 1

        if r-3 >= 0 and c+3 < C and file[r][c] == 'X' and file[r-1][c+1] == 'M' and file[r-2][c+2] == 'A' and file[r-3][c+3] == 'S':
            res += 1
        if r-3 >= 0 and c+3 < C and file[r][c] == 'S' and file[r-1][c+1] == 'A' and file[r-2][c+2] == 'M' and file[r-3][c+3] == 'X':
            res += 1

        

print(res)