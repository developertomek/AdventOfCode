import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()

ROWS, COLS = len(file), len(file[0])

file = [list(line) for line in file]
backup = file
res = 0

while True:
    mark_to_delete = False
    for i in range(ROWS):
        for j in range(COLS):
            ch = file[i][j]
            if ch == '.': continue
            num = 0
            for x,y in [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]:
                r, c = i + x, j + y

                if r < 0 or c < 0 or r == ROWS or c == COLS:
                    num += 1
                elif file[r][c] == '.':
                    num += 1
                if num == 5:
                    backup[i][j] = '.'
                    mark_to_delete = True
                    res += 1
                    break
    if not mark_to_delete:
        break
    file = backup

print(res)