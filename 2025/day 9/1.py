import os

file_path = os.path.join('./', 'test.txt')
file = open(file_path, 'r').read().splitlines()
points = []
res = 0

for line in file:
    x,y = line.split(',')
    points.append((int(x),int(y)))

area = 0
for i in range(len(points)-1):
    x1, y1 = points[i]
    for j in range(i+1, len(points)):
        x2, y2 = points[j]
        curr_area = (abs(x1-x2) + 1) * (abs(y1-y2) + 1)
        area = max(area,curr_area)

print(area)
        