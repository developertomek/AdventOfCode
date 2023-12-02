import os
file_path = os.path.join('./2023/day 2', 'input.txt')
file = open(file_path, 'r').read()

file = file.split('\n')

colors = ['red', 'green', 'blue']
res = 0

for i, line in enumerate(file):
    d = {
        'red': [],
        'green': [],
        'blue': []
    }
    gs = line.split(':')
    if len(gs) > 1:
        game = gs[1].split(' ')
        for j in range(2, len(game), 2):
            for c in colors:
                if game[j].startswith(c):
                    d[c].append(int(game[j-1]))
        r = 1
        for v in d.values():
            r *= max(v)
        res += r
print(res)