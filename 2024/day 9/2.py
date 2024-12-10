import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read()


pos = 0
f = {}
idx = 0
blanks = []
for i, c in enumerate(file):
    c = int(c)
    if i % 2 == 0:
        f[idx] = (pos, c)
        idx += 1
    else:
        blanks.append((pos, c))
    pos += c

while idx > 0:
    idx -= 1
    pos, size = f[idx]
    for i in range(len(blanks)):
        start, length = blanks[i]
        if start >= pos:
            blanks = blanks[:i]
            break
        if size <= length:
            f[idx] = (start, size)
            if size == length:
                blanks.pop(i)
            else:
                blanks[i] = (start + size, length - size)
            break

res = 0

for fid, (pos, size) in f.items():
    for x in range(pos, pos + size):
        res += fid * x

print(res)