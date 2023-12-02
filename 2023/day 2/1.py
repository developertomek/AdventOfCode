import os
file_path = os.path.join('./2023/day 2', 'input.txt')
file = open(file_path, 'r').read()

file = file.split('\n')
d = {
    'red': 12,
    'green': 13,
    'blue': 14
}
colors = ['red', 'green', 'blue']

idx = 0
for i, line in enumerate(file):
    gs = line.split(':')
    if len(gs) > 1:
        game = gs[1].split(' ')
        isPossible = True
        for j in range(2, len(game), 2):
            for c in colors:
                if game[j].startswith(c):
                    if d[c] < int(game[j-1]):
                        isPossible = False
                        break
        if isPossible:
            idx += i + 1

print(idx)

