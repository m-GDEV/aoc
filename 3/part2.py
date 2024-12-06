# Part 2

def get_mul_num(mul):
    s = re.findall("mul\((\d+),(\d+)\)", mul)
#     print("thing:", mul, s)
    return int(s[0][0]) * int(s[0][1])

import re

# command that created this transformed input
# cmd cat input | grep -P -o "(do(n't)?\(\)|mul\(\d+,\d+\))" > transformed
f = open("/home/user/aoc-day-3-transformed", "r")

sum = 0
add = True

for line in f:
    if (line == "do()\n"):
        add = True
        continue
    if (line == "don't()\n"):
        add = False
        continue
    
    if add is True:
        sum += get_mul_num(line)

print(sum)
    
f.close()