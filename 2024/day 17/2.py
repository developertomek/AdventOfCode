import os
import re

file_path = os.path.join('./', 'input.txt')
g = open(file_path, 'r').read()

program = list(map(int, re.findall(r"\d+", g)[3:]))

def find(input, ans):
    if input == []:
        return ans
    for t in range(8):
        a = ans << 3 | t
        output = None
        b = 0
        c = 0
        adv3 = False

        def combo(operand):
            if 0 <= operand <= 3:
                return operand
            if operand == 4: return a
            if operand == 5: return b
            if operand == 6: return c
            raise RuntimeError(f"Invalid operand {operand}")

        
        for pointer in range(0, len(program) - 2, 2):
            ins = program[pointer]
            operand = program[pointer + 1]
            if ins == 0:
                assert not adv3, "program has multiple ADVs"
                assert operand == 3, "program has ADV with operand other than 3"
                adv3 = True
            elif ins == 1:
                b = b ^ operand
            elif ins == 2:
                b = combo(operand) % 8
            elif ins == 3:
                raise AssertionError("program has JNZ inside expected loop body")
            elif ins == 4:
                b = b ^ c
            elif ins == 5:
                assert output is None, "program has multiple OUTs"
                output = combo(operand) % 8
            elif ins == 6:
                b = a >> combo(operand)
            elif ins == 7:
                c = a >> combo(operand)
            if output == input[-1]:
                sub = find(input[:-1], a)
                if sub is None: continue
                return sub


        
print(find(program, 0))