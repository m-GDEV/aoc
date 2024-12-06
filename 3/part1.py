# Part 1
import re

f = open("/home/user/aoc-day-3-input", "r")

t = f.read()

m = re.findall("mul\((\d+),(\d+)\)", t)

sum = 0

for match in m:
#     print(match)
    sum += int(match[0]) * int(match[1])

print(sum)
    
f.close()