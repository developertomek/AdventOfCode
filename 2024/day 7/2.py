import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read().splitlines()


def calculate(target, array):
    if len(array) == 1:
        return target == array[0]
    if target % array[-1] == 0 and calculate(target // array[-1], array[:-1]):
        return True
    if target > array[-1] and calculate(target - array[-1], array[:-1]):
        return True
    s_target = str(target)
    s_last = str(array[-1])
    if len(s_target) > len(s_last) and s_target.endswith(s_last) and calculate(int(s_target[:-len(s_last)]), array[:-1]):
        return True
    return False


res = 0
for line in file:
    left, right = line.split(': ')
    target = int(left)
    arr = [int(x) for x in right.split(' ')]
    if calculate(target, arr):
        res += target
print(res)