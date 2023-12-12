import os
from collections import deque

file_path = os.path.join('./2023/day 12', 'input.txt')
grid = open(file_path, 'r').read().strip().splitlines()


def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if '#' in cfg else 1
    
    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    return result

total = 0

for line in grid:
    cfg, nums = line.split()
    nums = tuple(map(int, nums.split(',')))
    total += count(cfg, nums)

print(total)