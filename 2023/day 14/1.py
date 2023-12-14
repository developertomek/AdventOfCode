import os

file_path = os.path.join('./2023/day 14', 'input.txt')

grid = open(file_path, 'r').read().splitlines()
grid = list(map("".join, zip(*grid)))
grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]
grid = list(map("".join, zip(*grid)))

res = sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid))
print(res)