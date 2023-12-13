import os
from collections import deque

file_path = os.path.join('./2023/day 13', 'input.txt')
file = open(file_path, 'r').read().split("\n\n")

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[:len(below)]
        below = below[:len(above)]

        if above == below:
            return r
    return 0


total = 0

for block in file:
    grid = block.splitlines()

    row = find_mirror(grid)
    total += row * 100

    col = find_mirror(list(zip(*grid)))
    total += col

print(total)