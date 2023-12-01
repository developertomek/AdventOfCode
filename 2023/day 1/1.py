s = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

s = s.split('\n')

res = 0
d = ['one','two','three','four','five','six','seven','eight','nine'] 
for line in s:
    num = []
    for i,c in enumerate(line):
        if c.isdigit():
            num.append(c)
        else:
            for j, val in enumerate(d):
                if line[i:].startswith(val):
                    num.append(str(j+1))
    res += int(num[0]+num[-1])
print(res)