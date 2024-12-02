import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()


def safe(line):
    diffs = [x - y for x, y in zip(line, line[1:])]
    return all(0 < x < 4 for x in diffs) or all(0 > x > -4 for x in diffs)


res = 0
for l in file:
    line = [int(i) for i in l.split()]

    for i in range(len(line)):
        if safe(line[:i] + line[i + 1:]):
            res += 1
            break

print(res)
