import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read()

s = []
j = 0
for i, c in enumerate(file):
    c = int(c)
    if i % 2 == 0:
        while c: 
            s.append(j)
            c -= 1
        j += 1
    else:
        while c:
            s.append('.')
            c -= 1

s_final = []

l = 0
r = len(s) - 1

for i in range(len(s)):
    if i <= r:
        if s[i] == '.':
            while s[r] == '.':
                r -= 1
            s_final.append(int(s[r]))
            r -= 1
        else:
            s_final.append(int(s[i]))
    else:
        break

res = 0
for i,c in enumerate(s_final):
    c = int(c)
    res += c * i

print(res)