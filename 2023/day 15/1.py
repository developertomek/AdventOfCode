import os

file_path = os.path.join('./2023/day 15', 'input.txt')
file = open(file_path, 'r').read().split(',')

def hash(s):
    v = 0
    for ch in s:
        v += ord(ch)
        v *= 17
        v %= 256
    return v

res = sum(map(hash, file))
print(res)