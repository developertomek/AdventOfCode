import os
file_path = os.path.join('./2023/day 6', 'input.txt')
file = open(file_path, 'r').read().strip()

t, d = file.split('\n')

times = [int(val) for val in t.split(':')[1].split()]
distances = [int(val) for val in d.split(':')[1].split()]

def f(t,d):
    ans = 0
    for x in range(t+1):
        dx = x * (t-x)
        if dx > d:
            ans += 1
    return ans

p1 = 1
for i in range(len(times)):
    p1 *= f(times[i], distances[i])
print(p1)

T = ''
D = ''
for i in range(len(times)):
    T += str(times[i])
    D += str(distances[i])
T = int(T)
D = int(D)

print(f(T,D))
